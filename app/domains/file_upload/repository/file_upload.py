from crud.base import CRUDBase
from domains.file_upload.models.file_upload import FileUpload
from domains.file_upload.schemas.file_upload import (
    FileUploadCreate, FileUploadUpdate
)


class CRUDFileUpload(CRUDBase[FileUpload, FileUploadCreate, FileUploadUpdate]):
    pass
fileUploads_actions = CRUDFileUpload(FileUpload)