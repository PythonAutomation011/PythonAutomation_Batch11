import pytest
from helper_basic import *


def test_check_title():
    obj=HelpeBasic()
    result=obj.validate_title_url(exp_title=True)
    assert 'STEP UP' in result, "Failed due to title"

def test_check_url():
    obj=HelpeBasic()
    result=obj.validate_title_url(exp_url=True)
    assert 'http' in result , "failed due to url"