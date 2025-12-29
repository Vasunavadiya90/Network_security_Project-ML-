from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exceptions.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig , dataValidationConfig,DataTransformationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.data_validation import DataValidation
if __name__=='__main__':
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)

        logging.info('initiate the data ingestion')
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion completed")
        print(dataingestionartifact)


        data_validation_config = dataValidationConfig(trainingpipelineconfig)
        data_validation =  DataValidation(dataingestionartifact,data_validation_config)
        logging.info("initiate the data validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("data validation completed")
        print(data_validation_artifact)

        data_transformation_config = DataTransformationConfig(trainingpipelineconfig)
        logging.info("data transformation config started")
        data_transformation = DataTransformation(data_validation_artifact , data_transformation_config)
        data_transformation_artifact =  data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("Data transformation completed")
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
    