import sys
import logging
import traceback
from time import perf_counter
from pathlib import Path
import json

def log(level=logging.INFO):
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)]
    )

class T:
    def __init__(self, label): self.label = label
    def __enter__(self): self.start = perf_counter()
    def __exit__(self, *_): print(f"[{self.label}] {perf_counter() - self.start:.6f}s")

def dbg(v, label="dbg"):
    print(f"[{label}] {v}")
    return v

def ctx():
    f = sys._getframe(1)
    print(f"[{f.f_code.co_name}:{f.f_lineno}] {f.f_locals}")

def cli(i=1, default=0):
    try: return int(sys.argv[i])
    except: return default

def clif(i=1, default=0.0):
    try: return float(sys.argv[i])
    except: return default

def read(path):
    p = Path(path)
    if not p.exists(): raise FileNotFoundError(path)
    return p.read_text(encoding='utf-8')

def readjson(path):
    return json.loads(read(path))

def write(path, content):
    Path(path).write_text(content, encoding='utf-8')

def writejson(path, data):
    write(path, json.dumps(data, indent=2))
