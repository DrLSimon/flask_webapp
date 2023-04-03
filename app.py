from flask import Flask, render_template
import os
import numpy as np
import pickle
import requests


app = Flask(__name__)

def validate_url(urls):
    valid_urls = []
    for url in urls:
        a=requests.get(url,verify=False)
        report = str(a.status_code)
        if report != 404:
            valid_urls.append(url)
    return valid_urls

def url_checker(url):
    try:
        #Get Url
        get = requests.get(url)
        # if the request succeeds 
        if get.status_code == 200:
            return True
        else:
            return False

    #Exception
    except requests.exceptions.RequestException as e:
        return False


@app.route('/')
@app.route('/index')
def show_index():
    #all_pairs = np.load('pairs.npy')
    #nb_pairs = len(all_pairs)
    #k = int(np.random.choice(nb_pairs, 1))
    #left_image_url, right_image_url = all_pairs[k]
    with open('url_comps_rep_fp.pkl', 'rb') as file:
        comps = pickle.load(file)
    comps = [np.unique(comp) for comp in comps]
    comps = [comp for comp in comps if len(comp)>=4]
    nb_comps = len(comps)
    k = int(np.random.choice(nb_comps, 1))
    the_comp = comps[k]
    original = the_comp[0]
    dup_urls = [url for url in the_comp[1:] if url_checker(url)]
    return render_template("index.html", original_url=original, dup_urls=dup_urls)

if __name__ == '__main__':
    app.run()
