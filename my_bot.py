import discord
from search_util import g_search
from DB import cache_search


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hi'):
            await message.channel.send('hey')

        if message.content.startswith('!google'):
            query = message.content
            query = query.replace('!google', '')
            await message.channel.send(g_search(self, query))

        if message.content.startswith('!recent'):
            query = message.content
            query = query.replace('!recent', '')
            # query to get pattern matching string from table "recents" of the particular user
            exc = "select distinct searched from recents where user_id='{0}' and searched ~ '.*{1}.*'".format(self.user.id, query)
            await message.channel.send(cache_search(exc))


client = MyClient()
client.run('NzE1OTUwMzc5NTA1OTQyNjE5.XtJ8xQ.yYnL4Jt-bkVYqKcTosW_V52uHq8')