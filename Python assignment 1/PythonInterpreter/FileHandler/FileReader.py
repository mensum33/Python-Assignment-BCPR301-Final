import os
from Validation.Validator import Validator
from Validation.Pep8Formatter import Pep8Formatter


class FileReader:
    # Created by Bikrant
    @staticmethod
    def read_from_file(path):
        result = ""
        if path.endswith('.py'):
            valid = Validator.validate(path)
            if valid == 'ok':
                raw_data = FileReader.read(path)
                if Validator.contains_multiple_class(raw_data) is not False:
                    result = raw_data
                else:
                    print(
                        'Data Extraction has stopped as more than 1 class definition was found in \n' + path)
            elif valid == 'f':
                raw_data = Pep8Formatter.format_pep8(path)
                if Validator.contains_multiple_class(raw_data) is not False:
                    result = raw_data
                else:
                    print(
                        'Data Extraction has stopped as more than 1 class definition was found in \n' + path)
            else:
                print('Not a valid Python code in ',
                      path, ' Fix the file and try again')
        return result

    # Created by Jignesh
    @staticmethod
    def read_from_folder(path):
        data = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.abspath(os.path.join(root, file))
                    valid = Validator.validate(file_path)
                    if valid == 'ok':
                        raw_data = FileReader.read(file_path)
                        if Validator.contains_multiple_class(raw_data) is not False:
                            data.append(raw_data)
                        else:
                            print(
                                'Data Extraction has stopped as more than 1 class definition was found in \n' + file_path)
                            data = []
                            break
                    elif valid == 'f':
                        raw_data = Pep8Formatter.format_pep8(file_path)
                        if Validator.contains_multiple_class(raw_data) is not False:
                            data.append(raw_data)
                        else:
                            print(
                                'Data Extraction has stopped as more than 1 class definition was found in \n' + file_path)
                            data = []
                            break
                    else:
                        print('Not a valid Python code in ', file_path,
                              ' Extraction process has been stopped! Fix the file and try again')
                        data = []
                        break
        return data

    # Created by Suman
    @staticmethod
    def read(path):
        data = ""
        try:
            with open(path, 'r') as file:
                for aLine in file:
                    data += aLine
        except FileNotFoundError:
            print(path, ' was not found')
        except PermissionError:
            print("Access Denied for the specified file " + path)
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
        finally:
            return data
