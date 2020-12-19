# DICOM-Reader

Got a radiological exam and went home with a data carrier with nonfunctional
or no software? Use this tool to get access to the DICOM images for patient
transparency!

## Installation

```
python setup.py install
```

## Usage

To view DICOM files:
```
dicom-reader /path/to/dicom/directory
```

To export DICOM files:

```
dicom-reader --export /export/path /path/to/dicom/directory
```
