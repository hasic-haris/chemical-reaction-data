""" The 'chemical_reaction_data.miscellaneous' package 'preparation' module. """

from collections import defaultdict
from logging import getLogger
from os import listdir
from pandas import concat, DataFrame, read_csv

from os.path import abspath, join

from ..utilities.chemistry.reactions import ReactionFormatConversionUtilities


class MiscellaneousDataPreparationUtilities:
    """ The miscellaneous data preparation utilities class. """

    @staticmethod
    def prepare_2013_kraut_et_al(
            extracted_data_directory_path: str,
            output_directory_path: str = None,
            enable_logger: bool = False
    ) -> DataFrame:
        """
        Prepare the chemical reaction classification dataset by (2013, Kraut, H., et al.).

        :parameter extracted_data_directory_path: The path to the directory where the extracted data is stored.
        :parameter output_directory_path: The path to the directory where the prepared data should be stored.
        :parameter enable_logger: The indicator whether the logger should be enabled.

        :returns: The prepared chemical reaction classification dataset by (2013, Kraut, H., et al.).
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the preparation of the chemical reaction classification dataset by "
                    "(2013, Kraut, H., et al.)."
                )

            prepared_data_rows = defaultdict(list)

            for file_name in listdir(extracted_data_directory_path):
                if file_name.endswith(".rdf"):
                    with open(join(extracted_data_directory_path, file_name), "r") as file_handler:
                        file_contents = file_handler.read()

                        file_handler.close()

                    for reaction_rxn_block_without_identifier in file_contents.split("$RXN")[1:]:
                        reaction_rxn = ReactionFormatConversionUtilities.rxn_block_to_rxn(
                            reaction_rxn_block="$RXN{0}".format(reaction_rxn_block_without_identifier)
                        )

                        if reaction_rxn is not None:
                            reaction_smiles = ReactionFormatConversionUtilities.rxn_to_smiles(
                                reaction_rxn=reaction_rxn
                            )

                            if reaction_smiles is not None:
                                prepared_data_rows[file_name].append(
                                    reaction_smiles
                                )

            prepared_data = DataFrame(
                data={
                    "reaction_smiles": prepared_data_rows["MapTestExamplesV1.0.rdf"],
                    "reaction_smiles_icmap": prepared_data_rows["MapTestExamplesV1_ICMap.rdf"],
                    "reaction_smiles_icmap_reactant_copy": prepared_data_rows["MapTestExamplesV1_ICMapRctCpy.rdf"]
                }
            ).dropna(
                subset=[
                    "reaction_smiles",
                    "reaction_smiles_icmap",
                    "reaction_smiles_icmap_reactant_copy"
                ],
                how="all"
            ).drop_duplicates().reset_index(
                drop=True
            ).astype(
                dtype={
                    "reaction_smiles": str,
                    "reaction_smiles_icmap": str,
                    "reaction_smiles_icmap_reactant_copy": str
                }
            )

            if output_directory_path is None:
                if enable_logger:
                    getLogger(__name__).info(
                        "Completed the preparation of the chemical reaction classification dataset by "
                        "(2013, Kraut, H., et al.)."
                    )

                return prepared_data

            else:
                prepared_data.to_csv(
                    path_or_buf=join(output_directory_path, "2013_kraut_et_al.csv"),
                    index=False
                )

                if enable_logger:
                    getLogger(__name__).info(
                        "Completed the preparation of the chemical reaction classification dataset by "
                        "(2013, Kraut, H., et al.). The prepared data is stored at: '{0}'.".format(
                            abspath(join(output_directory_path, "2013_kraut_et_al.csv"))
                        )
                    )

                return prepared_data

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.MiscellaneousDataPreparationUtilities.prepare_2013_kraut_et_al".format(__name__)
                ).exception(exception_handle)

            raise

    @staticmethod
    def prepare_2016_wei_et_al_dataset(
            extracted_data_directory_path: str,
            output_directory_path: str = None,
            enable_logger: bool = False
    ) -> DataFrame:
        """
        Prepare the organic chemistry textbook questions dataset by (2016, Wei, J.N., et al.).

        :parameter extracted_data_directory_path: The path to the directory where the extracted data is stored.
        :parameter output_directory_path: The path to the directory where the prepared data should be stored.
        :parameter enable_logger: The indicator whether the logger should be enabled.

        :returns: The prepared organic chemistry textbook questions dataset by (2016, Wei, J.N., et al.).
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the preparation of the organic chemistry textbook questions dataset by "
                    "(2016, Wei, J.N., et al.)"
                )

            wade_8_47_data = read_csv(
                filepath_or_buffer=join(extracted_data_directory_path, "Wade8_47.ans_smi.txt"),
                header=None
            )

            wade_8_47_data.columns = [
                "reaction_smiles"
            ]

            wade_8_47_data["dataset_name"] = "wade_8_47"

            wade_8_48_data = read_csv(
                filepath_or_buffer=join(extracted_data_directory_path, "Wade8_48.ans_smi.txt"),
                header=None
            )

            wade_8_48_data.columns = [
                "reaction_smiles"
            ]

            wade_8_48_data["dataset_name"] = "wade_8_48"

            prepared_data = concat([
                wade_8_47_data,
                wade_8_48_data
            ])[[
                "dataset_name",
                "reaction_smiles"
            ]].dropna(
                subset=[
                    "reaction_smiles"
                ]
            ).drop_duplicates().reset_index(
                drop=True
            ).astype(
                dtype={
                    "dataset_name": str,
                    "reaction_smiles": str
                }
            )

            if output_directory_path is None:
                if enable_logger:
                    getLogger(__name__).info(
                        "Completed the preparation of the organic chemistry textbook questions dataset by "
                        "(2016, Wei, J.N., et al.)"
                    )

                return prepared_data

            else:
                prepared_data.to_csv(
                    path_or_buf=join(output_directory_path, "2016_wei_et_al.csv"),
                    index=False
                )

                if enable_logger:
                    getLogger(__name__).info(
                        "Completed the preparation of the organic chemistry textbook questions dataset by "
                        "(2016, Wei, J.N., et al.). The prepared data is stored at: '{0}'.".format(
                            abspath(join(output_directory_path, "2016_wei_et_al.csv"))
                        )
                    )

                return prepared_data

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.MiscellaneousDataPreparationUtilities.prepare_2016_wei_et_al".format(__name__)
                ).exception(exception_handle)

            raise

    @staticmethod
    def prepare_2018_avramova_et_al(
            extracted_data_directory_path: str,
            output_directory_path: str = None,
            enable_logger: bool = False
    ) -> DataFrame:
        """
        Prepare the RetroTransformDB dataset by (2018, Avramova, S., et al.).

        :parameter extracted_data_directory_path: The path to the directory where the extracted data is stored.
        :parameter output_directory_path: The path to the directory where the prepared data should be stored.
        :parameter enable_logger: The indicator whether the logger should be enabled.

        :returns: The prepared RetroTransformDB dataset by (2018, Avramova, S., et al.).
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the preparation of the RetroTransformDB dataset by (2018, Avramova, S., et al.)."
                )

            prepared_data = read_csv(
                filepath_or_buffer=join(extracted_data_directory_path, "RetroTransformDB-v-1-0.txt"),
                delimiter="\t"
            )

            prepared_data.columns = [
                "dataset_id",
                "reaction_transformation_name",
                "reaction_transformation_smirks",
                "reaction_transformation_functional_group",
                "reaction_transformation_type"
            ]

            prepared_data = prepared_data.dropna(
                subset=[
                    "reaction_transformation_smirks"
                ]
            ).sort_values(
                by=[
                    "dataset_id"
                ]
            ).drop_duplicates().reset_index(
                drop=True
            ).astype(
                dtype={
                    "dataset_id": int,
                    "reaction_transformation_name": str,
                    "reaction_transformation_smirks": str,
                    "reaction_transformation_functional_group": str,
                    "reaction_transformation_type": str
                }
            )

            if output_directory_path is None:
                if enable_logger:
                    getLogger(__name__).info(
                        "Completed the preparation of the RetroTransformDB dataset by (2018, Avramova, S., et al.)."
                    )

                return prepared_data

            else:
                prepared_data.to_csv(
                    path_or_buf=join(output_directory_path, "2018_avramova_et_al.csv"),
                    index=False
                )

                if enable_logger:
                    getLogger(__name__).info(
                        "Completed the preparation of the RetroTransformDB dataset by (2018, Avramova, S., et al.). "
                        "The prepared data is stored at: '{0}'.".format(
                            abspath(join(output_directory_path, "2018_avramova_et_al.csv"))
                        )
                    )

                return prepared_data

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.MiscellaneousDataPreparationUtilities.prepare_2018_avramova_et_al".format(__name__)
                ).exception(exception_handle)

            raise

    @staticmethod
    def prepare_grambow_2022_wen_et_al(
            extracted_data_directory_path: str,
            output_directory_path: str = None,
            enable_logger: bool = False
    ) -> DataFrame:
        """
        Prepare the Grambow dataset by (2022, Wen, M., et al.).

        :parameter extracted_data_directory_path: The path to the directory where the extracted data is stored.
        :parameter output_directory_path: The path to the directory where the prepared data should be stored.
        :parameter enable_logger: The indicator whether the logger should be enabled.

        :returns: The prepared Grambow dataset by (2022, Wen, M., et al.).
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the preparation of the Grambow dataset by (2022, Wen, M., et al.)."
                )

            train_data = read_csv(
                filepath_or_buffer=join(extracted_data_directory_path, "grambow_train.tsv"),
                delimiter="\t"
            )

            train_data.columns = [
                "reaction_smiles",
                "activation_energy",
                "reaction_enthalpy",
                "raw_id",
                "rmg_family",
                "reaction_type"
            ]

            train_data["dataset_name"] = "grambow_train"

            val_data = read_csv(
                filepath_or_buffer=join(extracted_data_directory_path, "grambow_val.tsv"),
                delimiter="\t"
            )

            val_data.columns = [
                "reaction_smiles",
                "activation_energy",
                "reaction_enthalpy",
                "raw_id",
                "rmg_family",
                "reaction_type"
            ]

            val_data["dataset_name"] = "grambow_val"

            test_data = read_csv(
                filepath_or_buffer=join(extracted_data_directory_path, "grambow_test.tsv"),
                delimiter="\t"
            )

            test_data.columns = [
                "reaction_smiles",
                "activation_energy",
                "reaction_enthalpy",
                "raw_id",
                "rmg_family",
                "reaction_type"
            ]

            test_data["dataset_name"] = "grambow_test"

            prepared_data = concat([
                train_data,
                val_data,
                test_data
            ])[[
                "dataset_name",
                "raw_id",
                "rmg_family",
                "reaction_type",
                "reaction_smiles",
                "activation_energy",
                "reaction_enthalpy"
            ]].dropna(
                subset=[
                    "reaction_smiles"
                ]
            ).sort_values(
                by=[
                    "raw_id"
                ]
            ).drop_duplicates().reset_index(
                drop=True
            ).astype(
                dtype={
                    "dataset_name": str,
                    "raw_id": int,
                    "rmg_family": str,
                    "reaction_type": int,
                    "reaction_smiles": str,
                    "activation_energy": float,
                    "reaction_enthalpy": float
                }
            )

            if output_directory_path is None:
                if enable_logger:
                    getLogger(__name__).info(
                        "Completed the preparation of the Grambow dataset by (2022, Wen, M., et al.)."
                    )

                return prepared_data

            else:
                prepared_data.to_csv(
                    path_or_buf=join(output_directory_path, "grambow_2022_wen_et_al.csv"),
                    index=False
                )

                if enable_logger:
                    getLogger(__name__).info(
                        "Completed the preparation of the Grambow dataset by (2022, Wen, M., et al.). "
                        "The prepared data is stored at: '{0}'.".format(
                            abspath(join(output_directory_path, "grambow_2022_wen_et_al.csv"))
                        )
                    )

                return prepared_data

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.MiscellaneousDataPreparationUtilities.prepare_grambow_2022_wen_et_al".format(__name__)
                ).exception(exception_handle)

            raise

    @staticmethod
    def prepare_tpl100_2022_wen_et_al(
            extracted_data_directory_path: str,
            output_directory_path: str = None,
            enable_logger: bool = False
    ) -> DataFrame:
        """
        Prepare the TPL100 dataset by (2022, Wen, M., et al.).

        :parameter extracted_data_directory_path: The path to the directory where the extracted data is stored.
        :parameter output_directory_path: The path to the directory where the prepared data should be stored.
        :parameter enable_logger: The indicator whether the logger should be enabled.

        :returns: The prepared TPL100 dataset by (2022, Wen, M., et al.).
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the preparation of the TPL100 dataset by (2022, Wen, M., et al.)."
                )

            train_data = read_csv(
                filepath_or_buffer=join(extracted_data_directory_path, "tpl100_train.tsv"),
                delimiter="\t"
            )

            train_data.columns = [
                "reaction_smiles",
                "reaction_type",
                "raw_id",
                "original_reaction_type"
            ]

            train_data["dataset_name"] = "tpl100_train"

            val_data = read_csv(
                filepath_or_buffer=join(extracted_data_directory_path, "tpl100_val.tsv"),
                delimiter="\t"
            )

            val_data.columns = [
                "reaction_smiles",
                "reaction_type",
                "raw_id",
                "original_reaction_type"
            ]

            val_data["dataset_name"] = "tpl100_val"

            test_data = read_csv(
                filepath_or_buffer=join(extracted_data_directory_path, "tpl100_test.tsv"),
                delimiter="\t"
            )

            test_data.columns = [
                "reaction_smiles",
                "reaction_type",
                "raw_id",
                "original_reaction_type"
            ]

            test_data["dataset_name"] = "tpl100_test"

            prepared_data = concat([
                train_data,
                val_data,
                test_data
            ])[[
                "dataset_name",
                "raw_id",
                "reaction_type",
                "original_reaction_type",
                "reaction_smiles"
            ]].dropna(
                subset=[
                    "reaction_smiles"
                ]
            ).sort_values(
                by=[
                    "raw_id"
                ]
            ).drop_duplicates().reset_index(
                drop=True
            ).astype(
                dtype={
                    "dataset_name": str,
                    "raw_id": int,
                    "reaction_type": int,
                    "original_reaction_type": int,
                    "reaction_smiles": str
                }
            )

            if output_directory_path is None:
                if enable_logger:
                    getLogger(__name__).info(
                        "Completed the preparation of the TPL100 dataset by (2022, Wen, M., et al.)."
                    )

                return prepared_data

            else:
                prepared_data.to_csv(
                    path_or_buf=join(output_directory_path, "tpl100_2022_wen_et_al.csv"),
                    index=False
                )

                if enable_logger:
                    getLogger(__name__).info(
                        "Completed the preparation of the TPL100 dataset by (2022, Wen, M., et al.). "
                        "The prepared data is stored at: '{0}'.".format(
                            abspath(join(output_directory_path, "tpl100_2022_wen_et_al.csv"))
                        )
                    )

                return prepared_data

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.MiscellaneousDataPreparationUtilities.prepare_tpl100_2022_wen_et_al".format(__name__)
                ).exception(exception_handle)

            raise
