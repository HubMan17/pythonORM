# ------------------------------------
# ------------BASE FIELD--------------
# ------------------------------------

class BaseFieldModel:
  
  def __init__(self, name, size) -> None:
    self._name = name
    self._size = size
    self._type_column = None
    

  @property
  def name(self) -> str:
    return self._name
  
  @property
  def size(self) -> int:
    return self._size
  
  @property
  def type_column(self) -> str:
    return self._type_column
