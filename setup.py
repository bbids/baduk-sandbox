import setuptools

setuptools.setup(
    name="baduk-sandbox",
    version="0.1.0",
    packages=["src/baduk_sandbox"],
    entry_points={
        "console_scripts": [
            "baduk = src.baduk_sandbox:main"
        ]
    },
)
