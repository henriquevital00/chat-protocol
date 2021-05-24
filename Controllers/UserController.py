from Services.UserService import UserService
from Server.Response.Status import *
from Controllers.BaseController import BaseController

class UserController(BaseController):

    def __init__(self, client):
        super().__init__(client)
        self.userService = UserService(client)

    def saveUser(self, username, password):

        responseBody = self.userService.saveUser(username, password)

        if responseBody is not None:
            return BadRequest(responseBody)

        return Ok(f"Created user {username} successfully!")

    def findByName(self, username):
        user = self.userService.findByName(username)

        if not len(user):
            return BadRequest('User was not found')

        return Ok(user)

    def findAll(self):

        users = self.userService.findAll()

        if not len(users):
            return BadRequest("No users were created!")

        return Ok(users)

    def findById(self, id):

        user = self.userService.findById(id)

        if not len(user):
            return BadRequest(f"No user with {id}")

        return Ok(user)

    def findUserRooms(self):

        userId = self.client.accountData.id
        rooms = self.userService.findUserRooms(userId)

        if not len(rooms):
            return BadRequest(f"No rooms")

        return Ok(rooms)
