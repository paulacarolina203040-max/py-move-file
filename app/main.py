import os


def move_file(command: str) -> None:
    parts = command.split()
    source = parts[1]
    destination = parts[2]

    destination_dir = os.path.dirname(destination)
    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    with open(source, "r", encoding="utf-8") as src_file:
        content = src_file.read()

    with open(destination, "w", encoding="utf-8") as dest_file:
        dest_file.write(content)

    os.remove(source)
