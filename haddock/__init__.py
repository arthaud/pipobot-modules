#-*- coding: utf-8 -*-
import random
import os
from pipobot.lib.modules import SyncModule, defaultcmd


class Haddock(SyncModule):
    def __init__(self, bot):
        desc = "Les insultes du capitaine haddock :p."
        SyncModule.__init__(self,
                            bot,
                            desc=desc,
                            name="haddock")
        self.quotes = []
        path = os.path.join(os.path.dirname(__file__), 'bdd.txt')
        with open(path, 'r') as fichier:
            content = fichier.read()
            self.quotes = content.split("\n")

    @defaultcmd
    def answer(self, sender, message):
        insult = random.choice(self.quotes)
        if message == self.bot.name:
            res = "%s: c'est toi qui es un %s" % (sender, insult)
        elif message != '':
            res = "%s: %s" % (message, insult)
        else:
            res = insult
        return res
