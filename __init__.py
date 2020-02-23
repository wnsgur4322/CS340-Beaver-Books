from flask import Flask, request, session, redirect, url_for, render_template
#from beaver_books.database import db_session
#create the web application
webapp = Flask(__name__)

@webapp.route("/")
def main():
    return "hello!"

#provide a route where requests on the web application can be addressed
@webapp.route('/hello')
#provide a view (fancy name for a function) which responds to any requests on this route
def hello():
    return "Hello World!";

@webapp.route('/add_books')
def add_books():
    print("fetching add_books.html")
    return render_template('shop.html', rows=result)

if __name__ == "__main__":
    webapp.run()