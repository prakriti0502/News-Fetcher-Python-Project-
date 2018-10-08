from nm import NewsMe
from flask import Flask, redirect, url_for, request, render_template
import requests
import re
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/getNews')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    check = request.form['search']
    show=""
    if check == "":
        return render_template('index.html')
    else:
        match = re.search(r'(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)',check)
        if match:
            obj = NewsMe(check)
            newsshow = []
            values = []
            for i in obj.headlines():
                newsshow.append(i[0])
                values.append(i[1])
            new_match = re.search(r'(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)', values[1])
            if new_match:
                new = ""
            else:
                if check[-1] == "/":
                    new = check[0:-1]
                else:
                    new = check

            return render_template('search.html', headline=newsshow, links=values, search=check, new=new)
        else:
            show = "Enter valid Url"
            return render_template("index.html", msg=show)


if __name__ == '__main__':
    app.run(debug=True)
