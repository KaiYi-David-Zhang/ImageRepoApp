from subprocess import Popen, PIPE, STDOUT

# Test_No_Flag
cmd = 'java ImageRepo'
p = Popen(cmd, stdout=PIPE, stderr=PIPE)
stdout, stderr = p.communicate()
print(stderr)
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