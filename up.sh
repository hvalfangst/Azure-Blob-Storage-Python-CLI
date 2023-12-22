#!/bin/sh

# Exits immediately if a command exits with a non-zero status
set -e

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <terraform|bicep>"
    exit 1
fi

case "$1" in
    "terraform")
        echo "Executing Terraform script..."
        terraform init;
        terraform plan;
        terraform apply;
        ;;
    "bicep")
        echo "Deploying ARM template via Bicep"
        az group create --name hvalfangstresourcegroup --location "Norway East";
        az bicep build --file main.bicep;
        az deployment group create --resource-group hvalfangstresourcegroup --template-file main.json;
        ;;
    *)
        echo "Invalid argument. Supported options: terraform, bicep"
        exit 1
        ;;
esac