import time
from random import randint, choice

import pygame

from pygame.mixer import Sound

accumulator = 0
instruments = []
BEAT_SPEED = 500


class Instrument:
  def __init__(self, sound_file, position):
    self.position = position + 1
    try:
      self.sound = Sound(sound_file)
    except pygame.error, message:
        # print 'Cannot load sound:', wav
        raise SystemExit, message
  
  _counter = 0
  
  def play(self):
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
      instruments[self.beat_index].play()
  
  @classmethod
  def draw(cls, screen, amount, full):
      screen_rect = screen.get_rect()
      font = pygame.font.Font( None, 440 )
      image = font.render( cls.beats[cls.beat_index], True, cls.color )
      rect = image.get_rect()
      rect.center = screen_rect.center
      screen.blit( image, rect )
  

def Beat(time_change, screen):
  global accumulator
  accumulator += time_change
    
  
  if (accumulator > BEAT_SPEED):
    accumulator -= BEAT_SPEED
    Count.beat()
  
  Count.draw(screen, accumulator, BEAT_SPEED)

def run_game():
  # Game parameters
  SCREEN_WIDTH, SCREEN_HEIGHT = 400, 400
  BG_COLOR = 0, 0, 0
  INSTRUMENT_FILENAMES = ["777_vitriolix_808_kick.wav"]
  N_INSTRUMENTS = 4
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
  clock = pygame.time.Clock()
  
  # Create N_CREEPS random creeps.
  global instruments
  for i in range(N_INSTRUMENTS):
    instruments.append(Instrument(choice(INSTRUMENT_FILENAMES), i))
  
  # The main game loop
  #
  while True:
    # Limit frame speed to 50 FPS
    #
    time_passed = clock.tick(10)
      
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()
      
      # Redraw the background
    screen.fill(BG_COLOR)
    Beat(time_passed, screen)
      # Update and redraw all creeps
    for instrument in instruments:
        # instrument.tick(time_passed)
        
        pygame.display.flip()


def exit_game():
  sys.exit()


run_game()
