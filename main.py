from flask import Flask, render_template
from PIL import Image

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def base():
    return render_template('base.html', title='Заготовка')


@app.route('/training/<prof>')
def trainers(prof):
    if 'инженер' in prof or "строитель" in prof:
        head = 'Инженерные тренажеры'
        path = '/static/img/starshipit.png'
    else:
        head = 'Научные симуляторы'
        path = '/static/img/starshipnc.png'
    return render_template('trainers.html', title='Заготовка', head=head, path=path)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
