from crud.base import CRUDBase
from domains.file_upload.models.gcs import FileUpload
from app.domains.file_upload.schemas.gcs import (
    FileUploadCreate, FileUploadUpdate
)


class CRUDFileUpload(CRUDBase[FileUpload, FileUploadCreate, FileUploadUpdate]):
    pass
fileUploads_actions = CRUDFileUpload(FileUpload)