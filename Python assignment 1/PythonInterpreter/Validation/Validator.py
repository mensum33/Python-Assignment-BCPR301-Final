from py_compile import compile
from py_compile import PyCompileError
from os.path import abspath
from Validation.QuietReport import QuietReport
from pycodestyle import Checker
import ast


class Validator:
    # Created by Jignesh
    @staticmethod
    def validate(file_path):
        error = 'ok'
        if Validator.can_compile(file_path):
            if len(Validator.execute_pep8(file_path)) != 0:
                error = 'f'
        else:
            error = 'c'
        return error

    #Created by Bikrant
    @staticmethod
    def can_compile(file_path):
        absolute_path = abspath(file_path)

       #Exception handling
        try:
            compile(absolute_path, doraise=True)
            module_ok = True
        except PyCompileError:
            module_ok = False
        except PermissionError:
            module_ok = False
            print("Access Denied for the specified file " + file_path)
        return module_ok

    # Created by Suman
    @staticmethod
    def execute_pep8(file_path):
        try:
            absolute_path = abspath(file_path)
        except FileNotFoundError:
            print('File at ' + file_path +' is not found')
        except Exception as e:
            print(e)
        checker = Checker(absolute_path, reporter=QuietReport)
        checker.check_all()
        return checker.report.full_error_results()

    # Created by Jignesh
    @staticmethod
    def contains_multiple_class(source):
        result = True
        classes = [a_class.name for a_class in ast.walk(ast.parse(source)) if isinstance(a_class, ast.ClassDef)]
        if len(classes) > 1:
            result = False
        return result
