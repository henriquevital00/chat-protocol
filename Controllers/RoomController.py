from Services.RoomService import RoomService
from Auth.Decorators import Authorization
from Server.Response.Status import *

@Authorization
class RoomController():

    roomService = RoomService()

    def findAll(self):

        rooms = self.roomService.findAll()

        if not len(rooms):
            return BadRequest("No rooms were created!")

        return Ok(rooms)

    def saveRoom(self, room_name):

        responseBody = self.roomService.saveRoom(room_name)

        if responseBody is not None:
            return BadRequest(responseBody)

        return Ok(f"Created room {room_name} successfully!")

    def findUsersAtRoom(self, id):

        users = self.roomService.findUsersAtRoom(id)

        if not len(users):
            return BadRequest("No users joined this room!")

        return Ok(users)

    def findRoomMessages(self, id):

        messages = self.roomService.findRoomMessages(id)

        if not len(messages):
            return BadRequest("No messages were sent in this room!")

        return Ok(messages)

    def findRoomFiles(self, id):

        files = self.roomService.findRoomFiles()

        if not len(files):
            return BadRequest("No files attached to this room!")

        return Ok(files)

    def insertUserInRoom(self, room_id, user_id):

        responseBody = self.roomService.insertUserInRoom(room_id, user_id)

        if responseBody is not None:
            return BadRequest(responseBody)

        return Ok(f"Inserted user in selected room successfully!")
