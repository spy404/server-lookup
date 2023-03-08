# ------ libs ------- #
import os
import sys
import requests
from colorama import init, Fore
from pystyle import Center

# ------ setup ------ #
init()
os.system("title Server look-up | spy404#1388")
os.system("cls" if os.name == "nt" else "clear")
print(Fore.GREEN + Center.XCenter("""
 ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄   ▄▄▄ ▄▄▄▄▄▄▄ ▄   ▄▄▄ 
█       █       █  █ █  █ █ █   █  ▄    █ █ █   █
█  ▄▄▄▄▄█    ▄  █  █▄█  █ █▄█   █ █ █   █ █▄█   █
█ █▄▄▄▄▄█   █▄█ █       █       █ █ █   █       █
█▄▄▄▄▄  █    ▄▄▄█▄     ▄█▄▄▄    █ █▄█   █▄▄▄    █
 ▄▄▄▄▄█ █   █     █   █     █   █       █   █   █
█▄▄▄▄▄▄▄█▄▄▄█     █▄▄▄█     █▄▄▄█▄▄▄▄▄▄▄█   █▄▄▄█

""") + Fore.RESET)

# ------ vars ------ #
link = input("Invite code: ")
print(Fore.GREEN + "Getting informations...." + Fore.RESET)

os.system("cls" if os.name == "nt" else "clear")

try:
    req = requests.get(f"https://discord.com/api/v9/invites/{link}")
except:
    print(Fore.RED + "[-] Failed!" + Fore.RESET)
    sys.exit()

if req.status_code == 200:
    req_json = req.json()
    invite = f'https://discord.gg/{req_json["code"]}'
    channel_name = req_json["channel"]["name"]
    channel_id = req_json["channel"]["id"]
    expire_at = req_json["expires_at"]

    username = f'{req_json["inviter"]["username"]}#{req_json["inviter"]["discriminator"]}'
    user_id = req_json["inviter"]["id"]

    server_name = req_json["guild"]["name"]
    server_id = req_json["guild"]["id"]
    banner = req_json["guild"]["banner"]
    description = req_json["guild"]["description"]
    vanity = req_json["guild"]["vanity_url_code"]
    verification_level = req_json["guild"]["verification_level"]
    splash = req_json["guild"]["splash"]
    features = req_json["guild"]["features"]
    print(Fore.GREEN + Center.XCenter(f"""
# ------ Invite info ------ #
link: {invite}
Channel name: {channel_name}
Channel id: {channel_id}
Expiration date: {expire_at}

# ------ Inviter info ------ #
Username: {username}
User id: {user_id}

# ------ Server info ------ #
Name: {server_name}
ID: {server_id}
Banner: {banner}
Description: {description}
Vanity: {vanity}
Verifiction level: {verification_level}
Splash: {splash}
Features:
    """) + Fore.RESET)
    for i in features:
        print(Fore.GREEN + Center.XCenter(i) + Fore.RESET)
else:
    print(Fore.RED + "[-] We have an error" + Fore.RESET)
