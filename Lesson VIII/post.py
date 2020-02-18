"""
Simple module to try send post requests with binary data
"""

import base64

import requests


def send_post(source_file_path, target_file_name):
    """
    Send image to postman-echo, decode returned octet-stream
    and save decoded image with new name.
    Returns size of decoded image
    """

    url = 'https://postman-echo.com/post'
    files = {'image': open(source_file_path, 'rb')}
    headers = {}

    response = requests.post(url, headers=headers, files=files)
    data = response.json()

    bytestr = bytes(data['files']['image.jpeg'][len(
        'data:application/octet-stream;base64,'):], encoding='UTF-8',)

    decoded = base64.decodebytes(bytestr)

    with open(target_file_name, 'wb') as file:
        file.write(decoded)

    return f'{len(decoded)}B'


if __name__ == '__main__':

    print(send_post('image.jpeg', 'img.jpg'))
