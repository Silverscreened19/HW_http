from pprint import pprint
import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload(self, disk_file_path, filename):
        result = self._get_upload_link(disk_file_path=disk_file_path)
        href = result.get('href', '')
        response = requests.put(href, data=open(filename, 'rb'))
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload('/netology/test1306.txt', 'test.txt')
