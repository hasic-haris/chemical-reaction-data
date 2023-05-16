""" The 'chemical_reaction_data.uspto' package 'extraction' module. """

from logging import getLogger
from os import listdir, remove

from os.path import abspath, join

from ..utilities.archive import ArchiveExtractionUtilities


class UsptoDatasetExtractionUtilities:
    """ The United States Patent and Trademark Office (USPTO) dataset extraction utilities class. """

    @staticmethod
    def extract_1976_2013_2014_lowe(
            downloaded_data_directory_path: str,
            output_directory_path: str,
            enable_logger: bool = False
    ) -> None:
        """
        Extract the USPTO (1976-2013) dataset by (2014, Lowe, D.M.).

        :parameter downloaded_data_directory_path: The path to the directory where the downloaded data is stored.
        :parameter output_directory_path: The path to the directory where the extracted data should be stored.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the extraction of the USPTO (1976-2013) dataset by (2014, Lowe, D.M.)."
                )

            ArchiveExtractionUtilities.extract_from_zip_archive(
                archive_file_path=join(downloaded_data_directory_path, "1"),
                output_directory_path=output_directory_path,
                archive_file_content_base_paths=[
                    # "1976-2013_USPTOgrants_CML.7z",
                    "1976-2013_USPTOgrants_reactionSmiles_feb2014filters.7z",
                    # "2001-2013_USPTOapplications_CML.7z",
                    "2001-2013_USPTOapplications_reactionSmiles_feb2014filters.7z",
                    # "2008-2011_USPTO_reactionSmiles_filtered.zip"
                ]
            )

            for file_path in listdir(output_directory_path):
                if file_path.endswith(".7z"):
                    ArchiveExtractionUtilities.extract_from_7z_archive(
                        archive_file_path=join(output_directory_path, file_path),
                        output_directory_path=output_directory_path
                    )

                    remove(
                        path=join(output_directory_path, file_path)
                    )

                if file_path.endswith(".zip"):
                    ArchiveExtractionUtilities.extract_from_zip_archive(
                        archive_file_path=join(output_directory_path, file_path),
                        output_directory_path=output_directory_path
                    )

                    remove(
                        path=join(output_directory_path, file_path)
                    )

            if enable_logger:
                getLogger(__name__).info(
                    "Completed the extraction of the USPTO (1976-2013) dataset by (2014, Lowe, D.M.). "
                    "The extracted data is stored at: '{0}'.".format(
                        abspath(output_directory_path)
                    )
                )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.UsptoDatasetExtractionUtilities.extract_1976_2013_2014_lowe".format(__name__)
                ).exception(exception_handle)

            raise

    @staticmethod
    def extract_50k_2016_schneider_et_al(
            downloaded_data_directory_path: str,
            output_directory_path: str,
            enable_logger: bool = False
    ) -> None:
        """
        Extract the USPTO-50k dataset by (2016, Schneider, N., et al.).

        :parameter downloaded_data_directory_path: The path to the directory where the downloaded data is stored.
        :parameter output_directory_path: The path to the directory where the extracted data should be stored.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the extraction of the USPTO-50k dataset by (2016, Schneider, N., et al.)."
                )

            ArchiveExtractionUtilities.extract_from_zip_archive(
                archive_file_path=join(downloaded_data_directory_path, "1"),
                output_directory_path=output_directory_path,
                archive_file_content_base_paths=[
                    "ci6b00564_si_002.zip"
                ]
            )

            ArchiveExtractionUtilities.extract_from_zip_archive(
                archive_file_path=join(downloaded_data_directory_path, "ci6b00564_si_002.zip"),
                output_directory_path=output_directory_path,
                archive_file_content_base_paths=[
                    "data/dataSetA.csv",
                    "data/dataSetB.csv"
                ]
            )

            remove(
                path=join(downloaded_data_directory_path, "ci6b00564_si_002.zip")
            )

            if enable_logger:
                getLogger(__name__).info(
                    "Completed the extraction of the USPTO-50k dataset by (2016, Schneider, N., et al.). "
                    "The extracted data is stored at: '{0}'.".format(
                        abspath(output_directory_path)
                    )
                )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.UsptoDatasetExtractionUtilities.extract_50k_2016_schneider_et_al".format(__name__)
                ).exception(exception_handle)

            raise

    @staticmethod
    def extract_15k_2017_coley_et_al(
            downloaded_data_directory_path: str,
            output_directory_path: str,
            enable_logger: bool = False
    ) -> None:
        """
        Extract the USPTO-15k dataset by (2017, Coley, C.W., et al.).

        :parameter downloaded_data_directory_path: The path to the directory where the downloaded data is stored.
        :parameter output_directory_path: The path to the directory where the extracted data should be stored.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the extraction of the USPTO-15k dataset by (2017, Coley, C.W., et al.)."
                )

            ArchiveExtractionUtilities.extract_from_zip_archive(
                archive_file_path=join(downloaded_data_directory_path, "data.zip"),
                output_directory_path=output_directory_path
            )

            if enable_logger:
                getLogger(__name__).info(
                    "Completed the extraction of the USPTO-15k dataset by (2017, Coley, C.W., et al.). "
                    "The extracted data is stored at: '{0}'.".format(
                        abspath(output_directory_path)
                    )
                )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.UsptoDatasetExtractionUtilities.extract_15k_2017_coley_et_al".format(__name__)
                ).exception(exception_handle)

            raise

    @staticmethod
    def extract_1976_2016_2017_lowe(
            downloaded_data_directory_path: str,
            output_directory_path: str,
            enable_logger: bool = False
    ) -> None:
        """
        Extract the USPTO (1976-2016) dataset by (2017, Lowe, D.M.).

        :parameter downloaded_data_directory_path: The path to the directory where the downloaded data is stored.
        :parameter output_directory_path: The path to the directory where the extracted data should be stored.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the extraction of the USPTO (1976-2016) dataset by (2017, Lowe, D.M.)."
                )

            ArchiveExtractionUtilities.extract_from_zip_archive(
                archive_file_path=join(downloaded_data_directory_path, "1"),
                output_directory_path=output_directory_path,
                archive_file_content_base_paths=[
                    "1976_Sep2016_USPTOgrants_cml.7z",
                    "2001_Sep2016_USPTOapplications_cml.7z",
                    "2001_Sep2016_USPTOapplications_smiles.7z",
                    "1976_Sep2016_USPTOgrants_smiles.7z"
                ]
            )

            for file_path in listdir(output_directory_path):
                if file_path.endswith(".7z"):
                    ArchiveExtractionUtilities.extract_from_7z_archive(
                        archive_file_path=join(output_directory_path, file_path),
                        output_directory_path=output_directory_path
                    )

                    remove(
                        path=join(output_directory_path, file_path)
                    )

            if enable_logger:
                getLogger(__name__).info(
                    "Completed the extraction of the USPTO (1976-2016) dataset by (2017, Lowe, D.M.). "
                    "The extracted data is stored at: '{0}'.".format(
                        abspath(output_directory_path)
                    )
                )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.UsptoDatasetExtractionUtilities.extract_1976_2016_2017_lowe".format(__name__)
                ).exception(exception_handle)

            raise

    @staticmethod
    def extract_mit_2017_jin_et_al(
            downloaded_data_directory_path: str,
            output_directory_path: str,
            enable_logger: bool = False
    ) -> None:
        """
        Extract the USPTO-MIT dataset by (2017, Jin, W., et. al.).

        :parameter downloaded_data_directory_path: The path to the directory where the downloaded data is stored.
        :parameter output_directory_path: The path to the directory where the extracted data should be stored.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the extraction of the USPTO-MIT dataset by (2017, Jin, W., et al.)."
                )

            ArchiveExtractionUtilities.extract_from_zip_archive(
                archive_file_path=join(downloaded_data_directory_path, "data.zip"),
                output_directory_path=output_directory_path
            )

            if enable_logger:
                getLogger(__name__).info(
                    "Completed the extraction of the USPTO-MIT dataset by (2017, Jin, W., et al.). "
                    "The extracted data is stored at: '{0}'.".format(
                        abspath(output_directory_path)
                    )
                )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.UsptoDatasetExtractionUtilities.extract_mit_2017_jin_et_al".format(__name__)
                ).exception(exception_handle)

            raise
