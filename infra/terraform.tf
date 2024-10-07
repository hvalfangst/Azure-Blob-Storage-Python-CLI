provider "azurerm" {
  features {}
  tenant_id       = var.tenant_id
  subscription_id = var.subscription_id
}

resource "azurerm_resource_group" "hvalfangst" {
  location = var.location
  name     = var.resource_group_name
}

resource "azurerm_storage_account" "hvalfangst" {
  account_replication_type = "LRS"
  account_tier             = "Standard"
  location                 = azurerm_resource_group.hvalfangst.location
  name                     = var.storage_account_name
  resource_group_name      = azurerm_resource_group.hvalfangst.name
}

resource "azurerm_storage_container" "hvalfangst" {
  name                 = var.storage_container_name
  storage_account_name = azurerm_storage_account.hvalfangst.name
}