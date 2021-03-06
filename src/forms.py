from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField
from wtforms.validators import DataRequired
from .models import Portfolio

class CompanyForm(FlaskForm):
    """
    """
    symbol = StringField('Company Search', validators=[DataRequired()])


class CompanyAddForm(FlaskForm):
    """
    """
    symbol = StringField('symbol', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    portfolios = SelectField('portfolios')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.portfolios.choices = [(str(c.id), c.name) for c in Portfolio.query.all()]

class PortfolioCreateForm(FlaskForm):
    """
    """
    name = StringField('name', validators=[DataRequired()])

class AuthForm(FlaskForm):
    """
    """
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])