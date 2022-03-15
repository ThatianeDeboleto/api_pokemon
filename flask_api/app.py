from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    r = requests.get('https://pokeapi.co/api/v2/pokedex/2')
    pokemon = r.json()
    return render_template('index.html', pokemon=pokemon, title='PyDex')

@app.route('/<pokemon_id>', methods=['GET'])
def pokemon(pokemon_id):
  r = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon_id))
  pokemon = r.json()
  return render_template('pokemon.html', pokemon=pokemon, pokemon_id=pokemon_id, title='Pydex')

if __name__ == "__main__":
  app.run(debug=True)