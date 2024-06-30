# ------------------------------------
# -------MODEL SQLite Database--------
# ------------------------------------

from sqlite3 import connect, Cursor

class SQLiteDatabase:
  
    def __init__(self) -> None:
        self._path = 'database.db'
        self._connect = None
        self._cursore = None
        
        # make connect and crate cursore for database
        self.connect()
        self.cursore()
    
    @property
    def path(self) -> str:
        return self._path
  
    def connect(self) -> connect:
        self._connect = connect(self._path)
        return self._connect
    
    def cursore(self) -> Cursor:
        self._cursore = self._connect.cursor()
        return self._cursore
    
    def close(self) -> None:
        self._connect.close()
    
    def create_table(self, tables: list) -> None:
        for table in tables:
            self.cursore().execute(
                f"""CREATE TABLE IF NOT EXISTS {table.name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    {', '.join([f'{field.name} {field.type_column}({field.size})' for field in table.fields])}
                    )"""
                )