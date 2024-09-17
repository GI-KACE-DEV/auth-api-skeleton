from fastapi import status,File,UploadFile,status,Form,Depends
from domains.file_upload.models.gcs import FileUpload
from domains.file_upload.services.gcstorage import GCStorage
from utils.rbac import check_if_is_super_admin
from fastapi.exceptions import HTTPException
from typing import Optional,Annotated
from sqlalchemy.orm import Session
from pydantic import UUID4
import random
import string
from domains.auth.models.users import User
from domains.auth.respository.user_account import users_form_actions as users_form_repo




class FileUploadService:
        



        def get_uploaded_file_by_id(self,db: Session, file_id: UUID4, current_user: User =Depends(check_if_is_super_admin)):
            get_uploaded_file =  db.query(FileUpload).filter(FileUpload.id == file_id).first()
            if not get_uploaded_file:
                 raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="File not found")
            user_db = users_form_repo.get_by_id(id=get_uploaded_file.uploaded_by, db=db)
            
            db_data = {
                 "id": get_uploaded_file.id,
                 "url": get_uploaded_file.url,
                 "type": get_uploaded_file.type,
                 "description": get_uploaded_file.description,
                 "filename": get_uploaded_file.filename,
                 "created_at": get_uploaded_file.created_date,
                 "updated_at": get_uploaded_file.updated_date,
                 "is_deleted": get_uploaded_file.is_deleted,
                 "uploaded_by": {
                      "username": user_db.username,
                      "email": user_db.email
                 },
                 "deleted_by": get_uploaded_file.deleted_by,
                 "deleted_at": get_uploaded_file.deleted_at,
                 "deleted_reason": get_uploaded_file.deleted_reason,
            }
            return db_data



        def upload_file(self,db: Session,type: Annotated[str, Form()],
                      description: Annotated[str, Form()], file: Optional[UploadFile] = File(None), current_user=Depends(check_if_is_super_admin)):
            size=10
            chars=string.ascii_lowercase + string.digits
            create_ramdom = ''.join(random.choice(chars) for _ in range(size))
            filename = create_ramdom + "-" + str(current_user.id) + "-" + file.filename
            file_url_path = GCStorage().upload_file_to_gcp(url=file, type=type, filename=filename)
            if not file_url_path:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error while uploading file")
            upload_file = FileUpload(uploaded_by = current_user.id, url=file_url_path, type=type, description=description, filename=filename)
            db.add(upload_file)
            db.commit()
            db.refresh(upload_file)

            user_db = users_form_repo.get_by_id(id=current_user.id, db=db)
            
            db_data = {
                 "id": upload_file.id,
                 "url": upload_file.url,
                 "type": upload_file.type,
                 "description": upload_file.description,
                 "filename": upload_file.filename,
                 "created_at": upload_file.created_date,
                 "updated_at": upload_file.updated_date,
                 "is_deleted": upload_file.is_deleted,
                 "deleted_at": upload_file.deleted_at,
                 "uploaded_by": {
                      "username": user_db.username,
                      "email": user_db.email
                 },
                 "deleted_reason": upload_file.deleted_reason,
                 "deleted_by": None
            }

            return db_data
        




        def remove_upload_file(self,db: Session, file_id: UUID4, filename: str, deleted_reason: str, current_user=Depends(check_if_is_super_admin)):
        
            get_file = db.query(FileUpload).filter(FileUpload.id == file_id).first()
            delete_file = GCStorage().delete_file_to_gcp(type=get_file.type, filename=filename)
            if not delete_file:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error while deleting file")
            
            user_db = users_form_repo.get_by_id(id=get_file.uploaded_by, db=db)
            
            
            db.query(FileUpload).filter(FileUpload.id == file_id).update({
            FileUpload.is_deleted: True,
            FileUpload.deleted_reason: deleted_reason,
            FileUpload.deleted_by: get_file.uploaded_by
            }, synchronize_session=False)
            db.flush()
            db.commit()

            # db.query(FileUpload).filter(FileUpload.id == file_id).delete()
            # db.commit()


            db_data = {
                 "id": get_file.id,
                 "url": get_file.url,
                 "type": get_file.type,
                 "description": get_file.description,
                 "filename": get_file.filename,
                 "uploaded_by": {
                      "username": user_db.username,
                      "email": user_db.email
                 },
                 "created_at": get_file.created_date,
                 "updated_at": get_file.updated_date,
                 "is_deleted": get_file.is_deleted,
                 "deleted_at": get_file.deleted_at,
                 "deleted_by": {
                      "username": user_db.username,
                      "email": user_db.email
                 },
                 "deleted_reason": get_file.deleted_reason,
            }
            return db_data



file_upload_service = FileUploadService()