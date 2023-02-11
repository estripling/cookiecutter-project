from importlib import metadata

import {{ cookiecutter.project_slug }}


def test_version():
    assert {{ cookiecutter.project_slug }}.__version__ == metadata.version("{{ cookiecutter.project_slug }}")
