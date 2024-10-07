from commands import (
    CommandExecutor,
    CreateContainerCommand,
    ListContainersCommand,
    DeleteContainerCommand,
    UploadBlobCommand,
    ListBlobsCommand,
    DownloadBlobCommand,
    DeleteBlobCommand
)
from menu import print_menu
from blob_service import validate_connection_string


def main():
    # Validate the connection string before proceeding
    validate_connection_string()

    # Initialize the CommandExecutor
    command_executor = CommandExecutor()

    # Register commands with corresponding numeral keys
    command_executor.register("1", CreateContainerCommand())
    command_executor.register("2", ListContainersCommand())
    command_executor.register("3", DeleteContainerCommand())
    command_executor.register("4", UploadBlobCommand())
    command_executor.register("5", ListBlobsCommand())
    command_executor.register("6", DownloadBlobCommand())
    command_executor.register("7", DeleteBlobCommand())

    while True:
        # Display the menu to the user
        print_menu()

        # Prompt user for their choice
        choice = input("Enter your choice (0-7): \n\n")

        if choice == "0":
            print("\nExiting...\n")
            break
        else:
            # Delegate the execution to CommandExecutor
            command_executor.execute(choice)


if __name__ == "__main__":
    main()
