"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
                "id": 1,
                "first_name": "Pedro",
                "last_name": self.last_name,
                "age": 45,
                "lucky_numbers": [31, 12, 28]
            },
            {
                "id": 2,
                "first_name": "Ana",
                "last_name": self.last_name,
                "age": 30,
                "lucky_numbers": [5, 3, 33]
            },
            {
                "id": 3,
                "first_name": "juan",
                "last_name": self.last_name,
                "age": 18,
                "lucky_numbers": [10, 24, 18]
            },
            {
                "id": 4,
                "first_name": "Maria",
                "last_name": self.last_name,
                "age": 33,
                "lucky_numbers": [5, 14, 8]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        if member["id"] is None:
            member["id"] = self._generateId()
        member["last_name"] = self.last_name
        self._members.append(member)
        return self._members
        pass

    def delete_member(self, id):
        self._members = list(
            filter(lambda item: id != item["id"], self._members))
        return None
        pass

    def get_member(self, id):
        for member in self._members:
            if id == member["id"]:
                return member
        pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
