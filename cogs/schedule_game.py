import discord
from discord.interactions import Interaction

from discord import app_commands
from discord.ext import commands
from discord.ui import Select, View, Button, Modal, TextInput

from functions import conversions, currentTime

#with open('imgs')
#DisapointedAbe = 

#['game type', 'ruleset', 'max','server']
message_data = ['','CPL','','']

#################################################################################################
# IF YOU EDIT THIS MODAL YOU PROBABLY ALSO NEED TO EDIT Schedule_Game_Modal
class Schedule_Game_Modal_With_Other(Modal, title="Configure your game: "):
    
    sgm_date = TextInput(
        style=discord.TextStyle.short,
        label="Date",
        required=True,
        placeholder="Pick a day... (yymmdd OR yy/mm/dd)"
    )
    
    sgm_time = TextInput(
        style=discord.TextStyle.short,
        label="Time",
        required=True,
        placeholder="Pick a time... (HHMMxm OR HH:MMxm)"
    )
    
    sgm_ruleset = TextInput(
        style=discord.TextStyle.short,
        label="Rule Set",
        required=True,
        placeholder="Pick a ruleset..."
    )
#
#    sgm_lobby_size = TextInput(
#        style=discord.TextStyle.short,
#        label="Lobby Size",
#        required=False,
#        placeholder="Pick a lobby size..."
#    )

    async def on_submit(self, interaction: Interaction):

        error = False
        
        if message_data[1] == 'Other':
            message_data[1] = self.sgm_ruleset
        
        # checking for users choice of formatting and splicing user responses to store data
        if str(self.sgm_date)[2] == '/' and str(self.sgm_date)[5] == '/':
            day = str(self.sgm_date)[6:8]
            month = str(self.sgm_date)[3:5]
            year = "20" + str(self.sgm_date)[0:2]
        else:
            day = str(self.sgm_date)[4:6]
            month = str(self.sgm_date)[2:4]
            year = "20" + str(self.sgm_date)[0:2]
            

        if str(self.sgm_time)[2] == ':':
            hour = str(self.sgm_time)[0:2]
            min = str(self.sgm_time)[3:5]
            meridiem = str(self.sgm_time)[5:7].lower()  
        else:
            hour = str(self.sgm_time)[0:2]
            min = str(self.sgm_time)[2:4]
            meridiem = str(self.sgm_time)[4:6].lower()
        
        #timezone = str(self.sgm_time)[8:].upper()
        #print(timezone)
        # checking for user errors

        # check for proper date format and responses
        currentYear = currentTime.year()
                
        if int(day) > 0 and int(day) < 31 and int(month) > 0 and int(month) < 13 and int(year) >= int(currentYear):
            #print('passed')
            pass
        else:
            await interaction.response.send_message(f'Invalid date. you answered: {year} {month} {day} for Date. Date format should be "ddmmyy"')

        # checking for proper time format and responses
            
        if int(hour) > 0 and int(hour) < 13 and int(min) >= 0 and int(min) <= 60:
            pass
        else:
            error = True 
            await interaction.response.send_message(f'Invalid Time. you answered {hour}:{min} for Time. Date format should be HHMMxm')

        # checking for am/pm
        if meridiem == 'pm':
            hour = int(hour)
            if hour != 12:
                hour += 12 
        elif meridiem == 'am':
            pass
        else:
            error = True
            await interaction.response.send_message(f'missing or misspelled am/pm after time. you answered: {self.sgm_time} for Time. Time format should be "XX:XXxm"')
        

        # sending scheduled game message
        
        if error == False:
            try:
                scheduled_game_time = conversions.convert_to_unix_time(day, month, year, hour, min)
                
                if message_data[3] == 'stable-host':
                    await interaction.response.send_message(f"React here if you will be participating in the {message_data[0]} game with the {message_data[1]} ruleset, {scheduled_game_time} (local time).  {message_data[2]} Slots Max.", ephemeral=False)
                else:
                    await interaction.response.send_message('you have broken me in ways I cannot begin to understand <a:wobble:1177214212284620811>')
                    
                # gets sent msg and adds reactions                 
                msg = await interaction.original_response()
                
                await msg.add_reaction('<:plus:1137771547566821456>')
                await msg.add_reaction('<:minus:1137771612695969792>')
                await msg.add_reaction('<:plusminus:1137771666693423228>')
                
                
            except:
                await interaction.response.send_message('you have broken me in ways I cannot begin to understand <a:wobble:1177214212284620811>')
        else:
            return
    
#################################################################################################

# IF YOU EDIT THIS MODAL YOU PROBABLY ALSO NEED TO EDIT Schedule_Game_Modal_With_Other   
class Schedule_Game_Modal(Modal, title="Configure your game: "):
    
    sgm_date = TextInput(
        style=discord.TextStyle.short,
        label="Date",
        required=True,
        placeholder="Pick a day... (yymmdd OR yy/mm/dd)"
    )
    
    sgm_time = TextInput(
        style=discord.TextStyle.short,
        label="Time",
        required=True,
        placeholder="Pick a time... (HHMMxm OR HH:MMxm)"
    )
    
#
#    sgm_lobby_size = TextInput(
#        style=discord.TextStyle.short,
#        label="Lobby Size",
#        required=False,
#        placeholder="Pick a lobby size..."
#    )

    async def on_submit(self, interaction: Interaction):

        error = False
        

        # checking for users choice of formatting and splicing user responses to store data
        if str(self.sgm_date)[2] == '/' and str(self.sgm_date)[5] == '/':
            day = str(self.sgm_date)[6:8]
            month = str(self.sgm_date)[3:5]
            year = "20" + str(self.sgm_date)[0:2]
        else:
            day = str(self.sgm_date)[4:6]
            month = str(self.sgm_date)[2:4]
            year = "20" + str(self.sgm_date)[0:2]
            

        if str(self.sgm_time)[2] == ':':
            hour = str(self.sgm_time)[0:2]
            min = str(self.sgm_time)[3:5]
            meridiem = str(self.sgm_time)[5:7].lower()  
        else:
            hour = str(self.sgm_time)[0:2]
            min = str(self.sgm_time)[2:4]
            meridiem = str(self.sgm_time)[4:6].lower()
        
        #timezone = str(self.sgm_time)[8:].upper()
        #print(timezone)
        # checking for user errors

        # check for proper date format and responses
        currentYear = currentTime.year()
                
        if int(day) > 0 and int(day) < 31 and int(month) > 0 and int(month) < 13 and int(year) >= int(currentYear):
            #print('passed')
            pass
        else:
            await interaction.response.send_message(f'Invalid date. you answered: {year} {month} {day} for Date. Date format should be "ddmmyy"')

        # checking for proper time format and responses
            
        if int(hour) > 0 and int(hour) < 13 and int(min) >= 0 and int(min) <= 60:
            pass
        else:
            error = True 
            await interaction.response.send_message(f'Invalid Time. you answered {hour}:{min} for Time. Date format should be HHMMxm')

        # checking for am/pm
        if meridiem == 'pm':
            hour = int(hour)
            if hour != 12:
                hour += 12 
        elif meridiem == 'am':
            pass
        else:
            error = True
            await interaction.response.send_message(f'missing or misspelled am/pm after time. you answered: {self.sgm_time} for Time. Time format should be "XX:XXxm"')
        

        # sending scheduled game message
        
        if error == False:
            try:
                scheduled_game_time = conversions.convert_to_unix_time(day, month, year, hour, min)
                
                if message_data[3] == 'other-game':
                    await interaction.response.send_message(f"React here if you will be participating in the {message_data[0]} game at {scheduled_game_time} (local time).  {message_data[2]} Slots Max.", ephemeral=False)
                elif message_data[3] == 'stable-host':
                    await interaction.response.send_message(f"React here if you will be participating in the {message_data[0]} game with the {message_data[1]} ruleset, {scheduled_game_time} (local time).  {message_data[2]} Slots Max.", ephemeral=False)
                else:
                    await interaction.response.send_message('you have broken me in ways I cannot begin to understand <a:wobble:1177214212284620811>')
                # gets sent msg and adds reactions 
                msg = await interaction.original_response()
                #print(msg.timest)
                await msg.add_reaction('<:plus:1137771547566821456>')
                await msg.add_reaction('<:minus:1137771612695969792>')
                await msg.add_reaction('<:plusminus:1137771666693423228>')
                
                
            except:
                await interaction.response.send_message('you have broken me in ways I cannot begin to understand <a:wobble:1177214212284620811>')
        else:
            return
    
#################################################################################################
    
class Ruleset_Select(Select):
    def __init__(self):
        
        options=[
            discord.SelectOption(
                default = True,
                label = "CPL", 
                emoji = "<a:amenity:1175170640475594932>", 
                description = "CPL ruleset"
            ),
            discord.SelectOption(
                label = "Shuffle", 
                emoji = "\U0001f500", 
                description = "Tech and Civic Shuffle",
            ),
            discord.SelectOption(
                label = "Other", 
                emoji = "\U0001f4ac", 
                description = "Custom one-time game type"
            ),
            
        ]

        # Initial prompt to user
        super().__init__(placeholder="Choose a ruleset:", max_values=1, min_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        
        # sets data to users selected value
        message_data[1] = self.values[0]
        await interaction.response.defer()

#################################################################################################

class Game_Type_Select(Select):
    
    def __init__(self):

        options=[
            discord.SelectOption(
                label = "FFA", 
                emoji = "\U0001f4a3", 
                description = "Free-for-all"
            ),
            discord.SelectOption(
                label = "Team", 
                emoji = "\U0001fa96", 
                description = "Team Vs. Team"
            )            
        ]
        
        # Initial prompt to user
        super().__init__(placeholder="Choose a game type:", max_values=1, min_values=1, options=options)
        
    # Responses
    async def callback(self, interaction: discord.Interaction):
        # sets data to users selected value
        message_data[0] = self.values[0]
        await interaction.response.defer()
     
        
#################################################################################################

class Max_Players_Select(Select):
    
    def __init__(self):

        # Select dropdown options
        options=[
            discord.SelectOption(
                label = "2", 
                emoji = "2\ufe0f\u20e3", 
                description = "2"
            ),
            discord.SelectOption(
                label = "3", 
                emoji = "3\ufe0f\u20e3", 
                description = "3"
            ),
            discord.SelectOption(
                label = "4", 
                emoji = "4\ufe0f\u20e3", 
                description = "4"
            ),
            discord.SelectOption(
                label = "5", 
                emoji = "5\ufe0f\u20e3", 
                description = "5"
            ),
            discord.SelectOption(
                label = "6", 
                emoji = "6\ufe0f\u20e3", 
                description = "6"
            ),
            discord.SelectOption(
                label = "7", 
                emoji = "7\ufe0f\u20e3", 
                description = "7"
            ),
            discord.SelectOption(
                label = "8", 
                emoji = "8\ufe0f\u20e3", 
                description = "8"
            ),
            discord.SelectOption(
                label = "9", 
                emoji = "9\ufe0f\u20e3", 
                description = "9"
            ),
            discord.SelectOption(
                label = "10", 
                emoji = "0\ufe0f\u20e3", 
                description = "10"
            ),
        ]
        
        # Initial prompt to user
        super().__init__(placeholder="How many players: ", max_values=1, min_values=1, options=options)
        
        # Responses
        
    async def callback(self, interaction: discord.Interaction):
        # sets data to users selected value
        message_data[2] = self.values[0]
        await interaction.response.defer()
        # await interaction.response.send_message(f"you chose: {self.values[0]}")
       
#################################################################################################

class Other_Game_Select(Select):
    
    def __init__(self):

        options=[
            discord.SelectOption(
                label = "Among Us", 
                emoji = "<a:sus:1137771770011721749> ", 
                description = "Sus."
            ),
            discord.SelectOption(
                label = "Bloons", 
                emoji = "\U0001f412", 
                description = "Z.O.M.G"
            ),
            discord.SelectOption(
                label = "Borderlands", 
                emoji = "<a:borderlandspsycho:1196731233389002794> ", 
                description = '"Get ready for a burning sensation" - Pyro Pete'
            ),
            discord.SelectOption(
                label = "Past Civ Games", 
                emoji = "<a:nice:1182187284104237116> ", 
                description = "MUHNaY"
            ),
            discord.SelectOption(
                label = "JackBox", 
                emoji = "<a:jackbox:1196732429990363166> ", 
                description = "R-O-N-G...wrong!"
            ),
            discord.SelectOption(
                label = "Minecraft", 
                emoji = "<a:sTeve:1196735275402010654> ", 
                description = "Yearn for the mines"
            ),
        ]
        
        # Initial prompt to user
        super().__init__(placeholder="Choose a game type:", max_values=1, min_values=1, options=options)
        
    # Responses
    async def callback(self, interaction: discord.Interaction):
        # sets data to users selected value
        message_data[0] = self.values[0]
        await interaction.response.defer()
     
        
#################################################################################################
        
class Schedule_Civ_Game_View(View):
    def __init__(self, *, timeout=600):
        super().__init__(timeout=timeout)

        # adds Select drop downs to the View
        self.add_item(Game_Type_Select())
        self.add_item(Max_Players_Select())
        self.add_item(Ruleset_Select())
        
    
    # Post Button
    @discord.ui.button(label='post',style = discord.ButtonStyle.green, emoji = "\u2705")
    async def post_button_callback(self, interaction: discord.Interaction, button: Button):
        message_data[3] = 'stable-host'
        if message_data[1] == "Other":
            await interaction.response.send_modal(Schedule_Game_Modal_With_Other())
        else:
            await interaction.response.send_modal(Schedule_Game_Modal())
        
        
        pass
    #self.add_item(Post_Button())

#################################################################################################
    
class Schedule_Other_Game_View(View):
    def __init__(self, *, timeout=600):
        super().__init__(timeout=timeout)

        # adds Select drop downs to the View
        self.add_item(Other_Game_Select())
        self.add_item(Max_Players_Select())
        
        
    
    # Post Button
    @discord.ui.button(label='post',style = discord.ButtonStyle.green, emoji = "\u2705")
    async def post_button_callback(self, interaction: discord.Interaction, button: Button):

        message_data[3] = 'other-game'
        await interaction.response.send_modal(Schedule_Game_Modal())
        
        
        pass
    #self.add_item(Post_Button())

#################################################################################################
    
class Schedule_Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("initialized bot")

    

    @app_commands.command(name='schedule_game', description="prompts user for game type, max players, game date, and game time ")
    async def schedule_game(self, interaction: discord.Interaction):
        stable_host_role = discord.utils.find(lambda r: r.name == 'stable-host', interaction.guild.roles)
        other_games_role = discord.utils.find(lambda r: r.name == 'Other-games', interaction.guild.roles)

        has_stable_host = False
        has_other_games = False

        test_site_denty_jr = 1175000095696093184
        scheduled_games_channel = 1097944940404801659
        other_games_channel = 1196511375703425044

        sg_channel_mention = interaction.user.guild.get_channel(scheduled_games_channel)
        og_channel_mention = interaction.user.guild.get_channel(other_games_channel)


        if stable_host_role in interaction.user.roles or other_games_role in interaction.user.roles:
            has_stable_host = True
            has_other_games = True
        elif stable_host_role in interaction.user.roles:
            has_stable_host = True
        elif other_games_role in interaction.user.roles:
            has_other_games = True
        else:
            has_stable_host = False
            has_other_games = False
        
        # checks if user has role "stable-host" and is sending the command from either "scheduled-games" or "test-site-denty-jr" channels
        if has_stable_host and (interaction.channel.id == scheduled_games_channel or interaction.channel.id == test_site_denty_jr):
                        
            # sends message containing Schedule_Civ_Game_View()
            await interaction.response.send_message("Configure your game: ", view=Schedule_Civ_Game_View(), delete_after=30, ephemeral=True)
        # checks if user has "other-games" role and is sending the command from either "scheduled-games" or "test-site-denty-jr" channels
        elif has_other_games and (interaction.channel.id == other_games_channel or interaction.channel.id == test_site_denty_jr):
            # sends message containing Schedule_Other_Game_View
            await interaction.response.send_message("Configure your game: ", view=Schedule_Other_Game_View(), delete_after=30, ephemeral=True)
        else: 
            # if stable host inform user which channel command is usable in
            if has_stable_host:
                
                await interaction.response.send_message(f'Command is only able to be used in {sg_channel_mention.mention} channel', ephemeral=True)
            # if user has other-games role inform user which channel command is usable in
            elif has_other_games:
                
                await interaction.response.send_message(f'Command is only able to be used in {og_channel_mention.mention} channel', ephemeral=True)
            # if not a stable host tell user they cannot use the command
            else:
                if interaction.channel.id == scheduled_games_channel or interaction.channel.id == test_site_denty_jr:
                    await interaction.response.send_message('Command is only able to be used if you have the role "stable-host"', ephemeral=True)
                elif interaction.channel.id == other_games_channel or interaction.channel.id == test_site_denty_jr:
                    await interaction.response.send_message('Command is only able to be used if you have the role "other-games"', ephemeral=True)
                else:
                    
                    await interaction.response.send_message('"My great concern is not whether you have failed, but whether you are content with your failure." - Abraham Lincoln', ephemeral=False)
                    msg = await interaction.original_response()
                
                    await msg.add_reaction('<a:DisappointedAbe:1196723318867365898>')
    @commands.Cog.listener()
    async def on_ready(self):
        print("Scheduled Games cog loaded")

#################################################################################################

# adding Schedule_Game class as a cog
async def setup(bot):
    await bot.add_cog(Schedule_Game(bot), guilds=[discord.Object(id=1065471300484743228)])