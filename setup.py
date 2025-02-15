import setuptools

setuptools.setup(
    name="piven",
    version="0.4.0",
    description="Prediction Intervals with specific value prediction",
    url="https://gitlab.com/jasperginn/piven.py",
    author="Jasper Ginn",
    author_email="jasperginn@godatadriven.com",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        "pytest>=2.0.0",
        "scikit-learn>=0.23.2",   
    ],
    extras_require={"dev": ["pytest", "bump2version"]},
)
