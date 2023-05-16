""" The 'chemical_reaction_data.rhea_db' package 'preparation' module. """

from logging import getLogger
from pandas import read_csv

from os.path import abspath, join


class RheaDatabasePreparationUtilities:
    """ The Rhea database preparation utilities class. """

    @staticmethod
    def prepare_2022_bansal_et_al(
            extracted_data_directory_path: str,
            output_directory_path: str = None,
            enable_logger: bool = False
    ) -> None:
        """
        Prepare the Rhea database by (2022, Bansal, P., et al.).

        :parameter extracted_data_directory_path: The path to the directory where the extracted data is stored.
        :parameter output_directory_path: The path to the directory where the prepared data should be stored.
        :parameter enable_logger: The indicator whether the logger should be enabled.

        :returns: The prepared Rhea database by (2022, Bansal, P., et al.).
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the preparation of the Rhea database by (2022, Bansal, P., et al.)."
                )

            prepared_data = read_csv(
                filepath_or_buffer=join(extracted_data_directory_path, "rhea-reaction-smiles.tsv"),
                delimiter="\t",
                header=None
            )

            prepared_data.columns = [
                "database_id",
                "reaction_smiles"
            ]

            prepared_data = prepared_data.dropna(
                subset=[
                    "reaction_smiles"
                ]
            ).sort_values(
                by=[
                    "database_id"
                ]
            ).drop_duplicates().reset_index(
                drop=True
            ).astype(
                dtype={
                    "database_id": int,
                    "reaction_smiles": str
                }
            )

            if output_directory_path is None:
                if enable_logger:
                    getLogger(__name__).info(
                        "Completed the preparation of the Rhea database by (2022, Bansal, P., et al.)."
                    )

                return prepared_data

            else:
                prepared_data.to_csv(
                    path_or_buf=join(output_directory_path, "rhea_2022_bansal_et_al.csv"),
                    index=False
                )

                if enable_logger:
                    getLogger(__name__).info(
                        "Completed the preparation of the Rhea database by (2022, Bansal, P., et al.). "
                        "The prepared data is stored at: '{0}'.".format(
                            abspath(join(output_directory_path, "rhea_2022_bansal_et_al.csv"))
                        )
                    )

                return prepared_data

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.RheaDatabasePreparationUtilities.prepare_2022_bansal_et_al".format(__name__)
                ).exception(exception_handle)

            raise
