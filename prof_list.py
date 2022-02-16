from flask import Flask, render_template

app = Flask(__name__)
pro = '''инженер-исследователь, пилот, строитель, экзобиолог, врач,
 инженер по терраформированию, климатолог, специалист по радиационной защите, 
 астрогеолог, гляциолог, инженер жизнеобеспечения, метеоролог, оператор марсохода, 
 киберинженер, штурман, пилот дронов'''
pro = pro.split(', ')


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


@app.route('/list_prof/<list>')
def list_prof(list):
    return render_template('list_prof.html', lst=list, list_prof=pro)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
