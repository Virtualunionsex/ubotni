import os
from os import getenv
from dotenv import load_dotenv
from distutils.util import strtobool


load_dotenv(".env")


API_ID = int(getenv("API_ID", "28094601")) #optional
API_HASH = getenv("API_HASH", "70756c6b7f3bf1d996ab7d157b270970") #optional
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1715348447").split()))
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
BOT_TOKEN = getenv("BOT_TOKEN", "6050133470:AAEj0R_Y0EUfsLLb8gYClqpaf5oYuZsIhyg")
BOT_WORKERS = int(getenv("BOT_WORKERS", "1"))
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
SESSION1 = getenv("SESSION1", "AQAhIHQAeQnv4G5m2oaXpj9ghuTDVuJAHRWLvc7f000skvbCAT4ZuqPzqavMCh3FIRq8zRBbBYcLRGWPk2EFbztcVdQf6eH5uTrsOI0R7vmmPl6G-hMo3faSxZ1gHdm0joeMnXBaG5zshNdueM-9waD9v1XxGgLM4CkO3-LIMCHL2O9AtlZc3PdZgYKyBqSfg7bBJqes-FMkBk0TpnLWPC5YbK9JEy2CvqsM4dWaqTn2I4muMdL4Hcikw4bH8FQu_utbef3oX0MBRhXTn3wEAxAWF2Q_03b9Shr2CRVovQ9X2PTPb2hH3yRCVUAlxvoBZFW7hj5CLJtSirmsu69LO3Bd3dM6LwAAAAFqbvYkAA")
SESSION2 = getenv("SESSION2", "AQAhIHQAUoxCnToCQzSyDBRVIsACPVZ966I4hE9Ul0vb91pUOhrlW69Aq0iAuvalkPgft307VQzN6RkqEP5yhT2kBEFlWn8zckpaVyL1z4MjHXH0mlDUzBAUKCDLJw9dvlgA20CA1hL-vpaVJtR35qeAEgYboHTZP92MvDOeiF-aTLOdH5rIlVeGCe7E4QMJl6KNxDVNtcL9avhCnFfEA5lLomOcx38mhijk5aViDD7t1HJ2p6xf-GlsqE4N6WxNn7evg5YQiQw_HojhVderoaO2qYLggH4zdZFNf6vt0JnVnheSk9zt9LAvSOB5kMe1_f_9psPsHfhoNxQTfcs-gwqZDbqeigAAAAFbDiKQAA")
SESSION3 = getenv("SESSION3", "AQAhIHQAhuPqb4PMWGXi94eHFnMbr7xPpajrYkVftgNZxY6VFQt0cAgtdC6LK555RfxsdshK-lQgBBgZATogxGTAEdzZt2IEkmIJTY5HwFEokWRvV0fCFzHbiWOa1kWYlhuNljiA8V8eLPAqTUUxEtwtub3ddadsQOUgY9yJ7vc-1gvGtamKijCWfbumqIuQHWYxj8vqj4QvMSizQi-uWvIfHOE67EafuwBy7pSyPUTRVBmdifB9m_fhvheNOXsALwr1ZaA6rLIxqiGqBaMw0lsXdRMMh-4t9erRtwX4lC-dLRtVpgR2d-dkUqqvxKucqHb38eOQEBVx3a2KxrMzcCyQvsLiVwAAAAFyZ2h-AA")
SESSION4 = getenv("SESSION4", "AQAhIHQAB-b_uVMkyQ_wLuJkb0uOJv7bd4nWu99DfOQh_RkIoZgQjRurXcfebaP5dmBZQ2NP6k9bdqXrATrYyfzTuyWYFTb-lp_rVDND1bzyDaVO2x4677tzv3WK6h3ZSJIcr4oA8IMECYUEJvkkQMaMX6luCtQLhQ-xCNfjj3v4rtZ1T2t9u0kceIS3wD8CyvDKlbV4FQm4mJojsoSxbbpF6ucoi-7DIQmeppYevbdfpG8GpdBGkX9jKxByG_jwNFOfWx7UPiE80H6LbW96DRhiK1pHdFoZMZBe9URO0a4TS6fa4J3gdMeuMPEE4tbKzBnocdN990mnV6soo8b5FH1DnHkEHQAAAAFPwsqUAA")
SESSION5 = getenv("SESSION5", "BQAhIHQAF6xxmf7ss5Ulc12JN0XJZIHHAqp9VzirlenPUuABGtKKiA1K4QDBBhef_gU9L3kLhAPwKw4OF5jPFz8Xd_5W-m_I4W10JYYZfFDNAlNhtbIupvci7OMLb0CGVIyc21UamlSzUR0h3ej3SV2CGtrZgYkLdcY7eBP8wDDc4-9mkNXfMjk9FMWPJFRdX2dN1j1V0p01zErgCTuulQPlyR2VY8y-Jm6dZKgNlZwbGhv-Uda63uE6o75d6LJlrd0XSG3xkZ4tnDIEtXE4iM5X1I4iWTJ55A7tmjnsAx3VPFeZ0FuCc6MnaSLYe7JfUg4kbvK_GUzj_6IlxN2fxQXCv4JOpQAAAABMgA6fAA")
SESSION6 = getenv("SESSION6", "AQAhIHQAlhnRzdFX58RA41zBD4RQUP5KLqhcVTucNZIwCxSbvmMsqczXzDHHMebFjM_uCIQYfiVR-Zm7UYTmsxUR-yVrN_Q7eOLCwRWwxl9sDoS8TnjRT2FjdNkMzrsvbvLb8doLXSjTqhts14mH1scU2ORipcAt5H-4tJ9aFZGk6G2s2LSTYnas7SPMELXT8K5zvbUrOAjETsdYmPte2hIxKVux-E1FEiunenV46Ap-1xAJZ6XMh2aDyt3uRJffX1vtwR3Cem4D7yUFkibzFmRVWyN0kYNEZASfn8OkO4qhQnE3rlYyG9zVqJrpOIRLevUDB6QJZ0c09GfVHYlqhDx2_pr9DAAAAAF2jq4MAA")
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
