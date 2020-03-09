#!/usr/bin/env python
# This file is part of Xpra.
# Copyright (C) 2020 Antoine Martin <antoine@xpra.org>
# Xpra is released under the terms of the GNU GPL v2, or, at your option, any
# later version. See the file COPYING for details.

import unittest

from xpra.util import AdHocStruct
from xpra.server.window.video_scoring import get_quality_score, get_speed_score


class TestVideoScoring(unittest.TestCase):

    def test_quality_score(self):
        csc_spec = AdHocStruct()
        csc_spec.quality = 50
        encoder_spec = AdHocStruct()
        encoder_spec.quality = 50
        encoder_spec.has_lossless_mode = False
        s1 = get_quality_score("YUV420P", csc_spec, encoder_spec, (1, 1))
        s2 = get_quality_score("BGRA", csc_spec, encoder_spec, (1, 1))
        assert s2>s1
        s3 = get_quality_score("YUV420P", csc_spec, encoder_spec, (1, 1), min_quality=50)
        assert s3<s1
        s4 = get_quality_score("YUV420P", csc_spec, encoder_spec, (2, 2))
        assert s4>s2

    def test_speed_score(self):
        csc_spec = AdHocStruct()
        csc_spec.speed = 50
        encoder_spec = AdHocStruct()
        encoder_spec.speed = 50
        encoder_spec.has_lossless_mode = True
        s1 = get_speed_score("YUV420P", csc_spec, encoder_spec, (1, 1))
        s2 = get_speed_score("YUV420P", csc_spec, encoder_spec, (2, 2))
        assert s2>s1
        s3 = get_speed_score("YUV420P", csc_spec, encoder_spec, (1, 1), min_speed=60)
        assert s3<s2


def main():
    unittest.main()

if __name__ == '__main__':
    main()
