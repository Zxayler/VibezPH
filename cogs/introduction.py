from discord.ext.commands import Cog, command
from discord import Embed
from asyncio import sleep

color = 0x47BFAA
emoji = "<:bbvibez_incoorect:773091288772771870>"
"<:bbvibez_ID:773091255667130368> "
class INTRODUCTION(Cog):
	def __init__(self, bot):
		self.client = bot

	@command(pass_context=True)
	async def intro(self, ctx):
		emoji1 = self.client.get_emoji(819772410076987402)
		emoji2 = self.client.get_emoji(819772384768032799)
		left = self.client.get_emoji(773092017404248104)
		right = self.client.get_emoji(773091768627494912)
		ID = self.client.get_emoji(773091255667130368)
		sign = self.client.get_emoji(773091654507692033)
		vibez = self.client.get_emoji(820008871069220942)
		if ctx.guild:
			await ctx.send(embed=Embed(color=color, description=f"{emoji} **This can only be done through DMS**"))
			return
		questions = [f"{emoji1} **Please input your Name**",
					 f"{emoji2} **Please input you nickname**",
					 f"{emoji1} **Please input your Age**",
					 f"{emoji2} **Please input you Gender**",
					 f"{emoji1} **Please input your Relationship Status**",
					 f"{emoji2} **Please input you Birthdate**",
					 f"{emoji1} **Please input your Nationality**",
					 f"{emoji2} **What are your hobbies?**",
					 f"{emoji1} **What are the things you like?**",
					 f"{emoji2} **What are the things you don't like?**",
					 f"{emoji1} **Describe yourself**",
					 f"{emoji2} **What is your motto?**"]
		message = await ctx.send(embed=Embed(color=color, description=f"           {left} I N T R O D U C T I O N {right}\n\nPlease wait 5 seconds..."))
		await sleep(5)
		answers = []
		for question in questions:
			await message.edit(embed=Embed(color=color, description=question))
			answer = await self.client.wait_for('message', check = lambda m: m.author == ctx.author and m.channel == ctx.channel)
			answers.append(str(answer.content))
		fields = [f"╭ {ID}❖⁀➷・⎯⎯⎯⎯⎯⎯⎯⎯・❖\n{emoji1} **ID:** __{ctx.author.id}__\n{emoji2} **Name**",
				  f"{emoji2} **Nickname**",
				  f"{emoji1} **Age**",
				  f"{emoji2} **Gender**",
				  f"{emoji1} **Relationship Status**",
				  f"{emoji2} **Birthdate**",
				  f"{emoji1} **Nationality**",
				  f"{emoji2} **Hobbies**",
				  f"{emoji1} **Likes**",
				  f"{emoji2} **Dislikes**",
				  f"{emoji1} **Describe yourself**",
				  f"{emoji2} **Motto**"]
		em = Embed(color=color, title=f"{vibez} INTRODUCTION").set_thumbnail(url=ctx.author.avatar_url)
		em.description= '\n'.join([f"{fields[idx]}: __{ans}__" for idx, ans in enumerate(answers)]) + f"\n╰{sign}❖⁀➷・⎯⎯⎯⎯⎯⎯⎯⎯・❖"
		channel = self.client.get_channel(834232644652892180)
		await channel.send(embed=em, content=str(ctx.author.mention))
		await ctx.send("**Introduction was sent successfully**")


def setup(bot):
	bot.add_cog(INTRODUCTION(bot))