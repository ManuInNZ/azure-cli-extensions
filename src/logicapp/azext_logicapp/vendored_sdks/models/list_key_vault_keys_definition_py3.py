# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ListKeyVaultKeysDefinition(Model):
    """The list key vault keys definition.

    All required parameters must be populated in order to send to Azure.

    :param key_vault: Required. The key vault reference.
    :type key_vault: ~azure.mgmt.logic.models.KeyVaultReference
    :param skip_token: The skip token.
    :type skip_token: str
    """

    _validation = {
        'key_vault': {'required': True},
    }

    _attribute_map = {
        'key_vault': {'key': 'keyVault', 'type': 'KeyVaultReference'},
        'skip_token': {'key': 'skipToken', 'type': 'str'},
    }

    def __init__(self, *, key_vault, skip_token: str=None, **kwargs) -> None:
        super(ListKeyVaultKeysDefinition, self).__init__(**kwargs)
        self.key_vault = key_vault
        self.skip_token = skip_token
