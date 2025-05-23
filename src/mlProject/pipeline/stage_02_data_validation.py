from src.mlProject.config.configuraton import ConfigurationManager
from src.mlProject.components.data_validation import DataValidation
from src.mlProject import logger

STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        data_validation_config = config.get_data_validataion_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validation_all_columns()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")
    except Exception as e:
        logger.exception(e)
        raise e