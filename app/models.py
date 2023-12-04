from datetime import datetime

from app.database import db, ma


class ContentModel(db.Model):
    __tablename__ = "content"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(100), unique=True)
    image = db.Column(db.String(100), nullable=True)
    source = db.Column(db.String(50))
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)


class ContentModelSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ('id', 'title', 'url', 'image', 'source')
        model = ContentModel
        load_instance=True