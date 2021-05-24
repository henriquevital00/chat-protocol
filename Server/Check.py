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
from Commands.Exit import Exit
from Services.UserService import UserService


class Check:
    @staticmethod
    def validateCommand(command, client):
        pattern = '(^send (-m)?\ \".+\"$)|(^send \S+( -m)?\ \".+\"$)|(^list files$)|(^list users$)|(^list rooms$)|(^list -r$)|(^accept \S+$)|(^decline \S+$)|(^left (-r)$)|(^create \S+ \S+$)|(^create -r \S+$)|(^mv \S+$)|(^login \S+ \S+$)|(^logout$)|(^request \S+$)|(exit)'
        isValid = re.search(pattern, command)
        if isValid:
            string = command.split(' ')[0]
            string = string.capitalize()
            return eval(string).run(command, client)
        else:
            return 'This is not a valid command'
