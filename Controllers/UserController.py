from Services.UserService import UserService
from Server.Response.Status import *
from Controllers.BaseController import BaseController
from Server.Auth.Decorator import AllowAnnonymous, Authorizate


class UserController(BaseController):
    def __init__(self, client):
        super().__init__(client)
        self.userService = UserService(client)

    @AllowAnnonymous
    def saveUser(self, username, password):

        responseBody = self.userService.saveUser(username, password)

        if responseBody is not None:
            return BadRequest(responseBody)

        return Ok(f"Created user {username} successfully!")

    @Authorizate
    def findByName(self, username):
        user = self.userService.findByName(username)

        if not len(user):
            raise Exception(BadRequest('User was not found'))

        return Ok(user)

    @Authorizate
    def findAll(self):

        users = self.userService.findAll()

        if not len(users):
            return BadRequest("No users were created!")

        return Ok(users)

    @Authorizate
    def findById(self, id):

        user = self.userService.findById(id)

        if not len(user):
            return BadRequest(f"No user with {id}")

        return Ok(user)

    @Authorizate
    def findUserRooms(self):

        userId = self.client.accountData.id
        rooms = self.userService.findUserRooms(userId)

        if not len(rooms):
            return BadRequest(f"No rooms")

        return Ok(rooms)

    @Authorizate
    def leftRoom(self):
        if self.client.activeRoom != None:
            self.client.activeRoom = None
            return Ok('Left room')

        return BadRequest('You are in menu')
