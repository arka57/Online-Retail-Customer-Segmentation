import logging
import os
from datetime import datetime

#Creating logs directory to store in log files
LOG_DIR="logs"
LOG_DIR=os.path.join(os.getcwd(),LOG_DIR)

#Creating log directory if it doesn't exist
os.makedirs(LOG_DIR,exist_ok=True)

#Creating file name for log file based on current timestamp
CURRENT_TIME_STAMP=f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
file_name=f"log_{CURRENT_TIME_STAMP}.log"

#output= log_2023_07_12_4_3_2.log

#Creating log file path
log_file_path=os.path.join(LOG_DIR,file_name)

logging.basicConfig(filename=log_file_path,
                    filemode='w',
                    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)