from app.i18n import lazy_translate as _l, translate as _t
from app import commands


class Settings(commands.Cog, description=_l("A group of setting commands.")):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="language", aliases=["setlang", "lang"],
        help=_l("Sets your personal language."),
    )
    async def set_language(self, ctx, language: str):
        self.bot.locales[ctx.message.author.id] = language
        await ctx.send(
            _t("Your language has been set to {0}.").format(language)
        )


def setup(bot):
    bot.add_cog(Settings(bot))
