import os
from pathlib import Path
import logging 

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s: ')

project_name="textSummarizer"
list_of_files =[
    ".gihub/workflows/.gitkeep"
        f"src/{project_name}/__init__.py",
        f"src/{project_name}/components/__init__.py",
        f"src/{project_name}/utils/__init__.py",
        f"src/{project_name}/utils/common.py",
        f"src/{project_name}/logging/__init__.py",
        f"src/{project_name}/config/__init__.py",
        f"src/{project_name}/config/configuration.py",
        f"src/{project_name}/pipelines/__init__.py",
        f"src/{project_name}/entitie/__init__.py",
        f"src/{project_name}/consonants/__init__.py",
        "config/config.yaml",
        "param.yamal",
        "app.py",
        "main.py"
        "Dockerfile"
        "requirements.txt",
        "setup.py",
        "reasearch/trials.ipynb",
        "test.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")