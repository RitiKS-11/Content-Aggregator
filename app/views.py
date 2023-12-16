from flask import jsonify, render_template

from app import app
from app.models import ContentModel, ContentModelSchema
from app.util.main import get_source

@app.route("/")
def index():
    result = {
        "BBC": get_source('BBC'),
        # "Manga": get_source('toonily'),
        # "Top Anime": get_source('aniwatch'),
        "Reddit Spacex": get_source('reddit spacex'),
        # "Reddit News": get_source('reddit_news'),
        "Verge": get_source('verge'),
        "TechCrunch": get_source('techcrunch'),
        # "Apple Insider": get_source("apple_insider"),
        "Linux Today": get_source("linux today"),
        "Game Informer": get_source("game informer")

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