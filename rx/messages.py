import inspect


class MessagesWrapper:
    def __init__(self, bot):
        self.bot = bot

        self.sequence = []
    
    async def eval(self, message):
        results = [[message]]

        for seq in self.sequence:
            if isinstance(seq, Filter):
                r = await seq.eval(*results[-1])

                if not r:
                    return
            elif isinstance(seq, Map):
                r = await seq.eval(*results[-1])

                results.append(r)
                print(r)
        
        await message.channel.send(**results[-1])

    def filter(self, callback):
        if self.sequence and isinstance(self.sequence[-1], Map):
            raise Exception('Cannot have a filter after map.')

        self.sequence.append(Filter(callback))
        return self
    
    def map(self, callback):
        self.sequence.append(Map(callback))
        return self


class Action:
    def __init__(self, callback):
        self.callback = callback
    
    async def eval(self, *args):
        return await self.follow_through(self.callback(*args))
    
    async def follow_through(self, result):
        if inspect.iscoroutine(result):
            return await result

        return result

class Filter(Action):
    ...

class Map(Action):
    async def eval(self, *args):
        return await self.follow_through(self.callback(*args))
