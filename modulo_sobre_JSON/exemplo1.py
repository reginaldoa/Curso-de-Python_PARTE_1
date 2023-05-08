import json
from pprint import pprint

arquivos = open("teste.txt", 'w')

string_json =  '''
{
    "title": "O senhor dos anéis: A sociedade do anel",
    "original_title": "The lord of the rings: the fellowship of the ring",
    "is_movie": true,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
    "budget": null
}
'''

#testando jogar pra TXT
movie = json.loads(string_json)
print(movie["characters"][1], file = arquivos)


arquivos.write()
arquivos.close() 