import sys
import re
from urllib.request import urlopen


SETUP_PY_VERSION_PATTERN = r'^\s*version=([\'"])(?P<version>[\w\d\.]+)\1'


def set_output(name: str, value: str):
    print(f'setting output {name} to {value}')
    print(f'::set-output name={name}::{value}')


def get_python_version_str(full: bool = False) -> str:
    vi = sys.version_info
    if full:
        return f'{vi.major}.{vi.minor}.{vi.micro}'
    return f'{vi.major}.{vi.minor}'


def get_eg_version(sha1: str) -> str:
    setup_py_url = (
        'https://raw.githubusercontent.com/easy-graph/Easy-Graph/{}/setup.py'.format(
            sha1
        )
    )
    setup_py_content = urlopen(setup_py_url).read().decode()
    return re.search(SETUP_PY_VERSION_PATTERN, setup_py_content, re.MULTILINE).groupdict()['version']  # type: ignore


def get_eg_egg_dir_name(package_version: str) -> str:
    # ubuntu-latest
    # Python_EasyGraph-0.2a40-py3.9-linux-x86_64.egg
    pkg_name = 'Python_EasyGraph'
    python_version_str = get_python_version_str()
    return f'{pkg_name}-{package_version}-py{python_version_str}.egg'


def get_eg_egg_dir_path(sha1: str) -> str:
    # /opt/hostedtoolcache/Python/3.9.13/x64/lib/python3.9/site-packages/Python_EasyGraph-0.2a40-py3.9-linux-x86_64.egg
    return f'/opt/hostedtoolcache/Python/{get_python_version_str(full=True)}/x64/lib/python{get_python_version_str()}/site-packages/{get_eg_egg_dir_name(get_eg_version(sha1))}'
