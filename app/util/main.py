from app.models import ContentModel, ContentModelSchema

def get_source(source=None):
    try:
        schema = ContentModelSchema(many=True)

        if not source:
            contents = ContentModel.query.all()
            return schema.dump(contents)
        
        contents = ContentModel.query.filter(ContentModel.source == source).order_by(ContentModel.created_at.desc()).limit(5).all()

        return schema.dump(contents)

    except Exception as e:
        raise e
