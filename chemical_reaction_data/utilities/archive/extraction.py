""" The 'chemical_reaction_data.utilities.archive' package 'extraction' module. """

from logging import getLogger
from typing import Iterable


class ArchiveExtractionUtilities:
    """ The archive extraction utilities class. """

    @staticmethod
    def extract_from_7z_archive(
            archive_file_path: str,
            output_directory_path: str,
            archive_file_content_base_paths: Iterable[str] = None,
            enable_logger: bool = False
    ) -> None:
        """
        Extract the contents from a '.7z' archive file.

        :parameter archive_file_path: The path to the archive file.
        :parameter output_directory_path: The path to the directory where the extracted archive file contents should be
                                          stored.
        :parameter archive_file_content_base_paths: The base paths of the archive file contents that should be
                                                    extracted.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        """

        try:
            from py7zr import SevenZipFile

            with SevenZipFile(archive_file_path) as archive:
                if archive_file_content_base_paths is None:
                    archive.extractall(
                        path=output_directory_path
                    )

                else:
                    archive_file_content_paths = list()

                    for archive_file_content_path in archive.getnames():
                        if any(
                            archive_file_content_path.startswith(archive_file_content_base_path)
                            for archive_file_content_base_path in archive_file_content_base_paths
                        ):
                            archive_file_content_paths.append(
                                archive_file_content_path
                            )

                    if len(archive_file_content_paths) > 0:
                        archive.extract(
                            path=output_directory_path,
                            targets=archive_file_content_paths
                        )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.ArchiveExtractionUtilities.extract_from_7z_archive".format(__name__)
                ).exception(exception_handle)

            raise

    @staticmethod
    def extract_from_tar_gz_archive(
            archive_file_path: str,
            output_directory_path: str,
            archive_file_content_base_paths: Iterable[str] = None,
            enable_logger: bool = False
    ) -> None:
        """
        Extract the contents from a '.tar.gz' archive file.

        :parameter archive_file_path: The path to the archive file.
        :parameter output_directory_path: The path to the directory where the extracted archive file contents should be
                                          stored.
        :parameter archive_file_content_base_paths: The base paths of the archive file contents that should be
                                                    extracted.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        """

        try:
            from tarfile import open

            with open(archive_file_path, "r:gz") as archive:
                if archive_file_content_base_paths is None:
                    archive.extractall(
                        path=output_directory_path
                    )

                else:
                    for archive_file_content_path in archive.getnames():
                        if any(
                            archive_file_content_path.startswith(archive_file_content_base_path)
                            for archive_file_content_base_path in archive_file_content_base_paths
                        ):
                            archive.extract(
                                member=archive_file_content_path,
                                path=output_directory_path
                            )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.ArchiveExtractionUtilities.extract_from_tar_gz_archive".format(__name__)
                ).exception(exception_handle)

            raise

    @staticmethod
    def extract_from_zip_archive(
            archive_file_path: str,
            output_directory_path: str,
            archive_file_content_base_paths: Iterable[str] = None,
            enable_logger: bool = False
    ) -> None:
        """
        Extract the contents from a '*.zip' archive file.

        :parameter archive_file_path: The path to the archive file.
        :parameter output_directory_path: The path to the directory where the extracted archive file contents should be
                                          stored.
        :parameter archive_file_content_base_paths: The base paths of the archive file contents that should be
                                                    extracted.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        """

        try:
            from zipfile import ZipFile

            with ZipFile(archive_file_path) as archive:
                if archive_file_content_base_paths is None:
                    archive.extractall(
                        path=output_directory_path
                    )

                else:
                    for archive_file_content_path in archive.namelist():
                        if any(
                            archive_file_content_path.startswith(archive_file_content_base_path)
                            for archive_file_content_base_path in archive_file_content_base_paths
                        ):
                            archive.extract(
                                member=archive_file_content_path,
                                path=output_directory_path
                            )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.ArchiveExtractionUtilities.extract_from_zip_archive".format(__name__)
                ).exception(exception_handle)

            raise
