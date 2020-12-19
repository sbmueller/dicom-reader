from setuptools import setup

setup(
    name="dicom-reader",
    version="0.1",
    description="Read medical DICOM images and their meta data",
    url="https://github.com/sbmueller/dicom-reader",
    author="Sebastian Müller",
    author_email="gsenpo@gmail.com",
    license="MIT",
    packages=["dicom_reader"],
    zip_safe=False,
    install_requires=["pydicom", "matplotlib", "tqdm"],
    scripts=["bin/dicom-reader"],
)