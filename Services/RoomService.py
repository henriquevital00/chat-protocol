from Repositories.RoomRepository import RoomRepository
from Auth.Auth import Auth

class RoomService():

    roomRepository = RoomRepository()

    def findAll(self):

        rooms = list(self.roomRepository.findAll())

        return rooms if len(rooms) > 0 else "No rooms were created!"

    def findUsersAtRoom(self, id):

        users = list(self.roomRepository.findUsersAtRoom(id))

        return users if len(users) > 0 else "No users joined this room!"

    def findRoomMessages(self, id):

        messages = list(self.roomRepository.findRoomMessages(id))

        return messages if len(messages) > 0 else "No messages were sent in this room!"

    def findRoomFiles(self, id):

        files = list(self.roomRepository.findRoomMessages(id))

        files = list(filter(lambda message: message.file != None, files))

        files = list(map(lambda message: (message.file_name, message.file), files))

        return files if len(files) > 0 else "No files attached to this room!"

    def saveRoom(self, room_name):

        try:
            user_id = Auth.logged_user().id

            room = {"name": room_name, "admin_id": user_id}

            self.roomRepository.saveRoom(room)

            new_room_id = list(self.roomRepository.findAll())[-1].id

            self.insertUserInRoom(new_room_id, user_id)

            return f"Created room {room} succesfully!"

        except:

            return "Not corresponding data was inserted"

    def insertUserInRoom(self, room_id, user_id):

        try:
            room_user = {"room_id": room_id, "user_id": user_id}

            self.roomRepository.insertUserInRoom(room_user)

            return f"User joined succesfully!"

        except:

            return "Not corresponding data was inserted"
