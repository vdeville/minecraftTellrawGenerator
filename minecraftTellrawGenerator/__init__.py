#!/bin/env python3
import json


class MinecraftTellRawGenerator:
    text = ''
    color = 'white'
    bold = False
    italic = False
    underlined = False
    strikethrough = False
    obfuscated = False

    insertion = None
    click = None
    hover = None

    def __init__(self, **kwargs):
        # Due to strange duplicate behavior of data i put __json attribute here
        self.__json = {}
        for k, v in kwargs.items():
            if hasattr(self, k):
                self.__setattr__(k, v)
        self.__format_mc()

    def __format_mc(self):
        self.__to_add('text', self.text)
        self.__to_add('color', self.color)
        self.__to_add('bold', self.bold)
        self.__to_add('italic', self.italic)
        self.__to_add('underlined', self.underlined)
        self.__to_add('strikethrough', self.strikethrough)
        self.__to_add('obfuscated', self.obfuscated)
        self.__to_add('insertion', self.insertion)

        if self.click is not None:
            self.__to_add('clickEvent', {"action": "run_command", "value": self.click})

        if self.hover is not None:
            if isinstance(self.hover, MinecraftTellRawGenerator):
                self.__to_add('hoverEvent', {"action": "show_text", "value": self.hover.__json})

    def __to_add(self, key, value):
        if value is not False and value is not None:
            self.__json[key] = value

    def get_json(self):
        return json.dumps(self.__json, separators=(',', ':'))

    @staticmethod
    def multiple_tellraw(*tellraws):
        return_list = ','.join(str(tellraw) for tellraw in tellraws)
        # Double quote is add to avoid parent heriarchy of Events
        return '["",' + return_list + ']'

    def __str__(self):
        return self.get_json()
