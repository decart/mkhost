from __future__ import print_function, unicode_literals

import os

from PyInquirer import style_from_dict, Token, prompt, Separator
from difflib import SequenceMatcher

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})

def guess_init_dir(init_dirs, vhost):
    closest = ''
    max_ratio = 0.5

    for dir_name in init_dirs:
        ratio = SequenceMatcher(None, dir_name, vhost).ratio()
        if ratio < 0.5: continue

        if ratio > max_ratio:
            max_ratio = ratio
            closest = dir_name

    return closest


def list_root_dirs(root_path, vhost):
    dirs = []
    for item in os.listdir(root_path):
        if os.path.isdir(root_path + item):
            dirs.append(item)

    first = guess_init_dir(dirs, vhost)
    dirs.pop(dirs.index(first))
    dirs.insert(0, first)

    return dirs

def guess_full_path_root(root_path, init_dir):
    full = root_path + init_dir
    public = full + '/public'

    return public if os.path.isdir(public) else full

def prompt_vhost(cert_path, key_path, root_path):
    questions = [
        {
            'type': 'input',
            'name': 'vhost',
            'message': 'Virtual host:'
        },
        {
            'type': 'list',
            'name': 'initDir',
            'message': 'Select a virtual host dir',
            'choices': lambda answers: list_root_dirs(root_path, answers['vhost'])
        },
        {
            'type': 'input',
            'name': 'rootDir',
            'message': 'Confirm full path to root dir:',
            'default': lambda answers: guess_full_path_root(root_path, answers['initDir'])
        },
        {
            'type': 'confirm',
            'name': 'needSSL',
            'message': 'You need SSL?',
            'default': True
        },
        {
            'type': 'input',
            'name': 'sslCert',
            'message': 'Path to ssl certificate:',
            'when': lambda answers: answers['needSSL'],
            'default': cert_path
        },
        {
            'type': 'input',
            'name': 'sslKey',
            'message': 'Path to ssl certificate key:',
            'when': lambda answers: answers['needSSL'],
            'default': key_path
        }
    ]

    return prompt(questions, style=style)