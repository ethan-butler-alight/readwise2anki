#!usr/bin/env python3
# Copyright: Ankitects Pty Ltd and contributors
# License: GNU AGPL, version 3 or later; https://www.gnu.org/licenses/agpl.html
# Found and adapted from: https://www.youtube.com/watch?v=c1BBPiN5ZKA&t=10s

import os
import aqt

if not os.environ.get("ANKI_IMPORT_ONLY"):
    aqt.run()
    