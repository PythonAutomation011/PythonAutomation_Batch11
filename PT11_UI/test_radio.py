import pytest
from helper_radio import *


def test_all_radio():
    assert click_all_radio(),"Failed due to radio"
def test_select_python():
    assert click_radio_value(val='Python'),"Failed due to selection"
def test_select_java():
    assert click_radio_value(),"Failed due to selection"
def test_select_php():
    assert click_radio_value(val='PHP'),"Failed due to selection"
def test_select_nodejs():
    assert click_radio_value(val='NODEJS'),"Failed due to selection"