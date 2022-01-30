import json
import urllib.request
from setuptools import setup, find_packages


def latest_version(package_name):
    url = f"https://pypi.python.org/pypi/{package_name}/json"
    try:
        response = urllib.request.urlopen(urllib.request.Request(url), timeout=1)
        data = json.load(response)
        versions = data["releases"].keys()
        versions = sorted(versions)
        return ">={}".format(versions[-1])
    except Exception:
        pass
    return ""


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="image-optimizer-cli",
    author="Ege Akman",
    author_email="egeakmanegeakman@hotmail.com",
    url="https://github.com/egeakman/image-optimizer-cli",
    description="A PIL based image optimizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="2022.1.30-1",
    license="AGPLv3",
    download_url="https://github.com/egeakman/image-optimizer-cli/archive/2022.1.30-1.tar.gz",
    packages=find_packages(where=".", exclude=["tests"]),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "image-optimizer=image_optimizer_cli.optimize:main",
        ]
    },
    install_requires=[
        f"setuptools{latest_version('setuptools')}",
        f"pillow{latest_version('pillow')}",
    ],
    keywords=["image", "optimize", "pillow", "PIL", "compression", "compressor"],
    classifiers=[
        "Topic :: Utilities",
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: Microsoft :: Windows",
    ],
    project_urls={
        "Homepage": "https://github.com/egeakman/image-optimizer-cli",
        "Issues": "https://github.com/egeakman/image-optimizer-cli/issues",
    },
)
