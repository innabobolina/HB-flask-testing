from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""

    # FIXME: write a function that creates a game and adds it to the database.
    
    g1 = Game(name="chess", description="a game of chess")
    g2 = Game(name="madlibs", description="a word game")
    g3 = Game(name="scrabble", description="another word game!")

    db.session.add_all([g1, g2, g3])
    db.session.commit()
   
   

if __name__ == '__main__':
    from party import app

    connect_to_db(app)
    print("Connected to DB.")
