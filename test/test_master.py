import os

testCases = ['test_errors.py', 'test2.py']

for case in testCases:
    stringCat = 'python ' + case
    os.system(stringCat)