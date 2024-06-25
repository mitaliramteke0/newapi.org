from flask import Flask, render_template
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

# Your API key
api_key = 'abe7dc0e68e542f9a0fcc2377ed530d3'

# Chemicals list
chemicals = [
    "Methanol", 
    # "Toluene", "Vinyl Acetate Monomer", "Butyl Acetate Monomer",
    # "Acetic acid", "Phenol", "Styrene", "N-Butanol", "Butyl Acetate",
    # "IsoPropyl alcohol", "IsoButanol", "c9", "Mono Ethylene glycol",
    # "Diethylene glycol", "Propylene glycol", "Methylpropanediol",
    # "1-Octanol", "Methyl dichloride", "Acetonitrile", "Acetone",
    # "Ethylene dichloride", "Butyl Glycol", "Mono Methyl Acrylate",
    # "Methyl ethyl ketone", "1-Hexene", "Aniline oil", "CycloHexanone",
    # "Methyl isobutyl ketone"
]

@app.route('/')
def index():
    # Create a query string with OR operators to search for all chemicals
    query = " OR ".join(chemicals)

    # Calculate the date range (past 30 days)
    to_date = datetime.now()
    from_date = to_date - timedelta(days=30)
    from_date_str = from_date.strftime('%Y-%m-%d')
    to_date_str = to_date.strftime('%Y-%m-%d')

    # API request URL
    url = f'https://newsapi.org/v2/everything?q={query}&from={from_date_str}&to={to_date_str}&sortBy=publishedAt&apiKey={api_key}'

    # Send the request to the API
    response = requests.get(url)
    articles = []

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        articles = data['articles']

    return render_template('home.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
