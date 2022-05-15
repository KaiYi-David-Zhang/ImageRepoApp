from subprocess import Popen, PIPE, STDOUT
from os.path import exists

# Test_Add_Image
cmd = 'java ImageRepo -add dice.png'
p = Popen(cmd, stdout=PIPE, stderr=PIPE)
stdout, stderr = p.communicate()
# checks if stderr has error
assert not stderr, ("Test_Add_Image failed: program should not print out and error to stderr \nCommand ran: %s" % (cmd)) 
assert exists("database/dice.pngen"), "Test_Add_Image failed: the encrypted image did not get created in the database folder"
print("Test_Add_Image: Passed")

# Test_List_Image
cmd = 'java ImageRepo -list'
p = Popen(cmd, stdout=PIPE, stderr=PIPE)
stdout, stderr = p.communicate()
# checks if stderr has error
assert not stderr, ("Test_List_Image failed: program should not print out and error to stderr \nCommand ran: %s" % (cmd)) 
assert 'dice.png' in stdout.decode('ascii'), "Test_List_Image failed: the decrypted image did not get created in the display folder"
print("Test_List_Image: Passed")

# Test_Delete_Image
cmd = 'java ImageRepo -del dice.png'
p = Popen(cmd, stdout=PIPE, stderr=PIPE)
stdout, stderr = p.communicate()
# checks if stderr has error
assert not stderr, ("Test_Delete_Image failed: program should not print out and error to stderr \nCommand ran: %s" % (cmd)) 
assert not exists("database/dice.pngen"), "Test_Delete_Image failed: the image did not get deleted"
print("Test_Delete_Image: Passed")
