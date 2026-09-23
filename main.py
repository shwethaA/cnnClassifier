from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from cnnClassifier.logging import logger

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f"******** {STAGE_NAME} started *********")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f"******** {STAGE_NAME} completed ********* \n\n")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model stage"
try:
    logger.info(f"******** {STAGE_NAME} started *********")
    prepare_base_model = PrepareBaseModelPipeline()
    prepare_base_model.main()
    logger.info(f"******** {STAGE_NAME} completed ********* \n\n")
except Exception as e:
    logger.exception(e)
    raise e

