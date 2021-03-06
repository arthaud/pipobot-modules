#! /usr/bin/python
# -*- coding: utf-8 -*-
from parser import extract, requete
from pipobot.lib.modules import SyncModule, defaultcmd, answercmd


class CmdTv(SyncModule):
    def __init__(self, bot):
        desc = u"""tv
Donne les programmes tv de la soirée
Les chaînes disponibles sont les suivantes :
%s""" % (", ".join(sorted(extract(requete.TNT).keys())))
        SyncModule.__init__(self,
                            bot,
                            desc=desc,
                            name="tv")

    @answercmd("channels")
    def channels(self, sender):
        return u"Les chaînes valides sont les suivantes :\n%s" % (", ".join(sorted(extract(requete.TNT).keys())))

    @defaultcmd
    def answer(self, sender, message):
        args = message.strip()
        if args == "":
            channels = ["tf1", "france 2", "france 3", "canal+", "arte", "m6"]
            res = extract(requete.SOIREE)
            return u"\n".join("%s : %s" % (key, res[key]) for key in channels)
        else:
            res = extract(requete.TNT)
            try:
                return u"%s : %s" % (args, res[args.lower()])
            except KeyError:
                return u"%s n'est pas une chaîne valide... Regardez le help pour plus d'informations" % args
