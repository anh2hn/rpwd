#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'arvin'

from template.scanner import WFingerprint, HFingerprint, BaseScanner, FingerprintConf

# www_fingerprint = namedtuple('w_fp', ['module', 'match_type', 'fp', 'exploit'])
BASIC_FP = [
    WFingerprint('JWNR200', 0, 'Basic realm="."JWNR2000', []),
    WFingerprint('DVG1000', 1, 'Basic realm="DVG1000', []),
    WFingerprint('KWGR614', 0, 'Basic realm="KWGR614"', []),
    WFingerprint('MR814', 0, 'Basic realm="MR814"', []),
    WFingerprint('N300', 0, 'Basic realm="N300"', []),
    WFingerprint('DG834', 0, 'Basic realm="NETGEAR DG834  "', []),
    WFingerprint('DG834', 0, 'Basic realm="NETGEAR DG834 "', []),
    WFingerprint('DG834 B', 0, 'Basic realm="NETGEAR DG834 B"', []),
    WFingerprint('DG834G', 0, 'Basic realm="NETGEAR DG834G "', []),
    WFingerprint('DG834GB', 0, 'Basic realm="NETGEAR DG834GB"', []),
    WFingerprint('DG834GL', 0, 'Basic realm="NETGEAR DG834GL "', []),
    WFingerprint('DG834Nv2', 0, 'Basic realm="NETGEAR DG834Nv2"', []),
    WFingerprint('DG834PNB', 0, 'Basic realm="NETGEAR DG834PNB"', []),
    WFingerprint('DGN1000', 0, 'Basic realm="NETGEAR DGN1000 "', []),
    WFingerprint('DGN1000B', 0, 'Basic realm="NETGEAR DGN1000B"', []),
    WFingerprint('DGN2000', 0, 'Basic realm="NETGEAR DGN2000 "', []),
    WFingerprint('DGN2200', 0, 'Basic realm="NETGEAR DGN2200"', []),
    WFingerprint('DGN2200Bv3', 0, 'Basic realm="NETGEAR DGN2200Bv3"', []),
    WFingerprint('DGN2200M', 0, 'Basic realm="NETGEAR DGN2200M"', []),
    WFingerprint('DGN2200v3', 0, 'Basic realm="NETGEAR DGN2200v3"', []),
    WFingerprint('DGN3500 ', 0, 'Basic realm="NETGEAR DGN3500 "', []),
    WFingerprint('DGN3500B', 0, 'Basic realm="NETGEAR DGN3500B"', []),
    WFingerprint('DGN3500_SSH', 0, 'Basic realm="NETGEAR DGN3500_SSH "', []),
    WFingerprint('DM111PSPv2', 0, 'Basic realm="NETGEAR DM111PSPv2"', []),
    WFingerprint('JNR1010v2', 0, 'Basic realm="NETGEAR JNR1010v2"', []),
    WFingerprint('JWNR2000v2', 0, 'Basic realm="NETGEAR JWNR2000v2 "', []),
    WFingerprint('JWNR2010v5', 0, 'Basic realm="NETGEAR JWNR2010v5"', []),
    WFingerprint('R6300', 0, 'Basic realm="NETGEAR R6300"', []),
    WFingerprint('WGR614v9', 0, 'Basic realm="NETGEAR WGR614v9"', []),
    WFingerprint('WNDR3600', 0, 'Basic realm="NETGEAR WNDR3600"', []),
    WFingerprint('WNDR3700v2', 0, 'Basic realm="NETGEAR WNDR3700v2"', []),
    WFingerprint('WNDR3800', 0, 'Basic realm="NETGEAR WNDR3800"', []),
    WFingerprint('WNDR4000', 0, 'Basic realm="NETGEAR WNDR4000"', []),
    WFingerprint('WNDR4500', 0, 'Basic realm="NETGEAR WNDR4500"', []),
    WFingerprint('WNDR4500v2', 0, 'Basic realm="NETGEAR WNDR4500v2"', []),
    WFingerprint('WNR1000v3', 0, 'Basic realm="NETGEAR WNR1000v3"', []),
    WFingerprint('WNR2000v5', 0, 'Basic realm="NETGEAR WNR2000v5"', []),
    WFingerprint('WNR2020', 0, 'Basic realm="NETGEAR WNR2020"', []),
    WFingerprint('WNR3500L', 0, 'Basic realm="NETGEAR WNR3500L"', []),
    WFingerprint('WNR3500Lv2', 0, 'Basic realm="NETGEAR WNR3500Lv2"', []),
    WFingerprint('WNR612ERT', 0, 'Basic realm="NETGEAR WNR612ERT"', []),
    WFingerprint('WNR612v2', 0, 'Basic realm="NETGEAR WNR612v2"', []),
    WFingerprint('WNR614', 0, 'Basic realm="NETGEAR WNR614"', []),
    WFingerprint('WNR618', 0, 'Basic realm="NETGEAR WNR618"', []),
    WFingerprint('WPN824N', 0, 'Basic realm="NETGEAR WPN824N"', []),
    WFingerprint('XWN5001', 0, 'Basic realm="NETGEAR XWN5001"', []),
    WFingerprint('WNR2000v3', 0, 'Basic realm="NETGEAR wnr2000v3"', []),
    WFingerprint('WNR2000v4', 0, 'Basic realm="NETGEAR wnr2000v4"', []),
    WFingerprint('WNR2200', 0, 'Basic realm="NETGEAR wnr2200"', []),
    WFingerprint('WNR3500Lv1', 0, 'Basic realm="Netgear WNR3500Lv1"', []),
    WFingerprint('RP614', 0, 'Basic realm="RP614"', []),
    WFingerprint('RP614v4', 0, 'Basic realm="RP614v4"', []),
    WFingerprint('WG602V3', 0, 'Basic realm="WG602V3"', []),
    WFingerprint('WG602V4', 0, 'Basic realm="WG602V4"', []),
    WFingerprint('WGR614v6', 0, 'Basic realm="WGR614v6"', []),
    WFingerprint('WGR614v7', 0, 'Basic realm="WGR614v7"', []),
    WFingerprint('WGT624', 0, 'Basic realm="WGT624"', []),
    WFingerprint('WGT624v3', 0, 'Basic realm="WGT624v3"', []),
    WFingerprint('WNDR4500', 0, 'Basic realm="WNDR4500"', []),
    WFingerprint('WNR3500L', 0, 'Basic realm="WNR3500L"', []),
    WFingerprint('WPN824v2', 0, 'Basic realm="WPN824v2"', []),
    WFingerprint('JWNR2000', 1, 'Digest realm="NETGEAR JWNR2000', []),
    WFingerprint('JNR3000', 0, 'Basic realm="NETGEAR JNR3000"', []),
    WFingerprint('JNR3210', 0, 'Basic realm="NETGEAR JNR3210"', []),
    WFingerprint('WN1000RP', 0, 'Basic realm="NETGEAR WN1000RP"', [])
]

# http_fingerprint = namedtuple('h_fp', ['module', 'segment', 'math_type', 'fp', 'extra', 'exploit'])
HTTP_FP = [
    HFingerprint('WNR612ERT', 'TEXT', 1, '<TITLE>NETGEAR Router WNR612ERT</TITLE>', [None, None], []),
    HFingerprint('WNR612v2', 'TEXT', 1, '<TITLE>NETGEAR Router WNR612v2</TITLE>', [None, None], []),
    HFingerprint('WPN824N ', 'TEXT', 1, '<TITLE>NETGEAR Router WPN824N </TITLE>', [None, None], []),
    HFingerprint('DGN2200v2', 'TEXT', 1, '<title>NETGEAR Router DGN2200v2</title>', [None, None], []),
    HFingerprint('WNR1000v2', 'TEXT', 1, '<title>NETGEAR Router WNR1000v2 </title>', [None, None], []),
    HFingerprint('WNR2000v3', 'TEXT', 1, '<title>NETGEAR Router WNR2000v3 </title>', [None, None], []),
    HFingerprint('WNR2000v4', 'TEXT', 1, '<title>NETGEAR Router WNR2000v4</title>', [None, None], []),
    HFingerprint('WNR2000v5', 'TEXT', 1, '<title>NETGEAR Router WNR2000v5</title>', [None, None], []),
    HFingerprint('WNR2200', 'TEXT', 1, '<title>NETGEAR Router WNR2200 </title>', [None, None], []),
    HFingerprint('WNR2500', 'TEXT', 1, '<title>NETGEAR Router WNR2500</title>', [None, None], []),
    HFingerprint('WNR3500L', 'TEXT', 1, '<title>NETGEAR Router WNR3500L</title>', [None, None], []),
    HFingerprint('WNR3500Lv2', 'TEXT', 1, '<title>NETGEAR Router WNR3500Lv2</title>', [None, None], []),
]

JUMP_LIST = []


class Scanner(BaseScanner):
    prompt = 'NETGEAR Scanner'
    FINGERPRINT_DB = [
        FingerprintConf('NETGEAR', BASIC_FP, HTTP_FP),
    ]

    JUMP_FEATURES = [JUMP_LIST]
