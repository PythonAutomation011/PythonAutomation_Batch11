
import pytest
from helper_login import *


def test_login_current_url():
    result=login('student','Password123',current_url=True)
    assert "practicetestautomation.com/logged-in-successfully/" in result,"failed due to url"

def test_login_wrong_username():
    result=login('student123','Password123',wrong_username_password=True)
    assert "Your username is invalid" in result,"failed due to url"

def test_login_wrong_password():
    result=login('student','admin123',wrong_username_password=True)
    assert "Your password is invalid" in result,"failed due to url"

def test_login_wrong_username_password():
    result=login('admin','admin',wrong_username_password=True)
    assert "Your username is invalid" in result,"failed due to url"