from flask import Flask, render_template  # Import Flask to allow us to create our app and add render_template, this allows us to return the rendered html we created
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following

def index():
    return render_template("index.html", phrase="hello", times=5)	# notice the 2 new named arguments!

def hello_world():
    # return 'Hello World!'  # Return the string 'Hello World!' as a response
    return render_template('index.html') #instead of returning a string, we'll return the result of the render_template method, passing in the name of our HTML file

# import statements, maybe some other routes
@app.route('/success')
def success():
  return "success"

@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

@app.route('/search')
def index():
    return render_template('index.html', people = people_list)

people_list = [
    {'name': "Bob"
    'height': 5.8,
    'gender': 'male',
    'money': 100,
    'age': 24,
    },
    {'name': "Stacy"
    'height': 5,
    'gender': 'female',
    'money': 10,
    'age': 30,
    },
    {'name': "Jessica"
    'height': 4.6,
    'gender': 'female',
    'money': 90,
    'age': 52,
    },
]

# app.run(debug=True) should be the very last statement! 


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port = 5001)    # Run the app in debug mode.

