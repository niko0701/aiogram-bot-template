from tortoise.models import Model
from tortoise import fields


class Base(Model):
    """
    Base models includes common fields for others models, you can add additional fields if it is necessary
    """
    # Primary key
    id = fields.BigIntField(pk=True)
    # Created at
    created_at = fields.DatetimeField(auto_now_add=True)

    # Magic method for string representation, you can change it and at using "print()" method chosen fields will be represented
    def __str__(self):
        return str(self.id)

    class Meta:
        abstract = True
