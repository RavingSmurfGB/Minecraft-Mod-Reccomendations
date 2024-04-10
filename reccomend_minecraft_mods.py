# This python file communicated with a Discord bot and passes information to it, based off of the commands recieved.
import discord
import yaml
import os
import logging
import datetime
      


if __name__ == '__main__': 

    log_file = datetime.datetime.now().strftime("%Y-%m-%d")  + "--reccomend_minecraft_mods.log" 

    # Setup logging
    logging.basicConfig(
        format="%(name)s: %(asctime)s | %(levelname)s | %(filename)s:%(lineno)s | %(process)d >>> %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%SZ",
        level=logging.CRITICAL,
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()])



    # Assign self.token from file "application_token.txt""
    # We also check application_token.txt if exists and if empty
    try: 
        with open("application_token.txt", "r") as stream:
            discord_token = stream.read()

            if discord_token == "":
                error_msg = '''\n \n Ensure that you have added your Discord bot Token to the file "application_token.txt" \n To view information on how to do this: https://realpython.com/how-to-make-a-discord-bot-python/#creating-an-application'''
                logging.exception(EOFError(error_msg))
                raise EOFError(error_msg)
    except FileNotFoundError as exc:
        error_msg = '''\n \n The discord bot "discord-reccomend-mod-bot.py" could not find the file "application_token.txt" \n - This file is needed to authenticate with Discord \n - Ensure it is in the same directory as "discord-reccomend-mod-bot.py" \n Create the file "application_token.txt" and paste your Discord Token in to it \n \n'''
        logging.exception(error_msg)
        exc.strerror =  error_msg + exc.strerror
        raise exc
    
    
    # Assign self.reccomends_dict from file mod-reccomendations.yaml
    # We also check mod-reccomendations.yaml if exists, if valid and if empty
    exception_msg = '''\n \n The discord bot "discord-reccomend-mod-bot.py" could not find the file "mod-reccomendations.yaml" \n   - This file contains the data about the reccomended mods \n  Please ensure that the file "mod-reccomendations.yaml" exists and is in the same directory as "discord-bot.py \n You may need to download "mod-reccomendations.yaml" again from GitHub\n \n'''
    try:
        with open("mod-reccomendations.yaml") as stream: 
            try:
                reccomends_dict = yaml.safe_load(stream)
                if reccomends_dict  == None:
                    logging.exception(exception_msg)
                    raise EOFError(exception_msg)
            except yaml.YAMLError as exc:
                logging.exception(exception_msg)
                raise exc(exception_msg)
    except FileNotFoundError as exc:
        exc.strerror =  exception_msg + exc.strerror
        raise exc






    ####### discord client 
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)


    @client.event
    async def on_ready():
        logging.info(f'Connected to Discord {client.user}')


    @client.event
    async def on_message(message):
        #Ignore own message..
        if message.author == client.user:
            return
        
        # discord embed - # https://stackoverflow.com/questions/72078273/how-to-embed-an-image-with-a-url-on-discord-with-a-bot-using-python
        # colours - https://discordpy.readthedocs.io/en/stable/api.html#colour
        
        
        # Commands
        if message.content.startswith('!commands'):
            embedVar = discord.Embed(title="Commands", description=" ", color=0x1ABC9C)
            embedVar.add_field(name="!commands", value="Lists all availible commands", inline=False )
            embedVar.add_field(name="!resource", value="Provides a list of all the Resource Packs Joe reccomends", inline=False)
            embedVar.set_footer(text = 'RavingSmurfGB', icon_url= "https://avatars.githubusercontent.com/u/23278939?s=400&u=d649e4f89ffcb3063eeabdbc41eee6fb071eeddb&v=4")
            await message.channel.send(embed=embedVar, delete_after=120)



        # Resource Packs
        if message.content.startswith('!resource'):
            embedVar = discord.Embed(title="Resource Packs", description=" ", color=0x00ff00)
            for key, value in reccomends_dict.items():
                if value["Catagory"]== "Resource Pack":

                    embedVar.add_field(name=key, value=value, inline=False)
                embedVar.set_footer()
                embedVar.set_footer(text = 'hey', icon_url= "https://cdn.modrinth.com/data/tOCRtfAR/f6cc525b2c8182da0eda51f94edf2915e5dc02a8.png")
                embedVar.set_footer(text = 'sdsdsd', icon_url= "https://cdn.modrinth.com/data/tOCRtfAR/f6cc525b2c8182da0eda51f94edf2915e5dc02a8.png")

                
                await message.channel.send(embed=embedVar, delete_after=120)


            
    client.run(discord_token)


