#!/usr/bin/python3

from models.engine import file_storage

storage = file_storage.FileStorage()
file_storage.FileStorage.reload(storage)
