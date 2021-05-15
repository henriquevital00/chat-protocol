import re


class Check:
    @staticmethod
    def validateCommand(command):
        pattern = '(^send( -m)?\ \"\S+\"$)|(^send( -f)?\ \S+\.\S+$)|(^get [\w\d\/]+\.\w+$)|(^list files$)|(^list users$)|(^list rooms$)|(^list -r$)|(^accept \S+$)|(^decline \S+$)|(^left( -r)?\ \S+$)|(^create \S+$)'
        isValid = re.search(pattern, command)
        if isValid:
            string = command.split(' ')[0]
            string = string.captalize()
            locals()[string].run()
        else:
            print('This is not a valid command')
