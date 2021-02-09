from file_service import FileService

import os

files_path = "c:\\temp"
files = [f for f in os.listdir(files_path) if os.path.isfile(os.path.join(files_path, f))
         and os.path.splitext(os.path.join(files_path, f))[1] == '.pdf']
print(len(files) > 5)
