discord-ext-rx
==============

|package| |versions| |dependencies| |license| |cloned|

Combine `RxPy`_ with `discord.py`_.

   ⚠️ Work In Progress!

Installation
------------

This extension is on `PyPI <https://pypi.org/project/discord-ext-rx/>`_.

.. code-block:: sh

    $ python3 -m pip install -U discord-ext-rx

Usage
-----

.. code:: py

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

.. _RxPy: https://github.com/ReactiveX/RxPy
.. _discord.py: https://github.com/Rapptz/discord.py

.. |package| image:: https://img.shields.io/pypi/v/discord-ext-rx.svg
.. |versions| image:: https://img.shields.io/pypi/pyversions/discord-ext-rx.svg
.. |dependencies| image:: https://img.shields.io/librariesio/github/Ext-Creators/discord-ext-rx
.. |license| image:: https://img.shields.io/pypi/l/discord-ext-rx.svg
.. |cloned| image:: https://img.shields.io/pypi/dm/discord-ext-rx.svg
