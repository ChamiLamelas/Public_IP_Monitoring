"""
Script for getting public IP address and saving it to a CSV file.

Chami Lamelas
Jan 2023
"""

import os
from datetime import datetime

import requests
from pytz import timezone

SAVE_FILE_NAME = 'ip_monitoring.csv'

US_EST_TIMEZONE = timezone('EST')

PUBLIC_IP_ENDPOINT = 'https://api.ipify.org'


def check_savefile():
    if not os.path.isfile(SAVE_FILE_NAME):
        with open(SAVE_FILE_NAME, mode='w', encoding='utf-8') as f:
            f.write('Datetime (US EST),IP Address\n')


def get_public_ip():
    response = requests.get(PUBLIC_IP_ENDPOINT)
    if not response.ok:
        print('Public IP address lookup failed.')
        exit(1)
    return response.content.decode(response.encoding)


def save_public_ip(public_ip):
    dt = datetime.now(US_EST_TIMEZONE).strftime("%Y-%m-%d %H:%M:%S")
    print(f'Saved {public_ip} at {dt}.')
    with open(SAVE_FILE_NAME, mode='a+', encoding='utf-8') as f:
        f.write(f'{dt},{public_ip}\n')


def main():
    check_savefile()
    save_public_ip(get_public_ip())


if __name__ == '__main__':
    main()
