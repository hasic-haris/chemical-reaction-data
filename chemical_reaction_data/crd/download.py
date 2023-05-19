""" The 'chemical_reaction_data.crd' package 'download' module. """

from logging import getLogger
from typing import Dict, List, Union

from os.path import abspath

from .download_information import CRD_DOWNLOAD_INFORMATION

from ..utilities.download import DownloadUtilities


class CrdDownloadUtilities:
    """ The Chemical Reaction Database (CRD) download utilities class. """

    @staticmethod
    def download_2022_van_der_lingen(
            output_directory_path: str,
            download_information_source: str = "official_figshare",
            custom_download_information: Dict[str, Union[str, List[str]]] = None,
            enable_logger: bool = False
    ) -> None:
        """
        Download the CRD by (2022, van der Lingen, R.).

        :parameter output_directory_path: The path to the directory where the downloaded data should be stored.
        :parameter download_information_source: The indicator of the download information source.
        :parameter custom_download_information: The custom download information.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the download of the CRD by (2022, van der Lingen, R.)."
                )

            download_information = CRD_DOWNLOAD_INFORMATION["v_2022_van_der_lingen"][
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
                    "Completed the download of the CRD by (2022, van der Lingen, R.). "
                    "The downloaded data is stored at: '{0}'.".format(
                        abspath(output_directory_path)
                    )
                )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.CrdDownloadUtilities.download_2022_van_der_lingen".format(__name__)
                ).exception(exception_handle)

            raise
