import os
import time

main_songs_folder = r"C:\Users\user\AppData\Local\osu!\Songs"

# Preload all .osu files
osu_files = [
    os.path.join(root, file)
    for root, _, files in os.walk(main_songs_folder)
    for file in files if file.endswith(".osu")
]

# Store initial access times
osu_times = {path: os.stat(path).st_atime for path in osu_files}

print("Monitoring all .osu files...")

try:
    while True:
        time.sleep(0.1)  # faster polling
        for path in osu_files:
            try:
                atime = os.stat(path).st_atime
                if atime != osu_times[path]:
                    print(f"started game: {os.path.basename(path)}")
                    osu_times[path] = atime
            except FileNotFoundError:
                pass
except KeyboardInterrupt:
    print("Stopped monitoring.")
