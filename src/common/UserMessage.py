#!/usr/bin/python
# -*- coding: utf-8 -*-

class UserMessage:
    def __init__(self, text, username):
        self.text = text
        self.username = username

    def __str__(self) -> str:
        return "(text={}, username={})".format(self.text, self.username)
