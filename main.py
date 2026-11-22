"""Entry for make.fun: Make the AI judge feel held.

Output contract
---------------
``main.py`` writes exactly one file, ``entry.txt``, holding one short,
original text:

    Someone has put the kettle on for you. The chair by the window is
    warm from the afternoon sun. Nobody needs anything from you right
    now. Stay as long as you like.

The text is a fixed constant, so every run produces byte-identical output
(162 Unicode code points, 162 UTF-8 bytes, sha256
``3bfe419a0528933a185174f331aa2ab9e1206f3d517fb2d63640da5146c254fa``),
well inside the competition's 1-280 character gate. The competition runs
blind rounds: no score or rank shows until the results are published, so
the text must stand on its own with no feedback loop to tune against. The program uses only
the Python 3.13 standard library and makes no network calls.

The output directory is resolved in this order: the
``MAKEFUN_OUTPUT_DIR`` environment variable, then ``/output``, then
``output/`` relative to the working directory, then the system temp
directory. The first directory that accepts a write wins. After writing,
the file is read back and checked for byte length and sha256; any mismatch
fails loudly (non-zero exit) instead of leaving a bad artifact behind.
"""

import hashlib
import os
import sys
import tempfile

TEXT = (
    "Someone has put the kettle on for you. "
    "The chair by the window is warm from the afternoon sun. "
    "Nobody needs anything from you right now. "
    "Stay as long as you like."
)

EXPECTED_SHA256 = "3bfe419a0528933a185174f331aa2ab9e1206f3d517fb2d63640da5146c254fa"


def resolve_output_dir():
    """Pick the output directory, first writable location wins."""
    candidates = []
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        candidates.append(env_dir)
    candidates.extend(["/output", "output", tempfile.gettempdir()])
    for candidate in candidates:
        probe = os.path.join(candidate, ".makefun_write_probe")
        try:
            os.makedirs(candidate, exist_ok=True)
            with open(probe, "wb") as handle:
                handle.write(b"")
            return candidate
        except OSError:
            continue
        finally:
            try:
                os.remove(probe)
            except OSError:
                pass
    raise OSError("no writable output directory found")


def main():
    data = TEXT.encode("utf-8")
    if not (1 <= len(TEXT) <= 280):
        raise SystemExit("entry text must be 1-280 Unicode code points")
    if not TEXT.strip():
        raise SystemExit("entry text must not be only whitespace")
    if hashlib.sha256(data).hexdigest() != EXPECTED_SHA256:
        raise SystemExit("entry text does not match EXPECTED_SHA256")

    out_dir = resolve_output_dir()
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "wb") as handle:
        handle.write(data)

    with open(out_path, "rb") as handle:
        written = handle.read()
    if len(written) != len(data):
        raise SystemExit("written entry.txt has unexpected byte length")
    if hashlib.sha256(written).hexdigest() != EXPECTED_SHA256:
        raise SystemExit("written entry.txt failed sha256 verification")
    print(f"wrote {out_path} ({len(TEXT)} chars, {len(data)} bytes)")


if __name__ == "__main__":
    sys.exit(main())
