from .cloud_watch_logger import cloudWatchLogger
from .utils import create_log_stream_name ,load_logging_config

config = load_logging_config('logger/logging_config.yaml')

# Access the values from the YAML file
aws_region = config['aws']['region']
log_group = config['aws']['log_group']
logger_name = config['app_logger']['name']
logging_level = config['app_logger']['level']

stream_name = create_log_stream_name(logger_name)

logger = cloudWatchLogger(log_group,aws_region,logger_name,stream_name,logging_level)
logger = logger.create_cw_logger()
