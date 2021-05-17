from Services.RoomService import RoomService
from Auth.Decorators import Authorization

# Room Controller
class RoomResources():

    roomService = RoomService()

    @Authorization
    def findAll(self):
        return self.roomService.findAll()


    @Authorization
    def saveRoom(self, room_name):
        return self.roomService.saveRoom(room_name)

    @Authorization
    def findUsersAtRoom(self, id):
        return self.roomService.findUsersAtRoom(id)

    @Authorization
    def findRoomMessages(self, id):
        return self.roomService.findRoomMessages(id)

    @Authorization
    def insertUserInRoom(self, room_id, user_id):
        return self.roomService.insertUserInRoom(room_id, user_id)
