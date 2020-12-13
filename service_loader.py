import os, fnmatch, importlib

BASEDIR = os.path.dirname(os.path.abspath(__file__))
SELF_FILE = os.path.abspath(__file__)
SERVICE_FILENAME = os.environ.get("SERVICE_FILENAME", "services.py")


def ignore_dir(root):
    ignore_dirs = [
        ".env",
        ".venv",
        "external",
        ".pytest_cache",
        "__pycache__",
        "cache",
        ".git",
    ]
    for ignore in ignore_dirs:
        if ignore in root:
            return True
    return False


def find_all(pattern, path):
    result = set()

    for root, dirs, files in os.walk(path):
        if ignore_dir(root):
            continue
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                file_name = os.path.join(root, name)
                if file_name != SELF_FILE:
                    full_path = os.path.join(root, name)
                    relative_path = full_path.replace(BASEDIR + "/", "")
                    result.add(relative_path)
    return result


all_services = find_all(SERVICE_FILENAME, BASEDIR)


for file_path in all_services:
    relative_python_path = file_path.replace("/", ".").replace(".py", "")
    print(f"Loading services in... {relative_python_path}")
    exec(f"from {relative_python_path} import *")
