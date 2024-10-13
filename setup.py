import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="napalm",
    version="0.0.1",
    author="Abdiel Souza",
    author_email="abdielcsouza@gmail.com",
    description="A micro framerwork to make a web server or API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abdielsouza/NapalmProject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)