import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format")

    _, source, destination = parts

    destination_dir = os.path.dirname(destination)
    if destination_dir:
        current_path = ""
        for folder in destination_dir.split("/"):
            current_path = (
                os.path.join(current_path, folder)
                if current_path
                else folder
            )
            if not os.path.isdir(current_path):
                try:
                    os.mkdir(current_path)
                except (FileExistsError, OSError):
                    pass

    with open(source, "r", encoding="utf-8") as src_file:
        content = src_file.read()

    with open(destination, "w", encoding="utf-8") as dest_file:
        dest_file.write(content)

    os.remove(source)
