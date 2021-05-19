import re
from Commands.Get import Get
from Commands.List import List
from Commands.Send import Send
from Commands.Create import Create
from Commands.Accept import Accept
from Commands.Decline import Decline
from Commands.Left import Left
from Commands.Login import Login
from Commands.Logout import Logout
from Commands.Mv import Mv
from Services.UserService import UserService


class Check:
    @staticmethod
    def validateCommand(command):
        pattern = '(^send (-m)?\ .+$)|(^send (-f)?\ \S+\.\S+$)|(^send \S+ (((-m)?\ .+)|((-f)?\ \S+\.\S+))$)|(^get [\w\d\/]+\.\w+$)|(^list files$)|(^list users$)|(^list rooms$)|(^list -r$)|(^accept \S+$)|(^decline \S+$)|(^left( -r)?\ \S+$)|(^create \S+$)|(^create -r \S+$)|(^mv \S+$)|(^login \S+ \S+$)|(^logout$)|(^request \S+$)'
        isValid = re.search(pattern, command)
        if isValid:
            string = command.split(' ')[0]
            string = string.capitalize()
            eval(string).run(command)
        else:
            print('This is not a valid command')


Check.validateCommand('login abc abc')
Check.validateCommand('create abcdefgh')
Check.validateCommand('mv abcdefgh')
