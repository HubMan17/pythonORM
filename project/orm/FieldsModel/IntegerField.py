# ------------------------------------
# ---------INTEGER FIELD--------------
# ------------------------------------

from . BaseFieldModel import BaseFieldModel

class IntegerField(BaseFieldModel):

  def __init__(self, name) -> None:
    self._name = name
    # set max size for integer in sql
    self._size = 11
    self._type_column = 'INTEGER'