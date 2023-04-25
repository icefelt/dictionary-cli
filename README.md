# Dictionary CLI

**Dictionary CLI** is a command-line interface application built with [Typer](https://typer.tiangolo.com/) that allows the user to query the Merriam-Webster dictionary and receive a formatted response with the word definiton. 

## Installation

To run **Dictionary CLI**, run the following steps:

1. Clone the source code to a local directory directory
2. Create a Python virtual environment and activate it

```sh
$ git clone git@github.com:icefelt/dictionary-cli.git && cd dictionary-cli/
$ python -m venv ./venv && source venv/bin/activate
(venv) $
```

2. Install dependencies

```sh
(venv) $ python -m pip install -r requirements.txt
```

<!-- 3. Initialize the application

```sh
(venv) $ python -m rptodo init
```

This command asks you to introduce the file path to store the application's database. You can also accept the default file path by pressing enter. -->

## Usage


```sh
(venv) $ python dictionary-api.py
Enter a word: rascal
rascal: a mean, unprincipled, or dishonest person
```

## Release History

- 0.2.0

## About the Author

Scott Eissfeldt - email: scott@eissfeldt.com

