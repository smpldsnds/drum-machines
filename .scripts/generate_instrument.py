import json
import os
import sys


def find_wav_files(folder_path):
    wav_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.wav'):
                full_path = os.path.join(root, file)
                wav_files.append(full_path)
    return wav_files

def generate_instrument(folder_path):
    files = find_wav_files(folder_path)
    samples = [os.path.splitext(os.path.relpath(f, folder_path))[0] for f in files]

    # Convert files
    for file in samples:
        file_path = os.path.join(folder_path, file)
        basename = file_path.replace(".wav", "")
        print(f"Converting {basename}.wav to {basename}.ogg and {basename}.m4a")
        # os.system(
        #         f"ffmpeg -i \"{file_path}\" -c:a libopus \"{basename}.ogg\"")
        # os.system(
        #         f"ffmpeg -i \"{file_path}\" -c:a aac \"{basename}.m4a\"")

    # Generate dm.json
    dm = {
        "baseUrl": f"https://smpldsnds.github.io/drum-machines/{folder_path}/",
        "name": folder_path,
        "samples": samples,
        "formats": ["ogg", "m4a"]
    }

    with open(os.path.join(folder_path, 'dm.json'), 'w') as f:
        json.dump(dm, f, indent=2)


if __name__ == "__main__":
    folder_path = sys.argv[1]
    generate_instrument(folder_path)
