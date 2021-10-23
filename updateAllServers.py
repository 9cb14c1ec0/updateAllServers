#!/usr/bin/python3
import os

# enter each server as a list of [address, port]
servers = [
    ['127.0.0.1', 22]
]


def main():
    for server in servers:
        command = f'ssh -p "{server[1]}" root@{server[0]} "apt update && unattended-upgrade -d | grep Setting"'
        os.system(command)


if __name__ == '__main__':
    main()
    input('Press enter to exit')
