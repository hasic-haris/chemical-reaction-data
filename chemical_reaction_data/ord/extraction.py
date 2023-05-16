""" The 'chemical_reaction_data.ord' package 'extraction' module. """

from logging import getLogger

from os.path import abspath, join

from ..utilities.archive import ArchiveExtractionUtilities


class OrdExtractionUtilities:
    """ The Open Reaction Database (ORD) extraction utilities class. """

    @staticmethod
    def extract_2021_kearnes_et_al(
            downloaded_data_directory_path: str,
            output_directory_path: str,
            enable_logger: bool = False
    ) -> None:
        """
        Extract the Open Reaction Database (ORD) by (2021, Kearnes, S.M., et al.).

        :parameter downloaded_data_directory_path: The path to the directory where the downloaded data is stored.
        :parameter output_directory_path: The path to the directory where the extracted data should be stored.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the extraction of the Open Reaction Database (ORD) by (2021, Kearnes, S.M., et al.)."
                )

            ArchiveExtractionUtilities.extract_from_zip_archive(
                archive_file_path=join(downloaded_data_directory_path, "main"),
                output_directory_path=output_directory_path,
                archive_content_base_paths=[
                    "ord-data-main/data"
                ]
            )

            if enable_logger:
                getLogger(__name__).info(
                    "Completed the extraction of the Open Reaction Database (ORD) by (2021, Kearnes, S.M., et al.). "
                    "The extracted data is stored at: '{0}'.".format(
                        abspath(output_directory_path)
                    )
                )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.OrdExtractionUtilities.extract_2021_kearnes_et_al".format(__name__)
                ).exception(exception_handle)

            raise
