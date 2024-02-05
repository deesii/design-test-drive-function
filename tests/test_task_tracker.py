from lib.task_tracker import *

"""
Given an empty string
Will return False
"""
def test_empty_string():
    assert task_tracker("") == False

"""
Given a string which contains #TODO 
Will return True
"""

def test_contains_TODO():
    assert task_tracker("#TODO dasnufnuobwa") == True


"""
Given long string which icludes #TODO embedded in the string
Returns True
"""
def test_embedded_TODO():
    assert task_tracker("bfuionawouibfwoiau#TODOfjabewgbfu") == True