from music21 import stream, note, midi

# Create a Stream
s = stream.Stream()

# Define the melody notes and durations
melody_notes = [
    ('G4', 1.0), ('G4', 0.5), ('A4', 1.0), ('G4', 1.0), ('C5', 1.0), ('B4', 2.0),
    ('G4', 1.0), ('G4', 0.5), ('A4', 1.0), ('G4', 1.0), ('D5', 1.0), ('C5', 2.0),
    ('G4', 1.0), ('G4', 1.0), ('G5', 1.0), ('E5', 1.0), ('C5', 1.0), ('B4', 1.0), ('A4', 2.0),
    ('F5', 1.0), ('F5', 0.5), ('E5', 1.0), ('C5', 1.0), ('D5', 1.0), ('C5', 2.0)
]

# Add notes to the stream
for pitch, duration in melody_notes:
    n = note.Note(pitch)
    n.quarterLength = duration
    s.append(n)

s

sp = midi.realtime.StreamPlayer(s)
sp.play()
