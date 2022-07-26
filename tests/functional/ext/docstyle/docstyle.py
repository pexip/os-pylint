"""Checks of Dosctrings 'docstring-first-line-empty' 'bad-docstring-quotes'"""


def check_messages(*messages):  # [docstring-first-line-empty]
    """
    docstring"""
    return messages


def function2():
    """Test Ok"""


class FFFF:  # [docstring-first-line-empty]
    """
    Test Docstring First Line Empty
    """

    def method1(self):  # [docstring-first-line-empty, bad-docstring-quotes]
        '''
        Test Triple Single Quotes docstring
        '''

    def method2(self):  # [bad-docstring-quotes]
        "bad docstring 1"

    def method3(self):  # [bad-docstring-quotes]
        'bad docstring 2'

    def method4(self):  # [bad-docstring-quotes]
        ' """bad docstring 3 '

    @check_messages("bad-open-mode", "redundant-unittest-assert", "deprecated-module")
    def method5(self):
        """Test OK 1 with decorators"""

    def method6(self):
        r"""Test OK 2 with raw string"""

    def method7(self):
        u"""Test OK 3 with unicode string"""
