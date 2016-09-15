#!/usr/bin/env python

import ez_setup
ez_setup.use_setuptools()

import os
import glob
from setuptools import setup, find_packages

import thug

configuration_path = "/etc/thug"

personalities_path = os.path.join(configuration_path, "personalities") 
rules_path         = os.path.join(configuration_path, "rules")
js_rules_path      = os.path.join(rules_path, "jsclassifier")
url_rules_path     = os.path.join(rules_path, "urlclassifier")
sample_rules_path  = os.path.join(rules_path, "sampleclassifier")

setup(
    name = "thug",
    version = thug.__version__,
    author = "Angelo Dell'Aera",
    author_email = "buffer@antifork.org",
    description = "Low-interaction honeyclient Thug",
    long_description = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.rst")).read(),
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Topic :: Security",
    ],
    package_data = {
           ""       : ["*.js"],
           },
    packages = find_packages(),
    #scripts = ["thug/thug.py", ],
    data_files = [
        (configuration_path, ["thug/Analysis/honeyagent/honeyagent.conf.sample",
                              "thug/Analysis/virustotal/virustotal.conf.default",
                              "thug/Logging/logging.conf.default",
                              "thug/Plugins/plugins.conf.default"]),
        (personalities_path, glob.glob("thug/DOM/personalities/*.json")),
        (rules_path        , glob.glob("thug/Classifier/rules/*.yar")),
        (js_rules_path     , glob.glob("thug/Classifier/rules/jsclassifier/*.yar")),
        (url_rules_path    , glob.glob("thug/Classifier/rules/urlclassifier/*.yar")),
        (sample_rules_path , glob.glob("thug/Classifier/rules/sampleclassifier/*.yar")),
    ],
    install_requires = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "requirements.txt")).read().splitlines(),
    entry_points = {
        "console_scripts": [
            "thug = thug.thug:main",
        ]
    }
)
