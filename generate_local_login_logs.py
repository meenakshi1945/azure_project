from FlaskWebProject import app
from FlaskWebProject.models import User
from create_local_db import create_local_database


create_local_database()

with app.app_context():
    bad_username = 'wrong'
    bad_password = 'wrong'
    bad_user = User.query.filter_by(username=bad_username).first()

    if bad_user is None or not bad_user.check_password(bad_password):
        app.logger.warning('Invalid login attempt for username: %s', bad_username)

    good_username = 'admin'
    good_password = 'pass'
    good_user = User.query.filter_by(username=good_username).first()

    if good_user and good_user.check_password(good_password):
        app.logger.info('%s logged in successfully', good_user.username)

print('Local login log test finished.')
