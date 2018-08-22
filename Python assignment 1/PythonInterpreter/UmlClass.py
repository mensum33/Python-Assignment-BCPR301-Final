from plantuml import PlantUML
from os.path import abspath


class UmlClass:
    @staticmethod
    def generate(path):
        server = PlantUML(url='http://www.plantuml.com/plantuml/img/', basic_auth={}, form_auth={}, http_opts={},
                     request_opts={})
        try:
            if server.processes_file(abspath('./rawUml.txt'), path, abspath('./output/error/error.txt')):
                print('Done, View your diagram in ' + path)
        except PermissionError:
            print('Permission Error occurred')
        except Exception as e:
            print(e)