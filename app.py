
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html_code = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>WOW CARS</title>
        <link rel="stylesheet" href="../css/style.css">
    </head>
    <body>
    <div class="container">
        <form action="https://www.pakwheels.com/used-cars/search" method="get" class="search-bar">
            <input type="text" placeholder="SEARCH CAR" name="q">
            <button type="submit"><img src="images\search.png"></button>
        </form>
    </div>
    </body>
    </html>
    """
    return render_template_string(html_code)

if __name__ == '__main__':
    app.run(debug=True)