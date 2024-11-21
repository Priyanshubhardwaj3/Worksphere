import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the environment variables
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
DATABASE_URL = os.getenv('DATABASE_URL')

# Print the values
print("SECRET_KEY:", SECRET_KEY)
print("DEBUG:", DEBUG)
print("DATABASE_URL:", DATABASE_URL)
