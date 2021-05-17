from Repositories.RoomRepository import RoomRepository
from Auth.Auth import Auth

class RoomService():

    roomRepository = RoomRepository()

    def findAll(self):

        rooms = list(self.roomRepository.findAll())

        return rooms

    def findUsersAtRoom(self, id):

        users = list(self.roomRepository.findUsersAtRoom(id))

        return users

    def findRoomMessages(self, id):

        messages = list(self.roomRepository.findRoomMessages(id))

        return messages

    def findRoomFiles(self, id):

        files = list(self.roomRepository.findRoomMessages(id))

        files = list(filter(lambda message: message.file != None, files))

        files = list(map(lambda message: (message.file_name, message.file), files))

        return files

    def saveRoom(self, room_name):

        try:
            user_id = Auth.logged_user().id

            room = {"name": room_name, "admin_id": user_id}

            self.roomRepository.saveRoom(room)

            new_room_id = list(self.roomRepository.findAll())[-1].id

            self.insertUserInRoom(new_room_id, user_id)

            return None

        except Exception as ex:

            return str(ex)

    def insertUserInRoom(self, room_id, user_id):

        try:
            room_user = {"room_id": room_id, "user_id": user_id}

            self.roomRepository.insertUserInRoom(room_user)

            return None

        except:

            return "Not corresponding data was inserted"
