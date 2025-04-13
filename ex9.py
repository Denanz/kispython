import re


def main(text):
    pattern = re.compile(
        r'@\"(.*?)\"\s*to\s+(\w+)|var\s+@\"(.*?)\"\s*to\s+(\w+)')
    matches = pattern.findall(text)

    result = []
    for m in matches:
        if m[0] and m[1]:
            result.append((m[1], m[0]))
        elif m[2] and m[3]:
            result.append((m[3], m[2]))
    return result