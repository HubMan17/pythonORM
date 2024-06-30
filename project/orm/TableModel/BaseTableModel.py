# ------------------------------------
# -------BASE MODEL TABLE-------------
# ------------------------------------

from orm.DatabaseModel.SQLiteDatabase import SQLiteDatabase

class BaseTableModel:

    name = None
    fields = []
    cursore = SQLiteDatabase().cursore()

    def __init__(self) -> None:
        self._cursore = SQLiteDatabase().cursore()
        
    @classmethod
    def select_all(cls) -> list:
        query = f"SELECT * FROM {cls.name}"
        return cls.cursore.execute(query).fetchall()
    
    @classmethod
    def select_where(cls, *args, **kwargs) -> list:
        if not args and not kwargs:
            return cls.cursore.execute(f"SELECT * FROM {cls.name}").fetchall()
        
        query = f"SELECT * FROM {cls.name} WHERE " + " AND ".join([f"{key} = '{value}'" for key, value in kwargs.items()])
        return cls.cursore.execute(query).fetchall()
    
    @classmethod
    def insert(cls, *args, **kwargs) -> None:
        query = f"INSERT INTO {cls.name} ({', '.join([field.name for field in cls.fields])}) VALUES ({', '.join(['?'] * len(cls.fields))})"
        print(query, tuple(kwargs.values()))
        cls.cursore.execute(query, tuple(kwargs.values()))
        cls.cursore.connection.commit()
        return cls.cursore.lastrowid
    
    @classmethod
    def delete(cls, *args, **kwargs) -> None:
        query = f"DELETE FROM {cls.name} WHERE " + " AND ".join([f"{key} = '{value}'" for key, value in kwargs.items()])
        cls.cursore.execute(query)
        cls.cursore.connection.commit()
        return cls.cursore.lastrowid
    
    @classmethod
    def columns(cls) -> list:
        return [field.name for field in cls.fields]