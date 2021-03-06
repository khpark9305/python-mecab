import os
import platform
from setuptools import setup, Extension

BUILD_COVERAGE = os.environ.get("BUILD_COVERAGE", "") == "ON"


def get_libraries():
    if platform.system() == "Darwin":
        return ["iconv"]
    if platform.system() == "Linux":
        return ["c"]


def get_coverage_args_for_cc():
    if BUILD_COVERAGE:
        return ["--coverage", "-O0"]
    return []


def get_coverage_args_for_ld():
    if BUILD_COVERAGE:
        return ["--coverage"]
    return []


mecab = Extension(
    "mecab._C",
    sources=["mecab/_C/mecab.cc", "mecab/_C/tagger.cc"],
    libraries=get_libraries(),
    include_dirs=["../../include"],
    extra_compile_args=["-std=c++11"] + get_coverage_args_for_cc(),
    extra_link_args=get_coverage_args_for_ld(),
    language="c++",
)

setup(
    name="python-mecab",
    version="1.0.1",
    python_requires=">=3.5",
    packages=["mecab"],
    ext_modules=[mecab],
    entry_points={
        "console_scripts": [
            "mecab=mecab.cli:run_mecab_main",
            "mecab-dict-index=mecab.cli:run_mecab_dict_index",
            "mecab-dict-gen=mecab.cli:run_mecab_dict_gen",
            "mecab-test-gen=mecab.cli:run_mecab_test_gen",
            "mecab-cost-train=mecab.cli:run_mecab_cost_train",
            "mecab-system-eval=mecab.cli:run_mecab_system_eval",
        ],
    },
    url="https://github.com/jeongukjae/python-mecab",
    author="Jeong Ukjae",
    author_email="jeongukjae@gmail.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: C++",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries",
        "Typing :: Typed",
    ],
)
