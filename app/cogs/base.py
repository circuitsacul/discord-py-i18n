from app.i18n import lazy_translate as _l, translate as _t
from app import commands


class Base(commands.Cog, description=_l("A group of basic commands.")):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="ping",
        help=_l("Shows the bots latency."),  # lazy translate the command help
    )
    async def ping(self, ctx):
        # send the response, but translate immediatly.
        await ctx.send(_t("Pong! {0}").format(ctx.bot.latency))

    @commands.command(
        name="hello",
        help=_l("Make the bot say hello."),
    )
    async def hello(self, ctx):
        await ctx.send(_t("Hello, {0}!").format(ctx.message.author.mention))

    @commands.group(
        name="testgroup",
        help=_l("Testing group commands."),
    )
    async def testgroup(self, ctx):
        await ctx.send_help(ctx.command)


def setup(bot):
    bot.add_cog(Base(bot))
