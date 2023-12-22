# Azure Blob Storage Python CLI App

Command Line Interface application for manipulating Blob Storage using Azure SDK for Python

## Requirements

* x86-64
* Linux/Unix
* [Python 3](https://www.python.org/downloads/)


## Startup

The script "up" provisions Azure resources either via Terraform or Bicep:
```
sh up.sh terraform -> init, plan & apply
sh up.sh bicep -> compiles & executes ARM template
```

## Run

The script "run" starts the event-loop of our CLI application:
```
python main.py
```


## Shutdown

The script "down" removes provisioned Azure resources, either via Terraform or Bicep:
```
sh down.sh terraform -> terraform destroy
sh down.sh az -> az group delete
```
