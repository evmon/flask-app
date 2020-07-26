from flask.ext.wtf import Form
from wtforms import TextAreaField, SelectField, DecimalField
from wtforms.validators import DataRequired

from models import CURRENCY_CHOICE


class PaymentCreateForm(Form):
    description = TextAreaField('Description', [DataRequired()])
    amount = DecimalField('Payment amount', [DataRequired()])
    currency = SelectField(
        'Currency',
        [DataRequired()],
        choices=CURRENCY_CHOICE)
