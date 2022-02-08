genres = [{"id": 18, "name": "драма"},{"id": 80,"name": "криминал"},{"id": 35,"name": "комедия"}]
genres2 = [{"id": 18, "name": "драма"},{"id": 380,"name": "криминал"},{"id": 35,"name": "комедия"}]

genres = set(genre["id"] for genre in genres)
genres = genres & set(genre["id"] for genre in genres2)
print(len(genres))
