import os
# file_check.py
filename = "cyber_log.txt"
if os.path.exists(filename):
    print(f"File {filename} exists.")
else:
    print(f"File {filename} does not exist.")