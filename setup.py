from setuptools import setup, find_packages

setup(
    name="fsm_project",
    version="1.0.0",
    description="A modular and extensible implementation of deterministic finite state machines (FSM).",
    author="Sharik Javid",
    url="https://github.com/sharikjavid/fsm_project",
    packages=find_packages(),
    install_requires=[
        "dataclasses; python_version<'3.7'",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'run-mod-three=fsm.examples.mod_three:mod_three_fsm',
        ],
    },
)
