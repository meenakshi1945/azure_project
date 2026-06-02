import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    # Azure Blob Storage settings
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'ENTER_STORAGE_ACCOUNT_NAME'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'ENTER_BLOB_STORAGE_KEY'
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'ENTER_IMAGES_CONTAINER_NAME'

    # Azure SQL Database settings
    SQL_SERVER = os.environ.get('SQL_SERVER')
    SQL_DATABASE = os.environ.get('SQL_DATABASE')
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME')
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD')

    if SQL_SERVER and SQL_DATABASE and SQL_USER_NAME and SQL_PASSWORD:
        SQLALCHEMY_DATABASE_URI = (
            f'mssql+pyodbc://{SQL_USER_NAME}:{SQL_PASSWORD}'
            f'@{SQL_SERVER}:1433/{SQL_DATABASE}?driver=ODBC+Driver+17+for+SQL+Server'
        )
    else:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Microsoft sign-in settings
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET") or "ENTER_CLIENT_SECRET_HERE"
    CLIENT_ID = os.environ.get("CLIENT_ID") or "ENTER_CLIENT_ID_HERE"
    AUTHORITY = "https://login.microsoftonline.com/common"
    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]
    SESSION_TYPE = "filesystem"
    SESSION_FILE_DIR = os.path.join(basedir, 'flask_session')
    USE_FLASK_SESSION = os.environ.get('USE_FLASK_SESSION') == 'true'
