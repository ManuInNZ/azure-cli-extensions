# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def create_logicapp(cmd, client, resource_group_name, workflow_name, location=None, tags=None):
    raise CLIError('TODO: Implement `logicapp create`')


def list_logicapp(cmd, client, resource_group_name=None):
    raise CLIError('TODO: Implement `logicapp list`')


def update_logicapp(cmd, instance, tags=None):
    with cmd.update_context(instance) as c:
        c.set_param('tags', tags)
    return instance