__author__ = "Jonathan Bonnaud"
__date__ = "4.12.2017"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "jonathan.bonnaud.pro@gmail.com"


class AbstractDay:

    def __init__(self, input_content):
        self.input_content = input_content

    def get_result(self):
        """
        Method that must be implement for all problems.
        :return: The result of the problem
        """
        raise NotImplementedError
