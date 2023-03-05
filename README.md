# install-easygraph


[![Test the install-easygraph Action](https://github.com/tddschn/install-easygraph/actions/workflows/test.yaml/badge.svg)](https://github.com/tddschn/install-easygraph/actions/workflows/test.yaml)
[![Test the install-easygraph Action (macOS)](https://github.com/tddschn/install-easygraph/actions/workflows/test-macos.yaml/badge.svg)](https://github.com/tddschn/install-easygraph/actions/workflows/test-macos.yaml)

[![Test the install-easygraph Action (dummy)](https://github.com/tddschn/install-easygraph/actions/workflows/test-dummy.yaml/badge.svg)](https://github.com/tddschn/install-easygraph/actions/workflows/test-dummy.yaml)
[![Test the install-easygraph Action (macOS)(dummy)](https://github.com/tddschn/install-easygraph/actions/workflows/test-macos-dummy.yaml/badge.svg)](https://github.com/tddschn/install-easygraph/actions/workflows/test-macos-dummy.yaml)


- [install-easygraph](#install-easygraph)
  - [What does this Action do?](#what-does-this-action-do)
  - [Usage and options](#usage-and-options)
    - [`tddschn/install-easygraph`](#tddschninstall-easygraph)
    - [`tddschn/install-easygraph/dummy`](#tddschninstall-easygraphdummy)
  - [Releases and changelog](#releases-and-changelog)
    - [v0.5.0](#v050)
    - [v0.4.0](#v040)
    - [v0.3.1](#v031)
    - [v0.2.0](#v020)
    - [v0.1.1](#v011)
  - [Used by](#used-by)

## What does this Action do?

`tddschn/install-easygraph` is a Action that builds and installs the [easygraph](https://github.com/easy-graph/Easy-Graph) from source, on ubuntu-latest.

## Usage and options

### `tddschn/install-easygraph`

See [`action.yml`](./action.yml)

```yaml
  benchmark:
    runs-on: ubuntu-latest # it's only tested to work on ubuntu-latest
    steps:
      # install-easygraph will use the the version of the `python` in your path
      - name: Set up Python 3.9
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'

      - name: 'Build and install easygraph'
        uses: tddschn/install-easygraph@master # or v0.1.1, or any other ref
        with:
          repository: 'easy-graph/Easy-Graph' # or tddschn/Easy-Graph
          ref: 'pybind11' # SHA1, tag, or branch
          use-cached-build: 'true' # defaults to true. cached builds won't be used for anything other than 'true'.
          install-lxml: 'false' # defaults to false. lxml is an optional dependency that doesn't provide wheel for macOS, installing it on macOS takes several minutes.
          install-pytorch: 'false' # whether to install pytorch
```

### `tddschn/install-easygraph/dummy`

With complicated caching logic removed.

See [`dummy/action.yml`](./dummy/action.yml)

```yaml
  benchmark:
    runs-on: ubuntu-latest # it's only tested to work on ubuntu-latest
    steps:
      # install-easygraph will use the the version of the `python` in your path
      - name: Set up Python 3.9
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'

      - name: 'Build and install easygraph'
        uses: tddschn/install-easygraph@master # or v0.1.1, or any other ref
        with:
        repository: 'easy-graph/Easy-Graph' # or tddschn/Easy-Graph
          ref: 'pybind11' # SHA1, tag, or branch
          install-lxml: 'false' # defaults to false. lxml is an optional dependency that doesn't provide wheel for macOS, installing it on macOS takes several minutes.
          install-pytorch: 'false' # whether to install pytorch
```

## Releases and changelog

### v0.5.0

**Warning**:  
`tddschn/install-easygraph@v0.5.0` only works for python>=3.10 on Ubuntu, I'm still investigating the issue.

For use with python <= 3.9, use `tddschn/install-easygraph/dummy@v0.5.0`  
which removed complicated caching logic.

Deprecates:
- Building C++ extension with `boost-python`.

Add:
- The `install-pytorch`, `repository`, and `ref` options.
- `install-pytorch` controls whether to install `pytorch` in the installation process
- `repository` and `ref` allow users to select other repository (e.g. a fork) and ref other than the tip of the `master` or `pybind11` branch.
- A new dummy workflow without caching logic:  
  `tddschn/install-easygraph/dummy`
  
Remove:
- The `cpp-binding-framework`, `boost-version` options.

### v0.4.0

<details>
  <summary>Click to expand</summary>

  Add:
  - macOS support when using `pybind11` as `cpp-binding-framework`.
  - The `install-lxml` option.
  
  
  
  Tested on ubuntu-latest with the following combination of options (note that `python-version` is not an option of this action):
  
  ```yaml
      matrix:
      python-version: ["3.7", "3.8", "3.9", "3.10"]
      cpp-binding-framework: ["pybind11"]
      include:
        - use-cached-build: 'true'
  ```
  
  
  Tested on ubuntu-latest with the following combination of options (note that `python-version` is not an option of this action):
  
  ```yaml
      matrix:
          python-version: ["3.7", "3.8", "3.9", "3.10"]
          cpp-binding-framework: ["pybind11", "boost-python"]
          use-cached-build: ["true", "false"]
  ```
<!-- Two important rules:
Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>


### v0.3.1

<details>
  <summary>Click to expand</summary>

  Fix:
  - The checking out this action repository step in v0.3.0
  
  Add:
  - Caches built egg directory and dependencies under `site-packages`,  
    greatly speed up the action to ~23 seconds.  
    Without caching,  
    building with `pybind11` takes ~90 s, and building with `boost-python` takes over 3 minutes.
  - The `use-cached-build` option to control whether to use the cache.
  
  The caches are identified with the combination of:  
  - the easygraph commit SHA1 they were built against
  - the python version (`sys.version`)
  
  The release was designed to work with [easygraph](https://github.com/easy-graph/Easy-Graph) before the `pybind11` branch is merged into master (which hasn't happened when this release was created).
  
  Tested on ubuntu-latest with the following combination of options (note that `python-version` is not an option of this action):
  
  ```yaml
        matrix:
          python-version: ["3.7", "3.8", "3.9"]
          cpp-binding-framework: ["pybind11", "boost-python"]
          use-cached-build: ["true", "false"]
  ```
<!-- Two important rules:
Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>


### v0.2.0

<details>
  <summary>Click to expand</summary>

  Changes from v0.1.1:
  - Remove `easygraph-checkout-path` option  
    The action will delete the checked out easygraph source code after building and installing.
  - Add Action branding
  
  The release was designed to work with [easygraph](https://github.com/easy-graph/Easy-Graph) before the `pybind11` branch is merged into master (which hasn't happened when this release was created).
<!-- Two important rules:
Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>


### v0.1.1

<details>
  <summary>Click to expand</summary>

  The v0.1.1 release has been tested and proved to work on these configurations on ubuntu-latest:
  ```
          python-version: ["3.7", "3.8", "3.9"]
          cpp-binding-framework: ["pybind11", "boost-python"]
  ```
  The release was designed to work with [easygraph](https://github.com/easy-graph/Easy-Graph) before the `pybind11` branch is merged into master (which hasn't happened when this release was created).
<!-- Two important rules:
Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>


## Used by

- [easygraph](https://github.com/easy-graph/Easy-Graph)
- [easygraph-bench](https://tddschn/easygraph-bench)