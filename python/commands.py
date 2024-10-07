from abc import ABC, abstractmethod
from blob_service import (
    create_container,
    list_containers,
    delete_container,
    upload_blob,
    list_blobs,
    download_blob,
    delete_blob
)


class Command(ABC):
    """Abstract base command class."""

    @abstractmethod
    def execute(self):
        pass


class CommandExecutor:
    """Executes registered commands based on user input."""

    def __init__(self):
        self._commands = {}

    def register(self, key, command: Command):
        self._commands[key] = command

    def execute(self, key):
        command = self._commands.get(key)
        if command:
            command.execute()
        else:
            print(f"Invalid choice: {key}")


# Concrete Command Classes
class CreateContainerCommand(Command):
    def execute(self):
        container_name = input("Enter desired container name: \n\n")
        create_container(container_name)


class ListContainersCommand(Command):
    def execute(self):
        list_containers(True)


class DeleteContainerCommand(Command):
    def execute(self):
        delete_container()


class UploadBlobCommand(Command):
    def execute(self):
        upload_blob()


class ListBlobsCommand(Command):
    def execute(self):
        list_blobs()


class DownloadBlobCommand(Command):
    def execute(self):
        destination_file_path = input("Enter destination file path: \n\n")
        download_blob(destination_file_path)


class DeleteBlobCommand(Command):
    def execute(self):
        delete_blob()
