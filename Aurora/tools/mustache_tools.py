import json
import os
import re

import Aurora.tools.display_tools as c
from Aurora.tools.__global__ import ifttt


def interpretAsJson(jsonString: str) -> dict:
    try:
        return json.loads(jsonString)
    except json.decoder.JSONDecodeError as error:
        c.error(f"Invalid JSON : {error.msg}")
        exit(os.EX_DATAERR)


def removeCommentaries(template: str) -> str:
    return re.sub(
        "//.*?//",
        lambda _: "",
        template
    )


def replaceConditionals(template: str, data: dict[str, bool]) -> str:
    return re.sub(
        "\\[\\[(.+?)\\?(.+?):(.+?)]]",
        lambda m: str(
            ifttt(
                bool(data.get(m.group(1), False)),
                m.group(2),
                m.group(3)
            )
        ),
        template
    )


def removeInvalidConditionals(template: str) -> str:
    return re.sub(
        "\\[\\[.*?]]",
        lambda m: "##INVALID##",
        template
    )


def replaceMustaches(template: str, data: dict[str, str]) -> str:
    return re.sub(
        '\\{\\{([^:?]+?)}}',
        lambda m: data.get(m.group(1), "##NOTFOUND##"),
        template
    )
