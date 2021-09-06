from discord.ext.commands import Cog, command 
from discord import Embed
from discord.utils import get


class StatusSupporter(Cog):
	def __init__(self, bot):
		self.bot = bot

	@Cog.listener()
	async def on_member_update(self, before, after):
		guild = self.bot.get_guild(733175002383253636)
		role = get(guild.roles, id = 831496107346624523)
		status = ["discord.gg/mf5UFMfzYG", "discord.gg/vibezph"]
		if any(x in str(after.activities) for x in status):
			print("sadfsadf")
			if not role in after.roles:
				await after.add_roles(role)
			else:
				return
		else:
			if role in after.roles:
				await after.remove_roles(role)
			else:
				return

def setup(bot):
	bot.add_cog(StatusSupporter(bot))