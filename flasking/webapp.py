from flask import Flask, render_template, flash
from flask import request, redirect
from flask import url_for, session
from db_connector.db_connector import connect_to_database, execute_query
from flask_bootstrap import Bootstrap
import base64

#create the web application
webapp = Flask(__name__, static_folder='static', static_url_path='/static')
Bootstrap(webapp)
webapp.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@webapp.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', title = '404'), 404

@webapp.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html', title = '500'), 500

@webapp.route('/admin.html', methods=['POST', 'GET'])
#the name of this function is just a cosmetic thing
def admin():
    print("Fetching and rendering admin web page")
    db_connection = connect_to_database()
    # load books table from DB
    query = "SELECT * FROM books;"
    result = execute_query(db_connection, query).fetchall()
    
    # load users table from DB
    query2 = "SELECT * FROM users;"
    result2 = execute_query(db_connection, query2).fetchall()
    print(result)
    return render_template('admin.html', rows=result, rows2=result2, font_url1="https://fonts.googleapis.com/css?family=Montserrat:200,300,400,500,600,700,800,900", font_url2="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")

@webapp.route('/add_new_books.html', methods=['POST','GET'])
def add_new_books():
    print("Add new books!\n")
    db_connection = connect_to_database()
    booklist_len = 0

    if request.method == 'GET':
        print("get GET \n")
        query = 'SELECT author_id, first_name, last_name from authors'
        result = execute_query(db_connection, query).fetchall()
        print(result)
        query2 = 'SELECT publisher_id, company_name from publishers'
        result2 = execute_query(db_connection, query2).fetchall()

        query5 = 'SELECT isbn from books'
        result4 = execute_query(db_connection, query5).fetchall()
        booklist_len = len(result4)

        return render_template('add_new_books.html', authors = result, publishers = result2, font_url1="https://fonts.googleapis.com/css?family=Montserrat:200,300,400,500,600,700,800,900", font_url2="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")
    
    elif request.method == 'POST':
        print("take user inputs for adding a new book! \n")
        isbn = request.form['isbn']
        title = request.form['title']
        price = request.form['price']
        year = request.form['year']
        author_id = request.form['author_id']
        publisher_id = request.form['publisher_id']
        #book_img = request.files['book_img']
        #with open(request.files['book_img'], "rb") as img:
        #    img_blob = base64.b64encode(img.read())
         #   print(img_blob)
        
        if int(price) >= 0 and int(year) >= 0 and int(isbn) >= 0: 
            query3 = 'INSERT INTO books (isbn, author_id, title, price, publisher_id, year) VALUES (%s,%s,%s,%s,%s,%s)'
            data = (isbn, author_id, title, price, publisher_id, year)
            execute_query(db_connection, query3, data)
            query4 = "SELECT isbn from books"
            result3 = execute_query(db_connection, query4).fetchall()
            if booklist_len != len(result3):
                flash("You have successfully added new book on the booklist!")
                return redirect(url_for('admin'))
            else:
                flash("please check your input !!")
                return redirect(url_for('add_new_books'))
        else:
            flash("Please check your input (positive integer only for price, isbn, and year) ")
            return redirect(url_for('add_new_books'))


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

@webapp.route('/shop.html', methods=['POST', 'GET'])
def shop():
    db_connection = connect_to_database()
    print("get GET ! \n")
    query = 'SELECT books.title, books.isbn, authors.first_name, authors.last_name, publishers.company_name, books.year, books.price from books INNER JOIN authors ON books.author_id = authors.author_id INNER JOIN publishers ON books.publisher_id = publishers.publisher_id;'
    result = execute_query(db_connection, query).fetchall()

    return render_template('shop.html', book_info = result, font_url1="https://fonts.googleapis.com/css?family=Montserrat:200,300,400,500,600,700,800,900", font_url2="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")

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

@webapp.route('/register.html', methods=['POST', 'GET'])
def register():
    db_connection = connect_to_database()
    query = "SELECT user_id FROM users;"
    result = execute_query(db_connection, query).fetchall()
    print(result, len(result))

    if request.method =='POST':
        print("add new account !")
        input_first_name = request.form['first_name']
        input_last_name = request.form['last_name']
        input_email = request.form['email']
        input_password = request.form['password']
        input_repeat_password = request.form['repeat_password']
        input_address = request.form['address']
        print("user inputted: {0}, {1}, {2}, {3}, {4}, {5}".format(input_first_name, input_last_name, input_email, input_password, input_repeat_password, input_address))

        if input_password == input_repeat_password:
            query3 = 'INSERT INTO users (email, first_name, last_name, address, password) VALUES (%s,%s,%s,%s,%s)'
            data2 = (input_email, input_first_name, input_last_name, input_address, input_password)
            execute_query(db_connection, query3, data2)
            flash("Welcome! You have successfully signed up on BEAVER BOOKS!")
            return redirect(url_for('register'))
        else:
            flash("Your password and confirm password are not the same! Please check it !")
            return redirect(url_for('register'))


    print("Fetching and rendering register web page")
    return render_template('register.html', font_url1="https://fonts.googleapis.com/css?family=Montserrat:200,300,400,500,600,700,800,900", font_url2="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")

@webapp.route('/')
def first_page():
    print("Fetching and rendering login web page")
    return render_template('login.html', font_url1="https://fonts.googleapis.com/css?family=Montserrat:200,300,400,500,600,700,800,900", font_url2="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")


@webapp.route('/delete_book/<int:isbn>')
def delete_book(isbn):
    '''deletes a person with the given isbn'''
    db_connection = connect_to_database()
    query = "DELETE FROM books WHERE isbn = %s"
    data = (isbn,)
    flash("selected book is sucessfully deleted !")
    execute_query(db_connection, query, data)
    return redirect(url_for('admin'))