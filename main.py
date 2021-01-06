from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=yw6QQhTjcoc')
ys = yt.streams.first()
ys.download('./videos')
