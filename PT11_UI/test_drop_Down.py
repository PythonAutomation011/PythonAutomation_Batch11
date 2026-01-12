from helper_drop_down import HelperDrop
import pytest

def test_select_intial_by_index():
    obj1=HelperDrop()
    assert obj1.select_by_my_index(0),"Failed due to index"

def test_select_op1_by_index():
    obj1=HelperDrop()
    assert obj1.select_by_my_index(1),"Failed due to index"

def test_select_op2_by_index():
    obj1=HelperDrop()
    assert obj1.select_by_my_index(2),"Failed due to index"

def test_select_op1_by_value():
    obj1=HelperDrop()
    assert obj1.select_by_my_value('1'),"Failed due to index"

def test_select_op2_by_value():
    obj1=HelperDrop()
    assert obj1.select_by_my_value('2'),"Failed due to index"

def test_select_op1_by_text():
    obj1=HelperDrop()
    assert obj1.select_by_my_text('Option 1'),"Failed due to index"

def test_select_op2_by_text():
    obj1=HelperDrop()
    assert obj1.select_by_my_text('Option 2'),"Failed due to index"

def test_select_intial_by_text():
    obj1=HelperDrop()
    assert obj1.select_by_my_text('Please select an option'),"Failed due to index"

