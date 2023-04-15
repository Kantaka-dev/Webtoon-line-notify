import os

def makedirs(directory, file=''):

    if not os.path.exists(directory):
        os.makedirs(directory)

    return os.path.join(directory, file)
