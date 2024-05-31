import random
import pygame

from src.config import Config
from src.services.visualization_service import VisualizationService
from src.utils.tools import sine

# make npc eagle fish, roam rand unless drop fish
# each eagle take one every 5s. continue roam once ate, then eat again. once eagle ate 2 fishes, drop poop.
# buy eagle
# add: eagle hatchings take 10s to hatch