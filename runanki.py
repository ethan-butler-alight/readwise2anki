#!usr/bin/env python3
# Copyright: Ankitects Pty Ltd and contributors
# License: GNU AGPL, version 3 or later; https://www.gnu.org/licenses/agpl.html
import os
import aqt

if not os.environ.get("ANKI_IMPORT_ONLY"):
    aqt.run()
