import os
from flask import Flask ,render_template,request,redirect,url_for,flash,session
from forms import MyForm ,RegisterForm
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, SelectField
from flask_mysqldb import MySQL
from flask_dropzone import Dropzone
from werkzeug.utils import secure_filename
from admin_forms import adminlogin
from functools import wraps #update 0.1
import urllib.request
from datetime import datetime
basedir = os.path.abspath(os.path.dirname(__file__))
app=Flask(__name__)
app.config.from_object('config.config')


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'affar'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'static/uploads'),
    # Flask-Dropzone config:
    DROPZONE_ALLOWED_FILE_TYPE='image',
    DROPZONE_MAX_FILE_SIZE=3,
    DROPZONE_MAX_FILES=5,   
)

dropzone = Dropzone(app)


def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, *kwargs)
        else:
            return redirect(url_for('login'))

    return wrap

#update 0.1

def not_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return redirect(url_for('index'))
        else:
            return f(*args, *kwargs)

    return wrap


def allowed_file(filename):
 return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/subscribe', methods=['GET', 'POST'])
@not_logged_in
def subscribe():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        pseudo = form.pseudo.data
        email = form.email.data
        password = form.password.data
        confirm = form.confirm.data
        phone = form.phone.data

        # Create Cursor
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (email, pseudo, phone ,password) VALUES (%s,%s,%s,%s)", (email, pseudo, phone ,password))

        # Commit cursor
        mysql.connection.commit()

        # Close Connection
        cur.close()

        flash('You are now registered and can login', 'success')

        return redirect(url_for('login'))
    return render_template('subscribe.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    form = MyForm()
    if request.method =="POST" :
            email= request.form.get("email")
            password = request.form.get("password")
            cur = mysql.connection.cursor()
            result= cur.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
            
            if result > 0:
                    data = cur.fetchone()
                    session['log']=True
                    session['id']=data[0]                   
                    flash('you are successfully loggin in ','success')
                    return render_template('home.html')
            else :
                flash('Email Or Password Are invalid ','danger')
                return render_template('login.html', form=form)
    return render_template('login.html', form=form)

@app.route('/logout', methods=["GET", "POST"])
def logout():
    session.clear()
    flash("Vous étes deconnecte","primary")
    return render_template('home.html')


@app.route("/deposerAnnonce",methods=["POST","GET"])
def upload():
    form = MyForm()
     
    return render_template('deposer_annonce.html',form=form)


@app.route('/upload', methods=['POST'])
def handle_upload():
    cur = mysql.connection.cursor()
    now = datetime.now() 
    for key, f in request.files.items():  # use request.files.items() in Python3
            if key.startswith('file'):
                f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
                maxx=cur.execute("SELECT MAX(id_produit)  FROM produit")
                result= cur.fetchone() 
                cur.execute("INSERT INTO images (source, id_produit) VALUES (%s, %s)",[f.filename, result[0]+1])
                mysql.connection.commit()
    return '', 204

@app.route('/MyAnnounce', methods=['POST'])
def handle_form():
    title = request.form.get('titre')
    categorie = request.form.get('categorie')
    description = request.form.get('description')
    prix = request.form.get('prix')
    now = datetime.now() 
    numero=request.form.get('phone')
    #ville= request.form.get('ville')   
    etat=1
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO produit (id,title,categorie,description,prix,date_ajout,numero,etat) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (session['id'],title, categorie, description ,prix,now,numero,etat))
    mysql.connection.commit()
    cur.close()
    return 'file uploaded and form submit<br>title: %s<br> description: %s' % (title, description)
    
    #admin log in
@app.route('/admin', methods=["GET", "POST"])
def admin():
    form = adminlogin()
    if request.method =="POST" :
        email= request.form.get("email")
        password= request.form.get("password")
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM admin WHERE email=%s AND password=%s", (email, password))
        result = cur.fetchall()
        if len(result)>0:
            #session['admin_log_in']=True
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM admin ")
            last_name= cur.fetchall()
            session["log_in"] = last_name
            session["log"]=True
            return redirect(url_for('admincon'))
        else:
            return render_template('admin/pages/login_2.html', form=form)
    return render_template('admin/pages/login_2.html', form=form)
 


@app.route('/admincon')
def admincon():
    curso = mysql.connection.cursor()
    users_rows = curso.execute("SELECT * FROM users")
    num_rows = curso.execute("SELECT * FROM produit")
    result = curso.fetchall()
    #order_rows = curso.execute("SELECT * FROM orders")
    return render_template('admin/pages/index.html',result=result, row=num_rows,users_rows=users_rows)

@app.route('/admin_out')
def admin_log_out():
    session.clear()
    
    return redirect(url_for('admin'))


#affichier la liste de utilisateurs
@app.route('/users')
def users():
    curso = mysql.connection.cursor()
    num_rows = curso.execute("SELECT * FROM produit")
    #order_rows = curso.execute("SELECT * FROM orders")
    users_rows = curso.execute("SELECT * FROM users")
    result = curso.fetchall()
    return render_template('admin/pages/all_users.html', result=result, row=num_rows,users_rows=users_rows)
'''
@app.route('/orders')
def orders():
    curso = mysql.connection.cursor()
    num_rows = curso.execute("SELECT * FROM products")
    order_rows = curso.execute("SELECT * FROM orders")
    result = curso.fetchall()
    users_rows = curso.execute("SELECT * FROM users")
    return render_template('admin/pages/all_orders.html', result=result, row=num_rows, order_rows=order_rows,
                           users_rows=users_rows)
'''

#affichier le liste de produits
@app.route('/Product')
def product():
    curso = mysql.connection.cursor()
    num_rows = curso.execute("SELECT * FROM produit")
    result = curso.fetchall()
    #order_rows = curso.execute("SELECT * FROM orders")
    users_rows = curso.execute("SELECT * FROM users")
    return render_template('admin/pages/all_product.html',result=result, row=num_rows,users_rows=users_rows)

#ajouter une categorie
@app.route('/add_categorie')
def add_categorie():
    return render_template('admin/pages/add_categorie.html')

#supprimer utilisateur
@app.route('/Delete_user')
def Delete_user():
    user_id = request.args['id']
    '''
    return render_template('admin/pages/test.html',uers_id=user_id)
    '''
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM users WHERE id=%s", [user_id])
    mysql.connection.commit()
    cur.close()
    flash('deleted successfully','success')
    return redirect(url_for("users"))

#suprimer produit
@app.route('/Delete_Product')
def Delete_product():
    user_id = request.args['id']
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM produit WHERE id=%s", [user_id])
    mysql.connection.commit()
    cur.close()
    flash('deleted successfully','success')
    return redirect(url_for("product"))
    

