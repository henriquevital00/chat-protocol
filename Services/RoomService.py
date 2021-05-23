from Repositories.RoomRepository import RoomRepository
from Auth.Auth import Auth
from Auth.Session import Session


class RoomService():

    roomRepository = RoomRepository()

    def findByName(self, room_name):
        return list(self.roomRepository.findByName(room_name))

    def findAll(self):

        rooms = list(self.roomRepository.findAll())

        return rooms

    def findUsersAtRoom(self, id):

        users = list(self.roomRepository.findUsersAtRoom(id))

        return users

    def findPendingUsers(self):

        room_id = Session.getRoomId()

        if not self.isRoomAdmin():
            return []

        pusers = list(self.roomRepository.findPendingUsers(room_id))

        return pusers

    def findRoomMessages(self, id):

        messages = list(self.roomRepository.findRoomMessages(id))

        return messages

    def rejectUser(self, user_id):
        try:
            room_id = Session.getRoomId()

            if not self.isRoomAdmin():
                raise Exception("Not allowed!")

            self.roomRepository.rejectUser(user_id, room_id)

            return None

        except Exception as ex:
            return str(ex)

    def acceptUser(self, user_id):
        try:
            room_id = Session.getRoomId()

            if not self.isRoomAdmin():
                raise Exception("Not allowed!")

            self.roomRepository.acceptUser(user_id, room_id)

            return None

        except Exception as ex:
            return str(ex)

    def createRequestToRoom(self, id):

        try:
            user_id = Auth.logged_user()

            self.roomRepository.createRequestToRoom({"room_id": id, "user_id": user_id})

            return None

        except Exception as ex:
            return str(ex)

    def isRoomAdmin(self):

        room_id = Session.getRoomId()
        user_id = Auth.logged_user().id

        roomUsers = list(self.roomRepository.isRoomAdmin(room_id, user_id))

        return len(roomUsers)

    def saveRoom(self, room_name):

        try:
            user_id = Auth.logged_user().id

            room = {"name": room_name, "admin_id": user_id}

            self.roomRepository.saveRoom(room)

            new_room_id = list(self.roomRepository.findAll())[-1].id

            self.insertUserInRoom(new_room_id, user_id, True)

            return None

        except Exception as ex:

            return str(ex)

    def insertUserInRoom(self, room_id, user_id, isInRoom=False):

        try:
            room_user = {
                "room_id": room_id,
                "user_id": user_id,
                "isInRoom": isInRoom
            }

            self.roomRepository.insertUserInRoom(room_user)

            return None

        except:

            return "Not corresponding data was inserted"
