# Import python libraries
import os
import sys
import csv

from datetime import datetime

if sys.platform == 'win32':
    input_path = os.getcwd() + '\\insight_testsuite\\test_input\\'
    output_path = os.getcwd() + '\\insight_testsuite\\test_output\\'
    sys.path.insert(1, os.getcwd() + '\\src\\')
elif sys.platform == 'linux':
    input_path = os.getcwd() + '/insight_testsuite/test_input/'
    output_path = os.getcwd() + 'insight_testsuite/test_output/'
    sys.path.insert(1, os.getcwd() + '/src/')
    
import IDE_lib as de_lib

# Create report_test.csv from a sample test data for consumer complaints
de_lib.create_reports(input_path, output_path, 'complaints_test.csv', 'report_test.csv')

# Importing report_test.csv to test results are correct
file=open(output_path+'report_test.csv','r')
reader=csv.reader(file)

# Sample results to test function
test_result_1 = ["debt collection",'2020','2','4','50']
test_result_2 = ["payday loan, title loan, or personal loan",'2019','1','1','100']
test_result_3 = ["credit card or prepaid card",'2019','4','4','100']
test_result_4 = ["debt collection",2020,2,4,50]

answer_list = []
for i, row in enumerate(reader):
    answer_list.append(row)

de_lib.test_one_scenario(answer_list, test_result_1, '1')
de_lib.test_one_scenario(answer_list, test_result_2, '2')
de_lib.test_one_scenario(answer_list, test_result_3, '3')
de_lib.test_one_scenario(answer_list, test_result_4, '4')



