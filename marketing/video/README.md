# Owl demo video: polishing

`polish.py` turns a raw screen recording into a clean product demo:
- the screen sits in a rounded frame with a shadow on a navy background
- smooth, eased zooms onto the part that matters (the button, the entries, the VAT result)
- a highlight ring on each click
- waiting parts sped up, with a visible "×N" badge so nobody is misled about real processing time
- an opening title card and a closing card (thinkactionn.com)
- the original voice is kept (muted only during sped-up parts)

`exemple-style.mp4` shows the style on a fake 12-second recording.

## How to send the raw video

Put the file in `marketing/video/raw/` in this repository:
- **GitHub website:** open the repo → `Add file` → `Upload files` (up to 25 MB per file), commit to branch `claude/marketing-skills-setup-u2bsot`.
- **Too big?** Export it as MP4 (H.264), 1080p, 30 fps. A 2-minute screen recording is usually 15–25 MB.

## What happens next
1. Claude extracts frames from the video, finds the key moments (upload, click on analyse, entries appear, VAT ready) and writes `edit.json` (zooms, clicks, speed-ups).
2. `python3 polish.py raw/demo.mp4 edit.json final.mp4`
3. You watch `final.mp4` and ask for changes (a zoom earlier, a different title…).

## Smooth cursor movement
A plain recording only contains pixels, so the cursor's own path can't be redrawn smoothly afterwards; the zooms and click rings give most of the polished feel. For a fully smoothed cursor, record with a tool that saves the cursor separately: **Screen Studio** (Mac) or **FocuSee** (Windows and Mac).

## Recording tips (2 minutes)
- One real client file, from the photo of the invoice to the VAT return ready to check.
- Show the client's sector and VAT regime on screen early: that's Owl's difference.
- Hide client names and ICE numbers, or use a demo file.
- Move the mouse slowly, and pause 1 second before each click.
- Speak in French, short sentences, or record without voice and add captions.
