import discord
from discord.ext import commands
from discord import app_commands
import os

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

class RoleView(discord.ui.View):
    def __init__(self, role: discord.Role):
        super().__init__()
        self.role = role

    @discord.ui.button(label="認証する", style=discord.ButtonStyle.success)
    async def role_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.role not in interaction.user.roles:
            await interaction.user.add_roles(self.role)
            await interaction.response.send_message(f"{interaction.user.mention} さんにロール {self.role.name} を付与しました！", ephemeral=True)
        else:
            await interaction.response.send_message("すでにそのロールを持っています。", ephemeral=True)

@bot.tree.command(name="panel")
@app_commands.describe(role="付与するロールを選んでください")
async def panel(interaction: discord.Interaction, role: discord.Role):
    view = RoleView(role)
    await interaction.response.send_message("以下のボタンを押してロールを付与してください：", view=view)

@bot.event
async def on_ready():
    await bot.tree.sync()  # スラッシュコマンドを同期
    print("ボットが起動しました！")

bot.run(os.getenv("TOKEN"))
