#!/bin/bash
# Maruri finishing pass v1 — raw clip -> graded + bed-ducked + captioned final
# Usage: ./finishing_pass.sh <raw.mp4> <bed.mp3> <captions.ass> <output.mp4>
#
# Drive storage (confirmed live 2026-07-16, Google Drive Desktop, Stream files mode):
#   Raw:       "G:/My Drive/Future Finds/04 Content Production/Raw Videos/<clip>_raw.mp4"
#   Final:     "G:/My Drive/Future Finds/04 Content Production/Published Videos/<clip>_graded.mp4"
#   Music:     "G:/My Drive/Future Finds/04 Content Production/Music Beds/"
# Writing to these paths is a normal file write — Drive Desktop syncs automatically,
# zero LLM/context cost. Do NOT route media through the Drive MCP tool's base64
# upload — confirmed unworkable for files over ~200KB (a 121KB audio test alone cost
# ~150K tokens). Small text/docs/xlsx (<50KB or so) are fine through the MCP tool.
set -e
FFMPEG="/c/Users/tensi/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe/ffmpeg-8.1.2-full_build/bin/ffmpeg.exe"

RAW="$1"
BED="$2"
ASS="$3"
OUT="$4"

"$FFMPEG" -i "$RAW" -i "$BED" -filter_complex "
[0:v]scale=w=trunc(iw*0.55/2)*2:h=trunc(ih*0.55/2)*2:flags=bicubic,scale=w=trunc(iw/0.55/2)*2:h=trunc(ih/0.55/2)*2:flags=bicubic,eq=contrast=0.88:saturation=0.78:brightness=0.02:gamma=0.95,colorbalance=rs=-0.06:gs=0.0:bs=0.09:rm=-0.04:gm=0.0:bm=0.06,noise=alls=18:allf=t+u,gblur=sigma=0.5,vignette=PI/6,ass=${ASS}[vout];
[0:a]highpass=f=120,lowpass=f=8500,acompressor=threshold=-18dB:ratio=3:attack=5:release=50[voice];
[1:a]volume=-22dB[bedvol];
[bedvol][voice]sidechaincompress=threshold=0.02:ratio=10:attack=5:release=400:makeup=1[bedduck];
[voice][bedduck]amix=inputs=2:duration=first:dropout_transition=0,alimiter=limit=0.9[aout]
" -map "[vout]" -map "[aout]" -c:v libx264 -crf 26 -preset medium -c:a aac -b:a 128k -movflags +faststart "$OUT" -y
