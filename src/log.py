import logging
from enum import StrEnum

BASIC_LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
LOG_FORMAT_DEBUG = "%(asctime)s - %(levelname)s - %(message)s - %(pathname)s - %(funcName)s - %(lineno)d"

class LogLevels(StrEnum):
	info = "INFO"
	warning = "WARNING"
	error = "ERROR"
	debug = "DEBUG"

def configure_logging(log_level: str = LogLevels.error):
	log_level = str(log_level).upper()
	log_levels = [level.value for level in LogLevels]
	
	if log_level not in log_levels:
		logging.basicConfig(level=LogLevels.error, format=BASIC_LOG_FORMAT)
		return
	
	if log_level == LogLevels.debug:
		logging.basicConfig(level=log_level, format=LOG_FORMAT_DEBUG)
		return
	
	logging.basicConfig(level=log_level, format=BASIC_LOG_FORMAT)
