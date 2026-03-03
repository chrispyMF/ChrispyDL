#!/usr/bin/env python3
import argparse
import subprocess
import sys

def main():
    parser = argparse.ArgumentParser(description='Download a video from YouTube as mp4 or mp3.')
    parser.add_argument('url', help='The URL of the YouTube video to download.')
    parser.add_argument('--format','-f', choices=['mp4', 'mp3'], required=True, default='mp4')

    parser.add_argument('--output', '-o',default='%(title)s.%(ext)s', help='The output filename')

    args = parser.parse_args()

    cmd = [sys.executable, "-m", "yt_dlp", args.url, "-o", args.output]

    if args.format == 'mp4':
        cmd += ['-f', 'bv*+ba/b', '--merge-output-format', 'mp4']

    else:
        cmd += ['-x', '--audio-format', 'mp3', '--audio-quality', '0']

    try:
        subprocess.run(cmd, check=True)
    except FileNotFoundError:
        print("Error: yt-dlp is not installed or not in PATH.", file=sys.stderr)
        print("Install it with: pip install yt-dlp", file=sys.stderr)
        sys.exit(1)
    except subprocess.CalledProcessError:
        sys.exit(2)

if __name__ == '__main__':
    main()
