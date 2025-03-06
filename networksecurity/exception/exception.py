'''import sys
from src.logger import logging


def error_message_details(error,error_details:sys):
    _,_,exc_tb=error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))

    return error_message

    

class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_details=error_details)

    def __str__(self):
        return self.error_message'''

import sys
from networksecurity.logging import logger

def error_message_details(error: Exception, error_details: sys):
    """Extracts and formats detailed error messages including script name and line number."""
    _, _, exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in script [{file_name}] at line [{exc_tb.tb_lineno}]: {str(error)}"
    return error_message

class NetworkSecurityException(Exception):
    def __init__(self, error: Exception, error_details: sys):
        super().__init__(str(error))
        self.error_message = error_message_details(error, error_details)
        
        # Logging the exception
        logger.error(self.error_message)

    def __str__(self):
        return self.error_message
    


    

