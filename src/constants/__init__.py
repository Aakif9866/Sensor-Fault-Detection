import os

# yet to be filled by mongo keys , aws keys etc etc

MONGO_DATABASE_NAME = "SensorFaultDetection2"
MONGO_COLLECTION_NAME = "waferFault2"
TARGET_COLUMN='quality'

MODEL_FILE_NAME = "model"

MODEL_FILE_EXTENSION = '.pkl'


artifact_folder = "artifacts"


MONGO_DB_URL = "mongodb+srv://aakif:fXHmx25n&0@cluster0.qfqxm.mongodb.net/?retryWrites=true&w=majorit&appName=Cluster0"