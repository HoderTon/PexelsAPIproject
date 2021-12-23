import requests
from PIL import Image
from io import BytesIO


def get_image(keyword, q_page):
    header = {'Authorization': '563492ad6f91700001000001be45b3d72f984233b60c342125b0b0c3'}
    url = 'https://api.pexels.com/v1/search'
    params = {'query': keyword, 'per_page': 1}
    i = 1
    while i <= q_page:
        params['page'] = i
        get_im = requests.get(url, headers=header, params=params)
        if get_im.status_code == 200:
            im = get_im.json()
            photos = im.get('photos')
            for photo in photos:
                get_original = photo.get('src').get('original')
                get_bytes = requests.get(get_original)
                print(get_original)

                image = Image.open(BytesIO(get_bytes.content))
                image.save(f'./media/{i}.{get_original.split(".")[-1]}')

        else:
            print(get_im.text)
        i += 1


def keyword_search():
    keyword = input('Keyword: ')
    q_pages = int(input('Pages quantity: '))
    get_image(keyword, q_pages)


keyword_search()
