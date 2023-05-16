""" The 'chemical_reaction_data.retro_rules' package 'extraction' module. """

from logging import getLogger

from os.path import abspath, join

from ..utilities.archive import ArchiveExtractionUtilities


class RetroRulesDatabaseExtractionUtilities:
    """ The RetroRules database extraction utilities class. """

    @staticmethod
    def extract_rr01_rp2_hs_2018_duigou_et_al(
            downloaded_data_directory_path: str,
            output_directory_path: str,
            enable_logger: bool = False
    ) -> None:
        """
        Extract the RetroRules (rr01.rp2.hs) database by (2018, Duigou, T., et al.).

        :parameter downloaded_data_directory_path: The path to the directory where the downloaded data is stored.
        :parameter output_directory_path: The path to the directory where the extracted data should be stored.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the extraction of the RetroRules (rr01.rp2.hs) database by (2018, Duigou, T., et al.)."
                )

            ArchiveExtractionUtilities.extract_from_tar_gz_archive(
                archive_file_path=join(downloaded_data_directory_path, "retrorules_rr01_rp2.tar.gz"),
                output_directory_path=output_directory_path,
                archive_file_content_base_paths=[
                    "retrorules_rr01_rp2/retrorules_rr01_rp2_flat_all.csv"
                ]
            )

            if enable_logger:
                getLogger(__name__).info(
                    "Completed the extraction of the RetroRules (rr01.rp2.hs) database by (2018, Duigou, T., et al.). "
                    "The extracted data is stored at: '{0}'.".format(
                        abspath(output_directory_path)
                    )
                )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.RetroRulesDatabaseExtractionUtilities.extract_rr01_rp2_hs_2018_duigou_et_al".format(__name__)
                ).exception(exception_handle)

            raise

    @staticmethod
    def extract_rr02_rp2_hs_2018_duigou_et_al(
            downloaded_data_directory_path: str,
            output_directory_path: str,
            enable_logger: bool = False
    ) -> None:
        """
        Extract the RetroRules (rr02.rp2.hs) database by (2018, Duigou, T., et al.).

        :parameter downloaded_data_directory_path: The path to the directory where the downloaded data is stored.
        :parameter output_directory_path: The path to the directory where the extracted data should be stored.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the extraction of the RetroRules (rr02.rp2.hs) database by (2018, Duigou, T., et al.)."
                )

            ArchiveExtractionUtilities.extract_from_tar_gz_archive(
                archive_file_path=join(downloaded_data_directory_path, "retrorules_rr02_rp2_hs.tar.gz"),
                output_directory_path=output_directory_path,
                archive_file_content_base_paths=[
                    "retrorules_rr02_rp2_hs/retrorules_rr02_rp2_flat_all.csv"
                ]
            )

            if enable_logger:
                getLogger(__name__).info(
                    "Completed the extraction of the RetroRules (rr02.rp2.hs) database by (2018, Duigou, T., et al.). "
                    "The extracted data is stored at: '{0}'.".format(
                        abspath(output_directory_path)
                    )
                )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.RetroRulesDatabaseExtractionUtilities.extract_rr02_rp2_hs_2018_duigou_et_al".format(__name__)
                ).exception(exception_handle)

            raise

    @staticmethod
    def extract_rr02_rp3_hs_2018_duigou_et_al(
            downloaded_data_directory_path: str,
            output_directory_path: str,
            enable_logger: bool = False
    ) -> None:
        """
        Extract the RetroRules (rr02.rp3.hs) database by (2018, Duigou, T., et al.).

        :parameter downloaded_data_directory_path: The path to the directory where the downloaded data is stored.
        :parameter output_directory_path: The path to the directory where the extracted data should be stored.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the extraction of the RetroRules (rr02.rp3.hs) database by (2018, Duigou, T., et al.)."
                )

            ArchiveExtractionUtilities.extract_from_tar_gz_archive(
                archive_file_path=join(downloaded_data_directory_path, "retrorules_rr02_rp3_hs.tar.gz"),
                output_directory_path=output_directory_path,
                archive_file_content_base_paths=[
                    "retrorules_rr02_rp3_hs/retrorules_rr02_flat_all.tsv"
                ]
            )

            if enable_logger:
                getLogger(__name__).info(
                    "Completed the extraction of the RetroRules (rr02.rp3.hs) database by (2018, Duigou, T., et al.). "
                    "The extracted data is stored at: '{0}'.".format(
                        abspath(output_directory_path)
                    )
                )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.RetroRulesDatabaseExtractionUtilities.extract_rr02_rp3_hs_2018_duigou_et_al".format(__name__)
                ).exception(exception_handle)

            raise

    @staticmethod
    def extract_rr02_rp3_nohs_2018_duigou_et_al(
            downloaded_data_directory_path: str,
            output_directory_path: str,
            enable_logger: bool = False
    ) -> None:
        """
        Extract the RetroRules (rr02.rp3.nohs) database by (2018, Duigou, T., et al.).

        :parameter downloaded_data_directory_path: The path to the directory where the downloaded data is stored.
        :parameter output_directory_path: The path to the directory where the extracted data should be stored.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the extraction of the RetroRules (rr02.rp3.nohs) database by (2018, Duigou, T., et al.)."
                )

            ArchiveExtractionUtilities.extract_from_tar_gz_archive(
                archive_file_path=join(downloaded_data_directory_path, "retrorules_rr02_rp3_nohs.tar.gz"),
                output_directory_path=output_directory_path,
                archive_file_content_base_paths=[
                    "retrorules_rr02_rp3_nohs/retrorules_rr02_flat_all.tsv"
                ]
            )

            if enable_logger:
                getLogger(__name__).info(
                    "Completed the extraction of the RetroRules (rr02.rp3.nohs) database by "
                    "(2018, Duigou, T., et al.). The extracted data is stored at: '{0}'.".format(
                        abspath(output_directory_path)
                    )
                )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.RetroRulesDatabaseExtractionUtilities.extract_rr02_rp3_nohs_2018_duigou_et_al".format(__name__)
                ).exception(exception_handle)

            raise
