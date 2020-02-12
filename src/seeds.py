from models import db, Users
def run():
    Users.query.delete()
    db.session.execute("ALTER SEQUENCE users_id_seq RESTART")

    db.session.add(Users(
        first_name = 'Arthur',
        last_name = 'Pendragon',
        username = 'X-calibur',
        date_of_birth = '2/14/1989',
        email = 'once_and_future@camelot.com'
    ))