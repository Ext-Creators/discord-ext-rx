import discord
from .messages import MessagesWrapper


class RxBot(discord.Client):
    streams = []

    @property
    def messages(self):
        mw = MessagesWrapper(self)
        self.streams.append(mw)
        return mw
    
    async def on_message(self, message):
        for s in self.streams:
            await s.eval(message)
