# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType
from azext_logicapp._client_factory import cf_logicapp


def load_command_table(self, _):

    logicapp_sdk = CliCommandType(
        operations_tmpl='azext_logicapp.vendored_sdks.operations#WorkflowRunsOperations.{}',
        client_factory=cf_logicapp)


    with self.command_group('logicapp', logicapp_sdk, client_factory=cf_logicapp) as g:
        g.custom_command('create', 'create_logicapp')
        g.command('delete', 'delete')
        g.custom_command('list', 'list_logicapp')
        g.show_command('show', 'get')
        g.generic_update_command('update', setter_name='update', custom_func_name='update_logicapp')


    with self.command_group('logicapp', is_preview=True):
        pass

