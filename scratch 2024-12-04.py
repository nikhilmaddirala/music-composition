import os
import shutil

def copy_files(src_dir, dest_txt_dir, dest_gka_dir):
    if not os.path.exists(dest_txt_dir):
        os.makedirs(dest_txt_dir)
    if not os.path.exists(dest_gka_dir):
        os.makedirs(dest_gka_dir)

    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.txt'):
                print(f"Found {os.path.join(root, file)}")
                shutil.copy(os.path.join(root, file), dest_txt_dir)
                print(f"Copied to {dest_txt_dir}")
            elif file.endswith('.gka'):
                print(f"Found {os.path.join(root, file)}")
                shutil.copy(os.path.join(root, file), dest_gka_dir)
                print(f"Copied to {dest_txt_dir}")

src_directory = "/workspaces/music-composition/Carnatic Tripod"
dest_txt_directory = os.path.join(src_directory, "new", "txt_files")
dest_gka_directory = os.path.join(src_directory, "new", "gka_files")

copy_files(src_directory, dest_txt_directory, dest_gka_directory)



import time
import fluidsynth

fs = fluidsynth.Synth()
fs.start()

sfid = fs.sfload("example.sf2")
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

!pip list | grep fluidsynth