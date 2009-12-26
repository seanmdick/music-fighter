import os, sys
from random import randint, choice

import pygame

from pygame.mixer import Sound

class Instrument:
  def __init__(self, sound_file, position):
    self.position = position + 1
    try:
      self.sound = Sound(sound_file)
    except pygame.error, message:
        # print 'Cannot load sound:', wav
        raise SystemExit, message
  
  _counter = 0
  
  def tick(self, tick):
    self._counter += tick
    if (self._counter > (10 * self.position)):
      self.sound.play()
      self._counter = 0


def run_game():
  # Game parameters
  SCREEN_WIDTH, SCREEN_HEIGHT = 400, 400
  BG_COLOR = 0, 0, 0
  INSTRUMENT_FILENAMES = ["777_vitriolix_808_kick.wav","5313_NoiseCollector_DynaE2.wav"]
  N_INSTRUMENTS = 2
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
  clock = pygame.time.Clock()
  
  # Create N_CREEPS random creeps.
  instruments = []
  for i in range(N_INSTRUMENTS):
    instruments.append(Instrument(choice(INSTRUMENT_FILENAMES), i))
  
  # The main game loop
  #
  while True:
    # Limit frame speed to 50 FPS
    #
    time_passed = clock.tick(1)
      
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()
      
      # Redraw the background
    screen.fill(BG_COLOR)
      
      # Update and redraw all creeps
    for instrument in instruments:
        instrument.tick(time_passed)
        
        pygame.display.flip()


def exit_game():
  sys.exit()


run_game()
