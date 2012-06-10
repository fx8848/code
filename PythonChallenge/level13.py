#http://www.pythonchallenge.com/pc/return/disproportional.html

import xmlrpclib
test = xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print test.system.listMethods()
print test.phone('Bert')
