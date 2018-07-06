#!/usr/bin/env python

import random
import clam.common.oauth

ip = "127.0.0.1"
token = "1234567890"


OAUTH_ENCRYPTIONSECRET = "%032x" % random.getrandbits(128)

enc = clam.common.oauth.encrypt(OAUTH_ENCRYPTIONSECRET,token,ip)

dec,ip = clam.common.oauth.decrypt(OAUTH_ENCRYPTIONSECRET,enc)

print(dec, ip)
