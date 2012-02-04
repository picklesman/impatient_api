#!/usr/bin/env python
# coding: utf-8

from pprint import pprint as p
from flask import Flask, jsonify, render_template, request, redirect, url_for, session
import json

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return 'Hello world'
