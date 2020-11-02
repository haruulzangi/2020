# hz{thisiswhereourworldscollide}
from flask import current_app, make_response, \
     Flask, render_template, request
from datetime import datetime
import base64
import hashlib

app = Flask(__name__)
app.config.from_object('config')

def generate_cookie():
    ts = datetime.now().timestamp()
    hash_v = hashlib.md5(str(ts).encode('ascii')).hexdigest()
    return "{}.{}".format(base64.b64encode(str(ts).encode('ascii')).decode('ascii'),
                          base64.b64encode(hash_v.encode('ascii')).decode('ascii'))


def check_cookie(data):
    try:
        current_app.logger.error(data)
        time_v = base64.b64decode(data.split('.')[0]).decode('ascii')
        hash_v = base64.b64decode(data.split('.')[1]).decode('ascii')
        current_app.logger.error(hashlib.md5(time_v.encode('ascii')).hexdigest())
        current_app.logger.error(hash_v)
        if hashlib.md5(time_v.encode('ascii')).hexdigest() == hash_v:
            if time_v == '1337133713'  or time_v == '1337133713000'or time_v == '13371337130000':
                return "yes"
            return "Can You Tell Your Story on Wednesday, May 16, 2012 02:01:53 GMT"
    except Exception as a:
        current_app.logger.error(a)

    return "Protagonist's exception"


@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        message = "You already tell your story on {}".format(
            datetime.fromtimestamp(int(datetime.now().timestamp())).strftime('%Y-%m-%d %H:%M'))
        if request.cookies.get('sator', False):
            message = check_cookie(request.cookies.get('sator'))
        resp = make_response(render_template('index.html', msg=message, datetime=datetime.now()))

        if not request.cookies.get('sator', False):
            resp.set_cookie('sator', generate_cookie())
        return resp

    resp = make_response(render_template('index.html'))
    return resp


if __name__ == '__main__':
    app.run(port=5000, debug=False, host='0.0.0.0')


