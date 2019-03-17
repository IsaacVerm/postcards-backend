# postcards-backend

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
- continuous integration
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

The Travis gem is necessary to encrypt environment variables for Travis. The version doesn't matter too much so just run `gem install travis`.

## Flask

Make app available: `export FLASK_APP=appname`

Activate debug mode: `export FLASK_ENV=development`

Run server: `flask run`

## API

Keep REST design principles in mind (e.g. [Programming historian](https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask#api-design-principles)).

## Documentation

[Sphinx](http://www.sphinx-doc.org/) seems a good candidate since it's also used for the offical Python documentation.

## Deployment

Heroku is used for deployment since it's easy to setup with Flask and there are [decent tutorials](https://medium.com/the-andela-way/deploying-a-python-flask-app-to-heroku-41250bda27d0) available.

Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).

Add Procfile. Deploying a single file module is [different](https://stackoverflow.com/questions/50023430/deploying-flask-application-written-in-one-file-to-heroku) from deploying a fullblown app as done in the tutorial so the `gunicorn` line is different.

Deploy: `heroku create appname`.

And push code to git repository used by Heroku: `git push heroku`

## Continuous integration

Both E2E and API tests are run each time a new commit is pushed to GitHub. New commits are automatically detected by [Travis](https://travis-ci.com/). The `.travis.yml` file configures exactly how the continuous integration works.

Currently the deployment process is still fairly manual:

* go to the [Heroku Dashboard](https://dashboard.heroku.com) and deploy your latest feature branch
* merge feature branch into master
* push master (triggers automated checks)

This gives confidence everything is tested at the end. However:

* you still have to deploy manually
* master branch can be in a broken state because testing happens after deploying

## TO DO

- update tests using the [Postman API](https://docs.api.getpostman.com/) (so collection doesn't has to be exported manually)
- add [documentation API](https://learning.getpostman.com/docs/postman/api_documentation/intro_to_api_documentation/)
- automated deployment (after testing)

## Issues

### Exporting collection is only semi automatic

It would be nice to export the Postman tests automatically. However, 2 separate jobs are necessary to do this at the moment. A Python job to export from Postman with a REST request and the other job is used to run the tests (example in commit `Configure Travis to use both Python and NodeJS`). I didn't find out yet how to share the exported collection from the Python job to the other job.

In order to avoid having to do it completely manually a shell script has to be run first before commiting.
