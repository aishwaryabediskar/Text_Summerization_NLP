import setuptools
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = '0.0.0'

REPO_NAME = "Text_Summerization_NLP"
AUTHOR_USER_NAME = "aishwaryabediskar" 
SRC_REPO = "TextSummerizer"
AUTHOR_EMAIL = "aishwaryabediskar123@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    AUTHOR_EMAIL=AUTHOR_EMAIL,
    description="A small python package of NLP app",
    long_description=long_description,
    long_description_content = "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)