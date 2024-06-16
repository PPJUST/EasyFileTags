import os
import pickle

from constant import _FILE_PKL


def create_default_pkl():
    if not os.path.exists(_FILE_PKL):
        tags = []
        with open(_FILE_PKL, 'wb') as f:
            pickle.dump(tags, f)


def read_tags():
    with open(_FILE_PKL, 'rb') as f:
        tags = pickle.load(f)

    return tags


def inset_tag(tag):
    tags = read_tags()
    if tag not in tags:
        tags.append(tag)
        with open(_FILE_PKL, 'wb') as f:
            pickle.dump(tags, f)


def delete_tag(tag):
    tags = read_tags()
    if tag in tags:
        tags.remove(tag)
        with open(_FILE_PKL, 'wb') as f:
            pickle.dump(tags, f)
