# ohno.py
from pathlib import Path
import sys

src_path = Path(sys.argv[1])
dest_path = Path(sys.argv[1] + ".ohno" )

try:
    with src_path.open() as src, dest_path.open(mode="x") as dest:
        for line in src:
            output = line.replace("o", "🚫")
            dest.write(output)
except OSError as error:
    print("A file error occured.", error)
