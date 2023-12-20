# Azure Blob Storage Python CLI App

Command Line Interface application for manipulating Blob Storage using Azure SDK for Python

## Requirements

* x86-64
* Linux/Unix
* [Python 3](https://www.python.org/downloads/)


## Startup

The script "up" provisions Azure resources:
```
1. terraform init
2. terraform plan
3. terraform apply
```

## Run

The script "run" starts the event-loop of our CLI application:
```
python main.py
```


## Shutdown

The script "down" removes provisioned Azure resources:
```
terraform destroy
```
