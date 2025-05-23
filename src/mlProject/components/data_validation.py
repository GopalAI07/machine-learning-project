import os 
from src.mlProject import logger
import pandas as pd
from src.mlProject.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validation_all_columns(self) -> bool:

        try: 

           validation_status = True

   

           data = pd.read_csv(self.config.unzip_data_dir)

           all_cols = list(data.columns)

   

           all_schema = self.config.all_schema.keys()

           for col in all_cols:

               if col not in all_schema:

                   validation_status = False

                   with open(self.config.STATUS_FILE, 'w') as f:

                       f.write(f"validation status : {validation_status}")

                   break

           else:

               with open(self.config.STATUS_FILE, 'w') as f:

                   f.write(f"validation status : {validation_status}")

           return validation_status

             

        except Exception as e:

               raise e  





    # def validation_all_column(self)->bool:
    #     try: 
    #        validation_status = True
   
    #        data = pd.read_csv(self.config.unzip_data_dir)
    #        all_cols = list(data.columns)
   
    #        all_schema = self.config.all_schema.keys()

    #       for col in all_cols:
    #           if col not in all_schema:
    #                  validation_status=False
    #                  with open(self.config.Status_FILE, 'w') as f:
    #                      f.write(f"validation status : {validaton_status}")
    #           else:
    #                  validation_status=True
    #                  with open(self.config.Status_FILE, 'w') as f:
    #                      f.write(f"validation status : {validaton_status}")
             
    #        return validation_status
             
    #     except Exception as e:
    #            raise e  

      