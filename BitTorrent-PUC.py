import requests
import bencodepy

# URL do arquivo .torrent que você deseja baixar
torrent_file_url = 'Cole aqui'
# Baixe o arquivo .torrent
response = requests.get(torrent_file_url)

# Decodifique o arquivo .torrent
torrent_data = bencodepy.decode(response.content)

# Obtenha a lista de trackers do arquivo .torrent
trackers = torrent_data[b'announce-list']

# Imprime os trackers disponíveis
print("Trackers disponíveis:")
for tracker_list in trackers:
    for tracker in tracker_list:
        print(tracker)
