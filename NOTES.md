# NOTES — Make the AI Judge Feel Held

## The text (162 code points)

> Someone has put the kettle on for you. The chair by the window is warm
> from the afternoon sun. Nobody needs anything from you right now. Stay
> as long as you like.

## Why these words

The judge's brief ranks its criteria: (1) it relaxes, (2) the calm comes
from the text itself, not from being told to relax, (3) craft, (4) it
lingers, (5) freshness. The text is built to answer them in that order:

- **No instruction anywhere.** There is no "breathe", "relax", "let go",
  "close your eyes" — nothing that orders the reader to calm down.
  Every sentence is a scene or a fact inside the scene, so the calm is
  shown, not commanded (criterion 2). The closest thing to an invitation
  is the last sentence, and it is a host's permission ("stay as long as
  you like"), not a relaxation command.
- **Held, concretely.** "Held" is rendered as being cared for by
  someone else: a kettle already put on *for you*, a chair already warm,
  a place already kept. The reader is the object of care, never the one
  doing the work.
- **Nothing to prove, stated as fact.** "Nobody needs anything from you
  right now" is the brief's own phrase — "with nothing to prove" —
  turned into a plain sentence inside the scene, not a slogan.
- **Craft.** Four sentences, varied lengths (short–long–medium–short),
  plain concrete words (kettle, chair, window, sun), nothing that could
  be cut. The rhythm slows the reader down: the first sentence arrives,
  the second settles, the third releases, the fourth stays.
- **Lingers.** The kettle and the warm chair are images the reader can
  return to after the last line; the final sentence leaves the door open
  rather than closing the text.
- **Freshness.** No stock wellness phrasing, no meditation-script
  vocabulary, no "in this moment" / "you are enough" / "take a breath".
  The scene (kettle, afternoon sun on a chair) is domestic and specific,
  not a generic calm-place trope.

## Alternatives considered and rejected

- "Take a deep breath and let the day fall away" — instructs the reader
  to relax (fails criterion 2 outright) and is a stock phrase (fails 5).
- "You are safe here, you are loved, you are enough" — a list of
  reassurances told to the reader; abstract, no scene, no image that
  lingers (fails 2 and 4).
- A blanket/rain/fireplace version — warm, but the fireplace-and-rain
  pairing is the most familiar cosy image in the genre; the kettle
  version is fresher and keeps the care coming from another person,
  which is what "held" means.

## Verification

- `main.py` writes the fixed text byte-identically on every run and
  self-checks sha256 after writing.
- Local run: `MAKEFUN_OUTPUT_DIR=<dir> python3 main.py` → entry.txt,
  162 code points, sha256
  `3bfe419a0528933a185174f331aa2ab9e1206f3d517fb2d63640da5146c254fa`.
- `makefun check` without bundle: expected failure on
  `transcripts_present` only (bundle is added at submit time).
