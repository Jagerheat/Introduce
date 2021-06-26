import pathlib
import logging

blockstorer_path = pathlib.Path("hello.txt")

class BlockStorer(object):
    def __init__(self, blockstorer_name, method):
        self.blockstorer_obj = open(blockstorer_name, method)
    def __enter__(self):
        return self.blockstorer_obj
    def __exit__(self, type, value, traceback):
        self.blockstorer_obj.close()

if __name__ == '__main__':
    try:
        with BlockStorer("filename", 10) as storer:
            while input("continue?")!='q':
                storer.append(input("enter text to store"))
    except OSError as error:
        logging.error("Writing to file %s failed due to: %s", blockstorer_path, error)


#try:
    #with file_path.open(mode="w") as file:
       # file.write("")
#except OSError as error:
    #logging.error("Writing to file %s failed due to: %s", file_path, error)
