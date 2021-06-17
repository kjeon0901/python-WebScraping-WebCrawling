import requests as rq

def image_download(url, file_name):
    image_request_result = rq.get(url)
    image = image_request_result.content

    with open(file_name, 'wb') as destination:
        destination.write(image)

url = 'https://avatars2.githubusercontent.com/u/12229295?v=4&s=60'

image_download(url, 't.png')
