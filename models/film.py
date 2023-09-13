from app import db

class Film(db.Model):
    __tablename__ = "films"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(64))
    genre = db.Column(db.String(64))
    release_date = db.Column(db.String(64))
    run_time = db.Column(db.Integer)
    watched = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __repr__(self):
        return f'<Film {self.id}: {self.title}>'