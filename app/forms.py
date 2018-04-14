from flask_wtf import FlaskForm
from wtforms import TextAreaField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired


class UploadForm(FlaskForm):
    image = FileField('Image',validators=[FileRequired(),FileAllowed(['jpg','png'])])
    description = TextAreaField('Description', validators=[InputRequired()])
    
