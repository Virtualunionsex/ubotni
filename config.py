import os
from os import getenv
from dotenv import load_dotenv
from distutils.util import strtobool


load_dotenv(".env")


API_ID = int(getenv("API_ID", "26780897")) #optional
API_HASH = getenv("API_HASH", "508a62724964c13ccc250ca21189fe54") #optional
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1715348447").split()))
DEEP_AI = getenv("DEEP_AI", "d7394561-0528-4714-a1ee-edd7020b48e1")
OWNER_ID = int(getenv("OWNER_ID") or 6233321769)
ADMIN1_ID = list(map(int, getenv("ADMIN1_ID", "6080624164").split()))
ADMIN2_ID = list(map(int, getenv("ADMIN2_ID", "1715348447").split()))
ADMIN3_ID = list(map(int, getenv("ADMIN2_ID", "5633133204").split()))
ADMIN4_ID = list(map(int, getenv("ADMIN2_ID", "5657257558").split()))


ADMIN1_ID.append(6080624164)
ADMIN2_ID.append(1715348447)
ADMIN3_ID.append(5633133204)
ADMIN4_ID.append(5657257558)

MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Menfess:Malik10_@cluster0.0q7u10d.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5995049651:AAH6P7YqSOEtoYiTLiPpzsg9aw-8mAaATj8")
BOT_WORKERS = int(getenv("BOT_WORKERS", "2"))
USER_WORKERS = int(getenv("BOT_WORKERS", "8"))
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT", "Malik Anak Ganteng... ututututu")
PM_LOGGER = getenv("PM_LOGGER", None)
OPENAI_API = getenv("OPENAI_API", "")
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "-1001566281443").split()}
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
BRANCH = getenv("BRANCH", "Fairy") #don't change
REPO_URL = getenv("REPO_URL", "https://github.com/Malik22222/Cuan")
CMD_HNDLR = getenv("CMD_HNDLR", ".")
SUPPORT = int(getenv("SUPPORT", "-1001528080636"))
CHANNEL = int(getenv("CHANNEL", "-1001841693247"))
SESSION1 = getenv("SESSION1", "BQAhIHQAXV4yMIUTbJvrtHivi6JXLn4RS8CW0cHIrTIFC1fEcYMGt4PFbf4NEExHh_sUlYu6JDSv7WLqQ6DklsL5FptC3-HspCLoZrbTlgkUg1OunYE14M2xjcbcgowC7RteP_s6WTyg-xuwvR2MNESIIF5mEX0gOWFTVpvK9uBZGjUk0CPv-Gj2bHTpF_wuqG9O-uycc74xkciwj0IV9bhYyM3heqX-KVN4hX8I6G22-7DOEuMDjHcP7dRya-e2hHmgJGV8Va9NDJBq7vc6j_Ks2XuMBpMxO8_GUNeRCUuwkk8n4s2sL47dRJdzmKlkMQdCbvop1chOH8IyHGSjaMb9EbQ_FQAAAABVLA5rAA")
SESSION2 = getenv("SESSION2", "BQAhIHQABZpwbo5iQkempl3xza0rD7uf_Zg2wAHTEHAtct0G61xdQtr0kauMz9nM1qzd6PQxOHSG2tW1yDp-YmBjXFV3z-crtvl9R02JO1ZbCQnSPhb0Jmey5dBeC_ylH2oKodCVH-otYpXUOs6hY9xUvB-AR1nWaZ2hlpFaZ_SpCH3hPoJLfl8XXI9CNF9ceNIVdQ9r5mA0GvUC9CPzLoS22SFG5UhSXXxePwlYWNUCt86T7RhIL5lZwqiOhniK3qvrHZCOk3eVFlL0sT6quswJ7vVWEj_iHhsBuphTZpqAEbvi_DE0Qa2JWQW7jtEH5w-JIoYkXK7J4soFUlZFTNpt4u35BwAAAABSa_gkAA") 
SESSION3 = getenv("SESSION3", "AQAhIHQAvxRTNaRmGPiRXdnoDxYr5qagOAhFW7Thqi8G8aB_lHxCo0IwwXbfwThUIhi0C3QVr29MXPwBjQGzIl2XsG24ZtByRzQUfhtYRYnzGDzjlnhKI4LNArz7492ClxDW_jD7GT9QsawHC53-2gTU6BBTu1d4lz1Sb_CS064Ugb1p5yQi5Vo3yaU7MB9t2bJHHgVeeSK8d85mU3PipOdBVkcsUiVQWnZadOIRlVsOiDHqkZtTK2s6gKx1zgH0BzP6FMpVSAQoH6RjOpLK29Regv-fWuAFNj_xFYwyW43xhwVqVgpAIBBxJ_fpWYWBPEtDN5p3Oc6daQ5jU30x_wtdx4oB9AAAAAFyZ2h-AA")
SESSION4 = getenv("SESSION4", "")
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
