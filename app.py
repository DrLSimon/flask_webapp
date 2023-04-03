from flask import Flask, render_template, request
import os
import numpy as np
import pickle


app = Flask(__name__)



@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def show_index():
    with open('filtered_url_comps_rep_fp.pkl', 'rb') as file:
        comps = pickle.load(file)
    comps = [np.unique(comp) for comp in comps]
    comps = [comp for comp in comps if len(comp)>=4]
    nb_comps = len(comps)
    k = request.form.get('selected')
    try:
        k=int(k) % nb_comps
    except:
        k = int(np.random.choice(nb_comps, 1))
    the_comp = comps[k]
    original = the_comp[0]
    dup_urls = [url for url in the_comp[1:]]
    return render_template("index.html", nb_comps=nb_comps-1, selected=str(k), original_url=original, dup_urls=dup_urls)

if __name__ == '__main__':
    app.run()
