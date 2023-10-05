import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s] : %(message)s:')

project_name = 'TextSummarizer'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]


for filepath in list_of_files:
    filepath = Path(filepath) # it will convert file path according to os
    filedir,filename = os.path.split(filepath) # split path into filename and directory

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'creating directory:{filedir} for file {filename}')
    
    # get size is used to check whether a given filepath contains data or not if not it will create a file
    # if filepath is already present and size=0 it will overwrite file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f'creating empty file:{filepath}')

    else:
        logging.info(f'{filepath} already exists')