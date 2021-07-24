from flask.cli import FlaskGroup
from project import app, db, AdminUser

cli = FlaskGroup(app)


@cli.command("create_db_if_not_exists")
def create_db_if_not_exists():
    if db.exists:
        return
    reset_db()


@cli.command("reset_db")
def reset_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(AdminUser(email="example@example.com"))
    db.session.commit()


if __name__ == "__main__":
    cli()
