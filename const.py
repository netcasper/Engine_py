#!/usr/bin/python
# Filename: const.py
# 2016.07.26

import sys

class Const(object):
    class ConstError(TypeError):pass
    def __setattr__(self, key, value):
        if set.__dict__.has_key(key):
            raise self.ConstError, 'Changine const.%s' %key
        else:
            self.__dict__[key] = value
    
    def __getattr__(self, key):
        if self.__dict__.has_key(key):
            return self.key
        else:
            return None
        
sys.modules[__name__] = Const()