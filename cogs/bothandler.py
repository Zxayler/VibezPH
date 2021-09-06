from discord.ext.commands import command, Cog, has_permissions
from discord import Embed 
import config

class BotHandler(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command()
    async def vhelp(self, ctx):
        em = Embed(color=config.color, title="Vibez PH Bot Commands")
        fields = [("Admin Commands", "`/status`\n`/send <message>`\n`/say <message>`\n`/edit-embed <message url>`\n`/edit-message <message url>`"),
                  ("Utility Commands", "`/nn <nickname>`\n`/user-info`\n`/server`\n`/avatar`"),
                  ("Image Commands", "`/vtab <text>`\n`/tab <text>`\n`/border <text>`\n`/player <text>`\n`/album <text>`"),
                  ("Bot Utilities", "`/botinfo`\n`/vhelp`\n`/bot-suggest <suggestion>`"),
                  ("Greeting Handler", "`/enable-greeting <channel`\n`/disable-greeting <channel>`\n`/greeting-status`\n`/configure-greeting`\n`/edit-duration <time>`\n`/greet-test`\n`/edit-greeting-mode <mode>`"),
                  ("Sticky Handler", "`/stick <channel> <'normal' | 'embed'> <message`\n`/delete-sticky <channel>`\n`/sticky-channels`")]
        for name, value in fields:
            em.add_field(name=name, value=value, inline=False)
        await ctx.send(embed=em)


    @command(aliases=['botinfo'])
    async def _botinfo(self, ctx):
        zach = self.bot.get_user(817701164258689054)
        em = Embed(color=config.color)
        fields = [("Bot Name", "Vibez PH"),
                  ("Bot ID", self.bot.user.id),
                  ("Version", "2.0"),
                  ("Bot Developer", zach.mention),
                  ("Github", "Coming Soon"),
                  ("Automations", "`Starboard System, Welcome System`")]
        for name, value, in fields:
            em.add_field(name=name, value=value, inline=False)
        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(BotHandler(bot))