import os


def create_project_directory(project_name, path):
    project_path = os.path.join(path, project_name)
    if os.path.isdir(path) and project_name not in os.listdir(path):
        os.mkdir(project_path)

def start_project(path: str, answers: dict) -> None:
    print(f"Path: {path}, Answers: {answers}")
    create_project_directory("uhuu", path)
    # TODO: create settings.py file
    # TODO: create game.py file
    # TODO: create root files: run.py, requirements.txt
