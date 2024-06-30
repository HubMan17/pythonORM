# ------------------------------------
# ------------BOOL FIELD--------------
# ------------------------------------

from . BaseFieldModel import BaseFieldModel

class BoolField(BaseFieldModel):

  def __init__(self, name) -> None:
    self._name = name
    self._size = 1
    self._type_column = 'INTEGER'