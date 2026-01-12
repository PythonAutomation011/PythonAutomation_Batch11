import pytest
from helper_checkbox import click_checkbox

def test_click_all():
    assert click_checkbox(all=True),'failed due to checkbox'

def test_click_on_position2():
    assert click_checkbox(position=2),'failed due to checkbox'

def test_click_on_position1():
    assert click_checkbox(position=1),'failed due to checkbox'

def test_click_on_position0():
    assert click_checkbox(position=0),'failed due to checkbox'

def test_click_on_position3():
    assert click_checkbox(position=3),'failed due to checkbox'