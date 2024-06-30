# ------------------------------------
# ----------FILE FOR TESTING----------
# ------------------------------------


from orm.orm import *


def main() -> int:

    db = SQLiteDatabase()
  
    # create tables
    # db.create_table([
    #     User,
    #     Comment
    # ])
  
    # get data from table
    print(User.delete(id=3))
    print(User.select_all())
  

class User(BaseTableModel):
    name = 'Пользователь'
    fields = [
        TextField('name'),
        IntegerField('age')
    ]

class Comment(BaseTableModel):
    name = 'Комментарий'
    fields = [
        TextField('name'),
        TextField('comment'),
        BoolField('Показывать комментарии')
    ]

if __name__ == "__main__":

    main()  
  