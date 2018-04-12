#!/usr/local/bin/python3

# Copyright: (c) 2018, Shihao Li <shli@thoughtworks.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = '''
---
module: welcome

author: Shihao Li <shli@thoughtworks.com>

short_description: Print welcome message.
'''

EXAMPLES = '''
- name: Welcome to Ansible
  welcome:
    user: Shihao Li
'''

RETURN = '''
welcome:
    description: welcome message
    returned: success
    type: string
    sample: Welcome to ANSIBLE, Shihao Li!
'''

import getpass

from ansible.module_utils.basic import AnsibleModule

MODULE_ARGS = dict(
    user=dict(type='str', required=False)
)


def build_welcome_message(user):
    return 'Welcome to ANSIBLE, {}!'.format(user)


if __name__ == '__main__':
    module = AnsibleModule(argument_spec=MODULE_ARGS)
    user = module['user'] if module['user'] else getpass.getuser()

    message = build_welcome_message(user)

    module.exit_json(changed=False, meta=dict(message=message))
