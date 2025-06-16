import sys
import os
import numpy as np
import pandas as pd
from pymongo import MongoClient
from zipfile import Path
from src.constants import * # get everything from constants
from src.exception import CustomException
from src.logger import logging
from src.utils.main_utils import MainUtils
from dataclasses import dataclass

# look through plan image to understand how each of the class works 

@dataclass
class DataIngestionConfig:
    artifact_folder = os.path.join(artifact_folder) # this comes from constants

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.utils = MainUtils()
    
    def export_collection_as_dataframe(self,collection_name,db_name):
        
        try:
            mongo_client = MongoClient(MONGO_DB_URL)
            collection = mongo_client[db_name][collection_name]
            df = pd.DataFrame(list(collection.find()))
            
            if "_id" in  df.columns.tolist():
                df = df.drop(columns=['_id'],axis=1) # remove this column
            # replce null values
            df.replace({"na":np.nan},inplace=True)
            
            return df
        except Exception as e:
            raise CustomException(e,sys)
    
    
    def export_data_into_feature_store_file_path(self)->pd.DataFrame:
        try:
            logging.info(f"exporting data from mongodb")
            raw_file_path = self.data_ingestion_config.artifact_folder
            # this object has another file path ie the artifact folder
            
            # now in above file path make directory
            os.makedirs(raw_file_path,exist_ok=True) # if this is true dont throw and error
            
            sensor_data = self.export_collection_as_dataframe(
                collection_name=MONGO_COLLECTION_NAME,
                db_name=MONGO_DATABASE_NAME
                # these are the only parameters needed
            )
            
            logging.info(f"saving data into feature store file path :{raw_file_path}")
            
            feature_store_file_path = os.path.join(raw_file_path,"wafer_fault.csv")
            
            sensor_data.to_csv(feature_store_file_path,index=False)
            
            return feature_store_file_path
        except Exception as e:
            raise CustomException(e,sys)
        
        
    def initiate_data_ingestion(self)->Path:
        
        logging.info("Entered initiate_data_ingestion method of DataIngestion class")
        try:
            feature_store_file_path = self.export_data_into_feature_store_file_path()
            
            logging.info("got the data from mongo db")
            
            logging.info("exited initiate_data_ingestion method from dataingestion class")
                      
            return feature_store_file_path
        except Exception as e:
            raise CustomException(e,sys)
        
            
            
    
        
        
