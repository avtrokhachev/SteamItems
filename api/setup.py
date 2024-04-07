from setuptools import find_packages, setup


def get_requirements() -> list:
    with open("requirements.txt") as file:
        requirements = file.read().splitlines()
        return requirements


setup(
    name="api",
    version="0.1",
    author="Andrey Trokhachev",
    author_email="theairdrop@yandex.ru",
    description="api lib for SteamItems project",
    packages=find_packages(),
    install_requires=get_requirements(),
)
