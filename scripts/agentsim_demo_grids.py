#!/usr/bin/env python3
"""Build the per-case grid videos for the AgentSim demo.

For every group in _data/agentsim_demo.yml this stacks the group's clips (logged drive
first, then the variants) into one time-synchronized video, burns the short `label` of
each clip into its cell, and writes grid.mp4 plus a poster frame grid.jpg next to the
clips under assets/demo/agentsim/<group>/.

Layout: 3 columns when a group has 5 or more clips (a short last row is centered),
otherwise 2 columns. Cells are 640x352 (the 960x528 clips scaled by 2/3).

Usage, from the repository root:
    python3 scripts/agentsim_demo_grids.py [--ffmpeg /path/to/ffmpeg] [--font /path/to/font.ttf]
                                           [--source /path/to/website_demo] [--group KEY ...]

By default the clips are read from the site's own assets folder; pass --source to read
them from the AgentSim demo package instead (e.g. after new renders arrive), then copy
the new clips into assets/ as well so the legend links keep working.
Requires an ffmpeg with libx264 and the drawtext filter (fontconfig/freetype).
"""
import argparse
import os
import subprocess
import sys
import tempfile

import yaml

CELL_W, CELL_H = 640, 352
DATA_FILE = os.path.join("_data", "agentsim_demo.yml")


def build_group(group, asset_dir, source_dir, ffmpeg, font, workdir):
    clips = group["clips"]
    n = len(clips)
    cols = 3 if n >= 5 else 2
    rows = [list(range(i, min(i + cols, n))) for i in range(0, n, cols)]
    width, height = cols * CELL_W, len(rows) * CELL_H

    cmd = [ffmpeg, "-y", "-v", "error"]
    for clip in clips:
        cmd += ["-i", os.path.join(source_dir, clip["video"])]

    filters = []
    for i, clip in enumerate(clips):
        label_file = os.path.join(workdir, f"{group['key']}_{clip['index']}.txt")
        with open(label_file, "w", encoding="utf-8") as fh:
            fh.write(clip["label"])
        filters.append(
            f"[{i}:v]scale={CELL_W}:{CELL_H},drawtext=fontfile={font}:textfile={label_file}:"
            f"fontsize=22:fontcolor=white:box=1:boxcolor=black@0.55:boxborderw=8:x=10:y=10[c{i}]"
        )
    for r, row in enumerate(rows):
        inputs = "".join(f"[c{i}]" for i in row)
        if len(row) == 1:
            filters.append(f"{inputs}pad={width}:{CELL_H}:{(width - CELL_W) // 2}:0:black[r{r}]")
        elif len(row) < cols:
            pad_x = (width - len(row) * CELL_W) // 2
            filters.append(f"{inputs}hstack=inputs={len(row)},pad={width}:{CELL_H}:{pad_x}:0:black[r{r}]")
        else:
            filters.append(f"{inputs}hstack=inputs={len(row)}[r{r}]")
    if len(rows) > 1:
        filters.append("".join(f"[r{r}]" for r in range(len(rows))) + f"vstack=inputs={len(rows)}[v]")
        out_label = "[v]"
    else:
        out_label = "[r0]"

    video_out = os.path.join(asset_dir, group["grid_video"])
    cmd += [
        "-filter_complex", ";".join(filters), "-map", out_label, "-an", "-r", "30",
        "-c:v", "libx264", "-preset", "medium", "-crf", "23", "-pix_fmt", "yuv420p",
        "-movflags", "+faststart", video_out,
    ]
    subprocess.run(cmd, check=True)
    poster_out = os.path.join(asset_dir, group["grid_poster"])
    subprocess.run([ffmpeg, "-y", "-v", "error", "-ss", "6", "-i", video_out,
                    "-frames:v", "1", "-q:v", "3", poster_out], check=True)
    size_mb = os.path.getsize(video_out) / 1e6
    print(f"{group['key']}: {n} clips, {cols}x{len(rows)} -> {width}x{height}, {size_mb:.1f} MB")
    if (width, height) != (group.get("grid_width"), group.get("grid_height")):
        print(f"  note: update grid_width/grid_height in {DATA_FILE} to {width}x{height}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--ffmpeg", default="ffmpeg")
    parser.add_argument("--font", default="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
    parser.add_argument("--source", default=None, help="folder holding <group>/clips/*.mp4 (default: the site assets)")
    parser.add_argument("--group", action="append", help="only build these group keys")
    args = parser.parse_args()

    with open(DATA_FILE, encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    asset_root = data["asset_root"].lstrip("/")
    with tempfile.TemporaryDirectory() as workdir:
        for group in data["groups"]:
            if args.group and group["key"] not in args.group:
                continue
            asset_dir = os.path.join(asset_root, group["key"])
            source_dir = os.path.join(args.source, group["key"]) if args.source else asset_dir
            build_group(group, asset_dir, source_dir, args.ffmpeg, args.font, workdir)


if __name__ == "__main__":
    main()
