from flask import Flask, render_template, flash
from flask import request, redirect
from flask import url_for, session
from db_connector.db_connector import connect_to_database, execute_query
from flask_bootstrap import Bootstrap

#create the web application
webapp = Flask(__name__, static_folder='static', static_url_path='/static')
Bootstrap(webapp)
webapp.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@webapp.route('/admin.html')
#the name of this function is just a cosmetic thing
def admin():
    print("Fetching and rendering admin web page")
    db_connection = connect_to_database()
    # load books table from DB
    query = "SELECT * FROM books;"
    result = execute_query(db_connection, query).fetchall();
    
    # load users table from DB
    query2 = "SELECT * FROM users;"
    result2 = execute_query(db_connection, query2).fetchall();
    print(result)
    return render_template('admin.html', rows=result, rows2=result2, font_url1="https://fonts.googleapis.com/css?family=Montserrat:200,300,400,500,600,700,800,900", font_url2="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")

@webapp.route('/about.html')
def about():
    print("Fetching and rendering about.html web page")
    return render_template('about.html', font_url1="https://fonts.googleapis.com/css?family=Montserrat:200,300,400,500,600,700,800,900", font_url2="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")

@webapp.route('/about_normal.html')
def about_normal():
    print("Fetching and rendering about.html web page")
    return render_template('about_normal.html', font_url1="https://fonts.googleapis.com/css?family=Montserrat:200,300,400,500,600,700,800,900", font_url2="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")


@webapp.route('/shopping_cart.html')
def shopping_cart():
    print("Fetching and rendering shopping_cart web page")
    return render_template('shopping_cart.html', font_url1="https://fonts.googleapis.com/css?family=Montserrat:200,300,400,500,600,700,800,900", font_url2="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")

@webapp.route('/shopping_cart_normal.html')
def shopping_cart_normal():
    print("Fetching and rendering shopping_cart web page")
    return render_template('shopping_cart_normal.html', font_url1="https://fonts.googleapis.com/css?family=Montserrat:200,300,400,500,600,700,800,900", font_url2="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")

@webapp.route('/shop.html')
def shop():
    print("Fetching and rendering shop web page")
    return render_template('shop.html', font_url1="https://fonts.googleapis.com/css?family=Montserrat:200,300,400,500,600,700,800,900", font_url2="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")

@webapp.route('/shop_normal.html')
def shop_normal():
    print("Fetching and rendering shop web page")
    return render_template('shop_normal.html', font_url1="https://fonts.googleapis.com/css?family=Montserrat:200,300,400,500,600,700,800,900", font_url2="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")


@webapp.route('/index.html')
def index():
    print("Fetching and rendering index web page")
    return render_template('index.html', font_url1="https://fonts.googleapis.com/css?family=Montserrat:200,300,400,500,600,700,800,900", font_url2="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")

@webapp.route('/index_normal.html')
def index_normal():
    print("Fetching and rendering index web page")
    return render_template('index_normal.html', font_url1="https://fonts.googleapis.com/css?family=Montserrat:200,300,400,500,600,700,800,900", font_url2="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")

@webapp.route('/login.html', methods=['POST', 'GET'])
def login():
    db_connection = connect_to_database()
    query = "SELECT email, password FROM users;"
    result = execute_query(db_connection, query).fetchall()
    print(result[1][0])
    print(len(result))
    if request.method =='POST':
        input_email = request.form['user_email']
        input_password = request.form['password']
        print("user inputted: {0}, {1}".format(input_email, input_password))

        if input_email == "kimchi@gmail.com" and input_password == "taco":
            flash("You were successfully logged in with SUPER ADMIN ACCOUNT !! ")
            return redirect(url_for('index'))
            
        for i in range(len(result)):
            if result[i][0] == input_email and result[i][1] == input_password:
                return redirect(url_for('index_normal'))
    
    print("Fetching and rendering login web page")
    return render_template('login.html', font_url1="https://fonts.googleapis.com/css?family=Montserrat:200,300,400,500,600,700,800,900", font_url2="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")

@webapp.route('/register.html')
def register():
    print("Fetching and rendering register web page")
    return render_template('register.html', font_url1="https://fonts.googleapis.com/css?family=Montserrat:200,300,400,500,600,700,800,900", font_url2="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")

@webapp.route('/')
def first_page():
    print("Fetching and rendering login web page")
    return render_template('login.html', font_url1="https://fonts.googleapis.com/css?family=Montserrat:200,300,400,500,600,700,800,900", font_url2="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")

