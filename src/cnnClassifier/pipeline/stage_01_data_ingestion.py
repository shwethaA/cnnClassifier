from cnnClassifier.config import ConfigurationManager
from cnnClassifier.components import DataIngestion
from cnnClassifier.logging import logger

class  DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config_mgr = ConfigurationManager()
        data_ingestion_config = config_mgr.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.unzip_and_clean()
