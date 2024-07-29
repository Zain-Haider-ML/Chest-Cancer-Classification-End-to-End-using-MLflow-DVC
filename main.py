from FineTunedClassifier import logger
from src.FineTunedClassifier.pipeline.stage_01_prepare_base_model import PrepareBaseModelTrainingPipeline




STAGE_NAME = "Prepare base model"


try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
