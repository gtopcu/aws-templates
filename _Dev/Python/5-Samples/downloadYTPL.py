import os
from pytube import Playlist

playlist_url = 'https://youtube.com/playlist?list=PLoEh936JkVwjGnRHu1vA9d_A2fjXAdwuu'
p = Playlist(playlist_url)
print(f'Downloading: {p.title}')

directory = p.title
parent_dir = "//Users/hukanege/Downloads/YTPL"
output_dir = os.path.join(parent_dir, directory)
os.mkdir(output_dir)

for video in p.videos:
    print(video.title)
    # st = video.streams.get_highest_resolution()
    st = video.streams.get_by_resolution("720p")
    st.download(output_dir)
    # video.streams.first().download(path)