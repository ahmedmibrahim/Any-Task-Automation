# Necessary packages
import sys, traceback, time, os
import warnings, re
from datetime import datetime

class DataLog(object):

    def __init__(self, directory='raw_data'):
        # Class for holding variables' values
        # Open log file
        self.raw_data_dir = os.path.abspath(os.path.join(os.path.dirname("__file__"), '..', directory))

    # Data log functions
    def new_log(self, filename='default'):
        """
            Creat's new log file, assign file name and type
            Parameters:
                filename: name of log file
        """
        # check if log directory exists, if not create it
        try:
            os.stat(self.raw_data_dir)
        except:
            os.makedirs(self.raw_data_dir)

        # file name
        self.filename = filename + '.csv'

        # Assign delimiter
        self.delimiter = ','
        
        # Open log file
        self.fp = open(self.raw_data_dir + "\\" + self.filename, 'a')
        print("Log file: %s" % self.raw_data_dir + '\\' + self.filename)

        return

    def print_log(self, task_results=None):
        """
            Prints header / results
        """
        # Create new print_line
        print_line = '\n'
        # Appending task header/results line
        if task_results is not None:
            print_line += self.delimiter.join(task_results) + self.delimiter

        # If closed, reopen
        if self.fp.closed:
            self.fp = open(self.raw_data_dir + "\\" + self.filename, 'a')

        # write header/results line
        if sys.version_info[0] < 3:
            self.fp.write(unicode(print_line))
        else:
            self.fp.write(str(print_line))
        self.fp.flush()
        self.fp.close()

        print("Results successfully logged to %s" % self.filename)

        return
