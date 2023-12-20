from azure.storage.blob import BlobServiceClient

connection_string = "PLACEHOLDER"


def get_blob_service_client():
    return BlobServiceClient.from_connection_string(connection_string)


def create_container(container_name):
    blob_service_client = get_blob_service_client()
    container_client = blob_service_client.get_container_client(container_name)
    container_client.create_container()


def list_containers(print_containers: bool) -> list:
    blob_service_client = get_blob_service_client()
    containers = list(blob_service_client.list_containers())

    if len(containers) == 0:
        print("No containers were found.\n\n")
        return []
    else:
        container_names = [container.name for container in containers]
        if print_containers:
            print("------------------------------------------------")
            for i, container_name in enumerate(container_names):
                print(f"[{i + 1}] {container_name}")
            print("------------------------------------------------")
        else:
            return container_names


def delete_container():
    container_names = list_containers(False)

    if not container_names:
        print("No containers have been created.")
    else:
        print("------------------------------------------------")
        for i, container_name in enumerate(container_names):
            print(f"[{i + 1}] {container_name}")
        print("------------------------------------------------")

        container_index = int(input("Choose Container: \n\n"))
        container_index -= 1

        if 0 <= container_index < len(container_names):
            selected_container = container_names[container_index]
            blob_service_client = get_blob_service_client()
            container_client = blob_service_client.get_container_client(selected_container)
            container_client.delete_container()
        else:
            print("Invalid Container index.\n\n")


def upload_blob():
    container_names = list_containers(False)
    if not container_names:
        print("No containers have been created.\n\n")
    else:
        print("------------------------------------------------")
        for i, container_name in enumerate(container_names):
            print(f"[{i + 1}] {container_name}")
        print("------------------------------------------------")

        container_index = int(input("Choose container: \n\n"))

        container_index -= 1

        if 0 <= container_index < len(container_names):
            selected_container = container_names[container_index]
            blob_name = input("Enter blob name: \n\n")
            source_file_path = input("Enter source file path: \n\n")
            blob_service_client = get_blob_service_client()
            container_client = blob_service_client.get_container_client(selected_container)

            with open(source_file_path, "rb") as data:
                blob_client = container_client.get_blob_client(blob_name)
                blob_client.upload_blob(data)
        else:
            print("Invalid index.\n\n")


def list_blobs():
    container_names = list_containers(False)

    if not container_names:
        print("No containers have been created.\n\n")
    else:
        print("------------------------------------------------")
        for i, container_name in enumerate(container_names):
            print(f"[{i + 1}] {container_name}")
        print("------------------------------------------------")

        container_index = int(input("Choose container: \n\n"))

        container_index -= 1

        if 0 <= container_index < len(container_names):
            selected_container = container_names[container_index]
            blob_service_client = get_blob_service_client()
            container_client = blob_service_client.get_container_client(selected_container)

            blobs = list(container_client.list_blobs())

            if len(blobs) == 0:
                print(f"No blobs found in container {selected_container}.\n\n")
            else:
                print("------------------------------------------------")
                for i, blob in enumerate(blobs):
                    print(f"[{i + 1}] {blob.name}")
                print("------------------------------------------------")
        else:
            print("Invalid index\n\n")


def download_blob(destination_file_path):
    container_names = list_containers(False)

    if not container_names:
        print("No containers have been created.\n\n")
    else:
        print("------------------------------------------------")
        for i, container_name in enumerate(container_names):
            print(f"[{i + 1}] {container_name}")
        print("------------------------------------------------")

        container_index = int(input("Choose Container: \n\n"))
        container_index -= 1

        if 0 <= container_index < len(container_names):
            selected_container = container_names[container_index]
            blob_service_client = get_blob_service_client()
            container_client = blob_service_client.get_container_client(selected_container)

            blobs = list(container_client.list_blobs())

            if not blobs:
                print(f"No blobs have been created in container [{selected_container}]\n\n")
            else:
                print("------------------------------------------------")
                for i, blob in enumerate(blobs):
                    print(f"[{i + 1}] {blob.name}")
                print("------------------------------------------------")

                blob_index = int(input("Choose Blob: \n\n"))
                blob_index -= 1

                if 0 <= blob_index < len(blobs):
                    selected_blob = blobs[blob_index]
                    with open(destination_file_path, "wb") as file:
                        blob_client = container_client.get_blob_client(selected_blob)
                        blob_data = blob_client.download_blob()
                        file.write(blob_data.readall())
                else:
                    print("Invalid Blob index.\n\n")

        else:
            print("Invalid Container index.\n\n")


def delete_blob():
    container_names = list_containers(False)

    if not container_names:
        print("No containers have been created.\n\n")
    else:
        print("------------------------------------------------")
        for i, container_name in enumerate(container_names):
            print(f"[{i + 1}] {container_name}")
        print("------------------------------------------------")

        container_index = int(input("Choose Container: \n\n"))
        container_index -= 1

        if 0 <= container_index < len(container_names):
            selected_container = container_names[container_index]
            blob_service_client = get_blob_service_client()
            container_client = blob_service_client.get_container_client(selected_container)

            blobs = list(container_client.list_blobs())

            if not blobs:
                print(f"No blobs have been created in container [{selected_container}]\n\n")
            else:
                print("------------------------------------------------")
                for i, blob in enumerate(blobs):
                    print(f"[{i + 1}] {blob.name}")
                print("------------------------------------------------")

                blob_index = int(input("Choose Blob: \n\n"))
                blob_index -= 1

                if 0 <= blob_index < len(blobs):
                    selected_blob = blobs[blob_index]
                    blob_client = container_client.get_blob_client(selected_blob)
                    blob_client.delete_blob()
                else:
                    print("Invalid Blob index.\n\n")

        else:
            print("Invalid Container index.\n\n")


def main():
    validate_connection_string()

    while True:
        print_menu()

        choice = input("Enter your choice (0-7): \n\n")

        if choice == "1":
            container_name = input("Enter desired container name: \n\n")
            create_container(container_name)

        elif choice == "2":
            list_containers(True)

        elif choice == "3":
            delete_container()

        elif choice == "4":
            upload_blob()

        elif choice == "5":
            list_blobs()

        elif choice == "6":
            destination_file_path = input("Enter destination file path: \n\n")
            download_blob(destination_file_path)

        elif choice == "7":
            delete_blob()

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please enter a number between 0 and 7.\n\n")


def validate_connection_string():
    if connection_string == "PLACEHOLDER":
        print(
            "The global variable named 'connection_string' must be replaced with the actual azure storage account "
            "connection string")
        exit(-1)


def print_menu():
    print("\nAzure Storage Blobs:")
    print("------------------------------------------------------------")
    print("1. Create Container")
    print("2. List Containers")
    print("3. Delete Container")
    print("4. Upload Blob")
    print("5. List Blobs")
    print("6. Download Blob")
    print("7. Delete Blob")
    print("0. Exit")
    print("------------------------------------------------------------")


if __name__ == "__main__":
    main()
