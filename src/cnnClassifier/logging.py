import os
import sys
import logging
from datetime import datetime

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs"
log_filename = f"running_logs_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')}.log"
log_filepath = os.path.join(log_dir, log_filename)

os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ])

logger = logging.getLogger("cnnClassifierLogger")