# Logger is for the purpose that any execution that probably happens we should be able to log all those information, the execution, everything in some files. So that will be able to track if there is some errors, even the custom exception error, we will try to log that into the text file.

# Overall, this code ensures that logging is configured to write messages to a file in a structured manner, with timestamps and other relevant information included in each log entry. It sets up logging in a Python application by creating a directory to store log files, generating a unique log file name based on the current date and time, and configuring the logging system to write log messages to the specified file with a defined format and logging level.

import logging  # This imports the logging module, which is used for logging messages to a file, console, or other output destinations.

import os  # This imports the os module, which provides functions for interacting with the operating system, such as file and directory manipulation.

from datetime import datetime # This imports the datetime class from the datetime module, which is used to work with dates and times.

# Next line generates a unique log file name using the current date and time formatted as month_day_year_hour_minute_second.log.
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# This constructs the path to the directory where log files will be stored. It uses os.getcwd() to get the current working directory & joins it with the "logs" directory & the generated log file name.
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)

# Creates the directory specified by logs_path if it does not exist already. The exist_ok parameter ensures that the function does not raise an error if the directory already exists.
os.makedirs(logs_path,exist_ok=True)

# Construct the full path to the log file by joining the logs_path with the generated log file name.
# my file name should have logs in forward and then this naming 'LOG_FILE'
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# Initialize the logging system with the specified configuration settings.
logging.basicConfig(
    # Specifies the file where log messages will be written.
    filename=LOG_FILE_PATH,
    
    # Specifies the format of log messages, this is how my entire message will get printed. It includes the timestamp (%(asctime)s), line number (%(lineno)d), logger name (%(name)s), log level (%(levelname)s), and the actual log message (%(message)s).
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    
    # Sets the logging level to INFO, meaning only log messages with severity INFO or higher will be recorded in the log file.
    level=logging.INFO,


)


# Check every thing is working:
if __name__=='__main__':
    logging.info("Logging has started")