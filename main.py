from azure.storage.blob import BlobServiceClient

connection_string = "PLACEHOLDER"

def get_blob_service_client():
    return BlobServiceClient.from_connection_string(connection_string)


def create_container(container_name):
    blob_service_client = get_blob_service_client()
    container_client = blob_service_client.get_container_client(container_name)
    container_client.create_container()
    print(f"Container with name '{container_name}' has been created.\n")


def list_containers(print_containers: bool) -> list:
    blob_service_client = get_blob_service_client()
    containers = list(blob_service_client.list_containers())

    if len(containers) == 0:
        print("No containers were found.\n\n")
        return []
    else:
        container_names = [container.name for container in containers]
        if print_containers:
            print("CONTAINERS")
            print("------------------------------------------------")
            for i, container_name in enumerate(container_names):
                print(f"[{i + 1}] {container_name}")
            print("------------------------------------------------")
        else:
            return container_names


def choose_container():
    container_names = list_containers(False)

    if not container_names:
        print("No containers have been created.\n\n")
        return None
    else:
        print("CONTAINERS")
        print("------------------------------------------------")
        for i, container_name in enumerate(container_names):
            print(f"[{i + 1}] {container_name}")
        print("------------------------------------------------")

        container_index = int(input("Choose container: \n\n"))
        container_index -= 1

        if 0 <= container_index < len(container_names):
            return container_names[container_index]
        else:
            print("Invalid index\n\n")
            return None


def choose_blob():
    selected_container = choose_container()

    if selected_container:
        blob_service_client = get_blob_service_client()
        container_client = blob_service_client.get_container_client(selected_container)

        blobs = list(container_client.list_blobs())

        if not blobs:
            print(f"No blobs have been created in container [{selected_container}]\n\n")
            return None, None
        else:
            print("BLOBS")
            print("------------------------------------------------")
            for i, blob in enumerate(blobs):
                print(f"[{i + 1}] {blob.name}")
            print("------------------------------------------------")

            blob_index = int(input("Choose Blob: \n\n"))
            blob_index -= 1

            if 0 <= blob_index < len(blobs):
                selected_blob = blobs[blob_index]
                return selected_blob, container_client
            else:
                print("Invalid Blob index.\n\n")
                return None, None


def delete_container():
    selected_container = choose_container()

    if selected_container:
        blob_service_client = get_blob_service_client()
        container_client = blob_service_client.get_container_client(selected_container)
        container_client.delete_container()
        print(f"Container with name '{selected_container}' has been deleted from the storage account.\n")


def list_blobs():
    selected_container = choose_container()

    if selected_container:
        blob_service_client = get_blob_service_client()
        container_client = blob_service_client.get_container_client(selected_container)
        blobs = list(container_client.list_blobs())

        if len(blobs) == 0:
            print(f"No blobs found in container {selected_container}.\n\n")
        else:
            print("BLOBS")
            print("------------------------------------------------")
            for i, blob in enumerate(blobs):
                print(f"[{i + 1}] {blob.name}")
            print("------------------------------------------------")


def upload_blob():
    selected_container = choose_container()

    if selected_container:
        blob_name = input("Enter blob name: \n\n")
        source_file_path = input("Enter source file path: \n\n")
        blob_service_client = get_blob_service_client()
        container_client = blob_service_client.get_container_client(selected_container)

        with open(source_file_path, "rb") as data:
            blob_client = container_client.get_blob_client(blob_name)
            blob_client.upload_blob(data)
            print(f"Blob with content derived from source '{source_file_path}' has been uploaded the "
                  f"following container: '{selected_container}'")


def download_blob(destination_file_path):
    selected_blob, container_client = choose_blob()

    if selected_blob and container_client:
        with open(destination_file_path, "wb") as file:
            blob_client = container_client.get_blob_client(selected_blob)
            blob_data = blob_client.download_blob()
            file.write(blob_data.readall())
            print(f"Blob with name '{selected_blob.name}' and size {selected_blob.size} bytes has been downloaded.\n")


def delete_blob():
    selected_blob, container_client = choose_blob()

    if selected_blob and container_client:
        blob_client = container_client.get_blob_client(selected_blob)
        blob_client.delete_blob()
        print(f"Blob with name '{selected_blob.name}' has been deleted.\n")


def main():
    validate_connection_string()
    print_menu()

    while True:
        choice = input("Enter your choice (0-7): \n\n")

        if choice == "1":
            print("\n")
            container_name = input("Enter desired container name: \n\n")
            create_container(container_name)
            back_to_menu_prompt()

        elif choice == "2":
            print("\n")
            list_containers(True)
            back_to_menu_prompt()

        elif choice == "3":
            print("\n")
            delete_container()
            back_to_menu_prompt()

        elif choice == "4":
            print("\n")
            upload_blob()
            back_to_menu_prompt()

        elif choice == "5":
            print("\n")
            list_blobs()
            back_to_menu_prompt()

        elif choice == "6":
            print("\n")
            destination_file_path = input("Enter destination file path: \n\n")
            download_blob(destination_file_path)
            back_to_menu_prompt()

        elif choice == "7":
            print("\n")
            delete_blob()
            back_to_menu_prompt()

        elif choice == "0":
            print("\n")
            break

        else:
            print("Invalid choice. Please enter a number between 0 and 7.\n\n")


def back_to_menu_prompt():
    while True:
        choice = input("\nBack to menu? Type 'y'\n")
        if choice == "y":
            print_menu()
            break


def validate_connection_string():
    if connection_string == "PLACEHOLDER":
        print(
            "The global variable named 'connection_string' must be replaced with the actual azure storage account "
            "connection string")
        exit(-1)


def print_menu():
    print("\n\n\nAzure Storage Blobs:")
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
