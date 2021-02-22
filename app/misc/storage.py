from os.path import exists
from datetime import datetime

from aiogram.types import User


class PhotoStorage:
    def __init__(self, path: str):
        self.path = path
        self.data = self.load()
    
    def load(self):
        if exists(self.path):
            with open(self.path) as file:
                return file.readlines()
        
        with open(self.path, "w") as file:
            return list()
    
    def save(self):
        with open(self.path, "w") as file:
            return file.writelines(self.data)
    
    def add(self, user: User, url: str):
        
        if user.username: username = f"@{user.username}"
        else: username = f"ID={user.id}"
        
        self.data.append(f"{datetime.now()} {username}: {url} \n")
        return self.save()
        

