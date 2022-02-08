import json
import os
import urllib.request
import urllib.parse
from tqdm import tqdm
from tmdb_helpers import get_user_api_key
from tmdb_helpers import make_tmdb_api_request

def load_films(user_api_key, films_amount=1000):
    all_films = []
    for film_id in tqdm(range(films_amount)):  # более дружелюбное отображение статуса
        try:
            all_films.append(make_tmdb_api_request(method=f'/movie/{film_id}', api_key=user_api_key))
        except urllib.error.HTTPError as err:
            if err.code == 404:  #if no film on this id
                continue
            else:
                raise
    return all_films

if __name__ == '__main__':
    user_api_key = get_user_api_key()
    if not user_api_key:
        print('Invalid api key')
        raise SystemExit
    print('please, wait, this operation may take smth like 15-20 minutes')

    films_amount = 1000
    all_films = load_films(user_api_key, films_amount)
    with open(file='fragment_of_films_DB.json', mode='w', encoding='utf-8') as my_file:  # with open(file=...) not path=
        json.dump(all_films, my_file, indent=4, ensure_ascii=False)
          # Целесообразно сохранить данные в читабельном виде.
          # Программе - все равно, а если пользователю или разработчику понадобится - поймет содержимое

      # Учитывая, что дальше пользователю понадобится вводить путь к базе,
      # целесообразно этот путь ему сообщить
    print(f'База фильмов сохранена в файле:\n{os.getcwd()}/fragment_of_films_DB.json')