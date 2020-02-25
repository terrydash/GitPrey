#!/usr/bin/env python

try:
    from colorama import init, Fore
except ImportError:
    print("[!]Error: You have to install colorama module.")
    exit()

import logging

init(autoreset=True)

logger = logging.getLogger('')
logger.setLevel(logging.DEBUG)
file_handle = logging.FileHandler('GitPrey-info.log')
file_handle2 = logging.FileHandler('GitPrey-debug.log')
file_handle.setLevel(logging.INFO)
file_handle2.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(message)s')
file_handle.setFormatter(formatter)
file_handle2.setFormatter(formatter)
logger.addHandler(file_handle)
logger.addHandler(file_handle2)


def error_print(string):
    # Print error information with red color
    print(Fore.RED + string)
    logger.error(string)


def info_print(string):
    # Print information with green color
    print(Fore.GREEN + string)
    logger.info(string)


def debug_print(string):
    # Print information with green color
    print(Fore.YELLOW + string)
    logger.debug(string)


def project_print(string):
    # Print project information with deep green color
    print(Fore.CYAN + string)
    logger.info(string)


def file_print(string):
    # Print file url with yellow color
    print(Fore.YELLOW + string)
    logger.info(string)


def code_print(string):
    # Print code line with white color
    print(Fore.WHITE + string)
    logger.info(string)


if __name__ == "__main__":
    pass
