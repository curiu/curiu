<!--
SPDX-FileCopyrightText: 2019 The curiu authors

SPDX-License-Identifier: LicenseRef-ISC-curiu
-->

# Contributing

- Add yourself to the [AUTHORS.md](AUTHORS.md) file.
- Autoformat new/changed code with [`black`](https://github.com/psf/black).
- Add SPDX copyright/license headers or `.license` files and check them via [`reuse lint`](https://github.com/fsfe/reuse-tool/tree/v0.5.0#usage).
- Add informative commit messages:
  - Use imperative language.
  - Use short titles.
  - If there are important or non-obvious details, mention them (succinctly) in the message
    body.
  - If possible, add references in the message body.
    Use tags or commit checksums in those references rather than just pointing to a file on some
    branch.
  - If one commit does more than one thing, be sure to list the individual changes in the
    message body.

  e.g.:
  ```
  Add functionality X

  Important details that are not covered in title or individual changes listed below.

  - fix feature A
    ref:
      - https://github.com/conda/conda/blob/4.7.12/conda/resolve.py#L945-L951
  - remove feature B
  - add feature C
    ref:
      - Proposal of feature C:
        https://github.com/curiu/curiu/issue/XXX

  ref:
  - Discussion of functionality X
    https://github.com/curiu/curiu/issues/YYY
    https://github.com/conda/conda/issues/7808
  ```
- Do not push directly to upstream branches:
  - Fork the project.
  - Push changes to a *new* branch on your fork.
  - Submit a pull request to the upstream branch.

- The project makes use of the [ISC License](LICENSES/LicenseRef-ISC-curiu.txt).
  - Your contributions are expected to be submitted to be used under this license.
  - If you want to submit a contribution under a different license, be sure to
    - adjust the SPDX license/copyright information of those files accordingly,
    - clearly point out that license in your pull request.

- Code in this repository is meant to be submitted to [Conda](https://github.com/conda).
  - **Please be sure to have signed the [Conda Contributor License Agreement](https://conda.io/en/latest/contributing.html#conda-contributor-license-agreement).**
  - **If you do not want or are not able to sign the Conda CLA, you can only submit contributions
    to the `external` directory. See [external/README.md](external/README.md) for details.**
  - **!!!**<br />
    **TODO: Check how we can contribute to Conda under the CLA.**
    https://github.com/conda/conda/blame/4.7.12/CONTRIBUTING.md#L117
    https://github.com/conda/conda/blame/4.7.12/CONTRIBUTING.md#L136-L137
    - **as "the curiu authors":**
      **Can we count as "one" copyright owner?**
      **We are no "legal entity"!**
    - **as an individual with only that person's content:**
      **Business as usual, but have to make sure git history only shows *one* author.**
    - **as an individual with content from multiple persons:**
      **Then point 7 of the CLA applies, see [external/README.md](external/README.md):**
      **Submit separately from anything else and add**
      **"Submitted on behalf of a third-party: [curiu](https://github.com/curiu/curiu/blob/<sha>/AUTHORS.md)"**

    **!!!**
