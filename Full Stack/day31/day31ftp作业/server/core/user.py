import os
from conf import settings


class User(object):
    def __init__(self, name):
        self.name = name
        self.home = os.path.join(settings.home_path, name)
        self.cur_path = self.home
        self.disk_space = settings.space
        self.filesize = 0
        
    