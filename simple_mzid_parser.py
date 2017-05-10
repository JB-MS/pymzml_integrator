#!/usr/bin/env python3.4
# encoding: utf-8

import os
import sys
from pymzid.pymzid import Mzid


def main():
    '''
    Simple parser for Mzid files based on pymzl_integrator module

    © Johannes Leufken 2017

    '''
    reader = Mzid(
        sys.argv[1],
        verbose = False
    )
    data_frame = reader.peptide_df
    for seq in data_frame['seq']:
        print(seq)
    return

if __name__ == '__main__':
    main()
