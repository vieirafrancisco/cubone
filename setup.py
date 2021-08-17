import setuptools

from cubone import __version__

setuptools.setup(
    name="cubone",
    version=__version__,
    packages=setuptools.find_packages(),
    install_requires=(
        "Jinja2>=3.0.1",
        "pygame>=2.0.1"
        "click>=8.0.1",
    ),
    entry_points={"console_scripts": ["cubone=cubone.cli.core:main"]},
)
