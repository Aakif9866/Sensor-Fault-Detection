import sys
import os
import pandas as pd
import pickle
import yaml

from src.constants import *
from src.exception import CustomException
from src.logger import logging


# copied directly from the resources given 



class MainUtils:
    # nothing to do with constructor as these are static methods
    def __init__(self) -> None:
        pass


    def read_yaml_file(self, filename: str) -> dict:
        try:
            with open(filename, "rb") as yaml_file:
                return yaml.safe_load(yaml_file)

        # in every step we are using try except 
        # to avoid error not handled
        
        # also along with exception handler logger is also there which helps in logging
        
        except Exception as e:
            raise CustomException(e, sys) from e


    def read_schema_config_file(self) -> dict:
        try:
            schema_config = self.read_yaml_file(os.path.join("config", "schema.yaml"))
            
            return schema_config


        except Exception as e:
            raise CustomException(e, sys) from e


   

    # static method is a method which is related to the class rather than an instance
    @staticmethod
    def save_object(file_path: str, obj: object) -> None:
        logging.info("Entered the save_object method of MainUtils class")


        try:
            with open(file_path, "wb") as file_obj:
                pickle.dump(obj, file_obj)


            logging.info("Exited the save_object method of MainUtils class")


        except Exception as e:
            raise CustomException(e, sys) from e


   


    @staticmethod
    def load_object(file_path: str) -> object:
        logging.info("Entered the load_object method of MainUtils class")


        try:
            with open(file_path, "rb") as file_obj:
                obj = pickle.load(file_obj)


            logging.info("Exited the load_object method of MainUtils class")


            return obj


        except Exception as e:
            raise CustomException(e, sys) from e
   
    @staticmethod    
    def load_object(file_path):
        try:
            with open(file_path,'rb') as file_obj:
                return pickle.load(file_obj)
        except Exception as e:
            logging.info('Exception Occured in load_object function utils')
            raise CustomException(e,sys)