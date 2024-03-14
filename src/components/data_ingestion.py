# This script represents a structured approach to handle data ingestion pipeline in the ML project, separating concerns into distinct classes and methods, and providing configurable options for file paths and logging.

# os, Sys: for interacting with the operating system and system-specific parameters and functions.
import os
import sys  #to use the CustomException,logging classes from exception& logger files in src directory
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass #Imports the dataclass decorator from the dataclasses module, used for creating classes with automatically generated special methods.

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

''' In data ingestion, whenever we are performing the data ingestion component, there should be some inputs that may be probably required by this data ingestion component. The input can be like where I have to probably save the training data, where to save the test data, where to save the raw data, or any kind of inputs to the data ingestion will basically be creating in a class, try to mention it as DataIngestionConfig class. The output can be anything, it can be a numpy array, it can be a file
saved in some folder, it can be multiple things as u like. 
'''

@dataclass #this decorator is quite amazing, because inside a class to define the class variables you basically use __init__, but if you use this dataclass @decorator, you will be able to define your class variable directly.

# DataIngestionConfig is defined to hold configuration parameters related to data ingestion, such as file paths for training, testing, and raw data.
class DataIngestionConfig:
    # Default values are provided for the file paths, with the os.path.join() function used to construct platform-independent file paths. so that my o/p will be saved on them.
    train_data_path: str=os.path.join('artifacts',"train.csv") #So, train_data_path is set to the file path 'artifacts/train.csv', where 'artifacts' is a directory containing the training data file named 'train.csv'.
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:    # This class manages the data ingestion process.
    def __init__(self):  # It initializes with an instance of DataIngestionConfig to access configuration parameters. Note that we didn't use decorator, as we will use functions later inside this class, so it's suggested to use __init__
        self.ingestion_config=DataIngestionConfig() #The upper 3pathes variables will be saved on it

    def initiate_data_ingestion(self): # the main function that performs data ingestion.
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            # keep on writing the logs because it is important, because anywhere the exception happens, we'll be able to understand which line the exception is basically happening.
            logging.info('Read the dataset as dataframe')
            ''' Next line creates the directory structure needed to store the training data file.
            - os.makedirs(): It will create all the directories in the specified path, including any missing parent directories.
            - os.path.dirname(self.ingestion_config.train_data_path):Extract the directory path from the train_data_path attribute of the DataIngestionConfig object (self.ingestion_config). 
            - os.path.dirname() returns the directory component of the specified path.
            - exist_ok=True: tells os.makedirs() to not raise an exception if the directory already exists. If exist_ok is set to True and the directory already exists, the function will not raise an error; otherwise, it will raise a FileExistsError. 
            - If the directories already exist, it doesn't do anything. If they don't exist, it creates them. This helps ensure that the directory structure is ready for writing the training data file.'''
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            # Save the DataFrame 'df' to a CSV file located at the path specified by 'self.ingestion_config.raw_data_path', without including row names 'index' & with column names as the header.
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Inmgestion of the data iss completed")

            return(
                # Return those data so that the next step: Data Transformation can use them
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
# Main Execution Block:
if __name__=="__main__":
    # Instantiates a DataIngestion object and calls its initiate_data_ingestion() method to perform data ingestion and retrieve the paths of the generated training and testing data files.
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    # Initializes a DataTransformation object to perform data transformation.
    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    # Initializes a ModelTrainer object to train a machine learning model. & Calls the initiate_model_trainer() method of the ModelTrainer object to initiate the model training process.
    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))



