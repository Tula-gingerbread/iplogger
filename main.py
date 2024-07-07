from flask import Flask, request, render_template
import config
from datetime import datetime

app = Flask(__name__)

with open('code.template', 'r', encoding='utf-8') as template:
    temp = template.read()

write = r'{datetime.now()}: IP: "{request.remote_addr}" User Agent: "{request.headers.get("User-Agent")}"' + '\n'
for logger, link in config.loggers.items():
    execute = temp.format(logger=logger, write=write, link=link)
    exec(execute)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.port, debug=config.debug)