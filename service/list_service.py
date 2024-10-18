from model import model

class ListDEService:
    def __init__(self):
        self.__kids = model.ListDE()

    def get_kids(self):
        return self.__kids.show()

    def add_kid(self, kid):
        self.__kids.add(kid)

    def add_kid_to_start(self, kid):
        self.__kids.add_to_start(kid)

    def add_kid_in_position(self, kid, position):
        self.__kids.add_in_position(kid, position)

    def delete_kid_by_id(self, kid_id):
        self.__kids.delete_by_id(kid_id)

    def delete_kid_by_position(self, position):
        self.__kids.delete_by_position(position)

    def switch_ends(self):
        self.__kids.switch_ends()

    def switch_by_gender(self):
        self.__kids.switch_by_gender()

    def invert(self):
        self.__kids.invert()

    def get_size(self):
        return self.__kids.get_size()