import sys
import inspect
from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return inspect.getsource(sys.modules[__name__])

@app.route('/~')
def rand():
    # oh classic!
    assert 1/0

if __name__ == '__main__':
    app.run(host='0.0.0.0', processes=1, threaded=True)

