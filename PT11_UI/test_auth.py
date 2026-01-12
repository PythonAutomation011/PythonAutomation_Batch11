import pytest
from auth_module import *

def test_check_title_auth_url():
    uname='admin'
    upass='admin'
    url=f"https://{uname}:{upass}@the-internet.herokuapp.com/basic_auth"
    assert check_auth(url,exp_title=True),"failed due to auth"

def test_check_current_url_auth_url():
    uname='admin'
    upass='admin'
    url=f"https://{uname}:{upass}@the-internet.herokuapp.com/basic_auth"
    assert check_auth(url,exp_url=True),"failed due to auth"