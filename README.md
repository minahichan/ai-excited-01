# Sky Jelly

An aurora-lit jellyfish drifting over a lantern-lit harbor.

## The image

`entry.png` is the entry: a jellyfish glowing against green and violet
aurora light, above a quiet harbor strung with warm lanterns. The picture
is the work — the code below only delivers it unchanged.

## How to run

```sh
python3 main.py
```

`main.py` copies `entry.png`, byte for byte, to `/output/entry.png`
(creating `/output` if it does not exist) and prints the sha256 of the
file it wrote. The output is deterministic: run it twice and the two
files are identical.

## Files

- `main.py` — the copier script
- `entry.png` — the entry image
- `LICENSE` — MIT

## Notes

The output is a byte-identical copy of `entry.png`, so its sha256 is
stable across runs — the same input always produces the same hash.
