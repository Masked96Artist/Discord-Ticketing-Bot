import discord
from discord.ext import commands
from discord.ui import Modal, TextInput, View, Button
import sqlite3


conn = sqlite3.connect('tickets.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY,
        user_id TEXT,
        challenge_name TEXT,
        problem_description TEXT,
        team_name TEXT,
        hall_number TEXT,
        channel_id TEXT,
        status TEXT
    )
''')
conn.commit()


intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix='/', intents=intents)

class TicketView(View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label="Create Ticket", style=discord.ButtonStyle.green, custom_id="create_ticket")
    async def create_ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        modal = TicketModal()
        await interaction.response.send_modal(modal)

class TicketModal(Modal):
    def __init__(self):
        super().__init__(title="Create a Ticket")
        self.add_item(TextInput(label="Challenge Name", placeholder="Enter the challenge name", required=True))
        self.add_item(TextInput(label="Problem Description", placeholder="Enter the problem description", required=True))
        self.add_item(TextInput(label="Team Name", placeholder="Enter the team name", required=True))
        self.add_item(TextInput(label="Hall Number", placeholder="Enter the hall number", required=True))

    async def on_submit(self, interaction: discord.Interaction):
        challenge_name = self.children[0].value
        problem_description = self.children[1].value
        team_name = self.children[2].value
        hall_number = self.children[3].value

        channel_name = f"ticket-{interaction.user.id}"
        category = discord.utils.get(interaction.guild.categories, name="Tickets")
        if not category:
            category = await interaction.guild.create_category(name="Tickets")

        
        tech_support_role = discord.utils.get(interaction.guild.roles, name="Tech Support")
        organizer_role = discord.utils.get(interaction.guild.roles, name="Organizer")

        overwrites = {
            interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            interaction.user: discord.PermissionOverwrite(read_messages=True),
        }

        if tech_support_role is not None:
            overwrites[tech_support_role] = discord.PermissionOverwrite(read_messages=True)

        if organizer_role is not None:
            overwrites[organizer_role] = discord.PermissionOverwrite(read_messages=True)

        
        ticket_channel = await interaction.guild.create_text_channel(name=channel_name, category=category, overwrites=overwrites)
        
        
        await ticket_channel.send(
            f"**Ticket Created by {interaction.user.mention}**\n"
            f"**Challenge Name:** {challenge_name}\n"
            f"**Problem Description:** {problem_description}\n"
            f"**Team Name:** {team_name}\n"
            f"**Hall Number:** {hall_number}\n"
            f"**Status:** Open",
            view=CloseTicketView()
        )

        
        c.execute('''
            INSERT INTO tickets (user_id, challenge_name, problem_description, team_name, hall_number, channel_id, status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (str(interaction.user.id), challenge_name, problem_description, team_name, hall_number, str(ticket_channel.id), 'Open'))
        conn.commit()

        await interaction.response.send_message("Your ticket has been created!", ephemeral=True)

class CloseTicketView(View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label="Close Ticket", style=discord.ButtonStyle.red, custom_id="close_ticket")
    async def close_ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.guild_permissions.manage_channels:
            
            c.execute('SELECT * FROM tickets WHERE channel_id = ?', (str(interaction.channel.id),))
            ticket = c.fetchone()
            if ticket:
                
                c.execute('UPDATE tickets SET status = ? WHERE channel_id = ?', ('Closed', str(interaction.channel.id)))
                conn.commit()

                
                await interaction.response.send_message("**Ticket has been closed**", ephemeral=True)
                await interaction.channel.delete()
            else:
                await interaction.response.send_message("Ticket not found.", ephemeral=True)
        else:
            await interaction.response.send_message("You do not have permission to close this ticket.", ephemeral=True)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def ticket(ctx):
    """Command to show the ticket creation button"""
    view = TicketView()
    await ctx.send("Click the button below to create a ticket:", view=view)

# Replace "Your_token" with the actual token from the discord developer portel
bot.run('Your_Token')
