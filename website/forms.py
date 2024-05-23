""" forms module """


from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired


class InputForm(FlaskForm):
    dl = FloatField('DL', validators=[DataRequired()])
    ll = FloatField('LL', validators=[DataRequired()])
    mxp = FloatField('mxp', validators=[DataRequired()])
    mxv = FloatField('mxv', validators=[DataRequired()])
    myp = FloatField('myp', validators=[DataRequired()])
    myv = FloatField('myv', validators=[DataRequired()])
    col = FloatField('COL', validators=[DataRequired()])
    coly = FloatField('COLY', validators=[DataRequired()])
    fck = FloatField('FCK', validators=[DataRequired()])
    fyk = FloatField('FYK', validators=[DataRequired()])
    bar = FloatField('BAR', validators=[DataRequired()])
    bc = FloatField('BC', validators=[DataRequired()])
    df = FloatField('DF', validators=[DataRequired()])
    cu = FloatField('CU', validators=[DataRequired()])
    phi = FloatField('PHI', validators=[DataRequired()])
    gam = FloatField('GAM', validators=[DataRequired()])
    submit = SubmitField('Submit')
    