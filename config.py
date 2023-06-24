import os
from os import getenv
from dotenv import load_dotenv
from distutils.util import strtobool


load_dotenv(".env")


API_ID = int(getenv("API_ID", "28094601")) #optional
API_HASH = getenv("API_HASH", "70756c6b7f3bf1d996ab7d157b270970") #optional
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
DEEP_AI = getenv("DEEP_AI", "d7394561-0528-4714-a1ee-edd7020b48e1")
OWNER_ID = int(getenv("OWNER_ID") or 6080624164)
ADMIN1_ID = list(map(int, getenv("ADMIN1_ID", "6080624164").split()))
ADMIN2_ID = list(map(int, getenv("ADMIN2_ID", "1715348447").split()))
ADMIN3_ID = list(map(int, getenv("ADMIN2_ID", "5633133204").split()))
ADMIN4_ID = list(map(int, getenv("ADMIN2_ID", "5657257558").split()))


ADMIN1_ID.append(6080624164)
ADMIN2_ID.append(1715348447)
ADMIN3_ID.append(5633133204)
ADMIN4_ID.append(5657257558)

MONGO_URL = getenv("MONGO_URL", "mongodb+srv://claypronek:Malik10_@cluster0.xtwc7.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5726387109:AAEGEoDQpDcKGPEUI_n435zOoTa61GOC5DE")
BOT_WORKERS = int(getenv("BOT_WORKERS", "2"))
USER_WORKERS = int(getenv("BOT_WORKERS", "8"))
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER", None)
OPENAI_API = getenv("OPENAI_API", "")
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "-1001566281443").split()}
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
BRANCH = getenv("BRANCH", "amang") #don't change
REPO_URL = getenv("REPO_URL", "https://github.com/virtualunionsex/AmangUbot")
CMD_HNDLR = getenv("CMD_HNDLR", ".")
SUPPORT = int(getenv("SUPPORT", "-1001528080636"))
CHANNEL = int(getenv("CHANNEL", "-1001841693247"))
SESSION1 = getenv("SESSION1", "AQAhIHQAeQnv4G5m2oaXpj9ghuTDVuJAHRWLvc7f000skvbCAT4ZuqPzqavMCh3FIRq8zRBbBYcLRGWPk2EFbztcVdQf6eH5uTrsOI0R7vmmPl6G-hMo3faSxZ1gHdm0joeMnXBaG5zshNdueM-9waD9v1XxGgLM4CkO3-LIMCHL2O9AtlZc3PdZgYKyBqSfg7bBJqes-FMkBk0TpnLWPC5YbK9JEy2CvqsM4dWaqTn2I4muMdL4Hcikw4bH8FQu_utbef3oX0MBRhXTn3wEAxAWF2Q_03b9Shr2CRVovQ9X2PTPb2hH3yRCVUAlxvoBZFW7hj5CLJtSirmsu69LO3Bd3dM6LwAAAAFqbvYkAA")
SESSION2 = getenv("SESSION2", "BQAhIHQAHEs2-J-v3lvsYw0Ljv8jbvOuGhvgf1VT3nVbxAT7aT1RhQfFsedC94qVnMCUfIrWCU7LP_O1pFh52Pi-O8EBBpaZm-0H-EGYgkUZZ-Q45E8VtvJmhecYFckUh3BSf5OoGwuBMP_O8U6oe6BlASbqDrq5FU7BPNjUmtJC7D9K8ZplN76kCewZDsTPvVvT_LfVVbU0y_YfhBiRONDF1BJVzYm-tPl4KdA6AAlPLKKeJNHTuK-urLFbIPhRhQI-8FWAKoQJawCa5s158IRU8_WzYTZUwWoIkymhD7O3qB7_JGMVV7PqcYf4TtHlNq4PMMRqM3uYVGFL2B8XoOz-_ArnygAAAABSa_gkAA")
SESSION3 = getenv("SESSION3", "AQAhIHQArd6dA-FlWA4Cu0dddOYDctI983ZK4mVKPtf3e0UIvvNpXoVkJifHqojzUU2IcxLMEzBKEUQjq0U2xL24AGCypV_s80nWnyW5ikl1_RYtadNhxgvtXBbZLU8-fobzn2q9QhDbV8rva1V0m8GpMp0Qr4hJG5JF2_2dHhgweORKL8P6BCcv2ytqhaB6R1ZtiiwufARKlqT8HqnunhPg_vXC7MoWeWD46gylJdMzXUzIPbliZjq5DX9o7QKV73lFtC-gFWGX1khcRWg1AlaHIa2KejQcEgSUqoS7cmsXNtmHaIj0-jH-WhLxcFVgIBiJ_2MYm-Kj9zkyZyevaYJVLLQm1gAAAAFoxH2IAA")
SESSION4 = getenv("SESSION4", "AQAhIHQArbsUcLnl_t8OUH9lMizUggTVLg-6zjLhFrFPDc_-4jyg14I_KEKxkXJvvbIlLVfYuLywv9ZVzbWCzYpRc31ZRoxH6sno3GR5SFtFcHGSjR0oD8tTyqK104AG3DFqQJ7EKNHnpJLU4mPDPwMA5KntCL8LffkX9p4xs37i4JsxIRr9Dc6sPxIfu8QMf51GjN29v6yzFJbkMsrpIqF9xduv503_f5r4yDjZc3W_0tTmvHYkwhBIIW8R8whl5vQhb6kTDS4Bt6MkNgERTIXnDnCWrQUVTLIGtwtQWpESRpLrUmUR3NHT5152Sa5h6elnCLnHdw-LGicdXUx-pZVMDmRp3AAAAAF2jq4MAA")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
SESSION11 = getenv("SESSION11", "")
SESSION12 = getenv("SESSION12", "")
SESSION13 = getenv("SESSION13", "")
SESSION14 = getenv("SESSION14", "")
SESSION15 = getenv("SESSION15", "")
SESSION16 = getenv("SESSION16", "")
SESSION17 = getenv("SESSION17", "")
SESSION18 = getenv("SESSION18", "")
SESSION19 = getenv("SESSION19", "")
SESSION20 = getenv("SESSION20", "")
SESSION21 = getenv("SESSION21", "")
SESSION22 = getenv("SESSION22", "")
SESSION23 = getenv("SESSION23", "")
SESSION24 = getenv("SESSION24", "")
SESSION25 = getenv("SESSION25", "")
SESSION26 = getenv("SESSION26", "")
SESSION27 = getenv("SESSION27", "")
SESSION28 = getenv("SESSION28", "")
SESSION29 = getenv("SESSION29", "")
SESSION30 = getenv("SESSION30", "")
SESSION31 = getenv("SESSION31", "")
SESSION32 = getenv("SESSION32", "")
SESSION33 = getenv("SESSION33", "")
SESSION34 = getenv("SESSION34", "")
SESSION35 = getenv("SESSION35", "")
