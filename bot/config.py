from decouple import config
from dotenv import load_dotenv

load_dotenv()


try:
    BOT_TOKEN = config("BOT_TOKEN")
    OWNER = config("OWNER", default="862271564 2147161622")
    STORAGE_CHANNEL = config("STORAGE_CHANNEL", cast=int)
    MAIN_CHANNEL = config("MAIN_CHANNEL", cast=int)

    # for speed time stuffs

    SPEED_START_TIME = 7
    SPEED_STOP_TIME = 1
    SPEED = 15

    # for railway

    REDISPASSWORD = config("REDISPASSWORD", default=None)
    REDISHOST = config("REDISHOST", default=None)
    REDISPORT = config("REDISPORT", default=None)
    REDISUSER = config("REDISUSER", default=None)
except Exception as ex:
    print(ex)
    exit(0)
