from helper_alerts import *


def test_info_alert():
    assert check_info_alert(info=True),"failed"

def test_confi_alert():
    assert check_info_alert(conf=True),"failed"

def test_input_alert():
    assert check_info_alert(inp=True),"failed"