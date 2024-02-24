# import pandas as pd
# from flask import Flask, render_template, request, jsonify
# import csv

# app = Flask(__name__)

# # Load the dataset
# dataset = pd.read_csv('data.csv')

# # Create a dictionary of cars
# cars = {}
# for index, row in dataset.iterrows():
#     car_name = f"{row['cars/model']}"
#     cars[car_name.lower()] = row

# @app.route("/", methods=["GET"])
# def home():
#     return render_template("index.html")

# @app.route("/search", methods=["POST"])
# def search():
#     car_name = request.form.get("name", "").strip().lower()
#     car_name = f"{car_name.lower()}, {car_name.lower()}"
#     cars = car.get(car_name)
#     if car is not None and not car.empty:
#         car = car.to_dict()
#         return render_template("result.html", car=car)
#     else:
#         return "Sorry We are trying to find the car you are looking for. Please try again later."

# if __name__ == "__main__":
#     app.run(debug=True)




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