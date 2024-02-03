import setuptools

setuptools.setup(
    name="go_sandbox",
    version="0.1.0",
    packages=["src/go_sandbox"],
    entry_points={
        "console_scripts": [
            "play_go = src.go_sandbox:main"
        ]
    },
    install_requires=[
        "tkSnack"
    ]
)
