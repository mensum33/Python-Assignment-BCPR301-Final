from pycodestyle import BaseReport

# got from internet
class QuietReport(BaseReport):
    """Version of checker that does not print."""

    def __init__(self, options):
        super(QuietReport, self).__init__(options)
        self.__full_error_results = []

    def error(self, line_number, offset, text, check):
        """Collect errors."""
        code = super(QuietReport, self).error(line_number,
                                              offset,
                                              text,
                                              check)
        if code:
            self.__full_error_results.append(
                {'id': code,
                 'line': line_number,
                 'column': offset + 1,
                 'info': text})

    def full_error_results(self):
        """Return error results in detail.

        Results are in the form of a list of dictionaries. Each
        dictionary contains 'id', 'line', 'column', and 'info'.

        """
        return self.__full_error_results
