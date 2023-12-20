provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "hvalfangst" {
  location = "Norway East"
  name = "hvalfangstresourcegroup"
}

resource "azurerm_storage_account" "hvalfangst" {
  account_replication_type = "LRS"
  account_tier = "Standard"
  location = azurerm_resource_group.hvalfangst.location
  name = "hvalfangststorageacount"
  resource_group_name = azurerm_resource_group.hvalfangst.name
}

resource "azurerm_storage_container" "hvalfangst" {
  name = "hvalfangststorageaccountcontainer"
  storage_account_name = azurerm_storage_account.hvalfangst.name
}