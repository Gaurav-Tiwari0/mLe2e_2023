import sys
from src.logger import logging

#inside execution_info you'd find tb_frame,filecode then filename
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line# [{1}] error-message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message, error_detail)
#super() object
    def __str__(self):
        return self.error_message

#checking. 2positional arguments required,error_message and error_detail
if __name__=="__main__":

    try:
        a=10/0
    except Exception as err:
        logging.info("Dividing by zero not allowed")
        raise CustomException(err,sys)
        