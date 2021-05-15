import re


class Check:
    @staticmethod
    def validateCommand(command):
        pattern = '(^send( -m)?\ \"\w+\"$)|(^send( -i)?\ \"\w+\"$)|(^get [\w\d\/]+\.\w+$)|(^list files$)|(^list users$)|(^list -r$)|(^accept \S+$)|(^decline \S+$)|(^left( -r)?\ \S+$)'
        isValid = re.search(pattern, command)
        if isValid:
            func.run()
        else:
            print('This is not a valid command')
