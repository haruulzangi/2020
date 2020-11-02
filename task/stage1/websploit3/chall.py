import os
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

@app.route('/~/config/<string:key>')
def config(key):
    modname = getattr(
        app,
        '__module__',
        getattr(app.__class__, '__module__')
    )
    config_set = {
        'node_addr': os.popen('cat /proc/net/arp').read(),
        'machine_id': os.popen('cat /etc/machine-id').read(),
        'whoami': os.popen('whoami').read(),
        '__file__': getattr(sys.modules.get(modname), '__file__', None)
    }
    return config_set.get(key, 'Not found')

@app.route('/~/<path:cmd>')
def exec_cmd(cmd):
    return 'Oops. Gone'

if __name__ == '__main__':
    app.run(host='0.0.0.0', processes=1, threaded=True)

