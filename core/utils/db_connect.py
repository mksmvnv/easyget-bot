# Created by @mksmvnv

import asyncpg


class Request():
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def add_user(self, user_id, username, full_name):
        query = f'INSERT INTO easyget_users (user_id, username, full_name) '\
            f'VALUES ({user_id}, \'{username}\', \'{full_name}\') '\
            f'ON CONFLICT (user_id) DO UPDATE SET username=\'{username}\''
        await self.connector.execute(query)
