# Azure Function Python v2 Blueprint Template

<!-- vscode-markdown-toc -->
* [Features](#Features)
* [Requirements](#Requirements)
* [Getting Started](#GettingStarted)
* [Pre-commit](#Pre-commit)
* [Pytest, Unit Testing](#PytestUnitTesting)
* [UV](#UV)
* [DevOps Pipeline](#DevOpsPipeline)
* [License](#License)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

This repository contains a template for creating an Azure Function using Python v2 and blueprints.

## Features

-   Azure Function v2 with blueprints
-   Unit testing with pytest
-   Automated linting, static analysis, and unit test using tox
-   Pre-commit configuration for formatting
-   DevOps pipeline to test, build and deploy
-   Devcontainer configuration for development

## Requirements

-   Azure Functions Core Tools v2.x or later
-   Python 3.12 or later
-   Visual Studio Code with the Remote - Containers extension installed
-   Optionally if not running in Devcontainer
    - UV installed
    - Pre-commit installed

## Getting Started

1.  Clone the repository
2.  Open the repository in Visual Studio Code
3.  When prompted, reopen the repository in a Devcontainer
4.  In the Devcontainer terminal, run the command `pip install -r requirements-dev.txt` to install the required dependencies
5.  run `uv sync` to install the dependancies
6.  run `pre-commit install` to have pre-commit automatically run before a commit.
7.  To run the function locally, run the command `func start`
8.  To run the unit tests, run the command `pytest`
9.  To run the linter and static analysis, as well as tests, run the command `ruff`
10.  To format the code according to pre-commit configuration, run the command `pre-commit run --all-files`
11. To build and deploy the function, configure the DevOps pipeline to suit your needs.

## Pre-commit

This template uses the  [pre-commit](https://pre-commit.com/) tool to enforce code formatting and consistency. Pre-commit is a framework for managing and maintaining multi-language pre-commit hooks.

The pre-commit configuration for this template can be found in the [.pre-commit-config.yaml](.pre-commit-config.yaml) file. The configuration specifies which hooks should be run, in what order, and with what arguments.

To install the pre-commit hooks, run the command `pre-commit install`. After installation, the hooks will run automatically before every commit. If a hook fails, the commit will be aborted, allowing you to fix any issues before committing the changes.

## Pytest, Unit Testing

This template includes the [pytest](https://pytest.org/) testing framework, which is used for both unit testing and behavior-driven development (BDD) testing.

Unit tests can be written in the `tests/unit_tests` directory.

To run tests, use the command `pytest`. To select which tests to run, use `pytest <folder>`.

Tests are automatically run in the DevOps pipeline's build stage, ensuring that any changes to the code do not introduce regressions or unexpected behavior.

## DevOps Pipeline

The DevOps pipeline is configured using Azure Pipelines. The pipeline contains the following stages:

1.  Test - Runs unit tests in Azure Function.
2.  Build - Builds the Azure Function and runs unit tests.
3.  Deploy to Dev - Deploys the Azure Function to the development environment.

The pipeline is triggered on changes to the `main` branch.

## License

This project is licensed under the [MIT License](./LICENSE).