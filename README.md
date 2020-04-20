# Insight_Data-_Engineering_Challenge
Summarize consumers complaints data for financial companies

Solution to this coding challenge is provided using python 3.7.3

## Background 
  This database is open source publically available dataset available at https://www.consumerfinance.gov/data-research/consumer-complaints/#download-the-data This dataset is collection of complaints about consumer financial products and services. Complaints were sent to these financial companies for responses. 
  This data set has ~ 1.5 million instances and 18 variables: Date received	Product, Company, Issue, Sub-product, Sub-issue, Consumer complaint narrative, Company public response, State, ZIP code, Tags, Consumer consent provided?, Submitted via, Date sent to company, Company response to consumer, Timely response?, Consumer disputed? and Complaint ID. This dataset has data collection from years 2011 to 2020. 
  
## Problem Statement
  The federal government provides a way for consumers to file complaints against companies regarding different financial products, such as payment problems with a credit card or debt collection tactics. In this task data has been analyzed to indentify the number of complaints filed and how they're spread across different companies. Out of the18 variables  in this ‘Date received’, ‘Product’, ‘Issues’, and ‘Complaint’ variables were used to answer following questions:
  
## Questions answered
1)	Modify product name to lower case 
2)	Extract year for each product listed from ‘Date received’
3)	Calculate total number of complaints received for that product and year
4)	Calculate total number of companies receiving at least one complaint for that product and year
5)	Calculate highest percentage of total complaints filed against one company for that product and year. 

## Summary
### Relevant functions
sys - provides information about constants, functions and methods of the Python interpreter
csv – used to import data in csv file format
datatime – used to extract year from date YYYY-MM-DD 

  In this task **complaints.csv** file is the input file found in input folder. Output file **report.csv** is output file showing total number of complaints and how they're spread across different companies for each product and year. The script generated using Python 3.7.3 provides information about total number of complaints received for each product year combination, total number of companies for each product year combination and highest percentage of total complaints filed against one company for that product and year. Results are generated in following format as required:
  
"bank account or service",2012,5,98,5
"bank account or service",2013,5,164,3
"bank account or service",2014,5,258,2
"bank account or service",2015,5,215,2
"bank account or service",2016,5,230,2
"bank account or service",2017,5,174,3
