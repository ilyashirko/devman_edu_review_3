import os
import json


  # незачем создавать отдельный .py файл. логично обращение к базе через файл "поиск в базе"
def load_data(path):
    if not os.path.exists(path):
        return None
    with open(path, mode='r', encoding='utf-8') as my_file:
        films_database = json.load(my_file)
        return films_database


  # films_data - может быть прочитана как film's data, т.е. информация о фильме, а не база фильмов
def search_for_film(keyword, films_database_fragment):  
    films_found = set()
    for film in films_database_fragment:
        if keyword.lower() in film['original_title'].lower():
            films_found.add(film['original_title'])
    return films_found


if __name__ == '__main__':
    path = input('Enter path to local fragment of films database: ')
    films_database_fragment = load_data(path)
    if not films_database_fragment:
        print('DataBase not found, sorry...')  # если назвали файл DataBase, то не найден DataBase, а не File
        raise SystemExit
    keyword_for_search = input('Enter film to search for: ')  # "keyword" не отображает назначение переменной
    result = search_for_film(keyword_for_search, films_database_fragment)
      # Не помешает добавить общительности. 
      # Без нее, если найден один фильм - программа похожа на echo, 
      # если ничего не найдено - похоже на поломку.
    if result:
        print(f'Found films: {len(result)}')
        for film in sorted(result):
            print(f'- "{film}"')
    else:
        print('Sorry, no matches!')
        