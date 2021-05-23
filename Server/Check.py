import re
from Commands.List import List
from Commands.Send import Send
from Commands.Create import Create
from Commands.Accept import Accept
from Commands.Decline import Decline
from Commands.Left import Left
from Commands.Login import Login
from Commands.Logout import Logout
from Commands.Mv import Mv
from Commands.Request import Request
from Services.UserService import UserService


class Check:
    @staticmethod
    def validateCommand(command):
        pattern = '(^send (-m)?\ \".+\"$)|(^send \S+( -m)?\ \".+\"$)|(^list files$)|(^list users$)|(^list rooms$)|(^list -r$)|(^accept \S+$)|(^decline \S+$)|(^left (-r)$)|(^create \S+ \S+$)|(^create -r \S+$)|(^mv \S+$)|(^login \S+ \S+$)|(^logout$)|(^request \S+$)'
        isValid = re.search(pattern, command)
        if isValid:
            string = command.split(' ')[0]
            string = string.capitalize()
            eval(string).run(command)
        else:
            print('This is not a valid command')


print("loga usuario")
Check.validateCommand('login testUser 123')
#Check.validateCommand('send felipe -m "iae arrombado"')
Check.validateCommand('mv abc')
Check.validateCommand('send -m "iae arrombado"')

# Check.validateCommand('mv abcdefgh')
# print("Lista usuarios pendentes")
# Check.validateCommand('list -r')
# print("Rejeita usuarios pendentes")
# Check.validateCommand('decline testUser')
# print("Aceita usuarios pendentes")
# Check.validateCommand('accept testUser')
# #print("Rejeita usuarios pendentes")
#Check.validateCommand('decline jao')