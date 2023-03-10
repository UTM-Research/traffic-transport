import gzip
import json
from tqdm import tqdm
from twarc import Twarc
from pathlib import Path
twarc = Twarc()
data_dirs = []
def main():
    for data_dir in data_dirs:
        for path in Path(data_dir).iterdir():
            if path.name.endswith('.txt'):
                hydrate(path)
def _reader_generator(reader):
    b = reader(1024 * 1024)
    while b:
        yield b
        b = reader(1024 * 1024)
def raw_newline_count(fname):
    f = open(fname, 'rb')
    f_gen = _reader_generator(f.raw.read)
    return sum(buf.count(b'\n') for buf in f_gen)
def hydrate(id_file):
    print('hydrating {}'.format(id_file))

    gzip_path = id_file.with_suffix('.jsonl.gz')
    if gzip_path.is_file():
        print('skipping json file already exists: {}'.format(gzip_path))
        return
    num_ids = raw_newline_count(id_file)
    with gzip.open(gzip_path, 'w') as output:
        with tqdm(total=num_ids) as pbar:
            for tweet in twarc.hydrate(id_file.open()):
                output.write(json.dumps(tweet).encode('utf8') + b"\n")
                pbar.update(1)
if __name__ == "__main__":
    main()