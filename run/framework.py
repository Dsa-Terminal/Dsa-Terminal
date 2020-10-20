from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
	with open('index.html') as index:
		index = index.read()
	return index

app.run()