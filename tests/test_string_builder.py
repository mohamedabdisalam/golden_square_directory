from lib.string_builder import *

"""
Initially, output empty string
"""

def test_empty_string():
    strings = StringBuilder()
    assert strings.output() == ""

"""
When we add a single string
The output is now that string
"""

def test_string_is_added():
    strings = StringBuilder()
    strings.add("Hello")
    assert strings.output() == "Hello"

"""
Checks the length of a single string
"""

def test_length_of_string():
    strings = StringBuilder()
    strings.add("Hello")
    assert strings.size() == 5

"""
When we add multiple strings
The output is that of those strings concatenated 
"""
def test_multiple__string_is_added():
    strings = StringBuilder()
    strings.add("Hello")
    strings.add(" World")
    assert strings.output() == "Hello World"

"""
When we add multiple strings
The output is the size of all those strings added
"""

def test_multiple__string_lengths_when_added():
    strings = StringBuilder()
    strings.add("Hello")
    strings.add(" World")
    assert strings.size() == 11