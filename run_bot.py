from TinderApi import Tinder
import random
import time
import os
from dotenv import load_dotenv

load_dotenv()

tinder = Tinder(debug=True, x_auth_token=os.getenv('AUTH_TOKEN'))

hrs_between_swipes = int(input("How many hours between swipes? "))

while True:
    # Chance to skip today
    if random.random() < 0.1:
        wait_time = hrs_between_swipes * 60 * 60 + random.randint(0, 3600)
        time.sleep(wait_time)

    users_to_swipe = tinder.swipe.get_users()

    for user in users_to_swipe:
        # print(user)
        if random.random() < 0.5:
            # LIKE USER
            liked = tinder.swipe.like_user(user["user_id"]) 
            # print("#### Liked")
            # print(liked) # -> {'status': 200, 'match': False, 'user_id': 'some_user_id', 'likes_left': 100}

            # TODO: different behavior if match is True
        else: 
            # PASS USER
            tinder.swipe.pass_user(user["user_id"]) 
            # print("#### Not liked")
        # Wait between 1 and 10 seconds because we aren't a bot ;)
        time.sleep(max(1, random.random() * 10))

    # Swipe again tommorow!
    wait_time = hrs_between_swipes * 60 * 60 + random.randint(0, 3600)
    time.sleep(wait_time)