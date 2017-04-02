""""mod: 'headlamp.get'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Handling api by UUID

"""

import json
import base64
import requests

from headlamp import common

__all__ = (
    'uuid',
    'username',
    'user_history',
    'user_profile',
    'user_image')


def uuid(username):
    """Get UUID from username"""
    r = requests.get(
        common.MOJANG_API + '/users/profiles/minecraft/' + username)
    if r.status_code is not 200:
        return r.status_code
    return r.json()['id']


def username(uuid):
    """Get username from UUID."""
    r = user_profile(uuid)
    if not isinstance(r, dict):
        return r
    return r['name']


def user_history(uuid):
    """Get user history by uuid"""
    r = requests.get(
        common.MOJANG_API + '/user/profiles/' + uuid + '/names')
    if r.status_code is not 200:
        return r.status_code
    return r.json()


def user_profile(uuid):
    """Get user profile by uuid"""
    r = requests.get(
        common.MOJANG_SESSION + '/session/minecraft/profile/' + uuid)
    if r.status_code is not 200:
        return r.status_code
    return r.json()


def user_image(uuid):
    """Get user image url by uuid"""
    r = user_profile(uuid)
    if not isinstance(r, dict):
        return r
    properties = r['properties'][0]
    if properties is False:
        return properties
    user_data = json.loads(
        base64.b64decode(properties['value']).decode("utf-8"))
    return user_data['textures']['SKIN']['url']
