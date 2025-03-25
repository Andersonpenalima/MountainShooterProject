#!/usr/bin/python
# -*- coding: utf-8 -*-
from Codigo.constant import ENTITY_SPEED
from Codigo.entity import Entity


class PlayerShot(Entity):

   def __init__(self, name: str, position: tuple):
       super().__init__(name, position)

   def move(self, ):
       self.rect.centerx += ENTITY_SPEED[self.name]