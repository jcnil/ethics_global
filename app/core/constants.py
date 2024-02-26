from decouple import config

AWS_DEFAULT_REGION = config("AWS_DEFAULT_REGION")
AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")

MONGO_URI = config("MONGO_URI")

SERVER_ERROR = "Internal Server Error"

OK = 200
