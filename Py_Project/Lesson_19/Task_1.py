import logging


class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        self.file_obj.close()

try:
    with File("craft.txt", 'w') as opened_file:
        opened_file.write("Hello, World!")
except OSError as error:
        logging.error("Writing to file %s failed due to: %s", error)




