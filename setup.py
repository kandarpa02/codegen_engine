from setuptools import setup, find_packages

setup(
    name="codegen_engine",
    version="0.0.1a1",
    author="Kandarpa Sarkar",
    author_email="kandarpaexe@gmail.com",
    description="A light-weight library for accelerating python functions",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kandarpa02/codegen_engine.git",
    packages=find_packages(),
    install_requires = ["numpy"],
    python_requires=">=3.8",
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries",
    ],
    zip_safe=False,
    
)