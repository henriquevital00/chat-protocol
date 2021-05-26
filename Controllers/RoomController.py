from Services.RoomService import RoomService
from Server.Response.Status import *
from Controllers.BaseController import BaseController


class RoomController(BaseController):
    def __init__(self, client):
        super().__init__(client)
        self.roomService = RoomService(client)

    def findByName(self, room_name):
        room_id = self.roomService.findByName(room_name)

        if not len(room_id):
            return BadRequest('Room was not found')
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

    def findPendingUsers(self):
        pusers = self.roomService.findPendingUsers()

        if not len(pusers):
            return BadRequest("No pending users at room")

        return Ok(pusers)

    def findRoomMessages(self):

        messages = self.roomService.findRoomMessages()

        if not len(messages):
            return Alert(
                f"Welcome to the room, {self.client.accountData.username}")

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

    def createRoomRequest(self, id):
        responseBody = self.roomService.createRequestToRoom(id)

        if responseBody is not None:
            return BadRequest(responseBody)

        return Ok("User admin will check your request!")

    def insertUserInRoom(self, room_id, user_id):

        responseBody = self.roomService.insertUserInRoom(room_id, user_id)

        if responseBody is not None:
            return BadRequest(responseBody)

        return Ok(f"Inserted user in selected room successfully!")
