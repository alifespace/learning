import os, threading
from tqdm import tqdm
from typing import Union
from pathlib import Path

class Boto3UploadProgress:
    def __init__(self, file_path: Union[str, Path]):
        self._filename = str(file_path)
        self._filesize = float(os.path.getsize(self._filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()
        self._pbar = tqdm(
            total=self._filesize,
            unit="B",
            unit_scale=True,
            desc=os.path.basename(self._filename)
        )

    def __call(self, bytes_amount: int):
        with self._lock:
            self._seen_so_far += bytes_amount
            self._pbar.update(bytes_amount)

    def close(self):
        self._pbar.close()
