import sys,os
from src.components.data_ingestion import DataIngestion

if __name__ == "__main__":
    obj = DataIngestion()
    feature_file_path = obj.initiate_data_ingestion