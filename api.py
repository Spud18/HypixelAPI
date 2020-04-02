import hypixel

open_key = open('api_key.txt', 'r')
key = str(open_key.read())

API_KEYS = [key]  # run '/api new' on Hypixel to retrieve your api key.
# Make sure your api_keys variable looks like :     API_KEYS = ['your-key-in-quote-marks']
hypixel.setKeys(API_KEYS)

options = ['*', 'rank', 'level', 'karma', 'twitter']


while True:
    userInput = input("\nEnter username/UUID: ")
    player = hypixel.Player(userInput)
    try:
        try:
            NAME = player.getName()
        except KeyError:
            print("Player doesn't exist")
            continue
        UUID = player.getPlayerInfo()['uuid']
        try:
            RANK = player.getRank()['rank']
        except KeyError:
            RANK = "Unknown"
        try:
            WAS_STAFF = player.getRank()['wasStaff']
        except KeyError:
            WAS_STAFF = "Unknown"
        try:
            GUILD_ID = player.getGuildID()
        except KeyError:
            GUILD_ID = "Unknown"

        try:
            FIRST_LOGIN = player.getPlayerInfo()['firstLogin']
        except KeyError:
            FIRST_LOGIN = "Unknown"
        try:
            LAST_LOGIN = player.getPlayerInfo()['lastLogin']
        except KeyError:
            LAST_LOGIN = "Unknown"
        try:
            MC_VERSION = player.getPlayerInfo()['mcVersionRp']
        except KeyError:
            MC_VERSION = "Unknown"
        try:
            SESSION = player.getSession()
        except KeyError:
            SESSION = "Unknown"
        try:
            KARMA = player.getPlayerInfo()['karma']
        except KeyError:
            KARMA = "Unknown"
        try:
            LEVEL = player.getLevel()
        except KeyError:
            LEVEL = "Unknown"
        try:
            NETWORK_LEVEL = player.getPlayerInfo()['networkLevel']
        except KeyError:
            NETWORK_LEVEL = "Unknown"
        try:
            NETWORK_XP = player.getPlayerInfo()['networkExp']
        except KeyError:
            NETWORK_XP = "Unknown"
        try:
            SOCIAL_MEDIAS = player.JSON['socialMedia']['links']
            YOUTUBE = SOCIAL_MEDIAS['YOUTUBE']
            TWITTER = SOCIAL_MEDIAS['TWITTER']
            INSTAGRAM = SOCIAL_MEDIAS['INSTAGRAM']
            DISCORD = SOCIAL_MEDIAS['DISCORD']
        except KeyError:
            YOUTUBE = "Unknown"
            TWITTER = "Unknown"
            INSTAGRAM = "Unknown"
            DISCORD = "Unknown"

        print(f"INFO: \n"
              f"| Name: {NAME}\n"
              f"| UUID: {UUID}\n"
              f"| Rank: {RANK}\n"
              f"| Was_Staff: {WAS_STAFF}\n"
              f"| Guild_ID: {GUILD_ID}\n")

        print(f"LOGIN: \n"
              f"| First_Login: {FIRST_LOGIN}\n"
              f"| Last_Login: {LAST_LOGIN}\n"
              f"| Last_Used_MCVER: {MC_VERSION}\n"
              f"| Session: {SESSION}\n")

        print(f"EXTENDED_INFO: \n"
              f"| Karma: {KARMA}\n"
              f"| Level: {LEVEL}\n"
              f"| Network_Level: {NETWORK_LEVEL}\n"
              f"| Network_XP: {NETWORK_XP}\n")

        print(f"SOCIAL_MEDIAS: ")
        try:
            print(f"| Youtube: {YOUTUBE}")
        except KeyError:
            print(f"| Youtube: NOT_LINKED")
        try:
            print(f"| Twitter: {TWITTER}")
        except KeyError:
            print(f"| Twitter: NOT_LINKED")
        try:
            print(f"| Instagram: {INSTAGRAM}")
        except KeyError:
            print(f"| Instagram: NOT_LINKED")
        try:
            print(f"| Discord: {DISCORD}")
        except KeyError:
            print(f"| Discord: NOT_LINKED")

    except KeyError:
        print("Fatal Error, who knows what happened...")
