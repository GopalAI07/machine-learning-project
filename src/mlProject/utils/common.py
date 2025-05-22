import os
from box.exceptions import BoxValueError
import yaml
from src.mlProject import logger
import json
import joblib
from ensure import ensure_annotiations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotiations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
       with open (path_to_yaml) as yaml_file:
         content=yaml.safe_load(yaml_file)
         logger.info(f"yaml file: {path_to_yaml} loaded successfully")
         return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
       raise e

@ensure_annotiations
def create_directories(path_to_directories:list, verbsoe=True):
    for path in path_to_directories:
      os.makedirs(path,exist_ok=True) 
      if verbsoe:
        logger.info(f"created directory at: {path}")

@ensure_annotiations
def save_json(path:Path,date:dict):
    with open(path,"w") as f:
      json.dump(date,f,indent=4)
    
    logger.info(f"json file saved at : {path}")

@ensure_annotiations
def load_json(path:Path)-> ConfigBox:
  with open(path) as f:
    content = json.load(f)
  
  logger.info(f"json file loaded successfully from : {path}")
  return ConfigBox(content)

@ensure_annotiations
def save_bin(data: Any , path:Path):
  joblib.dump(value=data, filename=path)
  logger.info(f"binary file saved at:{path}")

@ensure_annotiations
def load_bin(path:Path)->Any:
  data = joblib.load(path)
  logger.info(f"binary file loaded from: {path}")
  return data

@ensure_annotiations
def get_size(path:Path)->str:
  size_in_kb=round(os.path.getsize(path)/1024)
  return f"~ {size_in_kb} kb"

