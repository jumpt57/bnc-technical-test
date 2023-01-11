# BNC Technical test

## Goal of the program

Design and code a program that standardizes a given file into a quoted csv format. The program will meet the following
criterias:

- It will loop through files in the 'dataDropArea' directory to process all the files.
- It will use a configuration file as a YAML in order to pick up different parameters. The parameters should take into
  account:
    - File name Regex
    - Delimiter Used
- You can find a config example in `param/config.yaml`
- It will seek the file's configuration given a unique regex based on the file name pattern.
- The program should print errors if a file could not be standardized due to errors.
- The standardized output format is Quoted CSV, meaning seperated by comma, enclosed by quotes.
- The program has to be unit tested.
- The entrypoint of the program should be `standardize.py`

## Available commands

| Name                | Description                                        |
|---------------------|----------------------------------------------------|
| run                 | Will run the program with the default config file  |
| install             | Will install all necessary libraries               |
| test                | Will launch all the tests                          |
| test-cov            | Will generate a coverage repport in the terminal   |
| lint                | Will lint and correct formating issues in the code |
| export-requirements | Will freeze all dependencies of the project        |

## Setup your local environment

First of all start by install python on MacOS using brew, you can get it [here](https://brew.sh).

```
$ brew install python3
```

Add python and globally installed packages to your path :

```
export PATH="$HOME/Library/Python/3.10/bin:$PATH"
export PATH="$HOME/.local/bin:$PATH"
```

Source either `.bashrc` or `.zshrc`.

```
$ pip install --user pipx
$ pipx install pipenv
```

You can also install pipenv with pip directly :

```
$ pip install pipenv
```

Then when pipenv is installed, install the project dependencies with :

```
$ make install
```
