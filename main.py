from Insurance.logger import logging
from Insurance.exception import InsuranceException
from Insurance.utils import get_collection_as_dataframe
import sys, os
from Insurance.entity.config_entity import DataIngestionConfig
from Insurance.entity import config_entity
from Insurance.components.data_ingestion import DataIngestion
from Insurance.components.data_validation import DataValidation
from Insurance.components.model_trainer import ModelTrainer
from Insurance.components.data_transformation import DataTransformation
from Insurance.components.model_evaluation import ModelEvaluation
from Insurance.components.model_pusher import ModelPusher

#def test_logger_and_expection():
   # try:
       # logging.info("Starting the test_logger_and_exception")
        #result = 3/0
       # print(result)
       # logging.info("Stoping the test_logger_and_exception")
    #except Exception as e:
      #  logging.debug(str(e))
       # raise InsuranceException(e, sys)

if __name__=="__main__":
     try:
          #start_training_pipeline()
          #test_logger_and_expection()
       # get_collection_as_dataframe(database_name ="INSURANCE", collection_name = 'INSURANCE_PROJECT')
       training_pipeline_config = config_entity.TrainingPipelineConfig()
       
     except Exception as e:
          print(e)