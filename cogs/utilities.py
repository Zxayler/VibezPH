from discord.ext.commands import command, Cog 
from discord import Embed, Member
import config
from datetime import datetime, timedelta
from discord.utils import get

class Utilities(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(aliases=['vping'])
    async def ping(self, ctx):
        return await ctx.send(embed=Embed(color=config.color,
                              description=f"**PING:** {int(self.bot.latency*1000)} ms"))

    @command(aliases=['av'])
    async def avatar(self, ctx, member: Member = None):
        if member is None: member = ctx.author
        return await ctx.send(embed=Embed(color=config.color).set_image(url=member.avatar_url))

    @command(aliases=['user-info'])
    async def userinfo(self, ctx, mem: Member = None):
        if mem is None: mem = ctx.author
        em = Embed(color=config.color)
        fields = [("Name", mem.name),
                  ("ID", mem.id),
                  ("Discriminator", mem.discriminator),
                  ("Joined Discord on", (mem.created_at + timedelta(hours=8)).strftime("%A %B %d,%Y | %I:%M %p PH TIME")),
                  ("Joined VibezPH on", (mem.joined_at + timedelta(hours=8)).strftime("%A %B %d,%Y | %I:%M %p PH TIME"))]
        em.set_author(name=f"{mem}").set_thumbnail(url=mem.avatar_url)
        em.set_footer(text="/whois")
        await ctx.send(embed=em)

    @command(aliases=['server-info'])
    async def server(self, ctx):
        guild = ctx.guild
        em = Embed(color=config.color)
        em.set_author(name="Vibez PH Server Info")
        em.set_thumbnail(url=ctx.guild.icon_url)
        fields = [("ID", f"```{guild.id}```"),
                  ("Date of Creation", (guild.created_at + timedelta(hours=8)).strftime("```%A %B %d,%Y | %I:%M %p PH TIME```")),
                  (f"Members [{len(guild.members)}]", f"```Members: {len(list(filter(lambda m: not m.bot, guild.members)))} | Bots: {len(list(filter(lambda m: m.bot, guild.members)))}```"),
                  (f"Channels [{len(guild.channels)}]", f"```Text Channels: {len(guild.text_channels)} | Voice Channels: {len(guild.voice_channels)}```")]
        for name, value in fields:
            em.add_field(name=name, value=value, inline=False)
        em.set_footer(text="/server-info")
        await ctx.send(embed=em)

    @command(aliases=['nn'])
    async def nickname_change(self, ctx, *, nick = None):
        all_star = get(ctx.guild.roles, id = 805304497802575882)
        astro = get(ctx.guild.roles, id = 804117834905026580)
        babe_clan = get(ctx.guild.roles, id = 785823612107751454)
        nn_of_roles = {805304497802575882: "★", 804117834905026580: "⟁", 785823612107751454:"❥"}
        if not ctx.channel.id == 811528933253840956:
            return
        role = get(ctx.guild.roles, id = 739539840571277334)
        if not role in ctx.author.roles:
            return await ctx.send(embed=Embed(color=config.color, description = f"**You must have the {role.mention} role**"))
        if nick is None:
            return await ctx.send(embed=Embed(color=config.color, description = f"**:x: Please provide your nickname**"))
        if len(nick) > 24:
            return await ctx.send(embed=Embed(color=config.color, description = f"**:x: Nickname cannot be 25 characters or longer**"))
        if not any(c in ctx.author.roles for c in [all_star, astro, babe_clan]):
            await ctx.author.edit(nick=f"❖ {nick}")
            return await ctx.send(f"Nickname changed to `❖ {nick}`")
        for role in [all_star, astro, babe_clan]:
            if role in ctx.author.roles:
                await ctx.author.edit(nick=f"{nn_of_roles[role.id]} {nick}")
                await ctx.send(f"Nickname changed to `{nn_of_roles[role.id]} {nick}`")

    @command(aliases=['bot-suggest'])
    async def botsuggest(self, ctx, *, suggestion = None):
        zach = self.bot.get_user(817701164258689054)
        if suggestion is None: return await ctx.send(":x: Invalid Arguments. Provide your suggestion.")
        em = Embed(color=config.color, description=suggestion, timestamp=ctx.message.created_at)
        em.set_footer(text=f"Bot Suggestion | {ctx.author.name}")
        await ctx.send("Your suggestion has been sent successfully to the developer.")
        ch = self.bot.get_channel(828655864343953519)
        await ch.send(embed=em, content=zach.mention)

def setup(bot):
    bot.add_cog(Utilities(bot))