from flask import Flask, send_from_directory
from datetime import datetime
app = Flask(__name__)

@app.route('/files/<path:path>')
def send_js(path):
    return send_from_directory('files', path, mimetype='image/jpeg')

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>
	<img src=""/files/hoppo.jpg""/>
    """.format(time=the_time)

if __name__ == '__main__':
    app.run(debug=False, use_reloader=True)

