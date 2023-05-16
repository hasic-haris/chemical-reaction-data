""" The 'chemical_reaction_data.rhea' package 'download' module. """

from logging import getLogger
from typing import Dict, List, Union

from os.path import abspath

from .download_information import RHEA_DATABASE_DOWNLOAD_INFORMATION

from ..utilities.download import DownloadUtilities


class RheaDatabaseDownloadUtilities:
    """ The Rhea database download utilities class. """

    @staticmethod
    def download_2022_bansal_et_al(
            output_directory_path: str,
            download_information_source: str = "official_ftp",
            custom_download_information: Dict[str, Union[str, List[str]]] = None,
            enable_logger: bool = False
    ) -> None:
        """
        Download the Rhea database by (2022, Bansal, P., et al.).

        :parameter output_directory_path: The path to the directory where the downloaded data should be stored.
        :parameter download_information_source: The indicator of the download information source.
        :parameter custom_download_information: The custom download information.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the download of the Rhea database by (2022, Bansal, P., et al.)."
                )

            download_information = RHEA_DATABASE_DOWNLOAD_INFORMATION["v_2022_bansal_et_al"][
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
                    "Completed the download of the Rhea database by (2022, Bansal, P., et al.). "
                    "The downloaded data is stored at: '{0}'.".format(
                        abspath(output_directory_path)
                    )
                )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.RheaDatabaseDownloadUtilities.download_2022_bansal_et_al".format(__name__)
                ).exception(exception_handle)

            raise
