from flask import Flask, render_template
import os
import numpy as np


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def show_index():
    all_pairs = np.load('pairs.npy')
    #left_image_url = 'https://www.lightingdirect.com/imagebase/resized/x800/Lutronimages/lutron_v_600_al_9.jpg'
    #right_image_url = 'https://www.lightingdirect.com/imagebase/resized/x800/Lutronimages/lutron_v_600_la_3.jpg'
    nb_pairs = len(all_pairs)
    k = int(np.random.choice(nb_pairs, 1))
    left_image_url, right_image_url = all_pairs[k]
    return render_template("index.html", left_image_url=left_image_url, right_image_url=right_image_url)

if __name__ == '__main__':
    app.run()
