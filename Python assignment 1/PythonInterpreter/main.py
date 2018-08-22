from cmd import Cmd
from FileHandler.FileReader import FileReader
from FileHandler.FileWriter import FileWriter
from DataExtractor import DataExtractor
from UmlClass import UmlClass
from sys import argv
from Help import Help
import os
import re


class Interpreter(Cmd, Help):
    def __init__(self, new_name, new_output_path=None, db_name='Uml_Class'):
        Cmd.__init__(self)
        self.prompt = '>>> '
        self.intro = 'Hi ' + new_name + ' Welcome to the Interpreter. Type help or ? to list commands.\n'
        self.extracted_data = []
        self.output_path = new_output_path
        self.db_name = db_name

    # Created By Jignesh
    def do_extract(self, line):

        options = self.extract_line(line)
        if len(options) == 2:
            data = []
            if options[0].lower() == 'f':
                if os.path.isfile(options[1]):
                    file_data = FileReader.read_from_file(os.path.abspath(options[1]))
                    if file_data != '':
                        data.append(file_data)
                else:
                    print('The path provided is not a file!!')
            elif options[0].lower() == 'd':
                if os.path.isdir(options[1]):
                    data = FileReader.read_from_folder(options[1])
                else:
                    print('The path provided is not a directory!!')
            else:
                print('Please provide valid indicator')
            self.extracted_data = self.extract_class_data(data)
        else:
            print('Valid options not provided. Use "help extract" command')

    # Created By Suman
    def do_view(self, arg=""):
        if arg.lower() == 'data':
            if len(self.extracted_data) > 0:
                for a_class_data in self.extracted_data:
                    print('Data for ', a_class_data.class_name, ' class.')
                    print('\tInstance attributes names')
                    print('\t', a_class_data.instance_attributes)
                    print('\tInstance method names')
                    print('\t', a_class_data.instance_methods)
                    print('\tAssociation Relationship')
                    print('\t', a_class_data.association)
                    print('\tInheritance Relationship')
                    print('\t', a_class_data.inheritance)
            else:
                print('No data available to display. Use "extract" command')
        else:
            print('Valid options not provided. use "help view" command')

    # Created By Bikrant
    def do_generate(self, arg):
        if arg.lower() == 'c':
            if len(self.extracted_data) > 0:
                FileWriter.write(self.extracted_data)
                if self.output_path is None:
                    self.output_path = os.path.abspath('./output/success/class.png')
                elif self.output_path is not None and not self.output_path.endswith('.png'):
                    self.output_path = os.path.abspath(self.output_path + '/class.png')
                UmlClass.generate(self.output_path)
            else:
                print('No data available to generate diagram. Use "extract" command to extract data first')
        else:
            print('Valid options not provided. Use "help generate" command')

    # Created By Jignesh
    def do_exit(self, line):
        print('Thank You for using the Interpreter')
        print("Exiting ......")
        return True

    def extract_line(self, line):
        options = []
        for a_command in line.split(' -'):
            striped_command = re.sub('[-]', '', a_command).strip()
            if striped_command != '':
                options.append(striped_command)
        return options

    def extract_class_data(self, raw_data):
        extracted_data = []
        for a_class in raw_data:
            a_class_data = DataExtractor(a_class)
            if a_class_data.class_name is not None:
                extracted_data.append(a_class_data)
        return extracted_data


if __name__ == "__main__":
    # Created by Jignesh
    if len(argv) == 2:
        interpreter = Interpreter(argv[1])
        interpreter.cmdloop()
    # Created by Suman
    elif len(argv) == 3:
        if os.path.isdir(argv[2]):
            interpreter = Interpreter(argv[1], argv[2])
            interpreter.cmdloop()
        else:
            print('Please provide a valid path to a directory and try again!!!')
    # Created by Bikrant
    elif len(argv) == 4:
        if os.path.isdir(argv[2]):
            if os.path.isfile('./Database/' + argv[3] + '.db'):
                interpreter = Interpreter(argv[1], argv[2], argv[3])
                interpreter.cmdloop()
            else:
                print('Database ' + argv[3] + ' not found!!! Try again')
        else:
            print('Please provide a valid path to a directory and try again!!!')
    else:
        print('Please use the command "python main.py your name"')
