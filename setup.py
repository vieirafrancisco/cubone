import setuptools

from cubone import __version__

setuptools.setup(
    name="cubone",
    version=__version__,
    packages=setuptools.find_packages(),
    install_requires=(
        "Jinja2>=3.1.2",
        "pygame>=2.1.2"
        "click>=8.1.3",
    ),
    entry_points={"console_scripts": ["cubone=cubone.cli.core:main"]},
)
