# Created by @mksmvnv

import asyncpg


class Request():
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def add_user(self, user_id, username, full_name):
        query = 'INSERT INTO easyget_users (user_id, username, full_name) ' \
                'VALUES ($1, $2, $3) ' \
                'ON CONFLICT (user_id) DO UPDATE SET username=$2'

        await self.connector.execute(query, user_id, username, full_name)
