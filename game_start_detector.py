import os
import time

main_songs_folder = r"C:\Users\username\AppData\Local\osu!\Songs"  #replace with actual osu songs folder path

# Preload all .osu files
osu_files = [
    os.path.join(root, file)
    for root, _, files in os.walk(main_songs_folder)
    for file in files if file.endswith(".osu")
]

# Store initial access times
osu_times = {path: os.stat(path).st_atime for path in osu_files}

# Track last triggered time per file
last_triggered = {path: osu_times[path] for path in osu_files}

print("Monitoring all .osu files...")

try:
    while True:
        time.sleep(0.1)  # faster polling
        for path in osu_files:
            try:
                atime = os.stat(path).st_atime
                if atime != osu_times[path]:
                    # Trigger only if we haven't triggered for this atime yet
                    if atime != last_triggered[path]:
                        print(f"started game: {os.path.basename(path)}")
                        last_triggered[path] = atime  # mark as triggered
                    osu_times[path] = atime
            except FileNotFoundError:
                pass
except KeyboardInterrupt:
    print("Stopped monitoring.")
