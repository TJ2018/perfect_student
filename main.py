from flask import Flask, request
import json

PORT = 80
DEBUG = True

app = Flask(__name__, static_folder="web", static_url_path='')

@app.route('/')
def root():
	return app.send_static_file("index.html")


@app.route('/homework')
def homework():
	return app.send_static_file("homework.html")

@app.route('/nutrition')
def nutrition():
	return app.send_static_file("nutrition.html")


if __name__ == "__main__":
	app.run(port=PORT, debug=DEBUG)