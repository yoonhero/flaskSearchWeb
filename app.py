
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

from urllib.request import urlopen
app = Flask(__name__)


@ app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':
        search_keyword = request.form["search"]
        return redirect(url_for('search', keyword=search_keyword))


@ app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        search_keyword = request.args.get('keyword')
        driver = webdriver.Chrome(
            "/Users/yoonseonghyeon/Desktop/programming/python/selenium/chromedriver")
        driver.get("https://www.google.de/imghp?hl=ko&tab=wi&authuser=0&ogbl")
        return render_template("search.html", keyword=search_keyword)
    elif request.method == "POST":
        search_keyword = request.form["search"]
        return redirect(url_for('search', keyword=search_keyword))


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5005)
