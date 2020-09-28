from flask import Flask
app = Flask(__name__)
@app.route('/')
def __init__():
    index = '''
    <!DOCTYPE html>
    <head>
        <meta charset="UTF-8">
    </head>
    <body>
        <div id='site'>
            <div id='header'>
                <h1>Dsa Terminal localhost controler IDE Master</h1>
            </div>
            <div id='index site'>
                <p>Pagina fora do ar!</p>
            </div>
        </div>
    </body>
    </html>
    '''
    return index
app.run()
