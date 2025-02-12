import json
import os
import re

import tools.display_tools as c


def interpretAsJson(jsonString: str) -> dict:
    try:
        return json.loads(jsonString)
    except json.decoder.JSONDecodeError:
        c.error(f"Invalid JSON")
        exit(os.EX_DATAERR)


def replaceMustaches(template: str, data: dict[str, str]) -> str:
    def replacer(match):
        key = match.group(1)
        return str(data.get(key, '##NOTFOUND##'))

    return re.sub('{{(.*?)}}', replacer, template)
