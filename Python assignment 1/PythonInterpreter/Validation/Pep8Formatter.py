from autopep8 import fix_file
from os.path import abspath

# Created by Jignesh
class Pep8Formatter:
    @staticmethod
    def format_pep8(file_path):
        try:
            return fix_file(abspath(file_path))
        except FileNotFoundError:
            print("The " + file_path + " is not available")
        except Exception as e:
            print(e)