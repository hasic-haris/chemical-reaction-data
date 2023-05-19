""" The 'chemical_reaction_data.crd' package 'preparation' module. """

from logging import getLogger
from pandas import DataFrame, read_csv

from os.path import abspath, join


class CrdPreparationUtilities:
    """ The Chemical Reaction Database (CRD) preparation utilities class. """

    @staticmethod
    def prepare_2022_van_der_lingen(
            extracted_data_directory_path: str,
            output_directory_path: str = None,
            enable_logger: bool = False
    ) -> DataFrame:
        """
        Prepare the CRD by (2022, van der Lingen, R.).

        :parameter extracted_data_directory_path: The path to the directory where the extracted data is stored.
        :parameter output_directory_path: The path to the directory where the prepared data should be stored.
        :parameter enable_logger: The indicator whether the logger should be enabled.

        :returns: The prepared CRD by (2022, van der Lingen, R.).
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the preparation of the CRD by (2022, van der Lingen, R.)."
                )

            prepared_data = read_csv(
                filepath_or_buffer=join(extracted_data_directory_path, "reactionSmilesFigShare.txt"),
                header=None
            )

            prepared_data.columns = ["reaction_smiles"]

            prepared_data = prepared_data.dropna(
                subset=[
                    "reaction_smiles"
                ]
            ).drop_duplicates().reset_index(
                drop=True
            ).astype(
                dtype={
                    "reaction_smiles": str
                }
            )

            if output_directory_path is None:
                if enable_logger:
                    getLogger(__name__).info(
                        "Completed the preparation of the CRD by (2022, van der Lingen, R.)."
                    )

                return prepared_data

            else:
                prepared_data.to_csv(
                    path_or_buf=join(output_directory_path, "crd_2022_van_der_lingen.csv"),
                    index=False
                )

                if enable_logger:
                    getLogger(__name__).info(
                        "Completed the preparation of the CRD by (2022, van der Lingen, R.)."
                        "The prepared data is stored at: '{0}'.".format(
                            abspath(join(output_directory_path, "crd_2022_van_der_lingen.csv"))
                        )
                    )

                return prepared_data

        except Exception as exception_handle:
            getLogger(
                "{0}.CrdPreparationUtilities.prepare_2022_van_der_lingen".format(__name__)
            ).exception(exception_handle)

            raise
