from flask import Flask, url_for, render_template
import json

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    param = {}
    param['title'] = title
    return render_template('base.html', **param)


@app.route('/training/<prof>')
@app.route('/training', defaults={'prof': ''})
def training(prof=''):
    param = {}
    param['prof'] = prof.lower()
    return render_template('training.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
