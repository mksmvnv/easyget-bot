# Created by @mksmvnv

import asyncpg


class Request():
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector
    
    async def add_user(self, user_id, user_name):
        query = f'INSERT INTO user_data (user_id, user_name) VALUES ({user_id}, \'{user_name}\')'\
                f'ON CONFLICT (user_id) DO UPDATE SET user_name=\'{user_name}\''
        await self.connector.execute(query)
