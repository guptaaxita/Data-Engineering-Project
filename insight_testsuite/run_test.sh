# The script works for linux based systems

# Run the code for a sample data
python3 ./src/consumer_complaints.py ./insight_testsuite/test_input/ ./insight_testsuite/test_output/ complaints_test.csv report_test.csv

# For testing results against known output
python3 ./insight_testsuite/consumer_complaints_test.py ./insight_testsuite/test_output/
