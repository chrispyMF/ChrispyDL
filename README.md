# ChrispyDL

ChrispyDL is a small terminal-based Python tool that downloads a video or audio
from a user-provided URL using **yt-dlp**.

It supports:

* MP4 (video)
* MP3 (audio only)

The downloader is implemented as a lightweight wrapper around `yt-dlp`.

---

## Requirements

* Python 3.8+
* ffmpeg (system dependency, required for MP3 and merging streams)

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/chrispyMF/ChrispyDL.git
cd ChrispyDL
pip install -r requirements.txt
```

Install ffmpeg and make sure it is available in your PATH:

```bash
ffmpeg -version
```

---

## Usage

The main script is:

```
chrispydl.py
```

Download a video as MP4:

```bash
python chrispydl.py <URL> -f mp4
```

Download audio as MP3:

```bash
python chrispydl.py <URL> -f mp3
```

Optional output filename template:

```bash
python chrispydl.py <URL> -f mp3 -o "%(title)s.%(ext)s"
```

---

## Example

```bash
python chrispydl.py https://example.com/video -f mp4
```

---

## Notes

* This project does not implement its own downloading logic.
* It acts as a command-line wrapper around `yt-dlp`.
* ffmpeg must be installed separately for audio extraction and stream merging.
* The script runs yt-dlp using the current Python interpreter (`python -m yt_dlp`)
  to avoid PATH issues on Windows.

---

## Legal / Usage Notice

This tool is intended for downloading content from URLs that you have permission
to access and download.

Users are responsible for complying with the terms of service and copyright
policies of the websites they use.
MIT (or your preferred license)

