![Banner](src/assets/banner.png)

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=Flask&logoColor=white)](https://flask.palletsprojects.com/en/stable/)
[![Javascript](https://shields.io/badge/JavaScript-F7DF1E?logo=JavaScript&logoColor=000&style=flat-square)](https://www.javascript.com/)
[![Shell](https://img.shields.io/badge/Shell-4EAA25?&style=plastic&logo=gnu-bash&logoColor=white)]()
[![GHA workflow badge](https://github.com/valovalovalo/miniprojekti/workflows/CI/badge.svg)](https://github.com/valovalovalo/miniprojekti/actions)
[![codecov](https://codecov.io/gh/valovalovalo/miniprojekti/graph/badge.svg?token=DIS78IN4YX)](https://codecov.io/gh/valovalovalo/miniprojekti)

## Bibmanager: Simplify Your Citation Workflow

**Bibmanager** is a user-friendly app designed to streamline the way you manage academic and professional references. With an intuitive interface, the app allows you to:

- **Create** new references quickly and easily.
- **Edit** existing references to keep your citations accurate and up-to-date.
- **Delete** references you no longer need, maintaining a clutter-free library.
- **Search** your references efficiently, so you can always find what you're looking for.
- **Export** references in **BibTeX** format for seamless integration with LaTeX and other citation tools.

Whether you're writing a research paper, managing bibliographies, or keeping track of academic resources, Bibmanager makes citation management effortless.

## Links

[Backlog](https://github.com/orgs/valovalovalo/projects/1)  

[Definition of Done](https://github.com/valovalovalo/miniprojekti/wiki/Definition-Of-Done)

## Installation

**Requirements:** Python >=3.10.0, Poetry, and a PostgreSQL database.

1. Configure the PostgreSQL database and add its details to the `.env` file.
2. Run the following commands to install the application dependencies and initialize the database:

```
poetry install
poetry shell
python src/db_helper.py
```

## Usage

Start the application with the following commands:

```
poetry shell
python src/index.py
```

The application will be accessible at http://localhost:5001.

# License
