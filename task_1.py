import requests


def get_all():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    resp = requests.get(url)
    all_list = resp.json()
    return all_list


select_dict = {}


def select_hero(list, name):
    for hero in list:
        if hero['name'] == name:
            name = hero['name']
            intelligence = hero['powerstats']['intelligence']
            select_dict[name] = intelligence
    return select_dict


if __name__ == '__main__':
    select_hero(get_all(), 'Hulk')
    select_hero(get_all(), 'Captain America')
    select_hero(get_all(), 'Thanos')

    print(
        f'The smartest of them all is {max(select_dict, key=select_dict.get)}')
