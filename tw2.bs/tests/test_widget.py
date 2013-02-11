from tw2.core.testbase import WidgetTest
from tw2.bs import *

class TestBs(WidgetTest):
    # place your widget at the TestWidget attribute
    widget = Bs
    # Initilization args. go here 
    attrs = {'id':'bs-test'}
    params = {}
    expected = """<div id="bs-test"></div>"""
