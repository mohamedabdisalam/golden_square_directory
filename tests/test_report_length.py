from lib.report_length  import *

def test_correct_length():
    result = report_length("Abdisalam")
    assert result == f"This string was {9} characters long."