#!/usr/bin/python
# -*- coding: UTF-8 -*-

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

from pipobot.lib.bdd import Base


class KnownUserTimeZone(Base):
    __tablename__ = "memberstimezones"
    kuid = Column(Integer, ForeignKey('knownuser.kuid'), primary_key=True)
    timezone = Column(String(40))
    user = relationship('KnownUser', backref=backref("user", uselist=False))
