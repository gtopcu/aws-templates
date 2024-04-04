
# pip install --upgrade flask

from flask import Flask, jsonify, request, abort, redirect
import db_sqlite

# Flask-RESTful: Extension for Flask that adds support for quickly building REST APIs

app = Flask(__name__)

# http://127.0.0.1:5000/api/v1/blogs
# app.run(host='0.0.0.0', port=5000, debug=True, load_dotenv=True)
# app.run(port=5000, debug=True)

logger = app.logger
logger.info("Flask app starting..")

@app.route('/')
def home():
    # request.host
    # request.host_url
    # request.url
    # request.endpoint
    # request.headers
    # request.authorization
    # request.method
    # request.path
    # request.full_path
    # request.query_string
    # request.content_length
    # request.content_type
    # request.content_encoding
    # request.mimetype
    # request.is_secure
    # request.json
    # request.form
    # request.files
    # request.remote_addr
    # request.remote_user
    # request.user_agent
    
    return f"Hello! <br/>Addr: {request.remote_addr} <br/>User: {request.remote_user} <br/>Agent: {request.user_agent}"

@app.route('/api/v1/blogs', methods=['GET'])
def get_blogs():
    logger.debug("get blogs")
    result = handleDBRequest(db_sqlite.get_blogs, limit=1)
    logger.debug("get blogs success")
    return jsonify(result)

@app.route('/api/v1/blogs/<int:id>', methods=['GET'])
def get_blog(id: int):
    logger.debug(f"get blog {id}")
    result = handleDBRequest(db_sqlite.get_blogs, id=id, limit=1)
    logger.debug(f"get blog {id} success")
    return jsonify(result)

@app.route('/api/v1/blogs', methods=['POST'])
def create_blog():
    logger.debug("post blog")

    data = request.get_json()
    if data is None:
        abort(400, description="Bad request")
    logger.debug(f"post blog {data}")
    db_sqlite.create_blog(data)
    logger.debug(f"post blog success")

    return "post blog"


@app.errorhandler(404)
def handle_error_not_found(e):
    logger.debug(e, exc_info=True)
    return redirect(location="/", code=302)
    #return 'This URL does not exist', 404

@app.errorhandler(Exception)
def handle_error(e):
    logger.error(e)
    return "Server error", 500

def handleDBRequest(func, *args, **kwargs):
    try:
        result = func(*args, **kwargs)
    except db_sqlite.DatabaseError as e:
        logger.error(e, exc_info=True)
        abort(500, description="System error")
    except db_sqlite.BadRequestError as e:
        logger.debug(e, exc_info=True)
        abort(400, description="Bad request")
    except db_sqlite.NotFoundError as e:
        logger.debug(e, exc_info=True)
        abort(404, description="Not found")
    except db_sqlite.NotAuthorizedError as e:
        logger.debug(e, exc_info=True)
        abort(403, description="Not authorized")
    except Exception as e:
        logger.error(e, exc_info=True)
        abort(500, description="Server error")
    else:
        return result

app.run(debug=True)