import re

# Function to parse Carnatic-ABC lines and convert to ABC notation
def convert_carnatic_abc_to_abc(input_text):
    # Define mappings for Carnatic-ABC to ABC in C Major / Shankarabharanam
    carnatic_to_abc = {
        'S': 'C',    # Sa
        'R': 'D',    # Ri
        'G': 'E',    # Ga
        'M': 'F',    # Ma
        'P': 'G',    # Pa
        'D': 'A',    # Dha
        'N': 'B',    # Ni
        's': 'c',    # sa
        'r': 'd',    # ri
        'g': 'e',    # ga
        'm': 'f',    # ma
        'p': 'g',    # pa
        'd': 'a',    # dha
        'n': 'b',    # ni
    }    
    output_lines = []
    for line in input_text.splitlines():
        if re.match(r"^\s*$", line) or re.match(r"^[A-Z]{1,2}:", line):  # empty line or metadata line
            output_lines.append(line)
        else: # notes line
            converted_line = []
            for token in line.split():
                # Replace each character if it's a note, otherwise keep it as is
                converted_token = ''.join(carnatic_to_abc.get(char, char) for char in token)
                converted_line.append(converted_token)
            output_lines.append(" ".join(converted_line))
    return "\n".join(output_lines)


def convert_carnatic_abc_to_abc_with_solfege(input_text):
    # Define explicit mappings for Carnatic-ABC to ABC and solfege
    carnatic_to_abc = {
        'S': 'C', 'R': 'D', 'G': 'E', 'M': 'F',
        'P': 'G', 'D': 'A', 'N': 'B',
        's': 'c', 'r': 'd', 'g': 'e', 'm': 'f',
        'p': 'g', 'd': 'a', 'n': 'b',
    }
    
    carnatic_to_solfege = {
        'S': 'sa', 'R': 'ri', 'G': 'ga', 'M': 'ma',
        'P': 'pa', 'D': 'da', 'N': 'ni',
        's': 'sa', 'r': 'ri', 'g': 'ga', 'm': 'ma',
        'p': 'pa', 'd': 'da', 'n': 'ni',
    }
    
    output_lines = []
    solfege_lines = []
    previous_solfege = ""
    
    for line in input_text.splitlines():
        if not line.strip() or re.match(r"^[A-Z]{1,2}:", line):  # Empty or metadata line
            output_lines.append(line)
        else:  # Notes line
            converted_line = []
            solfege_line = []
            
            for token in line.split():
                converted_token = ''.join(carnatic_to_abc.get(char, char) for char in token)
                solfege_tokens = ' '.join([carnatic_to_solfege[char] for char in token if char in carnatic_to_solfege])
                
                if '-' in token:  # Handle tied notes
                    solfege_tokens = previous_solfege if previous_solfege else solfege_tokens
                else:
                    previous_solfege = solfege_tokens
                
                converted_line.append(converted_token)
                solfege_line.append(solfege_tokens)
            
            output_lines.append(" ".join(converted_line))
            output_lines.append(f"w: {' '.join(solfege_line)}")
    
    return "\n".join(output_lines)


# Example Carnatic-ABC input (as provided)
carnatic_abc_input = """
X:1
T:Shakti sahita ganapatim
M:10/8
L:1/8
K:C

s N s2 | D N | s N D P | 
M G M P | D P | M G R S
S S P2 | M G | M R G2 | 
S S s2 | N s | D N2 s |
r2 s N | D N | s N D P |
s4- | -s2 | s N D P |
M G M P- | -P2 | M G R S | 
r r N s | s D | N N P D |
D M P P | G M | M R G2 |
S R G M | P2 | D N s2 |
r r s N | D P | M G R S |
r r s N | D P | M G R S |
"""

abc_expected_output="""
X:1
T:Shakti sahita ganapatim
M:10/8
L:1/8
K:C

c B c2 | A B | c B A G |
w: sa ni sa da ni sa ni da pa 
F E F G | A G | F E D C
w: ma ga ma pa da pa ma ga ri sa
C C G2 | F E | F D E2 |
w: sa sa pa  ma ga  ma ri ga 
C C c2 | B c | A B2 c |
w: sa sa sa  ni sa  da ni sa 
d2 c B | A B | c B A G |
w: ri sa ni  da ni  sa ni da pa 
c4- | -c2 | c B A G |
w: sa sa ni da pa 
F E F G- | -G2 | F E D C |
w: ma ga ma ma pa ma ga ri sa 
d d B c | c A | B B G A |
w: ri ri ni sa  sa da  ni ni pa da 
A F G G | E F | F D E2 |
w: da ma pa pa  ga ma  ma ri ga 
C D E F | G2 | A B c2 |
w: sa ri ga ma  pa  da ni sa 
d d c B | A G | F E D C |
w: ri ri sa ni  da pa  ma ga ri sa 
d d c B | A G | F E D C |
w: ri ri sa ni  da pa  ma ga ri sa 
"""

# Convert and display the result
abc = convert_carnatic_abc_to_abc(carnatic_abc_input)
abc = convert_carnatic_abc_to_abc_with_solfege(carnatic_abc_input)
print(abc)



# convert abc to music21
import os
from dotenv import load_dotenv
from music21 import environment

# Load environment variables from .env file
load_dotenv()

# Get the MuseScore path from the environment variable
musescore_path = os.getenv('MUSESCORE_PATH')

if musescore_path:
    # Set the path to MuseScore executable in music21 environment
    us = environment.UserSettings()
    us['musicxmlPath'] = musescore_path
    print(f"MuseScore path set to: {musescore_path}")
else:
    print("MuseScore path not found in environment variables.")

from music21 import converter
s = converter.parse(abc)
# Display notes with octave numbers
# for n in s.recurse().notes:
#     print(f"{n.offset} {n.nameWithOctave}")
s.show('midi')
s.show()

# export musicxml
# s.write('musicxml', 'output.xml')
