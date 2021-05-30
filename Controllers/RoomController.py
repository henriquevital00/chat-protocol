from Services.RoomService import RoomService
from Server.Response.Status import *
from Controllers.BaseController import BaseController
from Server.Auth.Decorator import Authorizate


class RoomController(BaseController):
    def __init__(self, client):
        super().__init__(client)
        self.roomService = RoomService(client)

    @Authorizate
    def findByName(self, room_name):
        room_id = self.roomService.findByName(room_name)

        if not len(room_id):
            raise Exception(BadRequest('Room was not found'))

        return Ok(room_id)

    @Authorizate
    def findAll(self):

        rooms = self.roomService.findAll()

        if not len(rooms):
            return BadRequest("No rooms were created!")

        return Ok(rooms)

    @Authorizate
    def saveRoom(self, room_name):

        responseBody = self.roomService.saveRoom(room_name)

        if responseBody is not None:
            return BadRequest(responseBody)

        return Ok(f"Created room {room_name} successfully!")

    @Authorizate
    def findUsersAtRoom(self, id):

        if self.client.activeRoom != None:
            users = self.roomService.findUsersAtRoom(id)
            print('Users: ', users)

            if not len(users):
                return BadRequest("No users joined this room!")

            return Ok(users)
        else:
            return BadRequest('You are not in any room!')

    @Authorizate
    def findPendingUsers(self):
        pusers = self.roomService.findPendingUsers()

        if not len(pusers):
            return BadRequest("No pending users at room")

        return Ok(pusers)

    @Authorizate
    def findRoomMessages(self):

        messages = self.roomService.findRoomMessages()

        if not len(messages):
            return Alert(
                f"Welcome to the room, {self.client.accountData.username}")

        return Ok(messages)

    @Authorizate
    def acceptUser(self, user_id, accept=True):
        responseBody = self.roomService.acceptUser(user_id, accept)

        if responseBody is not None:
            return BadRequest(responseBody)

        if accept:
            return Ok("User accepted!")
        else:
            return Ok('User rejected!')

    @Authorizate
    def createRoomRequest(self, id):
        responseBody = self.roomService.createRequestToRoom(id)

        if responseBody is not None:
            return BadRequest(responseBody)

        return Ok("User admin will check your request!")

    @Authorizate
    def insertUserInRoom(self, room_id, user_id):

        responseBody = self.roomService.insertUserInRoom(room_id, user_id)

        if responseBody is not None:
            return BadRequest(responseBody)

        return Ok(f"Inserted user in selected room successfully!")
