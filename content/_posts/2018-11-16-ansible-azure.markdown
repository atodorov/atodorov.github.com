Title: How to authenticate Ansible with Azure
date: 2018-11-16 09:30
comments: true
Tags: fedora.planet
og_image: images/ansible-azure.png
twitter_image: images/ansible-azure.png

As I am working on cloud image testing for
[Composer](http://weldr.io) I need to create scripts that can provision
virtual machines in multiple cloud platforms. Instead of using their API directly
I can reuse the vast majority of
[Ansible cloud modules](https://docs.ansible.com/ansible/2.6/modules/list_of_cloud_modules.html).

There are modules for Azure of course however they poorly explain
how to configure authentication. Ansible docs say:

    For authentication with Azure you can pass parameters,
    set environment variables or use a profile stored in
    ~/.azure/credentials. Authentication is possible using
    a service principal or Active Directory user. To authenticate
    via service principal, pass subscription_id, client_id, secret
    and tenant or set environment variables AZURE_SUBSCRIPTION_ID,
    AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.

This is how you go about configuring these variables.

First install `azure-cli` tools:

    :::
    # rpm --import https://packages.microsoft.com/keys/microsoft.asc
    # echo -e "[azure-cli]\nname=Azure CLI\nbaseurl=https://packages.microsoft.com/yumrepos/azure-cli\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/azure-cli.repo
    # yum install azure-cli

then login:

    :::
    $ az login
    To sign in, use a web browser to open the page
    https://microsoft.com/devicelogin and enter the code XXXXXXXXX to authenticate.
    [
      {
        "cloudName": "AzureCloud",
        "id": "8d026bb1-.....",
        "isDefault": true,
        "name": "Pay-as-you-go",
        "state": "Enabled",
        "tenantId": "9f340302-......",
        "user": {
          "name": "atodorov@....",
          "type": "user"
        }
      }
    ]


Here `id==AZURE_SUBSCRITION_ID` and `tenantId==AZURE_TENANT`! Next you need
client id and secret before Ansible can be able to authenticate with Azure!
In fact you need to register an Active Directory Service Principal
which will authenticate with the Azure REST API, in other words when
executing Ansible commands in your shell (or via test script) that will be
treated as an application which must be allowed access to Azure resources.

From the command line this is done by:

    :::
    $ az ad sp create-for-rbac --name http://ansible-atodorov --role owner --scopes "/subscriptions/$ANSIBLE_SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP_NAME"
    {
      "appId": "f86af23a-......",
      "displayName": "ansible-atodorov",
      "name": "http://ansible-atodorov",
      "password": "37d908aa-.......",
      "tenant": "9f340302-........."
    }


Note: resource group is an Azure term, you can find more about it
[here](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-overview).

In this example `appId==ANSIBLE_CLIENT_ID` and `password==ANSIBLE_SECRET`. After exporting
these environment variables you should be able to use Ansible to upload blobs to
Azure or start virtual machines:

    :::
    $ export AZURE_SUBSCRIPTION_ID=8d026bb1-.....
    $ export AZURE_TENANT=9f340302-..............
    $ export AZURE_CLIENT_ID=f86af23a-...........
    $ export AZURE_SECRET=37d908aa-..............
    
    $ ansible localhost -m azure_rm_storageblob -a "resource_group=composer storage_account_name=composerredhat container=composerredhat blob=linux.vhd src=linux.vhd blob_type=page"



Thanks for reading and happy testing!
