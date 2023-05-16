""" The 'chemical_reaction_data.miscellaneous' package 'extraction' module. """

from logging import getLogger
from os import remove

from os.path import abspath, join

from ..utilities.archive import ArchiveExtractionUtilities


class MiscellaneousDataExtractionUtilities:
    """ The miscellaneous data extraction utilities class. """

    @staticmethod
    def extract_2013_kraut_et_al(
            downloaded_data_directory_path: str,
            output_directory_path: str,
            enable_logger: bool = False
    ) -> None:
        """
        Extract the chemical reaction classification dataset by (2013, Kraut, H., et al.).

        :parameter downloaded_data_directory_path: The path to the directory where the downloaded data is stored.
        :parameter output_directory_path: The path to the directory where the extracted data should be stored.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the extraction of the chemical reaction classification dataset by "
                    "(2013, Kraut, H., et al.)."
                )

            ArchiveExtractionUtilities.extract_from_zip_archive(
                archive_file_path=join(downloaded_data_directory_path, "1"),
                output_directory_path=output_directory_path,
                archive_file_content_base_paths=[
                    "ci400442f_si_002.zip"
                ]
            )

            ArchiveExtractionUtilities.extract_from_zip_archive(
                archive_file_path=join(downloaded_data_directory_path, "ci400442f_si_002.zip"),
                output_directory_path=output_directory_path
            )

            remove(
                path=join(downloaded_data_directory_path, "ci400442f_si_002.zip")
            )

            if enable_logger:
                getLogger(__name__).info(
                    "Completed the extraction of the chemical reaction classification dataset by "
                    "(2013, Kraut, H., et al.). The extracted data is stored at: '{0}'.".format(
                        abspath(output_directory_path)
                    )
                )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.MiscellaneousDataExtractionUtilities.extract_2013_kraut_et_al".format(__name__)
                ).exception(exception_handle)

            raise
