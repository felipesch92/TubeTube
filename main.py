from pytube import YouTube, Playlist


def baixa_video(yt):
    maior_res = 0
    maior_streams = ''
    for i in yt.streams.filter(file_extension='mp4'):
        x = str(i.resolution).replace('p', '')
        if x.isnumeric() and int(x) > maior_res:
            maior_res = int(x)
            maior_streams = i
    print(f'Baixando o vídeo {maior_streams.title}')
    maior_streams.download('./downloads')


while True:
    op = input('Video ou Playlist? [V/P] ').upper()
    if op not in 'VP':
        print('Apenas V ou P!')
    else:
        break
url = input('URL: ')
if op == 'V':
    yt = YouTube(url)
    baixa_video(yt)
else:
    p = Playlist(url)
    for video in p.videos:
        baixa_video(video)
