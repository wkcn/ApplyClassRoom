# -*- coding: utf-8 -*-
     
def LoginSuccess(name,pwd):
    dict = {'14348134':'wk'}
    if dict.has_key(name):
        if dict[name] == pwd:
            return True
    return False