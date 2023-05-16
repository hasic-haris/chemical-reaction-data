""" The 'chemical_reaction_data.miscellaneous' package 'download' module. """

from logging import getLogger
from typing import Dict, List, Union

from os.path import abspath

from .download_information import MISCELLANEOUS_DATA_DOWNLOAD_INFORMATION

from ..utilities.download import DownloadUtilities


class MiscellaneousDataDownloadUtilities:
    """ The miscellaneous data download utilities class. """

    @staticmethod
    def download_2013_kraut_et_al(
            output_directory_path: str,
            download_information_source: str = "official_acs",
            custom_download_information: Dict[str, Union[str, List[str]]] = None,
            enable_logger: bool = False
    ) -> None:
        """
        Download the chemical reaction classification dataset by (2013, Kraut, H., et al.).

        :parameter output_directory_path: The path to the directory where the downloaded data should be stored.
        :parameter download_information_source: The indicator of the download information source.
        :parameter custom_download_information: The custom download information.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the download of the chemical reaction classification dataset by (2013, Kraut, H., et al.)."
                )

            download_information = MISCELLANEOUS_DATA_DOWNLOAD_INFORMATION["v_2013_kraut_et_al"][
                download_information_source
            ] if custom_download_information is None else custom_download_information

            for url_file_path_index, url_file_path in enumerate(download_information["url_file_paths"]):
                DownloadUtilities.download_with_progress_bar(
                    url=download_information["base_url"] + url_file_path,
                    output_directory_path=output_directory_path,
                    description_message="Downloading file {0}/{1}".format(
                        url_file_path_index + 1,
                        len(download_information["url_file_paths"])
                    )
                )

            if enable_logger:
                getLogger(__name__).info(
                    "Completed the download of the chemical reaction classification dataset by "
                    "(2013, Kraut, H., et al.). The downloaded data is stored at: '{0}'.".format(
                        abspath(output_directory_path)
                    )
                )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.MiscellaneousDataDownloadUtilities.download_2013_kraut_et_al".format(__name__)
                ).exception(exception_handle)

            raise

    @staticmethod
    def download_2016_wei_et_al(
            output_directory_path: str,
            download_information_source: str = "official_github",
            custom_download_information: Dict[str, Union[str, List[str]]] = None,
            enable_logger: bool = False
    ) -> None:
        """
        Download the organic chemistry textbook questions dataset by (2016, Wei, J.N., et al.).

        :parameter output_directory_path: The path to the directory where the downloaded data should be stored.
        :parameter download_information_source: The indicator of the download information source.
        :parameter custom_download_information: The custom download information.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the download of the organic chemistry textbook questions dataset by "
                    "(2016, Wei, J.N., et al.)."
                )

            download_information = MISCELLANEOUS_DATA_DOWNLOAD_INFORMATION["v_2016_wei_et_al"][
                download_information_source
            ] if custom_download_information is None else custom_download_information

            for url_file_path_index, url_file_path in enumerate(download_information["url_file_paths"]):
                DownloadUtilities.download_with_progress_bar(
                    url=download_information["base_url"] + url_file_path,
                    output_directory_path=output_directory_path,
                    description_message="Downloading file {0}/{1}".format(
                        url_file_path_index + 1,
                        len(download_information["url_file_paths"])
                    )
                )

            if enable_logger:
                getLogger(__name__).info(
                    "Completed the download of the organic chemistry textbook questions dataset by "
                    "(2016, Wei, J.N., et al.). The downloaded data is stored at: '{0}'.".format(
                        abspath(output_directory_path)
                    )
                )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.MiscellaneousDataDownloadUtilities.download_2016_wei_et_al".format(__name__)
                ).exception(exception_handle)

            raise

    @staticmethod
    def download_2018_avramova_et_al(
            output_directory_path: str,
            download_information_source: str = "official_zenodo",
            custom_download_information: Dict[str, Union[str, List[str]]] = None,
            enable_logger: bool = False
    ) -> None:
        """
        Download the RetroTransformDB dataset by (2018, Avramova, S., et al.).

        :parameter output_directory_path: The path to the directory where the downloaded data should be stored.
        :parameter download_information_source: The indicator of the download information source.
        :parameter custom_download_information: The custom download information.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the download of the RetroTransformDB dataset by (2018, Avramova, S., et al.)."
                )

            download_information = MISCELLANEOUS_DATA_DOWNLOAD_INFORMATION["v_2018_avramova_et_al"][
                download_information_source
            ] if custom_download_information is None else custom_download_information

            for url_file_path_index, url_file_path in enumerate(download_information["url_file_paths"]):
                DownloadUtilities.download_with_progress_bar(
                    url=download_information["base_url"] + url_file_path,
                    output_directory_path=output_directory_path,
                    description_message="Downloading file {0}/{1}".format(
                        url_file_path_index + 1,
                        len(download_information["url_file_paths"])
                    )
                )

            if enable_logger:
                getLogger(__name__).info(
                    "Completed the download of the RetroTransformDB dataset by (2018, Avramova, S., et al.). "
                    "The downloaded data is stored at: '{0}'.".format(
                        abspath(output_directory_path)
                    )
                )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.MiscellaneousDataDownloadUtilities.download_2018_avramova_et_al".format(__name__)
                ).exception(exception_handle)

            raise
