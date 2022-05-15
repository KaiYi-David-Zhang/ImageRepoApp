import os

# Master Test Script
# Run this to automatically run all the test cases
# Please remember to add additional test cases to this file

testCases = ['test_errors.py', 'test_add_display_delete.py']

for case in testCases:
    stringCat = 'python ' + case
    os.system(stringCat)