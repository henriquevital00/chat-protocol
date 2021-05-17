from Services.UserService import UserService
from Auth.Decorators import Authorization
from Server.Response.Status import *

class UserController():

    userService = UserService()

    def saveUser(self, username, password):
        responseBody = self.userService.saveUser(username, password)

        if responseBody is not None:
            return BadRequest(responseBody)

        return Ok(f"Created user {username} successfully!")

    @Authorization
    def findAll(self):

        users = self.userService.findAll()

        if not len(users):
            return BadRequest("No users were created!")

        return Ok(users)

    @Authorization
    def findById(self, id):

        user = self.userService.findById(id)

        if not len(user):
            return BadRequest(f"No user with {id}")

        return Ok(user)


    @Authorization
    def findUserRooms(self, id: int):

        rooms = self.userService.findUserRooms(id)

        if not len(rooms):
            return BadRequest(f"No rooms")

        return Ok(rooms)


