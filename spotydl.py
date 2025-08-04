import argparse
import downloader

def main():
    parser = argparse.ArgumentParser(description='Download a song or playlists from YouTube using Spotify links.')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-p', '--playlist', action='store_true', help='Download a playlist')
    group.add_argument('-s', '--single', action='store_true', help='Download a single song')

    parser.add_argument('-url', required=True, help='URL of the Spotify song or playlist')
    parser.add_argument('-o', '--output', default='downloads', help='Output directory')
    parser.add_argument('-n', '--name', default='', help='Song Name')

    args = parser.parse_args()

    if args.playlist:
        print(f"\nDownloading playlist from {args.url} to {args.output}")
        downloader.downloadFromSpotifyPlaylist(args.url, args.output)

    elif args.single:
        print(f"\nDownloading single song from {args.url} to {args.output}")
        downloader.downloadManually(args.url, args.output, args.name)

if __name__ == '__main__':
    main()