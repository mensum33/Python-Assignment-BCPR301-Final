class Help:
    def help_extract(self):
        print(
            """
            Extracts UML Class Diagram data from the given file or folder.
            Syntax: extract -[indicator]=Required -[path]=Required
            :param indicator: [f]=file or [d]=Directory.
            :param path: Provide a Absolute or Relative path. "Path should not contain any '-' character".
            :return: None
            """
        )

    def help_exit(self):
        print(
            """
            Exit the application.
            Syntax: exit
            :param : None.
            :return: True
            """
        )

    def help_view(self):
        print(
            """
            View extracted data.
            Syntax: view [option]=Required
            :param option: [data]=currently extracted data.
            :return: None
            """
        )

    def help_generate(self):
        print(
            """
            Generates Diagram in a .png format.
            Syntax: generate [option]=Required
            :param option: [c]=Class Diagram.
            :return: None
            """
        )
