from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from cnnClassifier.logging import logger

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f"******** stage {STAGE_NAME} started *********")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f"******** stage {STAGE_NAME} completed ********* \n\n")
except Exception as e:
    logger.exception(e)
    raise e
