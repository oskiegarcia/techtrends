import sqlite3

from flask import Flask, jsonify, json, render_template, request, url_for, redirect, flash
from werkzeug.exceptions import abort
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '%(levelname)s:%(module)s:%(asctime)s, %(message)s',
        'datefmt': "%d/%m/%Y %H:%M:%S"
    }},
    'handlers': {
        'console': {
           'class': 'logging.StreamHandler',
           'stream': 'ext://sys.stdout',
           'formatter': 'default'
         },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['console']
    }
})

# Function to get a database connection.
# This function connects to database with the name `database.db`
def get_db_connection():
    try:
        connection = sqlite3.connect('database.db')
        connection.row_factory = sqlite3.Row
        return connection
    except sqlite3.Error as e:
        app.logger.error('Error connecting to database', e)
        return None


# Function to get a post using its ID
def get_post(post_id):
    try:
        connection = get_db_connection()
        post = connection.execute('SELECT * FROM posts WHERE id = ?',
                              (post_id,)).fetchone()
        connection.close()
        return post
    except sqlite3.Error as e:
        app.logger.error('Error accessing database: {}'.format(e))
        return None
    except Exception as e:
        app.logger.error('An expected error: {}'.format(e))
        return None


# Function to get the number of posts
def get_post_count():
    try:
        connection = get_db_connection()
        post_count = connection.execute('SELECT count(id) FROM posts').fetchone()
        connection.close()
        return post_count[0]
    except sqlite3.Error as e:
        app.logger.error('Error accessing database: {}'.format(e))
        return 0
    except Exception as e:
        app.logger.error('An expected error: {}'.format(e))
        return 0

# Function to get the number of active db connections
def get_active_db_connections():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # Query the master table to get the count of active connections
        cursor.execute("PRAGMA database_list;")
        rows = cursor.fetchall()
        active_connections = len(rows)

        cursor.close()
        connection.close()

        return active_connections
    except sqlite3.Error as e:
        app.logger.error('Error accessing database: {}'.format(e))
        return 0
    except Exception as e:
        app.logger.error('An expected error: {}'.format(e))
        return 0


# Define the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

# Define the main route of the web application
@app.route('/')
def index():
    try:
        connection = get_db_connection()
        posts = connection.execute('SELECT * FROM posts').fetchall()
        connection.close()
        app.logger.info('Index request successfull')
        return render_template('index.html', posts=posts)
    except sqlite3.Error as e:
        app.logger.error('Error accessing database: {}'.format(e))
        return render_template('error.html', errorMessage="Error accessing database")
    except Exception as e:
        app.logger.error('An expected error: {}'.format(e))
        return render_template('error.html', errorMessage="An expected error occurred")

# Define how each individual article is rendered
# If the post ID is not found a 404 page is shown
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    if post is None:
        app.logger.info('Article with id "{}" not found!'.format(post_id))
        return render_template('404.html'), 404
    else:
        app.logger.info('Article "{}" retrieved!'.format(post['title']))
        return render_template('post.html', post=post)


# Define the About Us page
@app.route('/about')
def about():
    app.logger.info('About request successfull')
    return render_template('about.html')


# Define the post creation functionality
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
            app.logger.warn('Title is required!')
        else:
            try:
                connection = get_db_connection()
                connection.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                               (title, content))
                connection.commit()
                connection.close()
                app.logger.info('Create request successfull')
                return redirect(url_for('index'))
            except sqlite3.Error as e:
                app.logger.error('Error accessing database: {}'.format(e))
                return render_template('error.html', errorMessage="Error accessing database")
            except Exception as e:
                app.logger.error('An expected error: {}'.format(e))
                return render_template('error.html', errorMessage="An expected error occurred")

    return render_template('create.html')


@app.route('/healthz')
def healthcheck():
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('healthz request successfull')
    return response


@app.route('/metrics')
def metrics():
    db_conn_count = get_active_db_connections()
    app.logger.debug("db_conn_count:", db_conn_count)
    posts_count = get_post_count()
    app.logger.debug("posts_count:", posts_count)

    response = app.response_class(
        response=json.dumps({"status": "success", "code": 0,
                             "data": {"db_connection_count": db_conn_count, "post_count": posts_count}}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('Metrics request successfull')
    return response


# start the application on port 3111
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='3111')
