import os

def check_file(path):
    if os.path.exists(path):
        return True
    else:
        return False

def remove_file(path):
    return os.remove(path)