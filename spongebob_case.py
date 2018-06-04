# Copyright © 2018 Daniel Hildebrandt <daniel.s.hildebrandt@gmail.com>
# This work is free. You can redistribute it and/or modify it under the terms of
# the Do What The Fuck You Want To Public License, Version 2, as published by
# Sam Hocevar. See the LICENSE.txt file for more details.

from random import random
from random import seed
from re import compile
from sys import argv

def to_spongecase(orig, cap_chance = 0.5):
  '''
  Returns a version of the given string that has randomly mixed case,
  in the style of the Mocking Spongebob meme. The capitalization
  pattern is consistent for a given string and capitalization chance.
  
  The capitalization chance is a number in the range [0.0, 1.0]. If a
  value outside these bounds is provided then this function will behave
  as though it had been clamped to the bounds. If no capitalization
  chance is given, it defaults to 50%.
  
  See alse: http://knowyourmeme.com/memes/mocking-spongebob
  
  PARAM orig :: the original string, to be converted into sponge-caps
  PARAM cap_chance :: the percentage chance that any give letter will
  be capitalized 
  
  RETURNS :: the spongecased version of the original string
  '''
  
  orig = str(orig)
  if len(orig) <= 1:
    return (orig.upper() if (random() < cap_chance) else orig.lower())
  else:
    seed(orig)
    
    spongecase = []
    for ch in orig:
      case_choice = random() < cap_chance
      spongecase.append(ch.upper() if (case_choice) else ch.lower())
    
    return ''.join(spongecase)

if __name__ == '__main__' and len(argv) > 1:
  if len(argv) >= 3:
    cap_chance_pattern = compile('^--cap-chance=0*(?:[0-9][0-9]?|100)(?:\\.\\d+)?%$')
    lower_chance_pattern = compile('^--lower-chance=0*(?:[0-9][0-9]?|100)(?:\\.\\d+)?%$')
    if cap_chance_pattern.match(argv[1]):
      all_text = ' '.join(argv[2:])
      cap_chance = float(argv[1][argv[1].index('=') + 1 : argv[1].index('%')]) / 100.0
      print(to_spongecase(all_text, cap_chance))
    elif lower_chance_pattern.match(argv[1]):
      all_text = ' '.join(argv[2:])
      cap_chance = 1.0 - (float(argv[1][argv[1].index('=') + 1 : argv[1].index('%')]) / 100.0)
      print(to_spongecase(all_text, cap_chance))
    else:
      all_text = ' '.join(argv[1:])
      print(to_spongecase(all_text))
  else:
    all_text = ' '.join(argv[1:])
    print(to_spongecase(all_text))
