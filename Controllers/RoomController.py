from Services.RoomService import RoomService
from Auth.Decorators import Authorization
from Server.Response.Status import *


@Authorization
class RoomController():

    roomService = RoomService()

    def findByName(self, room_name):
        room_id = self.roomService.findByName(room_name)

        if not len(room_id):
            return BadRequest('Room was not finded')
        return Ok(room_id)

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

    def findPendingUsers(self, id):
        pusers = self.roomService.findPendingUsers(id)

        if not len(pusers):
            return BadRequest("No pending users at room")




    def findRoomMessages(self, id):

        messages = self.roomService.findRoomMessages(id)

        if not len(messages):
            return BadRequest("No messages were sent in this room!")

        return Ok(messages)

    def rejectUser(self, user_id):

        responseBody = self.roomService.rejectUser(user_id)

        if responseBody is not None:
            return BadRequest(responseBody)

        return Ok("User rejected!")


    def acceptUser(self, user_id):
        responseBody = self.roomService.acceptUser(user_id)

        if responseBody is not None:
            return BadRequest(responseBody)

        return Ok("User accepted!")

    def findRoomFiles(self, id):

        files = self.roomService.findRoomFiles(id)

        if not len(files):
            return BadRequest("No files attached to this room!")

        return Ok(files)

    def insertUserInRoom(self, room_id, user_id):

        responseBody = self.roomService.insertUserInRoom(room_id, user_id)

        if responseBody is not None:
            return BadRequest(responseBody)

        return Ok(f"Inserted user in selected room successfully!")
