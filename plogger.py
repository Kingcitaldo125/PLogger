import logging
import os
import sys
import time


class Logger(object):
	def __init__(self, name):
		self.log_level_map = {"CRITICAL": logging.CRITICAL, "ERROR": logging.ERROR, "WARNING": logging.WARNING,
                     "INFO": logging.INFO, "DEBUG": logging.DEBUG}
		self.loglevel = ""
		self.logger = logging.getLogger(name)
		self.formatter = ""
		
		oslevel = os.getenv("LOG_LEVEL")
		if oslevel in self.log_level_map:
			level = self.log_level_map[oslevel]
			self.logger.setLevel(level)
			self.loglevel = level
			print("loglevel",self.loglevel)
		else:
			self.logger.error(f"ERROR: loglevel '{oslevel}' not recognized")
			
		self.formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
		self.formatter.converter = time.gmtime
		
	def write_message(self, message, level):
		if self.log_level_map[level.upper()] == self.log_level_map["CRITICAL"]:
			self.logger.critical(message)
		elif self.log_level_map[level.upper()] == self.log_level_map["ERROR"]:
			self.logger.error(message)
		elif self.log_level_map[level.upper()] == self.log_level_map["WARNING"]:
			self.logger.warning(message)
		elif self.log_level_map[level.upper()] == self.log_level_map["INFO"]:
			self.logger.info(message)
		elif self.log_level_map[level.upper()] == self.log_level_map["DEBUG"]:
			self.logger.debug(message)
		else:
			self.logger.critical(f"CRITICAL: Log level not in loglevels: {self.loglevel}")


class ErrorLogger(Logger):
	def __init__(self, name):
		super().__init__(name)
		self.name = name
		
		error_handler = logging.StreamHandler(stream=sys.stderr)
		error_handler.setFormatter(self.formatter)
		if not self.logger.handlers:
			self.logger.addHandler(error_handler)
		
		
class ConsoleLogger(Logger):
	def __init__(self, name):
		super().__init__(name)
		self.name = name
		
		console_handler = logging.StreamHandler(stream=sys.stdout)
		console_handler.setFormatter(self.formatter)
		if not self.logger.handlers:
			self.logger.addHandler(console_handler)


def main():
	clogger = ConsoleLogger("My Logger")
	clogger.write_message("MY MESSAGE 1", "debug")
	clogger.write_message("MY MESSAGE 2", "info")
	clogger.write_message("MY MESSAGE 3", "warning")
	clogger.write_message("MY MESSAGE 4", "error")
	clogger.write_message("MY MESSAGE 5", "critical")


if __name__ == "__main__":
	main()
