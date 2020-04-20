# Import python libraries
import os
import sys
import csv

from datetime import datetime

if sys.platform == 'win32':
    output_path = os.getcwd() + '\\insight_testsuite\\test_output\\'
elif sys.platform == 'linux':
    output_path = sys.argv[1]
    
# Importing report_test.csv to test results are correct
file=open(output_path+'report_test.csv','r')
reader=csv.reader(file)

# Sample results to test function
test_result_1 = ["debt collection",'2020','2','4','50']
test_result_2 = ["payday loan, title loan, or personal loan",'2019','1','1','100']
test_result_3 = ["credit card or prepaid card",'2019','4','4','100']
test_result_4 = ["debt collection",'2020','2','4','50']

answer_list = []
for i, row in enumerate(reader):
    answer_list.append(row)

def test_one_scenario(answer_list, test_result_list, test_name):
    
    '''
    Defining a test function to test and compare results against the known results.
    
    '''
    
    if len(test_result_list) != 5:
        sys.exit('Incorrect number of values in test scenario, no test can be executed')
    
    if test_result_list in answer_list:
        print('Test scenario {} passed'.format(test_name))
    else:
        print('Test failed: Wrong output generated for product: {}, year: {}'.format(test_result_list[0], 
                                                                                     test_result_list[1]))

# Run all test scenarios:
test_one_scenario(answer_list, test_result_1, '1')
test_one_scenario(answer_list, test_result_2, '2')
test_one_scenario(answer_list, test_result_3, '3')
test_one_scenario(answer_list, test_result_4, '4')