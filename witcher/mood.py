import sys

import requests

AVAILABLE_MOODS = {
    'smiling': 'https://images-cdn.9gag.com/photo/a4br4Xp_700b.jpg',
    'serious': 'https://i.pinimg.com/originals/d6/f2/6d/d6f26de04f2bc692a9e43f676f9e2149.jpg',
    'determined': 'http://images.pushsquare.com/news/2015/05/guide_the_best_character_builds_for_geralt_in_the_witcher_3_on_ps4/attachment/0/original.jpg'
}


def get_mood(mood):
    if mood not in AVAILABLE_MOODS.keys():
        sys.exit("Mood {} is not available".format(mood))

    response = requests.get(AVAILABLE_MOODS[mood])
    sys.stdout.buffer.write(response.content)
    sys.stdout.flush()
