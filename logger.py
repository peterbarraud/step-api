import inspect
import os


class APILogger:
    def __init__(self, file_name = None):
        if not os.path.exists('./test_log_for_rest_api'):
            os.mkdir('./test_log_for_rest_api')
        if file_name is None:
            __file_name = inspect.stack()[1][3]
        else:
            __file_name = file_name
        if __file_name[-4:] != '.log':
            __file_name += '.log'
        self.__file_handle = open('./test_log_for_rest_api/' + __file_name, 'w')

    def __del__(self):
        self.__file_handle.close()

    def write(self, line):
        self.__file_handle.write(line)

    def writeline(self, line):
        self.write(str(line) + "\n")
