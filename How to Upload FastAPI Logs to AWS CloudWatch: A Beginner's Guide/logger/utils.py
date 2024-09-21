import re
from datetime import datetime
import yaml

def create_log_stream_name(logger_name: str) -> str:
    # Sanitize the logger name: remove invalid characters
    sanitized_name = re.sub(r'[^a-zA-Z0-9_-]', '_', logger_name)
    
    # Get the current date in the desired format
    timestamp = datetime.now().strftime('%y-%m-%d')

    # Create the log stream name
    log_stream_name = f"{sanitized_name}-{timestamp}"
    return log_stream_name

def load_logging_config(file_path:str):
    # Load the YAML configuration file
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)

    return config
