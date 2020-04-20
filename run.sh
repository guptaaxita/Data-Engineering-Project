# The script works for linux based systems

# Run the code for sample data and whole data
python3 ./src/consumer_complaints.py ./input/ ./output/ ./insight_testsuite/test_input/ ./insight_testsuite/test_output/

# For testing results against known output
python3 ./insight_testsuite/consumer_complaints_test.py ./insight_testsuite/test_output/

