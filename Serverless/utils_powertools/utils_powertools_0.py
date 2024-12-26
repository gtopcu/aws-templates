
from distutils import version
import requests


def powertools_version() -> str:
    response = requests.get("https://pypi.org/pypi/aws-lambda-powertools/json")
    response.raise_for_status()

    data = response.json()
    releases = data["releases"]

    versions = []
    for release in releases:
        versions.append(version.parse(release))
    return max(versions).public

