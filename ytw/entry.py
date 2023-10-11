import argparse
import ffmpeg
from pytube import YouTube, Playlist
import os


def handle_download(url, od):
    file = YouTube(url).streams.get_audio_only().download()
    p = file.split("\\")
    new_path = f'{od}\\{p[len(p) -1]}'
    os.rename(file, new_path)
    f = ffmpeg.input(new_path)
    f = ffmpeg.output(f, new_path.replace(".mp4", "") + ".wav")
    ffmpeg.run(f)
    os.remove(new_path)



def handle_playlist(url, od):
    playlist = Playlist(url)
    l = playlist.video_urls
    for link in l:
        handle_download(link, od)


def cli_entry_point():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    parser_download = subparsers.add_parser('d', help='donwload and convert from a link')
    parser_download.add_argument('url', help='Url')
    parser_download.add_argument('-od', '--output-dest', help='Where to save the output file')

    parser_playlist = subparsers.add_parser('p', help='download and convert whole playlist')
    parser_playlist.add_argument('url', help='Url')
    parser_playlist.add_argument('-od', '--output-dest', help='Where to save the output file')

    args = parser.parse_args()

    if args.command == 'd':
        handle_download(args.url, args.output_dest)
    elif args.command == 'p':
        handle_playlist(args.url, args.output_dest)
    else:
        parser.print_help()