from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
ROBOFLOW_API_KEY = os.getenv('ROBOFLOW_API_KEY')