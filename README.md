# postcards-backend

## Installation

Install required Python packages.

`source venv/bin/activate`

`pip install -r requirements.txt`

## Flask

Make app available: `export FLASK_APP=appname`

Activate debug mode: `export FLASK_ENV=development`

Run server: `flask run`

## API design

Keep REST design principles in mind (e.g. [Programming historian](https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask#api-design-principles)).

## Documentation

[Sphinx](http://www.sphinx-doc.org/) seems a good candidate since it's also used for the offical Python documentation.

## Deployment

Deploying a single file module is [different](https://stackoverflow.com/questions/50023430/deploying-flask-application-written-in-one-file-to-heroku) from deploying a fullblown app as done in the tutorial so the `gunicorn` line is different.

For automated deployment using Travis there are some gotchas regarding Python:

* the Python version used is 3.6 because 3.7 is not supported by Travis yet
* there's a line saying `script: python -m unittest` although there are no unittests

The `script: python -m unittest` line is there because Travis refuses to go on if no tests are ran at all.

