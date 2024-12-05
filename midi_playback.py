import time
import fluidsynth

fs = fluidsynth.Synth()
fs.start(driver='file', midi_driver=None)

sfid = fs.sfload("/usr/share/sounds/sf2/FluidR3_GM.sf2")
fs.program_select(0, sfid, 0, 0)

fs.noteon(0, 60, 30)
fs.noteon(0, 67, 30)
fs.noteon(0, 76, 30)

time.sleep(1.0)

fs.noteoff(0, 60)
fs.noteoff(0, 67)
fs.noteoff(0, 76)

time.sleep(1.0)

fs.delete()


fluidsynth -ni "/usr/share/sounds/sf2/FluidR3_GM.sf2" "example.mid" -F "example.wav" -r 44100


from IPython.display import Audio
# Play audio from a file
Audio('example.wav')




import fluidsynth
import numpy as np
from IPython.display import Audio

settings = fluidsynth.Settings()
settings["audio.driver"] = "file"    # Use the "file" audio driver to avoid hardware dependency
settings["midi.driver"] = "null"     # Set MIDI driver to "null" to prevent ALSA sequencer error

# Initialize the synthesizer with the custom settings
fs = fluidsynth.Synth()
fs.start()

# Load the SoundFont
sfid = fs.sfload("/usr/share/sounds/sf2/FluidR3_GM.sf2")
fs.program_select(0, sfid, 0, 0)

# Load the MIDI file
fs.midi_player_add(midi_file)
total_time = fs.get_midi_total_time()
total_samples = int(total_time * sample_rate)

    # Prepare buffer to hold audio data
    audio_data = np.zeros((total_samples, 2), dtype=np.float32)  # Stereo output

    # Synthesize the MIDI data
    samples_per_block = 1024
    current_sample = 0

    while fs.midi_player_get_status() == pyfluidsynth.FLUID_PLAYER_PLAYING:
        fs.write(samples_per_block, audio_data[current_sample:current_sample+samples_per_block])
        current_sample += samples_per_block

    # Stop the synthesizer
    fs.delete()

    # Trim the audio data to the actual length
    audio_data = audio_data[:current_sample]

    # Normalize audio data to prevent clipping
    max_val = np.max(np.abs(audio_data))
    if max_val > 0:
        audio_data /= max_val

    # Play audio using IPython.display.Audio
    display(Audio(data=audio_data.T, rate=sample_rate))
