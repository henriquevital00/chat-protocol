class Session:
    room_id = None

    @staticmethod
    def get_instance(room=None):
        if Session.room_id == None:
            Session.room_id = room

        return Session.room_id

    @staticmethod
    def setRoomId(Id):
        Session.room_id = Id

    @staticmethod
    def getRoomId():
        return Session.room_id
