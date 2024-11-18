from TinderApi import Tinder
import os
from dotenv import load_dotenv

load_dotenv()

tinder = Tinder(debug=True)
tinder.login(
    os.getenv('PHONE_NUMBER'),
    os.getenv('EMAIL'),
    store_auth_token=True
)