import sys,os
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation

if __name__ == "__main__":
    data_ingestion_obj = DataIngestion()
    feature_file_path = data_ingestion_obj.initiate_data_ingestion()
    
    data_tranformation_obj = DataTransformation(feature_store_file_path=feature_file_path)
    train_arr, test_arr, preprocessor_path = data_tranformation_obj.initiate_data_transformation()