# postcards-backend

## Installation

Install required Python packages.

`source venv/bin/activate`

`pip install -r requirements.txt`

## Project structure

It's advised to use a package structure for larger projects or even blueprints but since I have no idea what the limitation of the current approach could be I prefer to keep it simple with a single file `app.py` importing other files.

## Flask

Make app available: `export FLASK_APP=app`

Activate debug mode: `export FLASK_ENV=development`

Run server: `flask run`

## Database

Database used is [`sqlite3`](https://docs.python.org/3/library/sqlite3.html#module-sqlite3) since it's just a file and no server setup is needed.

## Security

By default Cross Origin Resource Sharing (CORS) is disabled in Flask. Since we make calls to the API from another app (frontend) CORS is enabled.

## API design

Keep REST design principles in mind (e.g. [Programming historian](https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask#api-design-principles)).

## Documentation

[Sphinx](http://www.sphinx-doc.org/) seems a good candidate since it's also used for the offical Python documentation.

## Deployment

Deploying a single file module is [different](https://stackoverflow.com/questions/50023430/deploying-flask-application-written-in-one-file-to-heroku) from deploying a fullblown app as done in the tutorial so the `gunicorn` line is different.

For automated deployment using Travis there are some gotchas regarding Python:

- the Python version used is 3.6 because 3.7 is not supported by Travis yet
- there's a line saying `script: python -m unittest` although there are no unittests

The `script: python -m unittest` line is there because Travis refuses to go on if no tests are ran at all.

## Sources used

[Codementor tutorial Flask with SQLAlchemy](https://www.codementor.io/garethdwyer/building-a-crud-application-with-flask-and-sqlalchemy-dm3wv7yu2)

[SQLite3 tutorial](https://docs.python.org/3/library/sqlite3.html)

[How to work with Flask responses](https://blog.miguelgrinberg.com/post/customizing-the-flask-response-class)

[Which HTTP status code, response body and headers to return](https://evertpot.com/http/201-created)

[How ETags works](https://www.logicbig.com/quick-info/web/etag-header.html)

[How to make Row in Flask json serializable](https://stackoverflow.com/questions/34715593/rows-returned-by-pyodbc-are-not-json-serializable)

[Setup CORS](https://flask-cors.readthedocs.io/en/latest/)

[What to return when resource already exists](https://stackoverflow.com/questions/3825990/http-response-code-for-post-when-resource-already-exists)
