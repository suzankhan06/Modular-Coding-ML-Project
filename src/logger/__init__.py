import logging
import os, sys
from datetime import datetime

LOG_DIR = "logs"

# we need to make folder where we want to save in the main working porject dir to join 

LOG_DIR = os.path.join(os.getcwd(), LOG_DIR)

#create log_dir folder
os.makedirs(LOG_DIR, exist_ok=True)

# creating file with .log log_2024_

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
file_name = f"log_{CURRENT_TIME_STAMP}.log"

#output log_2024_ -7-3-3-4-5-.log

#now join all the variables created

log_file_path = os.path.join(LOG_DIR, file_name)

#create log now

logging.basicConfig(filename = log_file_path,
                    filemode = "w",
                    format ='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO )