import os

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5502855202:AAGW3MYUov5Gb2wWgpcaNTgxDjZ98IFh4P8")
    
    API_ID = int(os.environ.get("API_ID", "6534707"))
    
    API_HASH = os.environ.get("API_HASH" , "4bcc61d959a9f403b2f20149cbbe627a")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 50000000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 50000000
    
    CHUNK_SIZE = int(128)

    HTTP_PROXY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "1430593323"))

    SESSION_NAME = "UploadLinkToFileBot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Uploader:Uploader@cluster0.ba0ppxa.mongodb.net/?retryWrites=true&w=majority")

    MAX_RESULTS = "50"
