from flask import (
    Flask,
    render_template,
    request,
    session,
    make_response,
    current_app
)

app = Flask(__name__)

app.config.from_object('conf_file_')

@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        message = "Whaaaaaaaaaat?"
        if 'admin' not in session or not session['admin']:
            session['admin'] = False
        else:
            message = open('flag').read()
        return render_template('index.html', msg=message, link=True)
    return render_template('index.html')


@app.route('/inf0', methods=['GET'])
def hint():
    if 'hint' in request.args:
        info = request.args.get('hint')
    else:
        info = 'nohint'
    if 'flag' in info:
        info = 'noflag'
    current_app.logger.error(info)
    try:
        message = open('/usr/srcs/app/{}'.format(info)).read()
        print(message)
    except Exception as e:
        message = "Rotas's exception"

    return render_template('index.html', msg=message)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
