#logger/cloud_watch_logger.py
import logging
import watchtower
import boto3

class cloudWatchLogger():

    def __init__(self,log_group:str,aws_region:str,logger_name:str,stream_name:str,logging_level:int=logging.DEBUG) -> None:
        self.log_group = log_group
        self.aws_region=aws_region
        self.logger_name = logger_name
        self.logging_level = logging_level
        self.stream_name= stream_name

    def set_logger(self):
        self.logger = logging.getLogger(self.logger_name)
        self.logger.setLevel(self.logging_level)  # Set the logger level to DEBUG to capture all levels

    def add_cw_handler(self):
        
        cw_handler = watchtower.CloudWatchLogHandler(log_group=self.log_group,boto3_client=boto3.client("logs", region_name=self.aws_region),stream_name=self.stream_name)        
        self.logger.addHandler(cw_handler)        
    
    def add_stream_handler(self):
        # Create a console handler to log to the terminal
        self.logger.addHandler(logging.StreamHandler())

    def create_cw_logger(self):
        self.set_logger()
        self.add_stream_handler()
        self.add_cw_handler()
        return self.logger
