import os
import sys
from pathlib import Path
#sys.path.append("..")  # Adds the parent directory to the sys.path
sys.path.append(str(Path(__file__).parent.parent.parent))
#sys.path.append('../src')

from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
# dataclasses introduced in py 3.9,provides a decorator which implicitly adds method such as __init__(),__repr__(), __eq__() to a user defned class. Since no need to use init i can diectly define the class variables.Making code readable.

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion component")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info("reading the csvdataset as pdDataFrame for now ..later mongo")
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            
            logging.info("Initializing train-test split")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=40)
            
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("DataIngestion concludes")
            
            return(self.ingestion_config.train_data_path,self.ingestion_config.test_data_path)            
            
        except Exception as e:
            raise CustomException(e,sys)
        
# initializing & running. Artifact folder created
if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()
            
            