# Set up musescore
from music21 import *
us = environment.UserSettings()
us['musescoreDirectPNGPath'] = '/usr/bin/mscore'
us['directoryScratch'] = '/tmp'

# Create a Stream
s = converter.parse('tinyNotation: 4/4 C4 D4 E4 F4 G4 A4 B4 c4')
s.insert(0, instrument.Violin())
# s.getInstruments().show('text')
s.show()

s.show('midi')
