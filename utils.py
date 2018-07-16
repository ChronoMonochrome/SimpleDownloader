# -*- coding: utf-8 -*-

import sys, os

def getLocalPath(filename):
    app_dir = os.path.dirname(sys.argv[0])
    return os.path.join(app_dir, filename)
