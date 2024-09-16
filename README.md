# PROJECT DESCRIPTION
This help you with Authentication with JWT token and cookie authentication.
Implementation of Role Based Access Control(RBAC)
High security features with login attempts. User is limited to 3 chances of successful login.
After every login attempt, the user has to wait for the 10 minutes before continuing.
After the 3 chances is consumed, an email will be sent to the user to contact the system administrator for reactivation of account.
Show intruder to the system administrator.
User Management: Sends a reset password email to new users.
User can request a reset password.
Update password with reset password token.
Upload and delete files from Google Cloud Storage

## Ready to set up the project:
    git clone https://github.com/GI-KACE-DEV/auth-api-skeleton.git

## Installing Packages for Windows
- Run the following command in your terminal
    - cd backend
    - cd app
    - pip install -r requirements.txt


## CREATION OF DATABASE MANUALLY
>  Create a database name: **auth_api_db**



## RUNNING OR STARTING APPLICATION
- Running FastAPI Service Locally
    - uvicorn main:app --reload



## Installing Packages for Linux, Ubuntu
- Run the following command in your terminal
    - cd backend
    - cd app
    - python3 -m venv venv
    - source venv/bin/activate
    - pip install -r requirements.txt
    - uvicorn main:app --reload
