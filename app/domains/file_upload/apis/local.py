from domains.file_upload.services.local import local_file_upload_service as actions
from fastapi import APIRouter,File,UploadFile,Depends,status,Form
from utils.rbac import check_if_is_super_admin,check_if_is_super_admin_or_staff
from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session
from fastapi import HTTPException
from db.session import get_db
from pydantic import UUID4
from typing import Optional




local_file_upload_router = APIRouter(
       prefix="/local",
    tags=["LOCAL FILE UPLOAD"],
    responses={404: {"description": "Not found"}},
)



@local_file_upload_router.post("/")
async def upload_file(*, db: Session = Depends(get_db), file: UploadFile = File(...),  type: Optional[str] = Form(), 
            description: Optional[str] = Form(None), current_user=Depends(check_if_is_super_admin_or_staff)):
    upload_file = actions.upload_file(db=db, type=type, description=description, file=file, current_user=current_user)
    return upload_file





@local_file_upload_router.get("/")
async def get_uploaded(*, db: Session = Depends(get_db), file_id: UUID4, current_user=Depends(check_if_is_super_admin_or_staff)):
    upload_file = actions.get_uploaded_file_by_id(db=db, file_id=file_id, current_user=current_user)
    return upload_file




#function to delete files
@local_file_upload_router.delete("/{id}")
async def delete_file(*, db: Session = Depends(get_db), id: UUID4, deleted_reason: str, current_user=Depends(check_if_is_super_admin)):
    check_file = actions.get_uploaded_file_by_id(db=db, file_id=id)
    if not check_file:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'🚨 file does not exist - do something')
    upload_file = actions.remove_upload_file(db=db, file_id=id, deleted_reason=deleted_reason, current_user=current_user.id)
    return upload_file