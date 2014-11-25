import os
from flask import Flask
from flask.globals import request
from flask.templating import render_template
from flask_wtf import Form
from wtforms.fields.core import IntegerField
from wtforms.validators import DataRequired

__author__ = 'Michael Cheah'

templatePath = 'templates' if os.path.exists('templates') else 'webapp/templates'
staticPath = 'static' if os.path.exists('static') else 'webapp/static'

app = Flask(__name__, template_folder=templatePath, static_folder=staticPath)
magic_number = 7


class NumberForm(Form):
    """Create Form for Number to Guess"""
    number = IntegerField('You Number:', validators=[DataRequired()])


@app.route('/', methods=['GET', 'POST'])
def home():
    number_form = NumberForm()

    if number_form.validate_on_submit():
        user_number = int(request.form['number'])
        result = "Correct!"
        if user_number < magic_number:
            result = "Too Low!"
        elif user_number > magic_number:
            result = "Too High!"

        return render_template('home.html', form=number_form, result=result)

    return render_template('home.html', form=number_form)


if __name__ == '__main__':
    app.secret_key = os.environ.get('WEBAPP_SECRET_KEY', 'YOU_ARE_USING_AN_INSECURE_SECRET_KEY')

    '''Discover the Port number if we run on Heroku'''
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)