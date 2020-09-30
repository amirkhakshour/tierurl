"""Shortner services including url shortening functionality."""
import random
import string


def gen_random_alphanum_string(length=5):
    choices = string.ascii_lowercase + string.digits
    return ''.join([random.choice(choices) for _ in range(length)])
