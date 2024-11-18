### Goals

- Automatic swiping without being shadow banned.
    - Random and reasonable length pauses between swipes.
    - Randomly swipe left/right on users (Approx 50% or so).
- Swiping regularly when I have available likes.
    - Swiping occurring once per day at different hours. Sometimes skipping 1-3 days to avoid bot detection.
- Email or text me when I get a new match.

### Stretch Goals

- Automatic conversation (might be expensive if I use the GPT api haha).
    - Email or text me when a date is set up.
- Machine learning to help increase odds of swiping right on my type 🥺.

### Process

I knew I didn't want to use a browser automation tool like selenium if I could avoid it because Tinder is known to have a lot of pop-ups (eg. showing offers for premium) and other distractions which are very difficult to deal with. These are avoided entirely if an API is used. 

Looking for a working API was quite difficult because most of them are outdated, and Tinder keeps changing the API (eg. Using `protobuff` insteam of `json`). 

After finding a working API, it should be smooth sailing.