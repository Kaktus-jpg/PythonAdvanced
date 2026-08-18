# Python Advanced — Skillbox

This repository contains my learning materials, practice tasks, and homework assignments for the **Python Advanced** course by Skillbox.

The repository is organized by course modules. Each module may include examples, practical exercises, and completed assignments.

## Project Goals

During this course, I am improving my Python skills and exploring advanced topics such as:

- Object-oriented programming
- Decorators and context managers
- Iterators and generators
- Type hints
- Testing
- Working with files and data formats
- Asynchronous programming
- Python project structure and dependency management

## Project Structure

```text
.
├── Module_1/              # Module 1 materials and tasks
├── Module_3/              # Module 2 materials and tasks
├── ...
├── Module_N/              # Other course modules
├── src/
│   └── pythonadvanced/    # Package source code
├── .python-version        # Required Python version
├── pyproject.toml         # Project configuration and dependencies
├── uv.lock                # Locked dependency versions
└── README.md
```

## Requirements

- Python version specified in `.python-version`
- [uv](https://docs.astral.sh/uv/) for Python and dependency management

## Installation

Clone the repository:

```bash
git clone https://github.com/Kaktus-jpg/PythonAdvanced.git
cd PythonAdvanced
```

Install the required Python version and project dependencies:

```bash
uv sync
```

`uv sync` creates or updates the virtual environment and installs the exact dependency versions recorded in `uv.lock`.

## Running Code

Run a Python file from the project root:

```bash
uv run 'Module_N/Lesson_N/main.py'
```

## Adding Dependencies

To add a new dependency:

```bash
uv add package-name
```

For development-only dependencies:

```bash
uv add --dev package-name
```

After changing dependencies, commit both files:

```text
pyproject.toml
uv.lock
```

## Notes

- Every course module is stored in a separate directory.
- The repository is intended for educational purposes.
- Some files may be drafts, experiments, or intermediate solutions created while studying the course.

## Author

#### [Kaktus-jpg](https://github.com/Kaktus-jpg)

Learning Python backend development and advanced Python concepts.
