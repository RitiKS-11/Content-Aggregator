from flask import jsonify, render_template

from app import app
from app.models import ContentModel, ContentModelSchema
from app.utils import main


@app.route("/")
def index():
    result = {
        "Bbc": main.get_source('bbc'),
        "Manga": main.get_source('toonily'),
        "Top Anime": main.get_source('aniwatch'),
        "Reddit Spacex": main.get_source('reddit_spacex'),
        "Reddit News": main.get_source('reddit_news'),

    }

   
    return render_template('app/index.html', result=result)

@app.route("/db")
def database():
    try:
        contents = ContentModel.query.all()
        schema = ContentModelSchema(many=True)
        result = schema.dump(contents)

        if not result:
            return jsonify({"results": "No contents available in database."})
        return jsonify({"results":result})

    except Exception as e:
        raise e