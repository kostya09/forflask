from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def nothing():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    output = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
              'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
              'Присоединяйся!']
    return '</br>'.join(output)


@app.route('/image_mars')
def image_mars():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"  
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Жди нас, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='/img/mars.png')}">
                        <h2>Вот она какая, красная планета.</h2>
                      </body>
                    </html>'''


@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='/css/style.css')}" />
                            <title>Жди нас, Марс!</title>
                          </head>
                          <body>
                            <h1>Жди нас, Марс!</h1>
                            <img src="{url_for('static', filename='/img/mars.png')}">
                            <h2>Человечество вырастает из детства.</h2>
                            <h3>Человечеству мала одна планета.</h3>
                            <h4>Мы сделаем обитаемыми безжизненные пока планеты.</h4>
                            <h5>И начнем с Марса!</h5>
                            <h6>Присоединяйся!</h6>
                          </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
