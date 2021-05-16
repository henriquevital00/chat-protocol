from Services.RoomService import RoomService

# Room Controller
class RoomResources():

    roomService = RoomService()

    def findAll(self):
        return self.roomService.findAll()

    def saveRoom(self, room_name, user_id):
        return self.saveRoom(room_name, user_id)

    def findUsersAtRoom(self, id):
        return self.roomService.findUsersAtRoom(id)

    def findRoomMessages(self, id):
        return self.roomService.findRoomMessages(id)

    def insertUserInRoom(self, room_id, user_id):
        return self.roomService.insertUserInRoom(room_id, user_id)