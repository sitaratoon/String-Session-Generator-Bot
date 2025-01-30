from os import environ

# Telegram Account Api Id And Api Hash
API_ID = int(environ.get("API_ID", "18946488"))
API_HASH = environ.get("API_HASH", "c163d4e28e63196c3806cf3b9b2885de")

# Your Main Bot Token 
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Owner ID For Broadcasting 
OWNER_ID = int(environ.get("OWNER_ID", "6692613520")) # Owner Id or Admin Id

# Give Your Force Subscribe Channel Id Below And Make Bot Admin With Full Right.
F_SUB = environ.get("F_SUB", "-1002355394644")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = environ.get("MONGO_DB_URI", "mongodb+srv://Renamest:Renamest@cluster0.prfhc.mongodb.net/?retryWrites=true&w=majority")

# Port To Run Web Application 
PORT = int(environ.get('PORT', 8080))
