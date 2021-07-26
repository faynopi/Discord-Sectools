from libs.cfg import get_config


decodeHelp = """\n```
# $decode
Usage:
    $decode (type) [-s to set a prefix for encoded hex like 0x or \\x or ...] (input)

Args:
+---------+---------------+--------------------------------------------------------+
| Command |     usage     |                      example                           |
+---------+---------------+--------------------------------------------------------+
| hex     | Hex decode    | $decode hex [-s pretext] [pretext]41 | will return "A" |
| b64     | base64 decode | $decode b64 QUJDCg== | will return "ABC"               |
| url     | url decode    | $decode url alert%281%29 | will return "alert(1)"      |
| rot13   | rot13 decode  | $decode rot13 N | will return "A"                      |
+---------+---------------+--------------------------------------------------------+
```"""


encodeHelp = """\n```
# $encode
Usage:
    $encode (type) [-s to set a prefix for hex encode like 0x or \\x or ...] (input)

Args:
+---------+---------------+--------------------------------------------------------+
| Command |     usage     |                      example                           |
+---------+---------------+--------------------------------------------------------+
| hex     | Hex encode    | $encode hex [-s pretext] A | will return "[pretext]41" |
| b64     | base64 encode | $encode b64 ABC | will return "QUJDCg=="               |
| url     | url encode    | $encode url alert(1)  | will return "alert%281%29      |
| rot13   | rot13 encode  | $encode rot13 A | will return "N"                      |
+---------+---------------+--------------------------------------------------------+
```"""

hashidHelp = """\n```
# $hashid
Usage:
    $hashid (input)

Args:
+-----------------+------------------------------------------------------+
|      usage      |                      example                         |
+-----------------+------------------------------------------------------+
| Hash identifier | $hashid Hash                                         |
+-----------------+------------------------------------------------------+
```"""

hashesHelp = """\n```
# $hashit
** NOTE: -x is not supported yet. **

Usage:
    $hashit (type) [-x for texts that are not printable hex them and pass -x to unhex them and then hash them] (input)

Args:
+-----------+---------------------------+------------------------------------+
| Command   |          Usage            |             example                |
+-----------+---------------------------+------------------------------------+
| shake_256 | shake_256 [-x] TextToHash | $encrypt shake_256 [-x] TextToHash |
| shake_128 | shake_128 [-x] TextToHash | $encrypt shake_128 [-x] TextToHash |
| md5       | md5 [-x] TextToHash       | $encrypt md5 [-x] TextToHash       |
| sha512    | sha512 [-x] TextToHash    | $encrypt sha512 [-x] TextToHash    |
| sha3_224  | sha3_224 [-x] TextToHash  | $encrypt sha3_224 [-x] TextToHash  |
| sha3_256  | sha3_256 [-x] TextToHash  | $encrypt sha3_256 [-x] TextToHash  |
| sha3_512  | sha3_512 [-x] TextToHash  | $encrypt sha3_512 [-x] TextToHash  |
| sha384    | sha384 [-x] TextToHash    | $encrypt sha384 [-x] TextToHash    |
| sha3_384  | sha3_384 [-x] TextToHash  | $encrypt sha3_384 [-x] TextToHash  |
| sha1      | sha1 [-x] TextToHash      | $encrypt sha1 [-x] TextToHash      |
| blake2b   | blake2b [-x] TextToHash   | $encrypt blake2b [-x] TextToHash   |
| sha256    | sha256 [-x] TextToHash    | $encrypt sha256 [-x] TextToHash    |
| sha224    | sha224 [-x] TextToHash    | $encrypt sha224 [-x] TextToHash    |
| blake2s   | blake2s [-x] TextToHash   | $encrypt blake2s [-x] TextToHash   |
+-----------+--------------+------------+------------------------------------+
```"""

r3vHelp = f"""\n```
# $r3v
** NOTE: default shell is "{get_config("defaultShell")}" **

Usage:
    $r3v (cmd)
    
Args:
+---------+---------------------------+---------------------------------------------------------+
| Command |         Usage             |                      Example                            |
+---------+---------------------------+---------------------------------------------------------+
| list    | list all of the revShells | $r3v list                                               |
| search  | search with keyword       | $r3v search (keyword)                                   |
| os      | Search operating systems  | $r3v os [windows, linux, mac]                           |
| gen     | Create reverse shell      | $r3v gen (name *required)                               |
|         |                           |     (ip) (port) (shell # this arg isnt required)        |
+---------+---------------------------+---------------------------------------------------------+
```
"""

