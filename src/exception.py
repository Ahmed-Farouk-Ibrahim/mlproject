# This code defines a custom exception class CustomException and a helper function error_message_detail for generating detailed error messages, making it easier to debug and handle errors in your Python scripts.

import sys # sys module in Python: Used for accessing information about Python runtime environment. It provides various functions and variables that are used to manipulate different parts of the Python runtime environment. So any exception that is about getting control, the sys Library will automatically have that information.
from src.logger import logging  # src.logger.logging: Importing a custom logging module (assuming it's defined elsewhere in your project).

# Next function takes an error object and error details (from sys.exc_info()) as input.
#  here I'm going to give 2 input parameters: error: 1. The error object or message. and 2-error_detail: Additional details about the error, typically obtained from sys.exc_info()., so whenever an exception gets raised, I want to push this on my own custom message:
def error_message_detail(error,error_detail:sys):
    # Extract information about the file name, line number, and error message where the exception occurred. 
    # Next line Extracts information about the current exception. exc_info() returns a tuple representing the current exception being handled, and it contains three elements: the exception type, the exception value, and the traceback object.
    _,_,exc_tb=error_detail.exc_info()

    # This accesses the file name where the exception occurred from the traceback object (exc_tb). It retrieves the filename associated with the code object (f_code) of the traceback's frame.
    file_name=exc_tb.tb_frame.f_code.co_filename

    # It formats this information into a string and returns it.
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(file_name,exc_tb.tb_lineno,str(error))

    return error_message

    
# Next class is a custom exception class that inherits from the built-in Exception class. It overrides the __init__ method to initialize the exception with an error message and error detail.
class CustomException(Exception):

    '''Inside the __init__ method, it calls the error_message_detail function to generate a detailed error message. It takes three parameters:  1- self: A reference to the instance of the class. 
    2- error_message: The error message or object.
    3- error_detail: Additional details about the error, typically obtained from sys.exc_info().
    '''
    def __init__(self,error_message,error_detail:sys):

        # Calling the Parent Constructor: Next line calls the constructor of the superclass (Exception in this case) and initializes the exception with the provided error_message. It ensures that the base behavior of the Exception class is properly initialized.
        super().__init__(error_message)

        # Creating Custom Error Message: Next line invokes the error_message_detail function to generate a custom error message based on the provided error message and additional error details. It assigns this custom error message to the error_message attribute of the instance (self). This custom error message contains detailed information about where the error occurred, such as the filename and line number, along with the original error message.
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    
    # def __str__(self): This is a special method in Python classes that is invoked when the instance is converted to a string, typically by calling str(instance). It takes only one parameter, self, which refers to the instance itself. It overrides the __str__ method to return the detailed error message when the exception is converted to a string.
    def __str__(self):
        # Next line returns the error_message attribute of the instance when it is converted to a string. This attribute contains the custom error message generated during the initialization of the exception instance.
        return self.error_message
    # Purpose: The purpose of defining __str__ method in the CustomException class is to provide a human-readable representation of the exception when it is converted to a string. By returning the error_message attribute, which contains detailed information about the error, this method ensures that meaningful information is displayed when the exception is printed or converted to a string.


        