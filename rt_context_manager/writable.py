# writable
from contextlib import contextmanager

@contextmanager
def writable_file(file_path):
    file = open(file_path, mode="w")
    try:
        yield file
    finally:
        file.close()
