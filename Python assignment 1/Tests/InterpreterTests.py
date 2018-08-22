"""
# Created By Jignesh


# Testing default values
>>> cmd = Interpreter('Jignesh')
>>> print(cmd.intro)
Hi Jignesh Welcome to the Interpreter. Type help or ? to list commands.
<BLANKLINE>
>>> print(cmd.output_path)
None
>>> print(cmd.db_name)
Uml_Class

# Testing do_extract
>>> cmd.do_extract("")
Valid options not provided. Use "help extract" command

>>> cmd.do_extract("-f ./")
Valid options not provided. Use "help extract" command

>>> cmd.do_extract("-f -./")
The path provided is not a file!!

>>> cmd.do_extract("-d -../DataExtractor.py")
The path provided is not a directory!!


# Created by suman

#Testing do_view
>>> cmd.do_view()
Valid options not provided. use "help view" command

>>> cmd = Interpreter('Jignesh')
>>> cmd.do_view('data')
No data available to display. Use "extract" command

>>> cmd.do_extract('-f -../DataExtractor.py')
>>> cmd.do_view('data')
Data for  DataExtractor  class.
    Instance attributes names
     ['data', 'class_name', 'instance_attributes', 'instance_methods', 'inheritance', 'association']
    Instance method names
     ['__init__', 'get_class_name', 'get_instance_attributes', 'get_instance_method_names', 'get_inheritance', 'get_association']
    Association Relationship
     []
    Inheritance Relationship
     []

# Created By Bikrant

# Testing do_generate
>>> cmd = Interpreter('Jignesh')
>>> cmd.do_generate("")
Valid options not provided. Use "help generate" command
>>> cmd.do_generate("c")
No data available to generate diagram. Use "extract" command to extract data first
>>> cmd.do_extract('-f -../DataExtractor.py')
>>> cmd.output_path = './class.png'
>>> cmd.do_generate("c")
Done, View your diagram in ./class.png
>>> cmd.extract_line("-class -H:/Documents")
['class', 'H:/Documents']
>>> cmd.extract_line("-class H:/Documents")
['class H:/Documents']
"""
from main import Interpreter
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    doctest.testmod(verbose=True)