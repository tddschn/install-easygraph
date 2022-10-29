from functools import lru_cache
import sys
import re
import os
from urllib.request import urlopen
from pkg_resources import safe_name, safe_version, to_filename, get_build_platform
from sysconfig import get_paths


SETUP_PY_VERSION_PATTERN = r'^\s*version=([\'"])(?P<version>[\w\d\.]+)\1'

def sha1_str(s: str) -> str:
    """
    return the sha1 of the string
    """
    import hashlib

    return hashlib.sha1(s.encode()).hexdigest()


def set_output(name: str, value: str):
    print(f'setting output {name} to {value}')
    github_output_file = os.environ.get('GITHUB_OUTPUT')
    assert github_output_file is not None
    if '\n' in value:
        # generate a random delimiter
        delimiter = sha1_str(value)
        # append these lines to the file
        # {name}<<{delimiter}
        # {value}
        # {delimiter}
        with open(github_output_file, 'a') as f:
            f.write(f'{name}<<{delimiter}\n')
            f.write(f'{value}\n')
            f.write(f'{delimiter}\n')
    with open(github_output_file, 'a') as f:
        f.write(f'{name}={value}\n')


def get_python_version_str(full: bool = False) -> str:
    vi = sys.version_info
    if full:
        return f'{vi.major}.{vi.minor}.{vi.micro}'
    return f'{vi.major}.{vi.minor}'


@lru_cache()
def get_eg_setup_py_content(sha1: str) -> str:
    setup_py_url = (
        'https://raw.githubusercontent.com/easy-graph/Easy-Graph/{}/setup.py'.format(
            sha1
        )
    )
    setup_py_content = urlopen(setup_py_url).read().decode()
    return setup_py_content


@lru_cache()
def get_eg_version(sha1: str) -> str:
    setup_py_content = get_eg_setup_py_content(sha1)
    return re.search(SETUP_PY_VERSION_PATTERN, setup_py_content, re.MULTILINE).groupdict()['version']  # type: ignore


def get_eg_egg_dir_name(package_version: str) -> str:
    # ubuntu-latest
    # Python_EasyGraph-0.2a40-py3.9-linux-x86_64.egg
    # macos-12
    # Python_EasyGraph-0.2a40-py3.10-macosx-10.9-x86_64.egg

    # name ["-" version ["-py" pyver ["-" required_platform]]] "." ext
    # https://setuptools.pypa.io/en/latest/deprecated/python_eggs.html

    pkg_name = 'Python-EasyGraph'
    name = to_filename(safe_name(pkg_name))
    version = safe_version(package_version)
    pyver = get_python_version_str()
    required_platform = get_build_platform()
    return f'{name}-{version}-py{pyver}-{required_platform}.egg'


def get_site_packages_path() -> str:
    return get_paths()["purelib"]


def get_eg_egg_dir_path(sha1: str) -> str:
    # /opt/hostedtoolcache/Python/3.9.13/x64/lib/python3.9/site-packages/Python_EasyGraph-0.2a40-py3.9-linux-x86_64.egg
    return f'{get_site_packages_path()}/{get_eg_egg_dir_name(get_eg_version(sha1))}'


def append_eg_egg_dir_rel_path_to_easy_install_pth(sha1: str):
    eg_egg_dir_name = get_eg_egg_dir_name(get_eg_version(sha1))
    easy_install_pth_path = f'{get_site_packages_path()}/easy-install.pth'
    with open(easy_install_pth_path, 'a') as f:
        f.write(f'.{os.sep}{eg_egg_dir_name}\n')



def get_sys_version_sha1() -> str:
    return sha1_str(sys.version)
