from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    # Extract the query term from url using request.args.get()
    search_term = request.args.get('search_term')

    # Make 'params' dictionary containing:
     # a) the query term, 'q'
     # b) your API key, 'key'
     # c) how many GIFs to return, 'limit'
    params = {
        "q" : search_term,
        "Key" : "FGUMZP8TJDG6",
        "lmt" : 10
    }

    # Make an API call to Tenor using the 'requests' library. For
    # reference on how to use Tenor, see:
    # https://tenor.com/gifapi/documentation
    response = requests.get(
        'https://api.tenor.com/v1/search?limit=%s' % (params.get("lmt")),
        params=params)
        # 'https://api.tenor.com/v1/search', params=params)

    if response.status_code == 200:
        gifs = response.json()["results"]
    else:
        gifs = None


    # Use the '.json()' function to get the JSON of the returned response
    # object

    # Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list

    # Render the 'index.html' template, passing the list of gifs as a
    # named parameter called 'gifs'
    return render_template("index.html", gifs=gifs, query=search_term)

if __name__ == '__main__':
    app.run(debug=True)
