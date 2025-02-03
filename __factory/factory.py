import os
import re
import json
import sys


def readFile(filePath: str) -> str:
    try:
        with open(filePath, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"{sys.argv[0]} : ERROR - File not found", file=sys.stderr)
        exit(os.EX_DATAERR)


def interpretAsJson(jsonString: str) -> dict:
    try:
        return json.loads(jsonString)
    except json.decoder.JSONDecodeError:
        print(f"{sys.argv[0]} : ERROR - Invalid JSON", file=sys.stderr)
        exit(os.EX_DATAERR)


def saveFile(filePath: str, content: str) -> None:
    try:
        with open(filePath, 'w', encoding='utf-8') as file:
            file.write(content)
    except FileNotFoundError:
        print(f"{sys.argv[0]} : ERROR - File not found", file=sys.stderr)
        exit(os.EX_DATAERR)
    except IOError as e:
        print(f"{sys.argv[0]} : ERROR - Unable to edit '{filePath}': {e}", file=sys.stderr)
        exit(os.EX_DATAERR)


def replacePlaceHolders(template: str, data: dict[str, str]) -> str:
    def replacer(match):
        key = match.group(1)
        return str(data.get(key, '##NOTFOUND##'))

    return re.sub('{{(.*?)}}', replacer, template)


def main(templatePath: str, dataPath: str, outputPath: str) -> None:
    templateStr = readFile(templatePath)
    dataDict = interpretAsJson(readFile(dataPath))
    output = replacePlaceHolders(templateStr, dataDict)
    saveFile(outputPath, output)
    print(f"{sys.argv[0]} : INFO - Processed template saved to {outputPath}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <template_path> <data_path> <output_path>")
        exit(os.EX_NOINPUT)

    templateFile = sys.argv[1]
    dataFile = sys.argv[2]
    outputFile = sys.argv[3]
    main(templateFile, dataFile, outputFile)
