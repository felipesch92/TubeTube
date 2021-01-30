from pytube import YouTube, Playlist


def baixar(yt):
    print(f'Baixando o vídeo {yt.title}...', end=' ')
    yt.streams.get_highest_resolution().download('./downloads')
    print('Finalizado!')


while True:
    op = input('Vídeo ou Playlist? [V/P] ').upper()[0]
    if op not in 'VP':
        print('Opção inválida')
    else:
        break
url = input('URL: ')

if op == 'V':
    yt = YouTube(url)
    baixar(yt)
elif op == 'P':
    pl = Playlist(url)
    for video in pl.videos:
        baixar(video)
