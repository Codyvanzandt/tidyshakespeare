import setuptools

setuptools.setup(
    name="tidyshakespeare",
    version="0.1.0",
    url="https://github.com/Codyvanzandt/tidyshakespeare",
    author="Cody VanZandt",
    author_email="cody.a.vanzandt@@gmail.com",
    description="Provides access to Shakespeare's plays, tidy and ready to analyze.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=[],
    package_dir={"": "tidyshakespeare"},
    packages=setuptools.find_packages(where="tidyshakespeare"),
    python_requires=">=3.6",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ], 
)
