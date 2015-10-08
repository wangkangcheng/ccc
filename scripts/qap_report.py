#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: oesteban
# @Date:   2015-10-08 13:07:21
# @Last Modified by:   oesteban
# @Last Modified time: 2015-10-08 13:21:30

if __name__ == "__main__":
    import argparse
    import qap.viz.reports as qvr

    parser = argparse.ArgumentParser()
    req = parser.add_argument_group("Required Inputs")
    req.add_argument('-i', '--input_csv', type=str, required=True,
                     help='filepath to csv file generated by qap')

    req.add_argument(
        '-m', '--qap_mode', type=str, help='report type'
        choices=['anatomical', 'functional-temporal', 'functional-spatial'])

    args = parser.parse_args()

    csv_file = args.input_csv
    qap_mode = args.qap_mode

    # infer report type from filename
    if qap_mode is None:
        qap_mode = 'anatomical'
        if 'func' in csv_file:
            qap_mode = 'functional-spatial' if 'spat' in csv_file else \
                'functional-temporal'

    if 'anatomical' in qap_mode:
        out_file = qvr.report_anatomical(csv_file)
    elif 'functional-temporal' in qap_mode:
        out_file = qvr.report_func_temporal(csv_file)
    elif 'functional-spatial' in qap_mode:
        out_file = qvr.report_func_spatial(csv_file)
    else:
        raise RuntimeError('Report type is unknown')

    print 'Written output file: ', out_file
