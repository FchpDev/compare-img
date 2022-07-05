import urllib.parse
# ========== DB config ==========
# ========== DB program =========
DB_SV_SERVICE='postgresql'
DB_SV_SERVER='localhost'
DB_SV_PORT='5432'
DB_SV_USER='postgres'
DB_SV_PASS='Hello1234'
DB_SV_NAME='postgres'

# ========== DB user ============
DB_SERVICE='mssql+pymssql'
DB_SERVER='172.31.80.2'
DB_PORT='1433'
DB_USER='siscoweb'
DB_PASS=urllib.parse.quote_plus('siscoweb2001')

DB_NAME_SISCO='SISCO_BATC_WEB'
DB_NAME_NTS='nts'
DB_NAME_SCSC='scsc'

DB_URI='{}://{}:{}@{}:{}/{}'.format(DB_SV_SERVICE,DB_SV_USER,DB_SV_PASS,DB_SV_SERVER,DB_SV_PORT,DB_SV_NAME)
DB_URI_SISCO='{}://{}:{}@{}:{}/{}'.format(DB_SERVICE,DB_USER,DB_PASS,DB_SERVER,DB_PORT,DB_NAME_SISCO)
DB_URI_NTS='{}://{}:{}@{}:{}/{}'.format(DB_SERVICE,DB_USER,DB_PASS,DB_SERVER,DB_PORT,DB_NAME_NTS)
DB_URI_SCSC='{}://{}:{}@{}:{}/{}'.format(DB_SERVICE,DB_USER,DB_PASS,DB_SERVER,DB_PORT,DB_NAME_SCSC)

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1440


PATH_IMAGE_DATA = "C:\\darknet_billet_ocr\\CiraCore\\billet_image\\ciracore\\"
PATH_IMAGE_BILLET_FACTORY1="C:\\darknet_billet_ocr\\CiraCore\\billet\\billet_crop\\"
PATH_IMAGE_BILLET_FACTORY2="C:\\darknet_billet_ocr\\CiraCore\\billet\\billet_crop_factory2\\"
#PATH_IMAGE_BILLET_FACTORY3="C:\\darknet_billet_ocr\\CiraCore\\billet\\billet_crop_factory3\\"
PATH_IMAGE_BILLET_FACTORY3="C:\\darknet_billet_ocr\\CiraCore\\TATA_OCR\Factory3\cold\ocr\\"
PATH_IMAGE_HOT_BILLET_FACTORY1="C:\\darknet_billet_ocr\\CiraCore\\billet\\hot_billet_factory1\\"
PATH_IMAGE_HOT_BILLET_FACTORY2="C:\\darknet_billet_ocr\\CiraCore\\billet\\hot_billet_factory2\\"
#PATH_IMAGE_HOT_BILLET_FACTORY3="C:\\darknet_billet_ocr\\CiraCore\\billet\\hot_billet_factory3\\"
PATH_IMAGE_HOT_BILLET_FACTORY3="C:\\darknet_billet_ocr\\CiraCore\\TATA_OCR\\Factory3\hot\ocr\\"
PATH_IMAGE_DATA_FACTORY1="C:\\darknet_billet_ocr\\CiraCore\\billet_image\\ciracore\\"
PATH_IMAGE_DATA_FACTORY2="C:\\darknet_billet_ocr\\CiraCore\\billet_image\\ciracore_factory2\\"
#PATH_IMAGE_DATA_FACTORY3="C:\\darknet_billet_ocr\\CiraCore\\billet_image\\ciracore_factory3\\"
PATH_IMAGE_DATA_FACTORY3="C:\\darknet_billet_ocr\\CiraCore\\TATA_OCR\\Factory3\\image_data"
PATH_IMAGE_TEMP="C:\\darknet_billet_ocr\\CiraCore\\billet\\image_temp"

# ADD BY First
PATH_BACKUP_IMAGE_BILLET_FACTORY1=""
PATH_BACKUP_IMAGE_BILLET_FACTORY2=""
PATH_BACKUP_IMAGE_BILLET_FACTORY3="C:\\darknet_billet_ocr\\CiraCore\\TATA_OCR\\Factory3\\cold\\backup\\"
PATH_BACKUP_IMAGE_HOT_BILLET_FACTORY1=""
PATH_BACKUP_IMAGE_HOT_BILLET_FACTORY2=""
PATH_BACKUP_IMAGE_HOT_BILLET_FACTORY3="C:\\darknet_billet_ocr\\CiraCore\\TATA_OCR\\Factory3\\hot\\backup\\"

#Redis
CHANNEL = 'stream' 

# ========== BILLET/OCR config ============
OCR_CONFIDENCE=50
OCR_MAX_BILLET_NO=25

BILLET_WIDTH=220
BILLET_HEIGH=130
MAX_BILLET_WIDTH=450
#BILLET_WIDTH=380
#BILLET_HEIGH=270
#MAX_BILLET_WIDTH=450

list_of_image_path=["",
                    PATH_IMAGE_BILLET_FACTORY1, 
                    PATH_IMAGE_BILLET_FACTORY2,
                    PATH_IMAGE_BILLET_FACTORY3]
list_of_image_hot_billet_path=["",
                    PATH_IMAGE_HOT_BILLET_FACTORY1, 
                    PATH_IMAGE_HOT_BILLET_FACTORY2,
                    PATH_IMAGE_HOT_BILLET_FACTORY3]
list_of_data_path= ["",
                    PATH_IMAGE_DATA_FACTORY1,
                    PATH_IMAGE_DATA_FACTORY2, 
                    PATH_IMAGE_DATA_FACTORY3]

# ADD BY First
list_of_backup_image_path= ["",
                            PATH_BACKUP_IMAGE_BILLET_FACTORY1,
                            PATH_BACKUP_IMAGE_BILLET_FACTORY2,
                            PATH_BACKUP_IMAGE_BILLET_FACTORY3]
list_of_backup_hot_image_path= ["",
                                PATH_BACKUP_IMAGE_HOT_BILLET_FACTORY1,
                                PATH_BACKUP_IMAGE_HOT_BILLET_FACTORY2,
                                PATH_BACKUP_IMAGE_HOT_BILLET_FACTORY3]
