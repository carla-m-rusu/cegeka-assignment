# cegeka-assignment

Please write a Python Flask application that presents your CV data:

- As a JSON REST API with endpoints GET /personal, GET /experience, GET /education, ...
- As a Flask CLI command that prints the data to the console

The CV data can be hard-coded in the code or read from disk. You do not need to integrate with any database. Please include a README file on how to start the REST API and how to execute the CLI command.

It’s not a problem if you do not manage to get to a working version. Just send us the code you’ve written and describe the issue that is blocking you.

## Setup ##

Following Flask's [installation guide](https://flask.palletsprojects.com/en/2.2.x/installation/), create a virtual environment within the project's root directory, 
then activate the environment (Optional as Flask can also be installed globally).

### macOS/Linux ###

```
$ python3 -m venv venv
$ . venv/bin/activate
```

### Windows ###

```
$ py -3 -m venv venv
$ venv\Scripts\activate
```

Install Flask within the activated environment using pip.

```
$ pip install Flask==2.2.2
```

## Running the app ##

The available endpoints/options for the REST API and CLI command are: **about, personal, experience, education, skills and languages**.

### REST API ###

Use the following command to run the application:

```
$ flask run
```

The application can be accessed at [http://127.0.0.1:5000](http://127.0.0.1:5000/).

### CLI Command ###

For information on how to use the command:

```
$ flask cv --help
```

To print the entire CV use:

```
$ flask cv
```

To print a specific CV section (short form available):

<pre>
$ flask cv --section <i>SECTION_NAME</i>
$ flask cv -s <i>SECTION_NAME</i>
</pre>