from main.database import db


class Inventory(db.Model):
    __tablename__ = "inventory"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(200), index=True, unique=True)
    type = db.Column(db.String(100), index=True)
    created_date = db.Column(db.DateTime, nullable=False, default=db.func.now())
    assignee = db.Column(db.String(100), nullable=True)

    def __repr__(self) -> str:
        return f"<Iventory {self.id}:{self.code}>"