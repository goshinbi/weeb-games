#!/usr/bin/Python3


'''This is a docstring'''


from threading import Thread
from collections import OrderedDict
import database
import gen_page
import time
import hug


api = hug.API(__name__)


#   LEADER BOARD
@hug.get('/', output=hug.output_format.html)
def leader_board():
    topx = database.get_top(50)
    return gen_page.gen_leaderboad_page(topx)


#---LEADER BOARD


#   USER PAGE
@hug.get('/user/{name}', output=hug.output_format.html)
def user_page(name):
    name = name.lower()
    uid, upoints, strings = database.get_user(name)
    return gen_page.gen_user_page(name, upoints, strings)
#---USER PAGE


#   ADD String
@hug.get('/API/add_string')
def get_here(points, name, text):
    p = int(points)
    if p > 9:
        p = 10
    if p < -9:
        p = -10
    return database.add_string(name, text, p, time.time())
#---ADD STRING
