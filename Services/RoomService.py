from Services.BaseService import BaseService
from Repositories.RoomRepository import RoomRepository


class RoomService(BaseService):
    def __init__(self, client):
        super().__init__(client)
        self.roomRepository = RoomRepository()

    def findByName(self, room_name):
        return list(self.roomRepository.findByName(room_name))

    def findAll(self):from Services.BaseService import BaseService
from Repositories.RoomRepository import RoomRepository


class RoomService(BaseService):
    def __init__(self, client):
        super().__init__(client)
        self.roomRepository = RoomRepository()

    def findByName(self, room_name):
        return list(self.roomRepository.findByName(room_name))

    def findAll(self):

        rooms = list(self.roomRepository.findAll())

        return rooms

    def findUsersAtRoom(self, id):

        users = list(self.roomRepository.findUsersAtRoom(id))

        return users

    def findPendingUsers(self):

        room_id = self.client.activeRoom

        if not self.isRoomAdmin():
            return []

        pusers = list(self.roomRepository.findPendingUsers(room_id))

        return pusers

    def findRoomMessages(self):

        messages = list(
            self.roomRepository.findRoomMessages(self.client.activeRoom))

        return messages

    def rejectUser(self, user_id):
        try:
            room_id = self.client.activeRoom

            if not self.isRoomAdmin():
                return "Not allowed!"

            pending = self.client.roomController.findPendingUsers()

            if isinstance(pending, list):
                isUserPending = len(
                    list(filter(lambda room: room.user.id == user_id,
                                pending)))

                if not isUserPending:
                    return "This user has not requested the selected room!"
            else:
                return 'This room has no pending users!'

            self.roomRepository.rejectUser(user_id, room_id)

            return None

        except Exception as ex:
            return str(ex)

    def acceptUser(self, user_id):
        try:
            room_id = self.client.activeRoom

            if not self.isRoomAdmin():
                return "Not allowed!"

            pending = self.client.roomController.findPendingUsers()

            if isinstance(pending, list):
                isUserPending = len(
                    list(filter(lambda room: room.user.id == user_id,
                                pending)))

                if not isUserPending:
                    return "This user has not requested the selected room!"
            else:
                return 'This room has no pending users!'

            self.roomRepository.acceptUser(user_id, room_id)

            return None

        except Exception as ex:
            return str(ex)

    def createRequestToRoom(self, id):

        try:

            pendencies = list(self.roomRepository.findPendingUsers(id))

            for user in pendencies:
                if user.user_id.id == self.client.accountData.id:
                    return 'You have already sent a request to this room'

            room = self.client.userController.findUserRooms()

            if isinstance(room, list):
                alreadyInRoom = len(
                    list(filter(lambda user: user.user_room.id == id, room)))

                if alreadyInRoom:
                    return'You are already a member of this room'

            user_id = self.client.accountData.id

            self.roomRepository.createRequestToRoom({
                "room_id": id,
                "user_id": user_id
            })

            return None

        except Exception as ex:
            return str(ex)

    def isRoomAdmin(self):

        room_id = self.client.activeRoom
        user_id = self.client.accountData.id

        roomUsers = list(self.roomRepository.isRoomAdmin(room_id, user_id))

        return len(roomUsers)

    def saveRoom(self, room_name):

        try:
            roomAlreadyExists = len(
                list(self.roomRepository.findByName(room_name)))

            if roomAlreadyExists:
                return 'Room with the choosen name already exists!'

            user_id = self.client.accountData.id

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


        rooms = list(self.roomRepository.findAll())

        return rooms

    def findUsersAtRoom(self, id):

        users = list(self.roomRepository.findUsersAtRoom(id))

        return users

    def findPendingUsers(self):

        room_id = self.client.activeRoom

        if not self.isRoomAdmin():
            return []

        pusers = list(self.roomRepository.findPendingUsers(room_id))

        return pusers

    def findRoomMessages(self):

        messages = list(
            self.roomRepository.findRoomMessages(self.client.activeRoom))

        return messages

    def rejectUser(self, user_id):
        try:
            room_id = self.client.activeRoom

            if not self.isRoomAdmin():
                return "Not allowed!"

            pending = self.client.roomController.findPendingUsers()

            if isinstance(pending, list):
                isUserPending = len(
                    list(filter(lambda room: room.user.id == user_id,
                                pending)))

                if not isUserPending:
                    return "This user has not requested the selected room!"
            else:
                return 'This room has no pending users!'

            self.roomRepository.rejectUser(user_id, room_id)

            return None

        except Exception as ex:
            return str(ex)

    def acceptUser(self, user_id):
        try:
            room_id = self.client.activeRoom

            if not self.isRoomAdmin():
                return "Not allowed!"

            pending = self.client.roomController.findPendingUsers()

            if isinstance(pending, list):
                isUserPending = len(
                    list(filter(lambda room: room.user.id == user_id,
                                pending)))

                if not isUserPending:
                    return "This user has not requested the selected room!"
            else:
                return 'This room has no pending users!'

            self.roomRepository.acceptUser(user_id, room_id)

            return None

        except Exception as ex:
            return str(ex)

    def createRequestToRoom(self, id):

        try:

            pendencies = list(self.roomRepository.findPendingUsers(id))

            for user in pendencies:
                if user.user_id.id == self.client.accountData.id:
                    return 'You have already sent a request to this room'

            room = self.client.userController.findUserRooms()

            if isinstance(room, list):
                alreadyInRoom = len(
                    list(filter(lambda user: user.user_room.id == id, room)))

                if alreadyInRoom:
                    return'You are already a member of this room')

            user_id = self.client.accountData.id

            self.roomRepository.createRequestToRoom({
                "room_id": id,
                "user_id": user_id
            })

            return None

        except Exception as ex:
            return str(ex)

    def isRoomAdmin(self):

        room_id = self.client.activeRoom
        user_id = self.client.accountData.id

        roomUsers = list(self.roomRepository.isRoomAdmin(room_id, user_id))

        return len(roomUsers)

    def saveRoom(self, room_name):

        try:
            roomAlreadyExists = len(
                list(self.roomRepository.findByName(room_name)))

            if roomAlreadyExists:
                return 'Room with the choosen name already exists!'

            user_id = self.client.accountData.id

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
