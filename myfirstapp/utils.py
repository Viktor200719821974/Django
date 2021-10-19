import json
from typing import Optional

db = 'computers.json'

class DBUtils:
    @staticmethod
    def read_db()->list[dict]:
        try:
            with open(db) as file:
                return json.load(file)
        except Exception as ex:
            print(ex)
            return []

    @classmethod
    def create(cls, computer:dict)-> dict:
        computers = cls.read_db()
        new_computer = {'id':computers[-1].get('id')+1 if computers else 1, **computer}
        computers.append(new_computer)
        with open(db,'w') as file:
            json.dump(computers, file)
        return new_computer

    @classmethod
    def update(cls, data:dict, pk:int)->Optional[dict]:
        computers = cls.read_db()
        for computer in computers:
            if computer.get('id')==pk:
                computer.update(**data, id=pk)
                with open(db, 'w') as file:
                    json.dump(computers, file)
                return computer

    @classmethod
    def delete(cls, pk:int)->Optional[bool]:
        computers = cls.read_db()
        for computer in computers:
            if computer.get('id')==pk:
                computers.remove(computer)
                with open(db, 'w') as file:
                    json.dump(computers, file)
                return True

