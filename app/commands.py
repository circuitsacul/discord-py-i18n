from discord.ext import commands
from discord.ext.commands import *  # noqa F401


class Command(commands.Command):
    def __init__(self, *args, **kwargs):
        self._help = kwargs.pop("help", None)
        super().__init__(*args, **kwargs)

    @property
    def help(self):
        return str(self._help)

    @help.setter
    def help(self, *args, **kwargs):
        pass


class Group(commands.Group):
    def __init__(self, *args, **kwargs):
        self._help = kwargs.pop("help", None)
        super().__init__(*args, **kwargs)

    @property
    def help(self):
        return str(self._help)

    @help.setter
    def help(self, *args, **kwargs):
        pass


class Cog(commands.Cog):
    @property
    def description(self):
        return str(self.__cog_description__)

    @description.setter
    def description(self, desc):
        self.__cog_description__ = desc


def command(*args, **kwargs):
    return commands.command(*args, cls=Command, **kwargs)


def group(*args, **kwargs):
    return commands.group(*args, cls=Group, **kwargs)
