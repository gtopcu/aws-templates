import setuptools

with open("README.md") as fp:
    long_description = fp.read()

setuptools.setup(
    name="cdk-powertools-python",
    version="0.0.1",

    description="Sample CDK Python app utilizing AWS Lambda Powertools for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="S. Gökhan Topçu",

    package_dir={"": "cdk-powertools-python"},
    packages=setuptools.find_packages(where="cdk-powertools-python"),

    install_requires=[
        "aws-cdk-lib==2.38.1",
        "constructs>=10.0.0,<11.0.0",
        "aws-lambda-powertools==1.27.0"
    ],

    python_requires=">=3.9",

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)