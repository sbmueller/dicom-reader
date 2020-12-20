from setuptools import setup

setup(
    name="dicom-reader",
    version="1.0.0",
    description="Read medical DICOM images and their meta data",
    url="https://github.com/sbmueller/dicom-reader",
    author="Sebastian Müller",
    author_email="gsenpo@gmail.com",
    license="GPLv3",
    packages=["dicom_reader"],
    zip_safe=False,
    install_requires=["pydicom", "matplotlib", "tqdm"],
    scripts=["bin/dicom-reader"],
)
