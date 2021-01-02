from flask_wtf import FlaskForm
#from wtforms import StringField ,PasswordField ,SelectField ,validators,TextAreaField
#from wtforms.validators import DataRequired , Length, Email ,ValidationError,InputRequired
from wtforms import Form ,StringField, TextAreaField, PasswordField, validators, SelectField
from wtforms.validators import InputRequired,DataRequired, Length, Email, AnyOf,ValidationError ,EqualTo
from wtforms.fields import StringField
from wtforms.widgets import TextArea


def my_length_check(form, field):
    if len(field.data) < 5 :
        raise ValidationError('Field must at least 6 caractere')



class RegisterForm(Form):
    pseudo = StringField(label="pseudo :", validators=[DataRequired() ,my_length_check],
                       render_kw={'autofocus': True, 'placeholder': 'Votre pseudo'})
    #username = StringField('', [validators.length(min=3, max=25)], render_kw={'placeholder': 'Username'})
    email = StringField(label="email :", validators=[DataRequired() ],
                       render_kw={'placeholder': 'Votre adresse email'})
    password = PasswordField(label="password :", validators=[DataRequired()],
                             render_kw={'placeholder': 'Votre mot de passe'})
    confirm = PasswordField(label="confirm :", validators=[DataRequired(),EqualTo('password', message='les mots de passe ne correspondent pas') ],
                             render_kw={'placeholder': 'Confirmer votre mot de passe '})
    phone = StringField(label="Numéro de téléphone :", validators=[DataRequired() ], render_kw={'placeholder': 'Votre Numéro Telephone'})

    titre= StringField(label="Titre de l'annonce :", validators=[DataRequired() , Length(min=5) ] )
    categorie = SelectField(label="Categorie : ", validators=[DataRequired()], choices=[('', 'Informatique & Multimedia '),('0','Telephone'),('1','ordinateur portable'),('2','accessoire informatique')] )
    description= TextAreaField(label="Description de l'annonce : ", validators=[DataRequired()])
    prix=StringField(label="Prix :", validators=[DataRequired() ] )
   



class MyForm(FlaskForm):
    email=StringField(label="email :", validators=[DataRequired() ] , render_kw={"placeholder": "Votre adresse email"} )
    pseudo=StringField(label="pseudo :", validators=[DataRequired() ], render_kw={"placeholder": "Votre pseudo"})
    phone=StringField(label="Numéro de téléphone :", validators=[DataRequired() ] , render_kw={"placeholder": "Votre Numéro Telephone"})
    password = PasswordField(label="password :", validators=[DataRequired()], render_kw={"placeholder": "Votre mot de passe"})
    confirm = PasswordField(label="confirm :", validators=[DataRequired()], render_kw={"placeholder": "Confirmer votre mot de passe"})
    titre= StringField(label="Titre de l'annonce :", validators=[DataRequired() , Length(min=5) ] )
    categorie = SelectField(label="Categorie : ", validators=[DataRequired()], choices=[('', 'Informatique & Multimedia '),('0','Telephone'),('1','ordinateur portable'),('2','accessoire informatique')] )
    description= TextAreaField(label="Description de l'annonce : ", validators=[DataRequired()])
    prix=StringField(label="Prix :", validators=[DataRequired() ] )
