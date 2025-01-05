# Discord-Ticketing-Bot
Discord bot for managing CTF event tickets with role-based permissions and automated support channel creation. 

### Rias-Gremory-Discord-Ticket-Bot
Discord bot for managing CTF event tickets with role-based permissions and automated support channel creation.

This Discord bot is designed to streamline the management of Capture The Flag (CTF) competitions, providing automated ticketing systems for technical support and organizer queries. The bot is tailored for CTF events, allowing teams to open, manage, and close support tickets efficiently. It supports role-based permissions and ensures privacy for team-specific issues.


## Features
  - Feature 1: Allows participants to open tickets for challenge-related issues, specifying challenge name, team name, problem description, and hall number.
  - Feature 2: Tickets are visible only to the ticket creator, tech support, and organizers, ensuring privacy and smooth workflow.
  - Feature 3: Tech support and organizers can easily close tickets once the issue is resolved.
  - Feature 4: Simple /ticket command for opening tickets and a 'Close Ticket' button for ending discussions.
  - Feature 5: Automatically creates dedicated ticket channels that are deleted when closed, keeping the server organized.

## Additional Changes
  - Customizing Table
  - Changing Roles who can view and access the ticket

## Installation Guide
  - Clone the Repository
```
git clone https://github.com/kavin-surya/Rias-Gremory-Discord-Ticket-Bot.git
```
  - Install the required dependencies
```
pip install -r requirements.txt
```
  - Run the Python
```
python3 rias-gremory.py
```
### Use the ```/ticket``` command to create a new support ticket.

## Creating a BOT and generating BOT TOKEN from Discord Developer Portel

## Step 1: Create a Discord Application
- Visit the [Discord Developer Portal](https://discord.com/developers/applications) and log in with your Discord account.
- **Create a New Application**:
    - Click the **"New Application"** button.
    - Give your application a name (this will be the bot's name) and click **Create**.

## Step 2: Add a Bot to the Application
- **Navigate to the "Bot" Section**:
    - In your application's settings, on the left sidebar, click on **"Bot"**.
- **Add the Bot**:
    - Click the **"Add Bot"** button and confirm by clicking **"Yes, do it!"** to turn your application into a bot.
- **Customize Your Bot**:
    - You can upload an avatar, give it a description or username.
    - Make sure the **"Public Bot"** option is enabled if you want others to invite your bot to their servers.

## Step 3: Generate the Bot Token
- **Copy Your Token**:
    - Under the **"Bot"** section, find the **"Token"** area and click **"Reset Token"** (or **"Copy"** if one is already generated).
    - Copy the bot token. This is a secret key that allows your bot to connect to Discord’s API.
  
``` ⚠️ Important: Never share your bot token publicly. It grants control over your bot. ```

## Step 4: Set Up OAuth2 for Permissions (Optional but Recommended)
- **Go to the "OAuth2" Section**:
    - In the left sidebar of the application, go to **OAuth2**.
- **Generate an Invite Link**:
    - Scroll down to the **OAuth2 URL Generator**.
    - Under **Scopes**, check **bot**.
    - Under **Bot Permissions**, check the permissions you want your bot to have (e.g., **Manage Channels**, **Send Messages**).
    - Copy the generated URL under **Generated URL**. This link will allow you to invite the bot to your server.

## Step 5: Invite the Bot to Your Server
- **Paste the OAuth2 Invite Link**:
    - Paste the OAuth2 invite link into your browser and select the server where you want to invite the bot.
    - Click **Authorize** to add the bot to the server.
