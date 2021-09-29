from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, DataRequired


class BookForm(FlaskForm):
    name = StringField(label="Kitap Adı", validators=[Length(min=2, max=80), DataRequired()])
    description = StringField(label="Book Description", validators=[Length(min=30, max=255), DataRequired()])
    submit = SubmitField(label="Submit")

class BookShelfForm(FlaskForm):
    title = StringField(label="Kitaplık Adı", validators=[Length(min=2, max=80), DataRequired()])
    description = StringField(label="Açıklama", validators=[Length(max=255)])
    bookshelfcolor = StringField(label="Kitaplık Rengi")
    submit = SubmitField(label="Submit")
