import discord
import discord.app_commands
import os

intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(f'Running {client.user}')
    await tree.sync(guild=discord.Object(id=12345))

@client.event
async def on_interaction(inter:discord.Interaction):
    try:
        if inter.data['component_type'] == 2:
            await on_button_click(inter)
    except KeyError:
        pass

@tree.command(guild=discord.Object(id=12345), name='rolebuton', description='ロール付与パネルを表示します。')
async def launch_button(interaction: discord.Interaction, ロール: discord.Role, タイトル: str = None, 説明: str = None):

    if タイトル is None:
        タイトル = "役職パネル"
    if 説明 is None:
        説明 = f"「✅」を押すと、{ロール.mention}が付与されます。"

    embed = discord.Embed(title=タイトル, description=説明, color=discord.Color.blue())
    if interaction.user.guild_permissions.administrator:
        button = discord.ui.Button(label="✅", style=discord.ButtonStyle.primary, custom_id="check")
        view = discord.ui.View()
        view.add_item(button)
        await interaction.response.send_message(embed=embed, view=view)

async def on_button_click(inter: discord.Interaction):
    custom_id = inter.data["custom_id"]
    if custom_id == "check":
            
            await inter.user.add_roles()
            await inter.response.send_message("付与されました。", ephemeral = True)

client.run(os.getenv('TOKEN'))
