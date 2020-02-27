# Example Project

Short description.

## Installation

Steps for other people to start working with the code.

    git clone xxx
    ...

---

## 1. Create new project
### Simple

    mkdir example-project
    cd example-project
    
    spyder example.py
    
### New git repo

    git init example-project
    cd example-project
    
    touch example.py
    touch README.md
    touch LICENSE
    touch .gitignore
    
### Existing git repo

    git clone https://github.com/aprillion/python-solar.git
    cd python-solar
    
## 2. Install dependencies
### Simple
If you have 1 global Python for everything, just follow instructions on https://docs.sunpy.org/en/stable/guide/installation/

    conda config --add channels conda-forge
    conda install sunpy
    
    python
    >>> import sunpy

### Using conda environments
When multiple projects need different version of dependencies. https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

    conda create --name example-project sunpy
    
    conda activate example-project
    conda install xxx # to install more stuff in the environment
    
    python example.py

### If using Pipenv
Not recommended by SunPy project, but common in other Python communities. https://pipenv.kennethreitz.org/

    pipenv install sunpy[all]
    pipenv run python example.py

### How to use Anaconda for existing projects that used Pipenv
See e.g. https://stackoverflow.com/a/57128480/1176601

    conda install -c conda-forge Pipfile
    python example.py

## 3. Write working code
### Execute from command line

    python example.py
    
### Use a notebook

    jupyter notebook

### Sub-directorectories, reusable functions, updating docs as needed

    mkdir data
    mkdir results
    mkdir {versionA, versionB, versionC}

    touch utils.py

### If using git
After a piece of work is done, test it one more time, then:

    git status
    git add .
    git commit -m "process data, step 3: xxx"

## 4. Backup
### Using git

    git push

## Using git with other people

    git pull
    git push

## Bigger project with remote people
https://guides.github.com/introduction/flow/
