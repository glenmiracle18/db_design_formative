from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def gender_validator(value):
    if value not in [0, 1]:
        raise ValidationError(
            _('%(value)s is not in [0, 1]')
        )