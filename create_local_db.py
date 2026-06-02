from FlaskWebProject import app, db
from FlaskWebProject.models import User


def create_local_database():
    with app.app_context():
        db.create_all()

        admin = User.query.filter_by(username='admin').first()
        if admin is None:
            admin = User(username='admin')
            admin.set_password('pass')
            db.session.add(admin)
            db.session.commit()

    print('Local database is ready.')
    print('Username: admin')
    print('Password: pass')


if __name__ == '__main__':
    create_local_database()
