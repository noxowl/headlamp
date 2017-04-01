""""mod: 'headlamp.common'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Define common info, common function for mojang api

"""

import os
import json
import base64
import requests

from pathlib import Path


__all__ = ('MOJANG_STATUS', 'MOJANG_API', 'MOJANG_SESSION', 'get_status', 'decode_base64')

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


with (Path(__location__, 'config.json')).open('r') as f:
	conf = json.load(f)


MOJANG_STATUS = conf['mojang_status']
MOJANG_API = conf['mojang_api']
MOJANG_SESSION = conf['mojang_session']


def get_status():
	"""Get mojang api server status"""
	r = requests.get(MOJANG_STATUS + '/check')
	if r.status_code is not 200:
		return False
	status = {}
	for s in r.json():
		status.update(s)
	return status


def decode_base64(value):
	return base64.b64decode(value)