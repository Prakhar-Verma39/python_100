from flask import Flask
# do not call this application as 'flask.py'


# this instance of flask is WSGI(Web Server Gateway Interface) application
app = Flask(__name__)

# The first argument is the name of the application’s module or package. __name__ is a convenient shortcut for this
# that is appropriate for most cases. his is needed so that Flask knows where to look for resources such as templates
# and static files.



# the route() decorator to tell Flask what URL should trigger our function
@app.route("/<name>")
def hello_world(name):
    # The function returns the message we want to display in the user’s browser. The default content type is HTML,
    # so HTML in the string will be rendered by the browser.
    return f"<p>Hello, <script>{name}!</p>"


if __name__ == "__main__":
    app.run()
