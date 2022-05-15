import os

testCases = ['test_errors.py', 'test_add_display_delete.py']

for case in testCases:
    stringCat = 'python ' + case
    os.system(stringCat)