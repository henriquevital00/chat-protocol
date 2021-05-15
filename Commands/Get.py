class Get:
    @staticmethod
    def download(file):
        pass

    @staticmethod
    def run(command):
        var = command.split(' ')
        Get.download(var[1])
