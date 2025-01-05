import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "your_default_secret_key")
    UPLOAD_FOLDER = os.environ.get("UPLOAD_FOLDER", "./uploaded_docs")
    ALLOWED_EXTENSIONS = {"txt"}
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False


class TestingConfig(Config):
    DEBUG = False
    TESTING = True
    UPLOAD_FOLDER = "./test_uploads"


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY")


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}
