# ------------------------------------
# -----------TEXT FIELD---------------
# ------------------------------------

from . BaseFieldModel import BaseFieldModel

class TextField(BaseFieldModel):

  def __init__(self, name, size=255) -> None:
    self._name = name
    self._size = size
    self._type_column = 'TEXT'