# -*- coding: utf-8 -*-
"""
    jQuery Example
    ~~~~~~~~~~~~~~

    A simple application that shows how Flask and jQuery get along.

    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
from flask import Flask, jsonify, render_template, request, Response
app = Flask(__name__)
from werkzeug.urls import url_encode, url_fix
import requests
import justext
import json




@app.route('/v0/q')
def data():
    """data endpoint"""
    url = request.args.get('url', '')

    response = requests.get(url)
    paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
    return_array = []

    for paragraph in paragraphs:
      if not paragraph.is_boilerplate and paragraph.is_heading:
        return_array.append("HEADER: " + paragraph.text + " :HEADER")

    return_array.append("BODY: ")

    for paragraph in paragraphs:
      if not paragraph.is_boilerplate:
        return_array.append(paragraph.text + " ")

    return_array.append(" :BODY")

    if ('' == (''.join(return_array))):
        return "not today"
    return ''.join(return_array)

@app.route('/v0/q/metadata')
def qq():
    url = request.args.get('url', '')
    # import pdb; pdb.set_trace()


    # url_fix(url)
    response = requests.get(url)
    paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
    text = []
    for paragraph in paragraphs:
        p = {}
        p['is_boilerplate'] = paragraph.is_boilerplate
        p['class_type'] = paragraph.class_type
        p['content'] = paragraph.text
        p['heading'] = paragraph.heading
        text.append(p)


    # text.append({ 'response.content' : response.content })
    return json.dumps(text)

@app.route('/')
def index():
    print "bitch"
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
