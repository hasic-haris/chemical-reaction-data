""" The 'chemical_reaction_data.utilities.archive' package 'extraction' module. """

from logging import getLogger
from typing import Iterable


class ArchiveExtractionUtilities:
    """ The archive extraction utilities class. """

    @staticmethod
    def extract_from_zip_archive(
            archive_file_path: str,
            output_directory_path: str,
            archive_content_base_paths: Iterable[str] = None,
            enable_logger: bool = False
    ) -> None:
        """
        Extract the contents from a '.zip' archive file.

        :parameter archive_file_path: The path to the '.zip' archive file.
        :parameter output_directory_path: The path to the directory where the extracted contents should be stored.
        :parameter archive_content_base_paths: The base paths of the archive contents that should be extracted.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        """

        try:
            from zipfile import ZipFile

            with ZipFile(archive_file_path) as archive:
                if archive_content_base_paths is None:
                    archive.extractall(
                        path=output_directory_path
                    )

                else:
                    for file_path in archive.namelist():
                        if any(
                            file_path.startswith(archive_content_base_path)
                            for archive_content_base_path in archive_content_base_paths
                        ):
                            archive.extract(
                                member=file_path,
                                path=output_directory_path
                            )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.ArchiveExtractionUtilities.extract_from_zip_archive".format(__name__)
                ).exception(exception_handle)

            raise

    @staticmethod
    def extract_from_7z_archive(
            archive_file_path: str,
            output_directory_path: str,
            archive_content_base_paths: Iterable[str] = None,
            enable_logger: bool = False
    ) -> None:
        """
        Extract the contents from a '.7z' archive file.

        :parameter archive_file_path: The path to the '.7z' archive file.
        :parameter output_directory_path: The path to the directory where the extracted contents should be stored.
        :parameter archive_content_base_paths: The base paths of the archive contents that should be extracted.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        """

        try:
            from py7zr import SevenZipFile

            with SevenZipFile(archive_file_path) as archive:
                if archive_content_base_paths is None:
                    archive.extractall(
                        path=output_directory_path
                    )

                else:
                    archive_content_paths = list()

                    for file_path in archive.getnames():
                        if any(
                            file_path.startswith(archive_content_base_path)
                            for archive_content_base_path in archive_content_base_paths
                        ):
                            archive_content_paths.append(file_path)

                    if len(archive_content_paths) > 0:
                        archive.extract(
                            path=output_directory_path,
                            targets=archive_content_paths
                        )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.ArchiveExtractionUtilities.extract_from_7z_archive".format(__name__)
                ).exception(exception_handle)

            raise
