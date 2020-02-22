# Necessary packages 172.17.74.206
import time, sys, traceback

# configure your .py files paths
from Utilities.serial_port import SerialPort
from Utilities.data_log import DataLog

class TaskScript(object):

    def __init__(self):
        """
            Class Constructor: don't change
        """
        self._data_log = DataLog(directory=r'C:/MyScripts/raw_Data')

    def _init_task(self, log_file_name='task_results', log_file_header=['Datetime']):
        """
            _init_task is the first function that be called in any run_task_* function(s)
        """
        # Open Datalog file and print header
        self._data_log.new_log(filename=log_file_name)
        self._data_log.print_log(task_results=[log_file_header])

        return

    def _init_setup(self, com_port="COM4"):
        """
            [OPTIONAL]: _init_setup is the second function that be called in any run_test_* function(s)
            Here, you should configure your setup/platform/equipment/computer...etc.
        """
        self.serial_port = SerialPort(com_port)

        return True

    def run_task_1(self):
        try:
            # _init_task 
            self._init_task(log_file_name="task_1_results",
                            log_file_header=['Datetime', 'VAR1', 'VAR2'])
            self._init_setup(com_port="COM4")                                                   # Initialize Setup

            # Sweep Variables for example
            for var1 in range(0, 10
                for var2 in range(0, 20)
                    """ Your test here """
                    self.serial_port.write(str(var1))
                    self.serial_port.write(str(var2))

                    # read measurements and prepare "results" line for printing
                    self.results = [time.strftime("%Y-%m-%d %H:%M")]                            # Add timestamp to results

                    self.results.append(str(var1))
                    self.results.append(str(var2))

                    # Data log to file
                    self._data_log.print_log(task_results=[self.results])

            success = 1
        except:
            """
                TASK AUTOMATION FAILSAFE
                Assume the Task automation failed due to a bug, what will you do? power off computer?
            """
            print("TASK FAILED")
            traceback.print_exc(file=sys.stdout)
            success = 0
            # Failsafe commands goes here
            

        return success

