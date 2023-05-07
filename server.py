from flask import Flask, render_template
import requests
import json

def get_meme():
    url = 'https://meme-api.com/gimme'
    response = json.loads(requests.request('GET', url).text)
    meme_large = response['preview'][-2]
    subreddit = response['subreddit']
    return meme_large, subreddit

# create flask
server = Flask(__name__)

# define routes
@server.route('/')
def index():
    meme_pic, subreddit = get_meme()
    return render_template('meme_index.html', meme_pic=meme_pic, subreddit=subreddit)

# start the server
server.run(host='0.0.0.0', port='80')

