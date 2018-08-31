import argparse

from ..mood import get_mood, AVAILABLE_MOODS


def main():
    parser = argparse.ArgumentParser(
        description='This gives use an image of geralt in a specified mood in binary.'
    )
    parser.add_argument(
        'mood',
        type=str,
        help="Available moods: {}".format(list(AVAILABLE_MOODS.keys()))
    )
    options = parser.parse_args()

    get_mood(options.mood)
