decodeHelp = """\n```
# $decrypt
Usage:
    $decrypt (type) (input)
Args:
+---------+---------------+--------------------------------------------------------+
| Command |     usage     |                      example                           |
+---------+---------------+--------------------------------------------------------+
| hex     | Hex decode    | $decrypt hex [-s pretext] [pretext]41 | will return "A"|
| b64     | base64 decode | $decrypt b64 QUJDCg== | will return "ABC"              |
| url     | url decode    | $decrypt url alert%281%29 | will return "alert(1)"     |
| rot13   | rot13 decode  | $decrypt rot13 N | will return "A"                     |
+---------+---------------+--------------------------------------------------------+
```"""


encodeHelp = """\n```
# $encrypt
Usage:
    $encrypt (type) (input)
Args:
+---------+---------------+--------------------------------------------------------+
| Command |     usage     |                      example                           |
+---------+---------------+--------------------------------------------------------+
| hex     | Hex encode    | $encrypt hex [-s pretext] A | will return "[pretext]41"|
| b64     | base64 encode | $encrypt b64 ABC | will return "QUJDCg=="              |
| url     | url encode    | $encrypt url alert(1)  | will return "alert%281%29     |
| rot13   | rot13 encode  | $encrypt rot13 A | will return "N"                     |
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
