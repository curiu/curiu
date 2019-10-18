# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: 2019 The curiu authors
#
# SPDX-License-Identifier: LicenseRef-ISC-curiu

from setuptools import setup
import versioneer


setup(
    cmdclass=versioneer.get_cmdclass(),
    version=versioneer.get_version(),
    # cffi_modules=['src/curiu/some_cffi_module.py:ffi'],
)
