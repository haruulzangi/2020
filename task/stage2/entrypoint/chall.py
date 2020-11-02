import sys
import inspect
import re
from flask import Flask, render_template_string, request

def create_app():
    app = Flask(__name__)

    @app.template_filter()
    def filter_injection(output):
        if not isinstance(output, str):
            return f"Mm. Not an ip address. Weird type {output}. But I accept this anyways"

        match_result = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",output)
        if match_result:
            return output
        else:
            return "Mm. Not an ip address. But I accept this anyways"

    @app.route('/')
    def index():
        for head in request.headers:
            print(head)
        ip = request.headers.get(
            'X_FORWARDED_FOR', request.remote_addr)

        if "{%" in ip or "{{" in ip:
            ip = ip.strip("}}") + "|filter_injection}}"

        return render_template_string(
            "<h1>Welcome to HaruulZangi 2020 final round. I am challenge Entrypoint<h1><h5>Your ip address: {}".format(ip))

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', processes=1, threaded=True)

