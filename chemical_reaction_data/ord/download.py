""" The 'chemical_reaction_data.ord' package 'download' module. """

from logging import getLogger
from typing import Dict, List, Union

from os.path import abspath

from .download_information import ORD_DOWNLOAD_INFORMATION

from ..utilities.download import DownloadUtilities


class OrdDownloadUtilities:
    """ The Open Reaction Database (ORD) download utilities class. """

    @staticmethod
    def download_2021_kearnes_et_al(
            output_directory_path: str,
            download_information_source: str = "official_github",
            custom_download_information: Dict[str, Union[str, List[str]]] = None,
            enable_logger: bool = False
    ) -> None:
        """
        Download the Open Reaction Database (ORD) by (2021, Kearnes, S.M., et al.).

        :parameter output_directory_path: The path to the directory where the downloaded data should be stored.
        :parameter download_information_source: The indicator of the download information source.
        :parameter custom_download_information: The custom download information.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the download of the Open Reaction Database (ORD) by (2021, Kearnes, S.M., et al.)."
                )

            download_information = ORD_DOWNLOAD_INFORMATION["v_2021_kearnes_et_al"][
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
                    "Completed the download of the Open Reaction Database (ORD) by (2021, Kearnes, S.M., et al.). "
                    "The downloaded data is stored at: '{0}'.".format(
                        abspath(output_directory_path)
                    )
                )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.OrdDownloadUtilities.download_2021_kearnes_et_al".format(__name__)
                ).exception(exception_handle)

            raise
