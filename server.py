# -*- coding: utf-8 -*-
"""
    jQuery Example
    ~~~~~~~~~~~~~~

    A simple application that shows how Flask and jQuery get along.

    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)
import requests
import justext


@app.route('/q')
def data():
    """data endpoint"""
    url = request.args.get('url', '')


    response = requests.get(url)
    paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
    return_array = []
    print("after_request")


    for paragraph in paragraphs:
      if not paragraph.is_boilerplate:
        return_array.append(paragraph.text)
        print("after_request")
    # import pdb; pdb.set_trace()
    if ('' == (''.join(return_array))):
        return "not today"
    return ''.join(return_array)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
