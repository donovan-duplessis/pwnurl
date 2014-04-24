#!/usr/bin/env python
# -*- coding: utf-8 -*-

ADMIN = 1
USER = 2

ROLES = {ADMIN: (ADMIN, 'Administrator'), USER: (USER, 'User')}

administrators = {'Donovan du Plessis': 'donovan@verifaction.co.za'}

error_messages = {
    400: 'Bad request',
    403: 'Forbidden resource requested',
    404: [
        'Oops, page not found.', 'We\'re sorry', 'Uh Oh!', 'Nope, not here.'
    ],
    500: 'Something went wrong',
}
