import requests

def folder_photos():
    token = '' # нужно добавить токен
    folder = 'test_folder'
    url_f = 'https://cloud-api.yandex.net/v1/disk/resources'
    params_f = {'path': f'{folder}'}
    resp = requests.put(url_f, headers={'Authorization': token}, params=params_f)
    # return resp.json()
    return resp.status_code

if __name__ == "__main__":
    print(folder_photos())




