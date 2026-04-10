import pytest
from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://postgres:1211@localhost:5432/QA"


@pytest.fixture
def db_connection():
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()
    transaction = connection.begin()
    yield connection  # <-- тест получает это подключение
    transaction.rollback()
    connection.close()


def test_insert_user(db_connection):
    sql = text("INSERT INTO users(user_email) VALUES (:new_user)")
    db_connection.execute(sql, {"new_user": "sergey@mail.ru"})

    result = db_connection.execute(
        text("SELECT * FROM users WHERE user_email = :email"),
        {"email": "sergey@mail.ru"}
    )
    row = result.fetchone()
    assert row is not None, "Пользователь не был добавлен в БД"
    assert row.user_email == "sergey@mail.ru"


def test_update_user(db_connection):
    insert_sql = text("INSERT INTO users(user_email) VALUES (:new_user)")
    db_connection.execute(insert_sql, {"new_user": "sergey@mail.ru"})

    select_sql = text("SELECT * FROM users WHERE user_email = :email")
    row = (db_connection.execute
           (select_sql, {"email": "sergey@mail.ru"})
           .fetchone())
    assert row is not None

    update_sql = (text
                  ("UPDATE users SET subject_id ="
                   " :new_id WHERE user_email = :email"))
    db_connection.execute(update_sql, {"new_id": 1, "email": "sergey@mail.ru"})

    updated_row = (db_connection.execute
                   (select_sql, {"email": "sergey@mail.ru"})
                   .fetchone())
    assert updated_row.subject_id == 1


def test_delete_user(db_connection):
    db_connection.execute(
        text("INSERT INTO users(user_email) VALUES (:new_user)"),
        {"new_user": "sergey@mail.ru"}
    )

    select_sql = text("SELECT * FROM users WHERE user_email = :email")

    assert (db_connection.execute
            (select_sql, {"email": "sergey@mail.ru"})
            .fetchone() is not None)

    db_connection.execute(
        text("DELETE FROM users WHERE user_email = :email"),
        {"email": "sergey@mail.ru"}
    )

    assert \
        (db_connection.execute(select_sql,
                               {"email": "sergey@mail.ru"})
         .fetchone() is None)
