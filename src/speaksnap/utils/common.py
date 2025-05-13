import os
import yaml
from src.speaksnap import logger
import json
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError
import numpy as np

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input
    
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def save_json(path: Path, data:dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    
    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file
    
    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)
    
    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def create_directories(path_to_directories:list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directioy at: {path}")

@ensure_annotations
def save_numpy_array(file_path: str, array: np.array):
    """Save numpy array to file path

    Args:
        file_path (str): Path to save array
        array (numpy array): Array to save

    Returns:
        None  
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "wb") as file:
        np.save(file, array)
    logger.info(f"Numpy array saved at {file_path}")

@ensure_annotations
def load_numpy_array(file_path: str) -> np.ndarray:
    """Load numpy array from file path

    Args:
        file_path (str): Path to load array from

    Returns:
        np.ndarray: Loaded array
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"No file found at {file_path}")
    
    with open(file_path, "rb") as file:
        array = np.load(file)
    
    logger.info(f"Numpy array loaded from {file_path}")
    return array
