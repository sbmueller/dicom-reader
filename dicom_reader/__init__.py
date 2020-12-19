import os
from pydicom import dcmread
import matplotlib.pyplot as plt
from tqdm import tqdm


def quit_figure(event) -> None:
    """Matplotlib callback which closes current figure."""
    plt.close(event.canvas.figure)


class DicomData:
    """
    Represents a set of one or more DICOM files.

    :param path: Path of the folder containing DICOM data
    """

    def __init__(self, path: str):
        """C'tor."""
        path = os.path.abspath(path)
        if not os.path.exists(path):
            raise ValueError(f"Path does not exist: {path}")
        self.path = path
        self._files = [
            os.path.join(self.path, f)
            for f in sorted(os.listdir(self.path))
            if os.path.isfile(os.path.join(self.path, f))
        ]

    def get_metadata(self) -> str:
        """Return general meta data of whole DICOM data set."""
        ds = dcmread(self._files[0])  # take first file to read general data
        pat_name = ds.PatientName
        display_name = pat_name.family_name + ", " + pat_name.given_name
        return (
            f"File path........: {self.path}\n"
            f"SOP Class........: {ds.SOPClassUID} ({ds.SOPClassUID.name})\n"
            f"Institution Name.: {ds.InstitutionName}\n"
            f"Patient's Name...: {display_name}\n"
            f"Patient ID.......: {ds.PatientID}\n"
            f"Modality.........: {ds.Modality}\n"
            f"Study Date.......: {ds.StudyDate}\n"
            f"Image size.......: {ds.Rows} x {ds.Columns}\n"
            f"Pixel Spacing....: {ds.PixelSpacing}\n"
            f"Body part........: {ds.BodyPartExamined}\n"
            f"MRI Manufacturer.: {ds.Manufacturer}\n"
            f"MRI Model........: {ds.ManufacturerModelName}\n"
            f"MRI Version......: {ds.SoftwareVersions}"
        )

    def plot_images(self) -> None:
        """Use Matplotlib to plot all DICOM images."""
        for fpath in tqdm(self._files):
            ds = dcmread(fpath)
            plt.title(
                f"Loc: {ds.SliceLocation} Thick: {ds.SliceThickness} "
                "Seq: {ds.SequenceName}"
            )
            plt.imshow(ds.pixel_array, cmap=plt.cm.gray)
            plt.gcf().canvas.mpl_connect("key_press_event", quit_figure)
            plt.show()

    def export_to_folder(self, output_folder: str) -> None:
        """
        Export DICOM images to PNG images and metadata text file.

        :param output_folder: Location for exported PNGs
        """
        output_folder = os.path.abspath(output_folder)
        with open(os.path.join(output_folder, "metadata.txt"), "w") as f:
            f.write(self.get_metadata())
        for fpath in tqdm(self._files):
            ds = dcmread(fpath)
            _, filename = os.path.split(fpath)
            filename += ".png"
            fig = plt.figure(frameon=False, figsize=(ds.Columns // 96, ds.Rows // 96))
            ax = plt.Axes(fig, [0.0, 0, 1.0, 1.0])
            ax.set_axis_off()
            fig.add_axes(ax)
            ax.imshow(ds.pixel_array, cmap=plt.cm.gray)
            fig.savefig(os.path.join(output_folder, filename), dpi=96)
            plt.close()
