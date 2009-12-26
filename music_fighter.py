import os, sys
from random import randint, choice

import pygame
from pygame.locals import *
from pygame.mixer import Sound

accumulator = 0
instruments = []
BEAT_SPEED = 750


class Instrument:
  def __init__(self, sound_file, position):
    self.position = position
    try:
      self.sound = Sound(sound_file)
    except pygame.error, message:
        raise SystemExit, message
  
  def play(self, beat):
    if(self.position == beat):
      self.sound.play()

class Count:
  beat_index = 0
  beats = ['1', '2', '3', '4']
  color = (255,255,255)
  global instruments
  
  @classmethod
  def beat(self):
      self.beat_index += 1
      self.beat_index %= len(self.beats)
      for instrument in instruments:
        instrument.play(self.beat_index)
  
  @classmethod
  def draw(cls, screen, full):
      screen_rect = screen.get_rect()
      font = pygame.font.Font( None, 440 )
      image = font.render( cls.beats[cls.beat_index], True, cls.color )
      rect = image.get_rect()
      rect.center = screen_rect.center
      screen.blit( image, rect )
  

def Beat(time_change, screen):
  global accumulator
  accumulator += time_change
  avg_delta = BEAT_SPEED

  
  if (accumulator >= avg_delta): # - time_change/2 and accumulator <= avg_delta + time_change/2):
    print accumulator
    accumulator = 0
    Count.beat()
  
  Count.draw(screen, BEAT_SPEED)

def run_game():
  SCREEN_WIDTH, SCREEN_HEIGHT = 400, 400
  BG_COLOR = 0, 0, 0
  INSTRUMENT_FILENAMES = ["sounds/439_TicTacShutUp_prac_snare_2.wav", "sounds/777_vitriolix_808_kick.wav"]
  N_INSTRUMENTS = 4
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
  clock = pygame.time.Clock()
  print pygame.mixer.get_num_channels()
  global instruments
  for i in range(N_INSTRUMENTS):
    instruments.append(Instrument(INSTRUMENT_FILENAMES[1], i))
    if i % 2 == 1:
      instruments.append(Instrument(INSTRUMENT_FILENAMES[0], i))
  
  while True:
    time_passed = clock.tick(60)
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE or event.type == pygame.QUIT:
            exit_game()
      
    screen.fill(BG_COLOR)
    Beat(time_passed, screen)
    pygame.display.flip()


def exit_game():
  sys.exit()


run_game()
