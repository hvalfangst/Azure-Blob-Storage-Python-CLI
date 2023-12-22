#!/bin/sh

# Exits immediately if a command exits with a non-zero status
set -e

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <terraform|az>"
    exit 1
fi

case "$1" in
    "terraform")
        echo "Destroying resources..."
        terraform destroy
        ;;
    "az")
        echo "Deleting resource group"
        az group delete --name hvalfangstresourcegroup --yes --no-wait
        ;;
    *)
        echo "Invalid argument. Supported options: terraform, az"
        exit 1
        ;;
esac