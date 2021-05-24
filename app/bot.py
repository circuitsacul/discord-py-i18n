from discord.ext import commands

from app.i18n import current_locale, lazy_translate as _l


EXTENSIONS = [
    "app.cogs.base",
    "app.cogs.settings",
]


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
        )
        self._description = _l("This is the bots description.")
        self.locales = {}
        for ext in EXTENSIONS:
            self.load_extension(ext)

    @property
    def description(self):
        return str(self._description)

    @description.setter
    def description(self, *args, **kwargs):
        pass

    def set_locale(self, message):
        user_id = message.author.id
        current_locale.set(self.locales.get(user_id, "en_US"))

    async def on_message(self, message):
        if message.author.bot:
            return
        self.set_locale(message)
        await self.process_commands(message)
