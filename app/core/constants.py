from decouple import config

MONGO_URI = config("MONGO_URI")

SERVER_ERROR = "Internal Server Error"

OK = 200
