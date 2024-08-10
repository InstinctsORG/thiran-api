# thiran-api

# Configure Poetry to Create the Virtual Environment in the Project Directory
```shell
poetry config virtualenvs.in-project true
```
# To installs dependencies into the project's virtual environment.
```shell
cd thiran-api
poetry install
```

# Below Are Optional To Do.

# Automate Running with Scripts 
# Step 1 : Edit pyproject.toml:
```shell
[tool.poetry.scripts]
start = "uvicorn my_fastapi_project.app:app --reload"
```
# Step 2 : Now, you can start the server with:
```shell
poetry run start
```


