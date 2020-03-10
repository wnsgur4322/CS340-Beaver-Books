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

@webapp.route('/login.html', methods=['POST', 'GET'])
def login():
    db_connection = connect_to_database()
    query = "SELECT email, password FROM users;"
    result = execute_query(db_connection, query).fetchall()
    print(len(result))
    
    query2 = "SELECT user_id FROM users;"
    result2 = execute_query(db_connection, query2).fetchall()
    print(result2[0])

    if request.method =='POST':
        input_email = request.form['user_email']
        input_password = request.form['password']
        print("user inputted: {0}, {1}".format(input_email, input_password))
        global SUPER_USER_ID

        if input_email == "kimchi@gmail.com" and input_password == "taco":
            SUPER_USER_ID = result2[0][0]
            flash("You were successfully logged in with SUPER ADMIN ACCOUNT !! ")
            return redirect(url_for('index'))
            
        for i in range(len(result)):
            if result[i][0] == input_email and result[i][1] == input_password:
                SUPER_USER_ID = result2[i][0]
                print(SUPER_USER_ID)
                return redirect(url_for('index_normal'))
        
        flash("Wrong email or password, please check your input!")
        return redirect(url_for('login'))
    
    print("Fetching and rendering login web page")
    return render_template('login.html', font_url1="https://fonts.googleapis.com/css?family=Montserrat:200,300,400,500,600,700,800,900", font_url2="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")

@webapp.route('/logout')
def logout():
    SUPER_USER_ID = 0
    return redirect(url_for('login'))

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

    #load authors table from DB
    query3 = "SELECT * FROM authors;"
    result3 = execute_query(db_connection, query3).fetchall()
    
    #load publishers table from DB
    query4 = "SELECT * FROM publishers;"
    result4 = execute_query(db_connection, query4).fetchall()

    return render_template('admin.html', books=result, users=result2, authors=result3, publishers=result4, font_url1="https://fonts.googleapis.com/css?family=Montserrat:200,300,400,500,600,700,800,900", font_url2="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")

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
        publisher_id = request.form['publisher_id']
        book_img = request.form['book_img']
        author_id = request.form['author_id']
        
        if float(price) >= 0 and int(year) >= 0 and int(isbn) >= 0: 
            query3 = 'INSERT INTO books (isbn, title, price, publisher_id, year, book_img) VALUES (%s,%s,%s,%s,%s,%s)'
            data = (isbn, title, price, publisher_id, year, book_img)
            execute_query(db_connection, query3, data)
            query4 = "SELECT isbn from books"
            result3 = execute_query(db_connection, query4).fetchall()
            query5 = 'INSERT INTO books_authors (isbn, author_id) VALUES (%s,%s)'
            data2 = (isbn,author_id)
            execute_query(db_connection, query5,data2)
            if booklist_len != len(result3):
                flash("You have successfully added new book on the booklist!")
                return redirect(url_for('admin'))
            else:
                flash("please check your input !!")
                return redirect(url_for('add_new_books'))
        else:
            flash("Please check your input (positive integer only for price, isbn, and year) ")
            return redirect(url_for('add_new_books'))

@webapp.route('/add_new_authors.html', methods=['POST','GET'])
def add_new_authors():
    print("Add new authors!\n")
    db_connection = connect_to_database()

    if request.method == 'GET':
        print("get GET \n")
        query = 'SELECT * from authors'
        result = execute_query(db_connection, query).fetchall()
        print(result)

        return render_template('add_new_authors.html', authors = result, font_url1="https://fonts.googleapis.com/css?family=Montserrat:200,300,400,500,600,700,800,900", font_url2="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")

    
    elif request.method == 'POST':
        print("take user inputs for adding a new author\n")
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        address = request.form['address']
        url = request.form['url']

        if first_name != "" and last_name != "":
             query2 = 'INSERT INTO authors (first_name, last_name, address, url) VALUES (%s,%s,%s,%s)'
             data = (first_name, last_name, address, url)
             execute_query(db_connection, query2, data)
             flash("You have successfully added new author on the author list!")
             return redirect(url_for('admin'))
        
        else:
            flash("please check your input (don't empty on author name slots")
            return redirect(url_for('add_new_authors'))

@webapp.route('/add_new_publishers.html', methods=['POST','GET'])
def add_new_publishers():
    print("Add new publishers!\n")
    db_connection = connect_to_database()

    if request.method == 'GET':
        print("get GET \n")
        query = 'SELECT * from publishers'
        result = execute_query(db_connection, query).fetchall()
        print(result)

        return render_template('add_new_publishers.html', publishers = result, font_url1="https://fonts.googleapis.com/css?family=Montserrat:200,300,400,500,600,700,800,900", font_url2="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")

    
    elif request.method == 'POST':
        print("take user inputs for adding a new author\n")
        company_name = request.form['company_name']
        contact = request.form['contact']
        address = request.form['address']
        url = request.form['url']

        if company_name != "" and contact != "":
             query2 = 'INSERT INTO publishers (company_name, contact, address, url) VALUES (%s,%s,%s,%s)'
             data = (company_name, contact, address, url)
             execute_query(db_connection, query2, data)
             flash("You have successfully added new publisher on the publisher list!")
             return redirect(url_for('admin'))
        
        else:
            flash("please check your input (don't empty on company name and contact slots)")
            return redirect(url_for('add_new_publishers'))

@webapp.route('/about.html')
def about():
    print("Fetching and rendering about.html web page")
    return render_template('about.html', font_url1="https://fonts.googleapis.com/css?family=Montserrat:200,300,400,500,600,700,800,900", font_url2="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")

@webapp.route('/about_normal.html')
def about_normal():
    print("Fetching and rendering about.html web page")
    return render_template('about_normal.html', font_url1="https://fonts.googleapis.com/css?family=Montserrat:200,300,400,500,600,700,800,900", font_url2="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")


@webapp.route('/shopping_cart.html', methods=['POST', 'GET'])
def shopping_cart():
    db_connection = connect_to_database()
    print("get GET ! \n")
    print("user key: %d" % SUPER_USER_ID)
    
    query = 'SELECT books.title, shopping_carts.isbn, books.price, books.book_img, shopping_carts.date FROM shopping_carts INNER JOIN books ON shopping_carts.isbn = books.isbn WHERE user_id = %d ' % SUPER_USER_ID
    result = execute_query(db_connection, query).fetchall()
    count = len(result)
    total_price = 0
    for i in range(len(result)):
        total_price = result[i][2] + total_price

    print("Fetching and rendering shopping_cart web page")
    return render_template('shopping_cart.html', cart_list = result, user_key = SUPER_USER_ID, total_price = total_price, count = count, font_url1="https://fonts.googleapis.com/css?family=Montserrat:200,300,400,500,600,700,800,900", font_url2="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")

@webapp.route('/shopping_cart_normal.html')
def shopping_cart_normal():
    db_connection = connect_to_database()
    print("get GET ! \n")
    print("user key: %d" % SUPER_USER_ID)
    
    query = 'SELECT books.title, shopping_carts.isbn, books.price, books.book_img, shopping_carts.date FROM shopping_carts INNER JOIN books ON shopping_carts.isbn = books.isbn WHERE user_id = %d ' % SUPER_USER_ID
    result = execute_query(db_connection, query).fetchall()
    count = len(result)
    total_price = 0
    for i in range(len(result)):
        total_price = result[i][2] + total_price

    print("Fetching and rendering shopping_cart web page")
    return render_template('shopping_cart_normal.html', cart_list = result, user_key = SUPER_USER_ID, total_price = total_price, count = count, font_url1="https://fonts.googleapis.com/css?family=Montserrat:200,300,400,500,600,700,800,900", font_url2="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")

@webapp.route('/shop.html', methods=['POST', 'GET'])
def shop():
    db_connection = connect_to_database()
    print("get GET ! \n")
    query = 'SELECT books.title, books.isbn, authors.first_name, authors.last_name, publishers.company_name, books.year, books.price, books.book_img from books INNER JOIN books_authors ON books.isbn = books_authors.isbn INNER JOIN authors ON books_authors.author_id = authors.author_id INNER JOIN publishers ON books.publisher_id = publishers.publisher_id;'
    result = execute_query(db_connection, query).fetchall()
    
    for i in range(len(result)):
        try:
            key = result[i][1]
            for j in range(len(result)):
                if key == result[j][1] and i != j:
                    print("deleting!")
                    result = result[:j] + result[j+1:]
        except:
            break

    return render_template('shop.html', book_info = result, font_url1="https://fonts.googleapis.com/css?family=Montserrat:200,300,400,500,600,700,800,900", font_url2="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")

@webapp.route('/shop_normal.html', methods=['POST', 'GET'])
def shop_normal():
    db_connection = connect_to_database()
    print("get GET ! \n")
    query = 'SELECT books.title, books.isbn, authors.first_name, authors.last_name, publishers.company_name, books.year, books.price, books.book_img from books INNER JOIN books_authors ON books.isbn = books_authors.isbn INNER JOIN authors ON books_authors.author_id = authors.author_id INNER JOIN publishers ON books.publisher_id = publishers.publisher_id;'
    result = execute_query(db_connection, query).fetchall()
    
    for i in range(len(result)):
        try:
            key = result[i][1]
            for j in range(len(result)):
                if key == result[j][1] and i != j:
                    print("deleting!")
                    result = result[:j] + result[j+1:]
        except:
            break

    return render_template('shop_normal.html', book_info = result, font_url1="https://fonts.googleapis.com/css?family=Montserrat:200,300,400,500,600,700,800,900", font_url2="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")


@webapp.route('/index.html', methods=['POST', 'GET'])
def index():
    print("Fetching and rendering index web page")
    return render_template('index.html', font_url1="https://fonts.googleapis.com/css?family=Montserrat:200,300,400,500,600,700,800,900", font_url2="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")

@webapp.route('/index_normal.html', methods=['POST', 'GET'])
def index_normal():
    db_connection = connect_to_database()
    query = "SELECT user_id, first_name FROM users;"
    result = execute_query(db_connection, query).fetchall()
    for i in range(len(result)):
        print(result[i])
        if result[i][0] == SUPER_USER_ID:
            flash ("Welcome to Beaver Books ! %s !" % result[i][1])
    print("Fetching and rendering index web page (user_id = %d)" % SUPER_USER_ID )
    return render_template('index_normal.html', font_url1="https://fonts.googleapis.com/css?family=Montserrat:200,300,400,500,600,700,800,900", font_url2="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")

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
    db_connection = connect_to_database()
    query = "DELETE FROM books WHERE isbn = %s"
    data = (isbn,)
    flash("selected book is sucessfully deleted !")
    execute_query(db_connection, query, data)
    return redirect(url_for('admin'))

@webapp.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    db_connection = connect_to_database()
    query = "DELETE FROM users WHERE user_id = %s"
    data = (user_id,)
    if user_id == 1:
        flash("your selected account is SUPER ADMIN ACCOUNT, so CAN'T DELETE IT!")
        return redirect(url_for('admin')) 
        
    flash("selected user is sucessfully deleted !")
    execute_query(db_connection, query, data)
    return redirect(url_for('admin'))

@webapp.route('/delete_shopping_cart/<string:date>')
def delete_shopping_cart(date):
    db_connection = connect_to_database()
    query = "DELETE FROM shopping_carts WHERE date = %s;"
    data = (date,)
    execute_query(db_connection, query, data)
    flash("Your selected book has successfully deleted from your shopping cart !")
    return redirect(url_for('shopping_cart'))

@webapp.route('/delete_shopping_cart_normal/<string:date>')
def delete_shopping_cart_normal(date):
    db_connection = connect_to_database()
    query = "DELETE FROM shopping_carts WHERE date = %s;"
    data = (date,)
    execute_query(db_connection, query, data)
    flash("Your selected book has successfully deleted from your shopping cart !")
    return redirect(url_for('shopping_cart_normal'))

@webapp.route('/add_to_cart/<int:isbn>')
def add_to_cart(isbn):
    db_connection = connect_to_database()
    query = 'INSERT INTO shopping_carts (user_id, isbn) VALUES (%s,%s);'
    data = (SUPER_USER_ID, isbn)
    execute_query(db_connection, query, data)
    flash("Your selected book has successfully added on your shopping cart !")
    return redirect(url_for('shop'))

@webapp.route('/add_to_cart_normal/<int:isbn>')
def add_to_cart_normal(isbn):
    db_connection = connect_to_database()
    query = 'INSERT INTO shopping_carts (user_id, isbn) VALUES (%s,%s);'
    data = (SUPER_USER_ID, isbn)
    execute_query(db_connection, query, data)
    flash("Your selected book has successfully added on your shopping cart !")
    return redirect(url_for('shop_normal'))

@webapp.route('/account_update.html', methods=['POST', 'GET'])
def account_update():
    db_connection = connect_to_database()
    
    if request.method == "GET":
        query = "SELECT * FROM users WHERE user_id = %d" % SUPER_USER_ID
        result = execute_query(db_connection, query).fetchall()
        print(result)

    if request.method == "POST":
        print("update user info !")
        new_email = request.form['email']
        new_password = request.form['password']
        new_address = request.form['address']

        query2 = "UPDATE users SET email = %s, password = %s, address = %s WHERE user_id = %s"
        data = (new_email, new_password, new_address, SUPER_USER_ID)
        execute_query(db_connection, query2, data)
        flash("your information has successfully updated!")
        return redirect(url_for('index_normal'))

    print("Fetching and rendering account_update.html web page")
    return render_template('account_update.html', user_info = result, font_url1="https://fonts.googleapis.com/css?family=Montserrat:200,300,400,500,600,700,800,900", font_url2="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")

@webapp.route('/book_update.html/<int:isbn>', methods=['POST', 'GET'])
def book_update(isbn):
    db_connection = connect_to_database()

    if request.method == "GET":
        query = "SELECT * FROM books WHERE isbn = %d" % isbn
        result = execute_query(db_connection, query).fetchall()
        print(result)
        print("Fetching and rendering book_update.html web page")
        return render_template('book_update.html', book_info = result, font_url1="https://fonts.googleapis.com/css?family=Montserrat:200,300,400,500,600,700,800,900", font_url2="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")



    if request.method == "POST":
        print("update book info !")
        new_price = request.form['price']
        new_year = request.form['year']
        new_book_img = request.form['book_img']

        query2 = "UPDATE books SET price = %s, year = %s, book_img = %s WHERE isbn = %s"
        data = (new_price, new_year, new_book_img, isbn)
        execute_query(db_connection, query2, data)
        flash("selected book has successfully updated !")
        return redirect(url_for('admin'))
