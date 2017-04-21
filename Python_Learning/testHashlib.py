#-*- coding:utf-8 -*-
import hashlib

import hashlib
m = hashlib.md5()
m.update("Nobody inspects")
m.update(" the spammish repetition")
print m.digest()+'\n'
print m.hexdigest()

print m.digest_size
print m.block_size
n = m.copy()
print n.hexdigest()


import hmac

HMC = hmac.new('')
HMC.update("Nobody inspects")
HMC.update(" the spammish repetition")
print HMC.digest()+'\n'
print HMC.hexdigest()