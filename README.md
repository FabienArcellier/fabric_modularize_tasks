## Motivation

I have developped an application that rely on µservices. I have
one root repository by environment (dev, staging, production, ...).

On each repository, I have a makefile I copy/paste with all my routines with some customization.
I want to validate a way to modularize with fabric tasks.

## Synopsis

``Fabric`` propose a pythonic way to doing that with module inclusions.

## The latest version

You can find the latest version to ...

    git clone https://github.com/FabienArcellier/fabric_modularize_tasks.git

## Usage

This sample can be run

```bash
$ fab --list
Available commands:

    host_type
    subproject1.host_type
```

## Installation

Use make to instanciate a python virtual environment in ./venv and install the
python dependencies.

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Contributors

* Fabien Arcellier
