# Created by @mksmvnv

import asyncpg


class Request():
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def add_user(self, user_id, username, full_name):
        query = f'INSERT INTO easyget_users (user_id, username, full_name) VALUES'\
            f'({user_id}, \'{username}\', \'{full_name}\')'
        await self.connector.execute(query)
