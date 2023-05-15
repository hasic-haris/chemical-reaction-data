""" The 'chemical_reaction_data.utilities.download' package 'download' module. """

from logging import getLogger
from tqdm import tqdm
from typing import Optional

from os.path import basename, join
from urllib.request import urlretrieve


class _DownloadUtilitiesTqdm(tqdm):
    """ The download utilities 'tqdm' class wrapper. """

    def urlretrieve_reporthook_update(
            self,
            number_of_transferred_blocks: int = 1,
            block_size: int = 1,
            total_size: int = None
    ) -> Optional[bool]:
        """
        The 'tqdm' class 'update' method wrapper for the 'urllib.request.urlretrieve' function 'reporthook' argument.

        :parameter number_of_transferred_blocks: The number of blocks transferred so far.
        :parameter block_size: Size of each block in 'tqdm' units.
        :parameter total_size: Total size in 'tqdm' units.
        """

        if total_size is not None:
            self.total = total_size

        return self.update(number_of_transferred_blocks * block_size - self.n)


class DownloadUtilities:
    """ The download utilities class. """

    @staticmethod
    def download(
            url: str,
            output_directory_path: str,
            enable_logger: bool = False
    ) -> None:
        """
        Download the contents from a URL string.

        :parameter url: The URL string.
        :parameter output_directory_path: The path to the directory where the downloaded contents should be stored.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        """

        try:
            urlretrieve(
                url=url,
                filename=join(output_directory_path, basename(url))
            )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.DownloadUtilities.download".format(__name__)
                ).exception(exception_handle)

            raise

    @staticmethod
    def download_with_progress_bar(
            url: str,
            output_directory_path: str,
            description_message: str = None,
            enable_logger: bool = False
    ) -> None:
        """
        Download the contents from a URL string, and visualize the progress with a progress bar.

        :parameter url: The URL string.
        :parameter output_directory_path: The path to the directory where the downloaded contents should be stored.
        :parameter description_message: The progress bar description message.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        """

        try:
            with _DownloadUtilitiesTqdm(
                unit="B",
                unit_scale=True,
                miniters=1,
                ascii=True,
                ncols=150,
                desc="{0}".format(
                    description_message if description_message is not None else "Downloading"
                )
            ) as progress_bar:
                urlretrieve(
                    url=url,
                    filename=join(output_directory_path, basename(url)),
                    reporthook=progress_bar.urlretrieve_reporthook_update
                )

                progress_bar.total = progress_bar.n

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.DownloadUtilities.download_with_progress_bar".format(__name__)
                ).exception(exception_handle)

            raise
