# install-easygraph


[![Test the install-easygraph Action](https://github.com/tddschn/install-easygraph/actions/workflows/test.yaml/badge.svg)](https://github.com/tddschn/install-easygraph/actions/workflows/test.yaml)


- [install-easygraph](#install-easygraph)
  - [What does this Action do?](#what-does-this-action-do)
  - [Usage and options](#usage-and-options)
  - [Releases](#releases)
    - [v0.1.1](#v011)
  - [Used by](#used-by)

## What does this Action do?

`tddschn/install-easygraph` is a Action that builds and installs the [easygraph](https://github.com/easy-graph/Easy-Graph) from source, on ubuntu-latest.

## Usage and options

```yaml
  benchmark:
    runs-on: ubuntu-latest
    steps:
      # install-easygraph will use the the version of the `python` in your path
      - name: Set up Python 3.9
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'

      - name: 'Build and install easygraph'
        uses: tddschn/install-easygraph@master # or v0.1.0, or any other ref
        with:
          cpp-binding-framework: pybind11 # or boost-python, defaults to pybind11
          # boost-version: '1.79.0' # optional, defaults to '1.79.0'
          # easygraph-checkout-path: 'Easy-Graph' # optional, defaults to 'Easy-Graph'
```

## Releases

### v0.1.1

The v0.1.1 release has been tested and proved to work on these configurations on ubuntu-latest:
```
        python-version: ["3.6", "3.7", "3.8", "3.9"]
        cpp-binding-framework: ["pybind11", "boost-python"]
```
The release was designed to work with [easygraph](https://github.com/easy-graph/Easy-Graph) before the `pybind11` branch is merged into master (which hasn't happened when this release was created).

## Used by

- [easygraph-bench](https://tddschn/easygraph-bench)