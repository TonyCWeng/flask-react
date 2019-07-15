from flask.cli import FlaskGroup

from project import create_app, db
from project.api.models import User

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command('seed_db')
def seed_db():
    """Seed database."""
    db.session.add(User(username='test', email="test1@gmail.com"))
    db.session.add(User(username='test2', email="test2@gmail.org"))
    db.session.commit()

if __name__ == '__main__':
    cli()
