from flask_wtf import FlaskForm
from wtforms import StringField ,PasswordField ,SelectField ,TextAreaField
from wtforms.validators import DataRequired , Length, Email ,ValidationError
from wtforms.fields import StringField
from wtforms.widgets import TextArea


class MyForm(FlaskForm):
    email=StringField(label="email :", validators=[DataRequired() ] , render_kw={"placeholder": "Votre adresse email"} )
    pseudo=StringField(label="pseudo :", validators=[DataRequired() ] , render_kw={"placeholder": "Votre pseudo"})
    phone=StringField(label="Numéro de téléphone :", validators=[DataRequired() ] , render_kw={"placeholder": "Votre Numéro Telephone"})
    password = PasswordField(label="password :", validators=[DataRequired()], render_kw={"placeholder": "Votre mot de passe"})
    confirm = PasswordField(label="confirm :", validators=[DataRequired()], render_kw={"placeholder": "Confirmer votre mot de passe"})
    titre= StringField(label="Titre de l'annonce :", validators=[DataRequired() ] )
    categorie = SelectField(label="Categorie : ", validators=[DataRequired()], choices=[('', 'Informatique & Multimedia '),('0','Telephone'),('1','ordinateur portable'),('2','accessoire informatique')] )
    description= TextAreaField(label="Description de l'annonce : ", validators=[DataRequired()])
    prix=StringField(label="Prix :", validators=[DataRequired() ] )