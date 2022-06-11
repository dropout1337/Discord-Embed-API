import json
import asyncio
import motor.motor_asyncio as mongodb

class Database():

    def __init__(self):
        self.connection = mongodb.AsyncIOMotorClient("mongodb://localhost:27017")
        self.connection.get_io_loop = asyncio.get_running_loop
        self.database = self.connection["api"]["embeds"]
        