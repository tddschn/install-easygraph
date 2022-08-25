# install-easygraph


[![Test the install-easygraph Action](https://github.com/tddschn/install-easygraph/actions/workflows/test.yaml/badge.svg)](https://github.com/tddschn/install-easygraph/actions/workflows/test.yaml)


- [install-easygraph](#install-easygraph)
  - [What does this Action do?](#what-does-this-action-do)
  - [Usage and options](#usage-and-options)
  - [Releases and changelog](#releases-and-changelog)
    - [v0.3.0](#v030)
    - [v0.2.0](#v020)
    - [v0.1.1](#v011)
  - [Used by](#used-by)

## What does this Action do?

`tddschn/install-easygraph` is a Action that builds and installs the [easygraph](https://github.com/easy-graph/Easy-Graph) from source, on ubuntu-latest.

## Usage and options

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
          cpp-binding-framework: pybind11 # or boost-python, defaults to pybind11
          use-cached-build: 'true' # defaults to true. cached builds won't be used for anything other than 'true'.
          # boost-version: '1.79.0' # optional, defaults to '1.79.0'
```

## Releases and changelog

### v0.3.0


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
        python-version: ["3.6", "3.7", "3.8", "3.9"]
        cpp-binding-framework: ["pybind11", "boost-python"]
        use-cached-build: ["true", "false"]
```

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
          python-version: ["3.6", "3.7", "3.8", "3.9"]
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