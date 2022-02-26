from typing import Text
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired

class UploadForm(FlaskForm):
    image = FileField('Image', validators=[
        FileRequired(),
         FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')
    ])