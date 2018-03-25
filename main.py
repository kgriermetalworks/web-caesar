from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}

                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}

            </style>
        </head>
        <body>
            <form action="/" method="POST">
            <label>Rotate by:
                <input type="text" name="rot" value="0" />
            </label>
            <br>
            <textarea name="text" placeholder="Enter Message">{0}</textarea>
            <input type="submit">
            </form>
        </body>
    </html>
"""

@app.route("/", methods=["POST"])
def encrypt():
    
    plain_text = request.form['text']
    rotated = int(request.form['rot'])

    encrypt = rotate_string(plain_text, rotated)
    
    return form.format(encrypt)


#call to display the original form with text and textarea
@app.route("/")
def index():

    return form.format('')

app.run()