import requests


token =
headers = {'Content-Type': 'application/json',
           'Authorization': f'OAuth {token}'}


def create_folder(path):
    url = f'https://cloud-api.yandex.net/v1/disk/resources?path={path}'
    response = requests.put(url, headers=headers)
    print(response.status_code)
    return response.status_code


if __name__ == '__main__':
    name_album_yandex = input('Введите название альбома для сохранения: ')
    result = create_folder(name_album_yandex)
    if result == 409:
        print('Такой альбом уже существует.')
    elif result != 201:
        print('Ошибка обработки сервера')
    else:
        print(f'Создан альбом "{name_album_yandex}"')
