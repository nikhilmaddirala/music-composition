# Set up musescore
from music21 import *
us = environment.UserSettings()
us['musescoreDirectPNGPath'] = '/usr/bin/mscore'
us['directoryScratch'] = '/tmp'

# Create a Stream
s = converter.parse('tinyNotation: 4/4 C4 D4 E4 F4 G4 A4 B4 c4')

s.insert(0, instrument.Violin())

# s.getInstruments().show('text')
# # Ensure each note has the instrument set
# for n in s.flat.notes:
#     n.activeSite = None
#     n.instrument = instrument.Violin()

s.show()

s.show('midi')

# Play the stream using midi.realtime.StreamPlayer
sp = midi.realtime.StreamPlayer(s)
sp.play()

def write_midi(stream):
    mf = midi.translate.music21ObjectToMidiFile(stream)
    mf.open(f"{stream}.mid", 'wb')
    mf.write()
    mf.close()


def print_midi_file_info(path):
    midi_file = midi.MidiFile()
    midi_file.open(path, attrib='rb')
    midi_file.read()
    midi_file.close()

    # Print the MIDI file information
    for i, track in enumerate(midi_file.tracks):
        print(f"Track {i}:")
        for event in track.events:
            print(event)


write_midi(s)
print_midi_file_info('/workspaces/music-composition/<music21.stream.Part 0x7a2491d87bc0>.mid')

s.getInstrument()