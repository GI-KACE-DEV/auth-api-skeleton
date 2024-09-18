import secrets
import os
 
#from dotenv import load_dotenv

#load_dotenv(dotenv_path='CONFIG/conf.env')

class Settings:
    PROJECT_NAME:str = "API SKELETON WITH AUTH,USER MANAGEMENT,RBAC AND MESSAGING WITH EMAIL"
    PROJECT_VERSION: str = "1.0.0"

   

    SMS_API_KEY:str  = os.getenv("ARKESEL_API_KEY")
    SMS_API_URL: str = os.getenv("ARKESEL_BASE_URL")
    
    intruder_list = []
    
    MAX_CONCURRENT_THREADS: int = 10  # Maximum number of concurrent threads
    MAX_RETRIES: int = 1  # Maximum number of retry attempts
    RETRY_DELAY_BASE: int = 0  # Initial retry delay in seconds
    RETRY_DELAY_MULTIPLIER: int = 1  # Exponential backoff multiplier

    set_allow_origin = "http://localhost:4200,https://smconf.gikace.dev, https://smconf-test.web.app"

    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "password")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "auth_api_db")
    SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


    INSTANCE_CONNECTION_NAME: str = os.getenv("INSTANCE_CONNECTION_NAME", None)
    UNIX_SOCKET: str = os.getenv("INSTANCE_UNIX_SOCKET", '/cloudsql/')
    PROJECT_ID: str = os.getenv("PROJECT_ID", "smartconference-404416")
    BUCKET_NAME: str = os.getenv("BUCKET_NAME", "developers-bucket")
    IMAGE_PATH: str = os.getenv("IMAGE_PATH", "developers-bucket/test-app/file_path/media/images")
    DOCUMENT_PATH: str = os.getenv("DOCUMENT_PATH", "developers-bucket/test-app/file_path/docs")
    AUDIO_PATH: str = os.getenv("AUDIO_PATH", "developers-bucket/test-app/file_path/media/audios")
    VIDEO_PATH: str = os.getenv("VIDEO_PATH", "developers-bucket/test-app/file_path/media/videos")
    SHOW_DOCS: str = os.getenv("SHOW_DOCS", True)
    ALLOW_ORIGINS: str = os.getenv("ALLOW_ORIGINS", set_allow_origin)
    SET_NEW_ORIGIN : list = ALLOW_ORIGINS.split(',')
    SYSTEM_LOGO: str = os.getenv("SYSTEM_LOGO", "https://storage.googleapis.com/developers-bucket/developers-bucket/smart-conference-app/flyers/GI-KACE-Logo.jpeg")




    MAIL_USERNAME: str = os.getenv("MAIL_USERNAME", 'dev.aiti.com.gh@gmail.com')
    MAIL_PASSWORD: str = os.getenv("MAIL_PASSWORD", 'palvpbokbnisspps') #uefuovgtfwyfgskv previous password
    MAIL_FROM: str = os.getenv("MAIL_FROM", "dev.aiti.com.gh@gmail.com")
    MAIL_PORT: int = os.getenv("MAIL_PORT", 587)
    MAIL_SERVER: str = os.getenv("MAIL_SERVER", 'smtp.gmail.com')
    MAIL_STARTTLS: bool = True
    MAIL_SSL_TLS: bool = os.getenv("MAIL_SSL_TLS", False)
    USE_CREDENTIALS: bool = True
    VALIDATE_CERTS: bool = True






    FRONTEND_URL: str = os.getenv("FRONTEND_URL", "https://smconf-test.web.app")


    EMAIL_CODE_DURATION_IN_MINUTES: int = 15
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 2700
    REFRESH_TOKEN_DURATION_IN_MINUTES: int =  2592000
    REFRESH_TOKEN_REMEMBER_ME_DAYS: int = 5184000  # or any appropriate value
    COOKIE_ACCESS_EXPIRE = 1800
    COOKIE_REFRESH_EXPIRE = 2592000 # 1 Month
    COOKIE_DOMAIN: str = os.getenv("COOKIE_DOMAIN", "gikace.dev")
    PASSWORD_RESET_TOKEN_DURATION_IN_MINUTES: int = 15
    ACCOUNT_VERIFICATION_TOKEN_DURATION_IN_MINUTES: int = 15
    

    POOL_SIZE: int = 20
    POOL_RECYCLE: int = 3600
    POOL_TIMEOUT: int = 15
    MAX_OVERFLOW: int = 2
    CONNECT_TIMEOUT: int = 60
    connect_args = {"connect_timeout":CONNECT_TIMEOUT}

    JWT_SECRET_KEY : str = secrets.token_urlsafe(32)
    REFRESH_TOKEN_SECRET_KEY : str = secrets.token_urlsafe(32)
    ALGORITHM: str = "HS256"

    class Config:


        env_file = './.env'

settings = Settings()