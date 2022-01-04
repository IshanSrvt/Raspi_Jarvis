import random
from datetime import datetime


#------------ Finding Time --------------
now = datetime.now()
current_time = now.strftime("%H:%M")

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_TIME = (f"Sir, The time is {current_time}")


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response



