from setuptools import setup
import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setup(
    name="create-flask-app",
    version="0.1",
    description="Creates python flask application template",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ElvisRodriguez/create-flask-app",
    author="Elvis Rodriguez",
    author_email="elvisrodriguez1992@gmail.com",
    license="MIT",
    project_urls={
        "Bug Tracker": "https://github.com/ElvisRodriguez.create-flask-app/issues",
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython"
        "Topic :: Software Development :: Code Generators",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3",
    install_requires=["flask"],
)