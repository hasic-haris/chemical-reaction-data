""" The 'chemical_reaction_data.ord' package 'preparation' module. """

from logging import getLogger
from os import walk
from pandas import DataFrame
from tqdm import tqdm

from os.path import abspath, join

from ord_schema import message_helpers

from ord_schema.proto.dataset_pb2 import Dataset

from .parsing import OrdParsingUtilities

from ..utilities.multiprocessing import MultiprocessingUtilities


class OrdPreparationUtilities:
    """ The Open Reaction Database (ORD) preparation utilities class. """

    @staticmethod
    def prepare_2021_kearnes_et_al(
            extracted_data_directory_path: str,
            output_directory_path: str = None,
            number_of_cpu_cores: int = 1,
            enable_logger: bool = False
    ) -> DataFrame:
        """
        Prepare the Open Reaction Database (ORD) by (2021, Kearnes, S.M., et al.).

        :parameter extracted_data_directory_path: The path to the directory where the extracted data is stored.
        :parameter output_directory_path: The path to the directory where the prepared data should be stored.
        :parameter number_of_cpu_cores: The number of CPU cores that should be utilized.
        :parameter enable_logger: The indicator whether the logger should be enabled.

        :returns: The prepared Open Reaction Database (ORD) by (2021, Kearnes, S.M., et al.).
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the preparation of the Open Reaction Database (ORD) by (2021, Kearnes, S.M., et al.)."
                )

            prepared_data_rows = list()

            it = 0

            for directory_path, _, directory_file_names in walk(extracted_data_directory_path):
                it += 1

                if it > 4:
                    break

                if any(directory_file_name.endswith(".pb.gz") for directory_file_name in directory_file_names):
                    for directory_file_name in tqdm(
                        iterable=directory_file_names,
                        total=len(directory_file_names),
                        ascii=True,
                        ncols=150,
                        desc="Parsing '{0}' directory '*.pb.gz' files".format(directory_path.split("/")[-1])
                    ):
                        dataset_message = message_helpers.load_message(
                            filename=join(directory_path, directory_file_name),
                            message_type=Dataset
                        )

                        dataset_message_contents = MultiprocessingUtilities.run(
                            processing_procedure=OrdParsingUtilities.parse_reaction_message,
                            primary_input_arguments=dataset_message.reactions,
                            number_of_cpu_cores=number_of_cpu_cores,
                            enable_logger=enable_logger
                        )

                        prepared_data_rows.extend([(
                            directory_path.split("/")[-1],
                            dataset_message.dataset_id,
                            dataset_message.name,
                            dataset_message_content[0],
                            dataset_message_content[1],
                            dataset_message_content[2]
                        ) for dataset_message_content in dataset_message_contents])

            prepared_data = DataFrame(
                data=prepared_data_rows,
                columns=[
                    "dataset_directory_name",
                    "dataset_id",
                    "dataset_name",
                    "reaction_id",
                    "reaction_identifiers_smiles",
                    "reaction_inputs_and_outcomes_smiles"
                ]
            ).dropna(
                subset=[
                    "reaction_identifiers_smiles",
                    "reaction_inputs_and_outcomes_smiles"
                ],
                how="all"
            ).sort_values(
                by=[
                    "dataset_directory_name",
                    "dataset_id",
                    "dataset_name",
                    "reaction_id"
                ]
            ).drop_duplicates().reset_index(
                drop=True
            ).astype(
                dtype={
                    "dataset_directory_name": str,
                    "dataset_id": str,
                    "dataset_name": str,
                    "reaction_id": str,
                    "reaction_identifiers_smiles": str,
                    "reaction_inputs_and_outcomes_smiles": str
                }
            )

            if output_directory_path is None:
                if enable_logger:
                    getLogger(__name__).info(
                        "Completed the preparation of the Open Reaction Database (ORD) by "
                        "(2021, Kearnes, S.M., et al.)."
                    )

                return prepared_data

            else:
                prepared_data.to_csv(
                    path_or_buf=join(output_directory_path, "ord_2021_kearnes_et_al.csv"),
                    index=False
                )

                if enable_logger:
                    getLogger(__name__).info(
                        "Completed the preparation of the Open Reaction Database (ORD) by "
                        "(2021, Kearnes, S.M., et al.). The prepared data is stored at: '{0}'.".format(
                            abspath(join(output_directory_path, "ord_2021_kearnes_et_al.csv"))
                        )
                    )

                return prepared_data

        except Exception as exception_handle:
            getLogger(
                "{0}.OrdPreparationUtilities.prepare_2021_kearnes_et_al".format(__name__)
            ).exception(exception_handle)

            raise
