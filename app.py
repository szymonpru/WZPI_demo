from flask import Flask, send_from_directory
from datetime import datetime
app = Flask(__name__)
import os

@app.route('/files/<path:path>')
def send_js(path):
    return send_from_directory('files', path, mimetype='image/jpeg')

@app.route('/')
def homepage():
    kaczki = os.listdir('files')
    file_list = ['<a href="/files/{pet}">{pet}</a>'.format(pet=x) for x in kaczki]

    return """<h1>Demo WZPI</h1>
    <h3>Lista zwierząt</h3>
    """ + '<br>'.join(file_list)

if __name__ == '__main__':
    app.run(debug=False, use_reloader=True)

