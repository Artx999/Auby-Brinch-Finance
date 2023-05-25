import psycopg2
import hashlib
import datetime
import os


def db():
    host = os.environ['POSTGRES_HOST']
    port = 5432
    user = os.environ['POSTGRES_USER']
    password = os.environ['POSTGRES_PASSWORD']
    database = os.environ['POSTGRES_DB']
    return "dbname={} user={} password={} host={} port={}".format(database, user, password, host, port)


def list_users():
    _conn = psycopg2.connect(db())
    _c = _conn.cursor()

    _c.execute("SELECT id FROM users;")
    result = [x[0] for x in _c.fetchall()]

    _conn.close()

    return result


def verify(id, pw):
    _conn = psycopg2.connect(db())
    _c = _conn.cursor()

    _c.execute("SELECT pw FROM users WHERE id = '" + id + "';")
    result = _c.fetchone()[0] == hashlib.sha256(pw.encode()).hexdigest()

    _conn.close()

    return result


def delete_user_from_db(id):
    _conn = psycopg2.connect(db())
    _c = _conn.cursor()
    _c.execute("DELETE FROM users WHERE id = '" + id + "';")
    _conn.commit()
    _conn.close()

    # when we delete a user FROM database USERS, we also need to delete all his or her notes data FROM database NOTES
    _conn = psycopg2.connect(db())
    _c = _conn.cursor()
    _c.execute("DELETE FROM notes WHERE owner = '" + id + "';")
    _conn.commit()
    _conn.close()

    # when we delete a user FROM database USERS, we also need to 
    # [1] delete all his or her images FROM image pool (done in app.py)
    # [2] delete all his or her images records FROM database IMAGES
    _conn = psycopg2.connect(db())
    _c = _conn.cursor()
    _c.execute("DELETE FROM images WHERE owner = '" + id + "';")
    _conn.commit()
    _conn.close()


def add_user(id, pw):
    _conn = psycopg2.connect(db())
    _c = _conn.cursor()

    _c.execute("INSERT INTO users values(%s, %s)", (id.upper(), hashlib.sha256(pw.encode()).hexdigest()))

    _conn.commit()
    _conn.close()


def read_note_from_db(id):
    _conn = psycopg2.connect(db())
    _c = _conn.cursor()

    command = "SELECT note_id, timestamp, note FROM notes WHERE owner = '" + id.upper() + "';"
    _c.execute(command)
    result = _c.fetchall()

    _conn.commit()
    _conn.close()

    return result


def match_user_id_with_note_id(note_id):
    # Given the note id, confirm if the current user is the owner of the note which is being operated.
    _conn = psycopg2.connect(db())
    _c = _conn.cursor()

    command = "SELECT owner FROM notes WHERE note_id = '" + note_id + "';"
    _c.execute(command)
    result = _c.fetchone()[0]

    _conn.commit()
    _conn.close()

    return result


def write_note_into_db(id, note_to_write):
    _conn = psycopg2.connect(db())
    _c = _conn.cursor()

    current_timestamp = str(datetime.datetime.now())
    _c.execute("INSERT INTO notes values(%s, %s, %s, %s)", (
        id.upper(), current_timestamp, note_to_write,
        hashlib.sha1((id.upper() + current_timestamp).encode()).hexdigest()))

    _conn.commit()
    _conn.close()


def delete_note_from_db(note_id):
    _conn = psycopg2.connect(db())
    _c = _conn.cursor()

    command = "DELETE FROM notes WHERE note_id = '" + note_id + "';"
    _c.execute(command)

    _conn.commit()
    _conn.close()


def image_upload_record(uid, owner, image_name, timestamp):
    _conn = psycopg2.connect(db())
    _c = _conn.cursor()

    _c.execute("INSERT INTO images VALUES (%s, %s, %s, %s)", (uid, owner, image_name, timestamp))

    _conn.commit()
    _conn.close()


def list_images_for_user(owner):
    _conn = psycopg2.connect(db())
    _c = _conn.cursor()

    command = "SELECT uid, timestamp, name FROM images WHERE owner = '{0}'".format(owner)
    _c.execute(command)
    result = _c.fetchall()

    _conn.commit()
    _conn.close()

    return result


def match_user_id_with_image_uid(image_uid):
    # Given the note id, confirm if the current user is the owner of the note which is being operated.
    _conn = psycopg2.connect(db())
    _c = _conn.cursor()

    command = "SELECT owner FROM images WHERE uid = '" + image_uid + "';"
    _c.execute(command)
    result = _c.fetchone()[0]

    _conn.commit()
    _conn.close()

    return result


def delete_image_from_db(image_uid):
    _conn = psycopg2.connect(db())
    _c = _conn.cursor()

    command = "DELETE FROM images WHERE uid = '" + image_uid + "';"
    _c.execute(command)

    _conn.commit()
    _conn.close()


if __name__ == "__main__":
    print(list_users())
