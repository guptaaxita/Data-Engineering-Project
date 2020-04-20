# Import python libraries
import os
import sys
import csv

from datetime import datetime

if sys.platform == 'win32':
    input_path = os.getcwd() + '\\input\\'
    output_path = os.getcwd() + '\\output\\'
    test_input_path = os.getcwd() + '\\insight_testsuite\\test_input\\'
    test_output_path = os.getcwd() + '\\insight_testsuite\\test_output\\'
elif sys.platform == 'linux':
    input_path = os.getcwd() + '/input/'
    output_path = os.getcwd() + '/output/'
    test_input_path = os.getcwd() + '/insight_testsuite/input/'
    test_input_path = os.getcwd() + '/insight_testsuite/output/'

def check_filename(filename):
    
    '''
    Defining function to check filename. This function will check if the file has correct extentsion. 
    File should be in .csv format.
    
    '''
    
    if '.' in filename:
        if not 'csv' in filename:
            print('Given filename:', filename)
            sys.exit('Wrong file extension, please check if the filename ends with  \'.csv\' extension')
    else:
        print('Given filename:', filename)
        sys.exit('File extension missing, please check if the filename ends with a file extension')
        
        
def create_reports(input_path, output_path, input_filename, output_filename, flag = 'whole data'):
    
    '''
    input_path - directory where input file is stored.
    output_path - directory where output file generated will be stored.
    input_filename - name of input file.
    outfile_file - result file 
    
    Defining a function where input file will be used to generate output/results file
    
    '''
    
    # Check the inputs
    check_filename(input_filename)
    check_filename(output_filename)
    
    # Read given csv data as a dictionary object
    file=open(input_path+input_filename,'r', encoding = 'utf-8')
    reader=csv.DictReader(file)

    # Make a list of ordered dictionary with keys as column name for each dictionaryds=[]
    ds=[]
    for row in reader:
        ds.append(row)

    # Merge all the ordered dictionaries as a single dictionary with keys as column names and value from each dictionary in ds    
    d = {}
    for k in row.keys():
        d[k] = list(d[k] for d in ds)

    list_product = d['Product']
    list_company = d['Company']
    list_issue = d['Issue']
    
    # Extract product from dictionary d and convert all letters to lowercase
    list_product = [x.lower() for x in d['Product']]

    print('There are {} products: ({})'.format(len(set(list_product)), flag))
    for product in set(list_product):
        print('"', product, '"', sep='')
    print('\n')
        
    # Extracting year from date of product complaint received and add Year as a new dictionary key with values in d
    list_year = [datetime.strptime(x,'%Y-%m-%d').year for x in d['Date received']]
    d['Year'] = list_year

    print('Data cover for years: ({}) '.format(flag))
    for year in sorted(list(set(list_year))):
        print(year)
    print('\n')

    # Zip list of products and years to get combinations for products and years
    prod_yr_list = [(i, j) for i, j in zip(list_product, list_year)]

    # Count total number of complaints for each product and year
    print('Total number of complaints for each product and year: ({})'.format(flag))
    for prod_yr in set(prod_yr_list):
        print('"', prod_yr[0], '", ', prod_yr[1], ', ',
              len(set([j for i, j in zip(prod_yr_list, list_issue) if i == prod_yr])), sep='')
    print('\n')

    # Check if no issues exist for any date (extract index for the data when issues are not empty)
    index_with_null = [i for i, issue in enumerate(d['Issue']) if issue == ''] 
    if len(index_with_null) > 0:
        indices = [i for i, issue in enumerate(d['Issue']) if issue != '']
        list_product = [list_product[i] for i in indices]
        list_year = [list_year[i] for i in indices]
        list_company = [list_company[i] for i in indices]
        prod_yr_list = zip(list_product, list_year)

    # Count total number of companies with atleast 1 issue
    print('Total number of companies for each product and year: ({})'.format(flag))
    for prod_yr in set(prod_yr_list):
        print('"', prod_yr[0], '", ', prod_yr[1], ', ',
              len(set([j for i, j in zip(prod_yr_list, list_company) if i == prod_yr])), sep='')
    print('\n')
        
    # Merging total number of issues and total number of companies
    tot_issue = {}; tot_company = {}
    for prod_yr in set(prod_yr_list):
        tot_issue[prod_yr] = len(set([j for i, j in zip(prod_yr_list, list_issue) if i == prod_yr]))

    for prod_yr in set(prod_yr_list):
        tot_company[prod_yr] = len(set([j for i, j in zip(prod_yr_list, list_company) if i == prod_yr]))

    d_issue_company = [tot_issue, tot_company]
    d_result = {}
    for k in tot_issue.keys():
        d_result[k] = tuple(d_result[k] for d_result in d_issue_company)

    # Generating final results - Highest percentage of total complaints/issues filed against one complay for that product /year 
    d_final_result = {}
    for k, v in d_result.items():
        d_final_result[k] = tuple((v[0], v[1], round(100*v[0]/v[1])))

    # Writing and exporting results "report.csv"
    with open(output_path+output_filename, 'w') as f:
        for key in sorted(d_final_result.keys()):
            f.write("%s,%s,%s,%s,%s\n"%('"'+key[0]+'"', key[1], 
                                        d_final_result[key][0], d_final_result[key][1], d_final_result[key][2]))
            
    
# Run the script for a sample dataset:
create_reports(test_input_path, test_output_path, 'complaints_test.csv', 'report_test.csv', flag = 'sample data')

# Run the script on the whole dataset:
create_reports(input_path, output_path, 'complaints.csv', 'report.csv')