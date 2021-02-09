import os


class FileMonitor:
    CHECK_TIMESLOT = 1
    FILE_THOTTLE = 10

    def __init__(self):
        pass

    def is_files_delay(self, path):
        files_path = path
        files = [f for f in os.listdir(files_path) if os.path.isfile(os.path.join(files_path, f))
                 and os.path.splitext(os.path.join(files_path, f))[1] == '.pdf']
        return len(files) > self.FILE_THOTTLE