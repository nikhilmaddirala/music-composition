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
                # Create a pattern that matches any of the Carnatic notes
                converted_token = token
                for carnatic, abc in carnatic_to_abc.items():
                    # Replace the note while preserving surrounding characters
                    converted_token = re.sub(carnatic, abc, converted_token)
                converted_line.append(converted_token)
            output_lines.append(" ".join(converted_line))
    return "\n".join(output_lines)

# Example Carnatic-ABC input (as provided)
carnatic_abc_input = """
X:1
T:Shakti sahita ganapatim
M:6/8
L:1/8
K:C

G2 G G M G | R S R S3 | N,2 S R2 N, | S2 R G2 S |
W: śa-kti sa-hi-ta ga-ṇa-pa-tim śa-ṃka-rā-di sē-vi-taṃ vi

G2 G G M G | R S R S R G | M2 G R G S | P, S N, S3 |
W: ra-kta sa-ka-la mu-ni-va-ra-su-ra rā-ja vi-nu-ta gu-ru-gu-haṃ

R3 N,2 P | S2 G R3 | R G R N,2 P, | S2 G R3 |
W: bha-ktā ḷi pō-ṣa-kam bha-va-su-taṃ vi-nā-ya-kam

P D P M P M | G M G R3 | S R S N, S N, | D, N, D, s3 |
W: bhu-kti mu-kti pra-dam bhū-ṣi-tam gam ra-kta pā-dām-bu-jam bhā-va-yā-mi
"""

# Convert and display the result
abc = convert_carnatic_abc_to_abc(carnatic_abc_input)
print(abc)

# convert abc to music21
from music21 import converter
s = converter.parse(abc)
s.show()