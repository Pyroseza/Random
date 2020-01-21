#!/usr/bin/env python3
"""Speakout
# TODO 
Make a Version with Huge Ascii Letters and also with colors 
"""
import os
from time import sleep
#import speech # uses python2 EW!
from art import  *

def speak_out():
  while True:
    #user_input = input("Enter something you want spoken\n>")
    user_input = input("Enter something you want printed out funky:\n>")
    #speech.say(user_input)
    sleep(.200)
    print("\n" + " ")
    #print(user_input)
    tprint(user_input)
    sleep(2)
    #clear()
    aprint("rand")

speak_out()
