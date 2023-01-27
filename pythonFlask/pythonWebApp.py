# this is the import statement.
# here we are impoerinf flask as a helper to our python webserver
# render_template allows us to load the html files from the templates
# request allows us to get the item from the html form

from email.mime import application
from flask import Flask, render_template, request

app = Flask(__name__)

# here we have two routes setup for our simple application

@app.route('/', methods=['get'])
def input():
   # in the render_template, we pass in both the template for 
   # our html we want to use and the variables the template is looking for
    
    return render_template("basicForm.html", the_title="Adding is fun!")

@app.route('/add', methods=['post'])
def sum():
    # here we are using request to get the user inputted variables 
    a = request.form['firstNum']
    b = request.form['secondNum']
    results = int(a) + int(b)
    return render_template("results.html", the_title="The Answer", a = a, b = b, results=results)


if __name__ == '__main__':
   app.run()