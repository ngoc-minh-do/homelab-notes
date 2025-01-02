#!/usr/bin/env python3

import base64, datetime, json, requests, sys
from Crypto.Cipher import AES
from Crypto.Hash import CMAC

def main():
    try:
        command = sys.argv[1]
        api_key = sys.argv[2]
        uuid = sys.argv[3]
        secret_key = sys.argv[4]
    except IndexError:
        print("Usage: sesame <lock|unlock|toggle> <api_key> <uuid> <secret>")
        sys.exit(1)

    if command == "lock":
        cmd = 82
    elif command == "unlock":
        cmd = 83
    else:
        cmd = 88

    history = 'Python'
    base64_history = base64.b64encode(bytes(history, 'utf-8')).decode()

    ts = int(datetime.datetime.now().timestamp())
    message = ts.to_bytes(4, byteorder='little')
    message = message.hex()[2:8]

    cmac = CMAC.new(bytes.fromhex(secret_key), ciphermod=AES)
    cmac.update(bytes.fromhex(message))
    sign = cmac.hexdigest()

    url = f'https://app.candyhouse.co/api/sesame2/{uuid}/cmd'
    headers = { "x-api-key": api_key }
    body = {
        "cmd": cmd,
        "history": base64_history,
        "sign": sign
    }

    try:
        res = requests.post(url, json.dumps(body), headers=headers)
        print(res.status_code, res.text)
    except Exception as error:
        print("An exception occurred:", error)

if __name__ == "__main__":
    main()