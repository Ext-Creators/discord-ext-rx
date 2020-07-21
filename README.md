# discord-ext-rx

> Work In Progress!

Combine [RxPy](https://github.com/ReactiveX/RxPy) with [discord.py](https://github.com/Rapptz/discord.py).

## Example

```py
from discord.ext.rx import RxBot, _
from rx import operators as ops

bot = RxBot()

bot.messages.pipe(
    ops.filter(lambda m: m.author.id == 121678432504512512),
    ops.filter(lambda m: m.content == '418'),
    ops.map(lambda m: m.channel)
).subscribe(
    _(lambda c: c.send("I'm a teapot!"))
)

bot.run('token')
```
