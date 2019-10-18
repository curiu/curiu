# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: 2019 The curiu authors
#
# SPDX-License-Identifier: LicenseRef-ISC-curiu


def main(args=None):
    from conda.cli import main as conda_cli_main

    return conda_cli_main(args)
