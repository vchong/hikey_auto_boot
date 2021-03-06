#!/usr/bin/env python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser

import sys

# Local imports
import cfg
import hab

################################################################################
# Argument parser
################################################################################
def get_parser():
    """ Takes care of script argument parsing. """
    parser = ArgumentParser(description='Script used to flash HiKey 620 \
            automatically')

    parser.add_argument('-v', required=False, action="store_true", \
            default=False, \
            help='Output some verbose debugging info')

    parser.add_argument('--project', required=False, action="store_true", \
            default=False, \
            help='Full path to the repo project making the HiKey build')

    parser.add_argument('-c', '--config', required=False, action="store", \
            default=None, \
            help='hab config file to use [default: <hikey_flash_cfg.yaml>]')

    return parser

################################################################################
# Main function
################################################################################
def main(argv):
    print("HiKey auto OP-TEE xtest")

    parser = get_parser()
    cfg.args = parser.parse_args()

    h = hab.HiKeyAutoBoard()

    flash_config = "hikey_flash_cfg.yaml"
    if cfg.args.config:
        flash_config = cfg.args.config

    h.run_test(flash_config)

if __name__ == "__main__":
    main(sys.argv)
