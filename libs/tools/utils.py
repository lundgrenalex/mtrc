import os


def proj_path(project_root, *args):
    '''Получить абсолютный путь к args в проекте'''
    return os.path.realpath(os.path.join(project_root, *args))
