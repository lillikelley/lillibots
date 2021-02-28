"""
file: bot.py
author: lilli kelley
desc: discord bot that messages a user over a given interval
"""

import discord

client = discord.Client()


@client.event
async def on_ready():  # runs once the client is ready; triggers once after logging on
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    server_id = client.get_guild(773225984706609232)

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    elif message.content.startswith('$users'):
        await message.channel.send(f"""# of Members: {server_id.member_count}""")

    if message.content == "$help":
        embed = discord.Embed(title="medbot commands")
        embed.add_field(name="$hello", value="greets the user")
        embed.add_field(name="$users", value="prints number of users")
        await message.channel.send(content=None, embed=embed)


async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "breakroom":  # makes sure to send in general
            await channel.send_message(f"""Welcome to the server {member.mention}""")


# logs in to discord with app's token
client.run('ODEzOTMyMTMzNTk2MTM1NDg1.YDWfXg.XkDTscqJcj9KucRTEq9pnemor28')
