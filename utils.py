import requests
import config

API_ENDPOINT = 'https://discord.com/api/v10'
CLIENT_ID = config.CLIENT_ID
CLIENT_SECRET = config.CLIENT_SECRET
REDIRECT_URI = config.REDIRECT_URI
BOT_TOKEN = config.BOT_TOKEN
def get_token(code: str):
    data = {
    'grant_type': 'authorization_code',
    'code': code,
    'redirect_uri': REDIRECT_URI,
    'scope': 'identify guilds'
  }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    resp = requests.post('%s/oauth2/token' % API_ENDPOINT, data=data, headers=headers, auth=(CLIENT_ID, CLIENT_SECRET))
    resp.raise_for_status()
    # Debug: Print status code and response content
    print("Status Code:", resp.status_code)
    print("Response Content:", resp.content)
    return resp.json()['access_token']


def get_user_guild(token: str):
    resp = requests.get("https://discord.com/api/v10/users/@me/guilds", headers={'Authorization': f"Bearer {token}"})
    resp.raise_for_status
    return resp.json()


def get_bot_guilds():
    token = BOT_TOKEN
    resp = requests.get("https://discord.com/api/v10/users/@me/guilds", headers={'Authorization': f"Bot {token}"})
    resp.raise_for_status
    return resp.json()

def get_mutual_guild(user_guilds: list, bot_guilds: list):
    return [
        guild for guild in user_guilds
        if guild['id'] in map(lambda i: i['id'], bot_guilds) and (int(guild['permissions']) & 0x20) == 0x20
    ]


def get_guild_data(guild_id: int):
    token = BOT_TOKEN
    resp = requests.get(f"https://discord.com/api/v10/guilds/{guild_id}", headers={'Authorization': f"Bot {token}"})

    try:
        resp.raise_for_status
        return resp.json()
    except requests.exceptions.HTTPError:
        return None

    