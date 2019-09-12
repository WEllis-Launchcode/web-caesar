from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>



<html>

    <head>

        <style>

            form{{

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

      <!-- create your form here -->
      <form action="/" method="post">
      <label for="rot">Rotate by:</label>
      <input type="text" name="rot" value="0">
      <textarea name="text" {0}> </textarea>
      <input type="submit" />
      </form>

    </body>

</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=["POST"])
def encryption():
        rots = int(request.form["rot"])
        new = request.form["text"]
        aencrypted = (rotate_string(new, rots))
        encrypted = form.format(rotate_string(new, rots))
        return "<h1>" + aencrypted + "</h1>" + encrypted

app.run()