from setuptools import setup, find_packages
setup(
    name="colaboratory_utils",
    version="0.1",
    packages=['colaboratory_utils'],
    install_requires=['scipy', 'pillow', 'numpy'],

    # metadata to display on PyPI
    keywords="Notebook colab colaboratory google Numpy PIL OpenCV",
    url="https://github.com/albertofernandezvillan/colaboratory_utils",
    classifiers=[
        'Programming Language :: Python :: 3 :: Only' # https://pypi.org/classifiers/
    ]
)
