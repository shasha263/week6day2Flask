from app import app
from flask import render_template


@app.route('/')
def home():
    import requests as r
    data=r.get('https://pokeapi.co/api/v2/pokedex/hoenn')       
    if data.status_code==200:
        data=data.json() 
        context={
            'name':data['name'].title(),
            'poke':data['pokemon_entries']
        }

    return render_template('index.html',**context)

@app.route('/about')
def about():
    context={
        'teacher':'Sam',
        'students':['Shasha','Arefin','Nujbah', 'Nashita', 'Ibrahim'],
        'classname':'Fox78'}
    

    return render_template('components/about.html',**context)

