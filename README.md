# Postcards

## Goal

Project according to best practices:

- documented
  - code
  - wiki
- tested
  - low level (unit or API tests)
  - E2E
- deployed early
- use virtual environment
- (optional) CLI

## Possible technologies

Either completely Django (Python):

- database included
- no separate API (so less modular)

Or flask (Python) with a Javascript framework (e.g. Elm):

- decoupled API
  - easier to plug other Javascript framework
  - can test with Postman
- more room for error

Since the project is still relatively vague at the moment a more Modular approach with flask is preferred.

E2E testing done with Cypress since it's very easy to use. API testing done with Postman.

If a CLI would be added Click is a popular Python library to do it.

## Example sites

Example sites and interesting functionality to reuse in own project.

- [postcardman.net](https://www.postcardman.net/)
  - show new postcards
  - quick view to glimpse at card
  - sort by dimension
- [teich](http://collections.carli.illinois.edu/cdm/landingpage/collection/nby_teich)
  - show cards on map
- [discogs](https://www.discogs.com)
  - explanations everywhere

What seems missing:

- filter on crucial criteria (e.g. has )

## Functionality

- add postcard
- update postcard
  - validation
- view postcards
  - filter
  - different types of views (e.g. with picture or not)
  - glimpse at postcard
  - analysis shows relation with other postcards

## Installation

Install required Python packages.

`source venv/bin/activate`

`pip install -r requirements.txt`

Install required Javascript packages. `node` version used is v10.15.3. `npm` is by default a part of `node`.

`npm install`

## Flask

Make app available: `export FLASK_APP=appname`

Activate debug mode: `export FLASK_ENV=development`

Run server: `flask run`

## API

Keep REST design principles in mind (e.g. [Programming historian](https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask#api-design-principles)).

## Testing

### API testing

Testing is done using Postman and Newman (the Postman CLI).

Requests are part of collections and tests are linked to requests.

Tests can be run using `newman run collection`.

### E2E testing

E2E testing is done with Cypress.

Launch Cypress from root: `npm run cypress:open`. Based on script in `package.json`.

## Documentation

[Sphinx](http://www.sphinx-doc.org/) seems a good candidate since it's also used for the offical Python documentation.

## Deployment

Heroku is used for deployment since it's easy to setup with Flask and there are [decent tutorials](https://medium.com/the-andela-way/deploying-a-python-flask-app-to-heroku-41250bda27d0) available.

Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).

Add Procfile. Deploying a single file module is [different](https://stackoverflow.com/questions/50023430/deploying-flask-application-written-in-one-file-to-heroku) from deploying a fullblown app as done in the tutorial so the `gunicorn` line is different.

Deploy: `heroku create hello-flask-example`.

And push code to git repository used by Heroku: `git push heroku`
