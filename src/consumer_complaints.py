# Import python libraries
import os
import sys
import csv

from datetime import datetime

import IDE_lib as de_lib

if sys.platform == 'win32':
    input_path = os.getcwd() + '\\input\\'
    output_path = os.getcwd() + '\\output\\'
elif sys.platform == 'linux':
    input_path = os.getcwd() + '/input/'
    output_path = os.getcwd() + '/output/'

de_lib.create_reports(input_path, output_path, 'complaints.csv', 'reports.csv')
