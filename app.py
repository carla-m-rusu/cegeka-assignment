import pprint
import click
from flask import Flask
from util import load_cv, INDEX

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.cli.command("cv", help='Print the cv data.')
@click.option("-s", "--section", default=None, help='Section to print. All if not specified.')
def cli_cv(section):
    output = load_cv(section)
    print(output[0]) if isinstance(output, tuple) else pprint.pprint(output)


@app.route('/', defaults={'section': None})
@app.route('/<section>')
def personal(section):
    return load_cv(section) if section else INDEX


if __name__ == '__main__':
    app.run()
