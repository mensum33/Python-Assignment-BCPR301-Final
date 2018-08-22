"""
>>> help = Help()
>>> help.help_exit()
<BLANKLINE>
            Exit the application.
            Syntax: exit
            :param : None.
            :return: True
<BLANKLINE>
"""
from Help import Help
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    doctest.testmod(verbose=True)