from Services.RoomService import RoomService
from Auth.Decorators import Authorization

@Authorization
class RoomController():

    roomService = RoomService()

    def findAll(self):
        return self.roomService.findAll()

    def saveRoom(self, room_name):
        return self.roomService.saveRoom(room_name)

    def findUsersAtRoom(self, id):
        return self.roomService.findUsersAtRoom(id)

    def findRoomMessages(self, id):
        return self.roomService.findRoomMessages(id)

    def insertUserInRoom(self, room_id, user_id):
        return self.roomService.insertUserInRoom(room_id, user_id)
