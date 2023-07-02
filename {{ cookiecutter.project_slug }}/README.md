# {{ cookiecutter.project_name }}

Author(s): {{ cookiecutter.authors }}

{{ cookiecutter.project_description }}

## Environment Setup

This project comes with a Docker setup.
To get started, make sure you have the following software installed on your machine:

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

After the installation:

1. Start the Docker Desktop application

2. On your host machine, open a terminal and run one of the following commands in the root directory:

   - If you have GNU Make installed:

     ```shell
     make start
     ```

   - Otherwise:

     ```shell
     docker compose up --build
     ```

   This will create a Docker container and start JupyterLab inside it.
   Once it has started up, click on the link shown in the terminal to log in to JupyterLab.

3. Once inside the Docker container (e.g. through JupyterLab), open a terminal and run in the root directory:

   ```shell
   make install
   ```

4. Still in the terminal, run the following to check everything works as expected:

   ```shell
   make check
   ```

You are all set to run code inside the Docker container!
Happy coding!
