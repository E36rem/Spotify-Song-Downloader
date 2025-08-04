# Spotify Song Downloader

A personal tool for downloading songs from Spotify.

> ⚠️ This project is for **personal use only** and not intended for distribution.

## Features

- Download Spotify songs to local files
- Simple command-line interface

## Requirements

- `Python 3.x`
- `spotipy`
- `ytmusicapi`
- `yt_dlp`

## Setup

You technically don’t have to create a `cookies.txt` file, but age-restricted songs won't download without it.

To generate a `cookies.txt` file, I used this browser extension:  
[Get cookies.txt locally](https://chromewebstore.google.com/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc)

## Usage

**Spotydl** has two main functions right now: downloading a **playlist** or a **single track (YouTube only)**.

### ▶️ Playlist Mode

```bash
python spotydl.py -p -url "playlist_url" -o "output_location"
```

### 🎵 Single Track Mode

```bash
python spotydl.py -s -url "yt_track_url" -o "output_location" -n "track_name"
```
