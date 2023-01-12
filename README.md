# Python Technical test

## Summary

1. Goal of the program
2. Available commands
3. Run the application 
4. Configuration
5. Setup your local environment
6. Limit of the solution

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
| run                 | Will run the program with the two promps           |
| install             | Will install all necessary libraries               |
| test                | Will launch all the tests                          |
| test-cov            | Will generate a coverage report in the terminal    |
| lint                | Will lint and correct formating issues in the code |
| export-requirements | Will freeze all dependencies of the project        |


## Run the application
To run the application it is very simple :

```
$ make run
```

You we will prompted with 2 choices :
- The name of the configuration file, default is config.yaml
- To dump the result of the standardization to a file or only print it to the terminal, default is false.

## Configuration

They are two types of files :
- config: is a YAML where the key is a regex of file name with two attributes (delimiter and column_count), must be located in the folder param.
- data: is a csv file to standardize, must be located in the folder dataDropArea.

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

Then install pipenv with pipx :

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

## Limit of the solution

- Dates are not handled
- Some integeres are handled as strings 
- If a rogue separator is added in the middle of a column it is processed as one string and it will add any missing column
- Might add `.0` at the end of some integers
