""" The 'chemical_reaction_data.uspto' package 'download' module. """

from logging import getLogger
from typing import Dict, List, Union

from os.path import abspath

from .download_information import USPTO_DATASET_DOWNLOAD_INFORMATION

from ..utilities.download import DownloadUtilities


class UsptoDatasetDownloadUtilities:
    """ The United States Patent and Trademark Office (USPTO) dataset download utilities class. """

    @staticmethod
    def download_1976_2013_2014_lowe(
            output_directory_path: str,
            download_information_source: str = "official_figshare",
            custom_download_information: Dict[str, Union[str, List[str]]] = None,
            enable_logger: bool = False
    ) -> None:
        """
        Download the USPTO (1976-2013) dataset by (2014, Lowe, D.M.).

        :parameter output_directory_path: The path to the directory where the downloaded data should be stored.
        :parameter download_information_source: The indicator of the download information source.
        :parameter custom_download_information: The custom download information.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the download of the USPTO (1976-2013) dataset by (2014, Lowe, D.M.)."
                )

            download_information = USPTO_DATASET_DOWNLOAD_INFORMATION["v_1976_2013_2014_lowe"][
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
                    "Completed the download of the USPTO (1976-2013) dataset by (2014, Lowe, D.M.). "
                    "The downloaded data is stored at: '{0}'.".format(
                        abspath(output_directory_path)
                    )
                )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.UsptoDatasetDownloadUtilities.download_1976_2013_2014_lowe".format(__name__)
                ).exception(exception_handle)

            raise

    @staticmethod
    def download_50k_2016_schneider_et_al(
            output_directory_path: str,
            download_information_source: str = "official_acs",
            custom_download_information: Dict[str, Union[str, List[str]]] = None,
            enable_logger: bool = False
    ) -> None:
        """
        Download the USPTO-50k dataset by (2016, Schneider, N., et al.).

        :parameter output_directory_path: The path to the directory where the downloaded data should be stored.
        :parameter download_information_source: The indicator of the download information source.
        :parameter custom_download_information: The custom download information.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the download of the USPTO-50k dataset by (2016, Schneider, N., et al.)."
                )

            download_information = USPTO_DATASET_DOWNLOAD_INFORMATION["v_50k_2016_schneider_et_al"][
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
                    "Completed the download of the USPTO-50k dataset by (2016, Schneider, N., et al.). "
                    "The downloaded data is stored at: '{0}'.".format(
                        abspath(output_directory_path)
                    )
                )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.UsptoDatasetDownloadUtilities.download_50k_2016_schneider_et_al".format(__name__)
                ).exception(exception_handle)

            raise

    @staticmethod
    def download_15k_2017_coley_et_al(
            output_directory_path: str,
            download_information_source: str = "unofficial_github",
            custom_download_information: Dict[str, Union[str, List[str]]] = None,
            enable_logger: bool = False
    ) -> None:
        """
        Download the USPTO-15k dataset by (2017, Coley, C.W., et al.).

        :parameter output_directory_path: The path to the directory where the downloaded data should be stored.
        :parameter download_information_source: The indicator of the download information source.
        :parameter custom_download_information: The custom download information.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the download of the USPTO-15k dataset by (2017, Coley, C.W., et al.)."
                )

            download_information = USPTO_DATASET_DOWNLOAD_INFORMATION["v_15k_2017_coley_et_al"][
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
                    "Completed the download of the USPTO-15k dataset by (2017, Coley, C.W., et al.). "
                    "The downloaded data is stored at: '{0}'.".format(
                        abspath(output_directory_path)
                    )
                )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.UsptoDatasetDownloadUtilities.download_15k_2017_coley_et_al".format(__name__)
                ).exception(exception_handle)

            raise

    @staticmethod
    def download_1976_2016_2017_lowe(
            output_directory_path: str,
            download_information_source: str = "official_figshare",
            custom_download_information: Dict[str, Union[str, List[str]]] = None,
            enable_logger: bool = False
    ) -> None:
        """
        Download the USPTO (1976-2016) dataset by (2017, Lowe, D.M.).

        :parameter output_directory_path: The path to the directory where the downloaded data should be stored.
        :parameter download_information_source: The indicator of the download information source.
        :parameter custom_download_information: The custom download information.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the download of the USPTO (1976-2016) dataset by (2017, Lowe, D.M.)."
                )

            download_information = USPTO_DATASET_DOWNLOAD_INFORMATION["v_1976_2016_2017_lowe"][
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
                    "Completed the download of the USPTO (1976-2016) dataset by (2017, Lowe, D.M.). "
                    "The downloaded data is stored at: '{0}'.".format(
                        abspath(output_directory_path)
                    )
                )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.UsptoDatasetDownloadUtilities.download_1976_2016_2017_lowe".format(__name__)
                ).exception(exception_handle)

            raise

    @staticmethod
    def download_50k_2017_coley_et_al(
            output_directory_path: str,
            download_information_source: str = "official_github",
            custom_download_information: Dict[str, Union[str, List[str]]] = None,
            enable_logger: bool = False
    ) -> None:
        """
        Download the USPTO-50k dataset by (2017, Coley, C.W., et al.).

        :parameter output_directory_path: The path to the directory where the downloaded data should be stored.
        :parameter download_information_source: The indicator of the download information source.
        :parameter custom_download_information: The custom download information.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the download of the USPTO-50k dataset by (2017, Coley, C.W., et al.)."
                )

            download_information = USPTO_DATASET_DOWNLOAD_INFORMATION["v_50k_2017_coley_et_al"][
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
                    "Completed the download of the USPTO-50k dataset by (2017, Coley, C.W., et al.). "
                    "The downloaded data is stored at: '{0}'.".format(
                        abspath(output_directory_path)
                    )
                )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.UsptoDatasetDownloadUtilities.download_50k_2017_coley_et_al".format(__name__)
                ).exception(exception_handle)

            raise

    @staticmethod
    def download_mit_2017_jin_et_al(
            output_directory_path: str,
            download_information_source: str = "official_github",
            custom_download_information: Dict[str, Union[str, List[str]]] = None,
            enable_logger: bool = False
    ) -> None:
        """
        Download the USPTO-MIT dataset by (2017, Jin, W., et al.).

        :parameter output_directory_path: The path to the directory where the downloaded data should be stored.
        :parameter download_information_source: The indicator of the download information source.
        :parameter custom_download_information: The custom download information.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the download of the USPTO-MIT dataset by (2017, Jin, W., et al.)."
                )

            download_information = USPTO_DATASET_DOWNLOAD_INFORMATION["v_mit_2017_jin_et_al"][
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
                    "Completed the download of the USPTO-MIT dataset by (2017, Jin, W., et al.). "
                    "The downloaded data is stored at: '{0}'.".format(
                        abspath(output_directory_path)
                    )
                )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.UsptoDatasetDownloadUtilities.download_mit_2017_jin_et_al".format(__name__)
                ).exception(exception_handle)

            raise
