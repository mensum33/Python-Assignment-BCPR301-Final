from os.path import abspath


class FileWriter:

    #Created by Bikrant & Suman
    inheritance = ' --|> '
    association = ' --> '

    @staticmethod
    def write(class_data):
        try:
            with open(abspath('./rawUml.txt'), 'w') as file:
                file.write('@startuml \n')
                for a_class in class_data:
                    for a_attribute in a_class.instance_attributes:
                        file.write(a_class.class_name + ' : ' + a_attribute + '\n')
                    for a_method in a_class.instance_methods:
                        file.write(a_class.class_name + ' : ' + a_method + '()\n')
                    if len(a_class.inheritance) != 0:
                        for aclass in a_class.inheritance:
                            file.write(a_class.class_name + FileWriter.inheritance + aclass + '\n')
                    if len(a_class.association) != 0:
                        for aclass in a_class.association:
                            file.write(a_class.class_name + FileWriter.association + aclass + '\n')
                file.write('@enduml')
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
