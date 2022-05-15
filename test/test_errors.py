from subprocess import Popen, PIPE, STDOUT

# These tests will test the error return by the program

# Test_No_Flag
cmd = 'java ImageRepo'
p = Popen(cmd, stdout=PIPE, stderr=PIPE)
stdout, stderr = p.communicate()
# checks if stderr has error
assert stderr, ("Test_No_Flag failed: program should print out and error to stderr \nCommand ran: %s" % (cmd)) 
print("Test_No_Flag: Passed")

# Test_No_Filename_Add
cmd = 'java ImageRepo -a'
p = Popen(cmd, stdout=PIPE, stderr=PIPE)
stdout, stderr = p.communicate()
assert stderr, ("Test_No_Filename failed: program should print out and error to stderr \nCommand ran: %s" % (cmd)) 
print("Test_No_Filename: Passed")


# Test_No_Filename_Dis
cmd = 'java ImageRepo -dis'
p = Popen(cmd, stdout=PIPE, stderr=PIPE)
stdout, stderr = p.communicate()
assert stderr, ("Test_No_Filename_Dis failed: program should print out and error to stderr \nCommand ran: %s" % (cmd)) 
print("Test_No_Filename_Dis: Passed")

# Test_No_Filename_Del
cmd = 'java ImageRepo -del'
p = Popen(cmd, stdout=PIPE, stderr=PIPE)
stdout, stderr = p.communicate()
assert stderr, ("Test_No_Filename_Del failed: program should print out and error to stderr \nCommand ran: %s" % (cmd)) 
print("Test_No_Filename_Del: Passed")

# Test_No_Filename_Help
cmd = 'java ImageRepo -h'
p = Popen(cmd, stdout=PIPE, stderr=PIPE)
stdout, stderr = p.communicate()
assert not stderr, ("Test_No_Filename_Help failed: program should not print out and error to stderr \nCommand ran: %s" % (cmd)) 
print("Test_No_Filename_Help: Passed")

# Test_No_Filename_List
cmd = 'java ImageRepo -h'
p = Popen(cmd, stdout=PIPE, stderr=PIPE)
stdout, stderr = p.communicate()
assert not stderr, ("Test_No_Filename_List failed: program should not print out and error to stderr \nCommand ran: %s" % (cmd)) 
print("Test_No_Filename_List: Passed")