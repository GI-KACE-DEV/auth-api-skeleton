
from google.cloud.exceptions import NotFound
from fastapi.exceptions import HTTPException
from google.cloud import storage
from config.settings import Settings
from fastapi import status
import os


project_id = Settings.PROJECT_ID
bucket_name = Settings.BUCKET_NAME
flyerPath = Settings.FLYER_PATH
program_outlinePath = Settings.OUTLINE_PATH


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'apis/google_cloud_storage_api.json'


class GCStorage:
    # @staticmethod 
    def __init__(self):
        self.client_storage = storage.Client()
        self.bucket_name = bucket_name





    def upload_file_to_gcp(self, url, type, filename):
        if url is not None:
            if type == "Flyer":
                bucket = self.client_storage.get_bucket(self.bucket_name)
                flyer_path = flyerPath + "/" + filename
                blob = bucket.blob(flyer_path)
                blob.upload_from_file(url.file)
                flyer_url = f'https://storage.googleapis.com/{self.bucket_name}/{flyer_path}'
                return flyer_url

            elif type == "Document":
                bucket = self.client_storage.get_bucket(self.bucket_name)
                docs_path = program_outlinePath + "/" + filename
                blob = bucket.blob(docs_path)
                blob.upload_from_file(url.file)
                outline_url = f'https://storage.googleapis.com/{self.bucket_name}/{docs_path}'
                return outline_url   
            
            elif type == "Logo":
                bucket = self.client_storage.get_bucket(self.bucket_name)
                logo_path = flyerPath + "/" + filename
                blob = bucket.blob(logo_path)
                blob.upload_from_file(url.file)
                logo_url = f'https://storage.googleapis.com/{self.bucket_name}/{logo_path}'
                return logo_url 
            else:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="File type should be eg. Flyer, Document")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Upload a valid file")
    




    def delete_file_to_gcp(self, type, filename):
        if filename is not None:
            if type == "Flyer":
                try:
                    bucket = self.client_storage.get_bucket(self.bucket_name)
                    flyer_path = flyerPath + "/" + filename
                    blob = bucket.blob(flyer_path)
                    blob.delete()
                except NotFound:
                    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'🚨Flyer does not exist - do something')
            elif type == "Document":
                try:
                    bucket = self.client_storage.get_bucket(self.bucket_name)
                    flyer_path = program_outlinePath + "/" + filename
                    blob = bucket.blob(flyer_path)
                    blob.delete()
                except NotFound:
                    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'🚨 Document does not exist - do something')
            elif type == "Logo":
                try:
                    bucket = self.client_storage.get_bucket(self.bucket_name)
                    logo_path = flyerPath + "/" + filename
                    blob = bucket.blob(logo_path)
                    blob.delete()
                except NotFound:
                    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'🚨 Logo does not exist - do something')
        return "File delete successful from GCP"