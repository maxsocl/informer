#!/usr/bin/python
#encoding: utf-8
'''
Created on 21.12.2011

@author: maksim
'''


import pynotify

"""Notify for AON service"""

def view_notify(data):
    n = pynotify.Notification("Входящий звонок", data)
    n.set_hint('x', 200)
    n.set_hint('y', 400)
    pynotify.init("aon")
    n.show()
