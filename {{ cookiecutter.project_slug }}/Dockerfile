# https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html
FROM {{ cookiecutter.docker_base_image }}:{{ cookiecutter.docker_base_image_tag }}

# configurations
ENV PYTHONUNBUFFERED=on \
    PYTHONFAULTHANDLER=on \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=on \
    # pip:
    PIP_NO_CACHE_DIR=on \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=120 \
    # poetry:
    POETRY_VERSION={{ cookiecutter.poetry_version }} \
    POETRY_NO_ANSI=on \
    POETRY_NO_INTERACTION=on \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_HOME="/opt/poetry" \
    PATH="${POETRY_HOME}/bin:${PATH}"

RUN pip install poetry==${POETRY_VERSION} \
    && fix-permissions "${CONDA_DIR}" \
    && fix-permissions "/home/${NB_USER}"
