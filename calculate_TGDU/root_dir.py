import os, sys
from ctypes import *

def getRootDir(*args):
    if getattr(sys, 'frozen', False):
        application_path = os.path.abspath(os.path.dirname(sys.executable))
    else:
        application_path = os.path.dirname(__file__)
    if args:
        application_path = os.path.join(application_path, os.path.join(*args))
    application_path = application_path.replace('\\', '/')
    return application_path

def toLongName(path):
    '''
    from dos 8.3 format
    '''
    buf = create_unicode_buffer(500)
    windll.kernel32.GetLongPathNameW(path, buf, 500)
    return buf.value

def get_icon():
    return os.path.join(getRootDir(),'icon.png')

