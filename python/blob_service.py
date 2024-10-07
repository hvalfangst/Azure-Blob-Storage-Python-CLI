from azure.storage.blob import BlobServiceClient

connection_string = "[KELLERESSEN_70]"


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

        try:
            container_index = int(input("Choose container: \n\n"))
            container_index -= 1

            if 0 <= container_index < len(container_names):
                return container_names[container_index]
            else:
                print("Invalid index\n\n")
                return None
        except ValueError:
            print("Please enter a valid number.\n\n")
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

            try:
                blob_index = int(input("Choose Blob: \n\n"))
                blob_index -= 1

                if 0 <= blob_index < len(blobs):
                    selected_blob = blobs[blob_index]
                    return selected_blob, container_client
                else:
                    print("Invalid Blob index.\n\n")
                    return None, None
            except ValueError:
                print("Please enter a valid number.\n\n")
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

        try:
            with open(source_file_path, "rb") as data:
                blob_client = container_client.get_blob_client(blob_name)
                blob_client.upload_blob(data)
                print(f"Blob '{blob_name}' has been uploaded to container '{selected_container}'.\n")
        except FileNotFoundError:
            print(f"The file '{source_file_path}' was not found.\n")
        except Exception as e:
            print(f"An error occurred: {e}\n")


def download_blob(destination_file_path):
    selected_blob, container_client = choose_blob()

    if selected_blob and container_client:
        try:
            with open(destination_file_path, "wb") as file:
                blob_client = container_client.get_blob_client(selected_blob)
                blob_data = blob_client.download_blob()
                file.write(blob_data.readall())
                print(
                    f"Blob '{selected_blob.name}' ({selected_blob.size} bytes) has been downloaded to '{destination_file_path}'.\n")
        except Exception as e:
            print(f"An error occurred while downloading the blob: {e}\n")


def delete_blob():
    selected_blob, container_client = choose_blob()

    if selected_blob and container_client:
        try:
            blob_client = container_client.get_blob_client(selected_blob)
            blob_client.delete_blob()
            print(f"Blob '{selected_blob.name}' has been deleted.\n")
        except Exception as e:
            print(f"An error occurred while deleting the blob: {e}\n")


def validate_connection_string():
    if connection_string == "[KELLERESSEN_70]":
        print(
            "The global variable 'connection_string' must be replaced with the actual Azure Storage account connection string.")
        exit(-1)
