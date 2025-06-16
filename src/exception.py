# after creating logger 
# we need to create the ( custom ) exception handler

# improved debugger from chatgpt

import sys

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()  # Extract traceback details
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get file where error occurred
    error_message = "Error occurred in python script [{0}] at line [{1}]: {2}".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error, error_detail: sys):
        super().__init__(str(error))  # Store original error message
        self.error_message = error_message_detail(error, error_detail)

    def __str__(self):
        return self.error_message
    
    
# old debugger 
# import sys


# def error_message_detail(error, error_detail:sys):
#     _,_,exc_tb = error_detail.exc_info()
#     file_name = exc_tb.tb_frame.f_code.co_filename
#     error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}] ".format(
#         file_name,exc_tb.tb_lineno,str(error)
#     )
    
#     return error_message
    

# class CustomException(Exception):
#     def __init__(self,error_message,error_detail : sys):
#         super().__init__(error_message)
#         self.error_message = error_message_detail(
#             error_message,error_detail=error_detail
#         )
        
#     def __str__(self):
#         return self.error_message
    
