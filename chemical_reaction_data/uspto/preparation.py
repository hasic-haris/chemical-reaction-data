""" The 'chemical_reaction_datasets.uspto' package 'preparation' module. """

from logging import getLogger
from pandas import concat, DataFrame, read_csv
from os import walk
from tqdm import tqdm

from os.path import abspath, join
from xml.etree.ElementTree import parse

from .parsing import UsptoDatasetParsingUtilities

from ..utilities.multiprocessing import MultiprocessingUtilities


class UsptoDatasetPreparationUtils:
    """ The United States Patent and Trademark Office (USPTO) dataset preparation utility class. """

    @staticmethod
    def prepare_1976_2013_2014_lowe(
            extracted_data_directory_path: str,
            output_directory_path: str = None,
            enable_logger: bool = False
    ) -> DataFrame:
        """
        Prepare the USPTO (1976-2013) dataset by (2014, Lowe, D.M.).

        :parameter extracted_data_directory_path: The path to the directory where the extracted data is stored.
        :parameter output_directory_path: The path to the directory where the prepared data should be stored.
        :parameter enable_logger: The indicator whether the logger should be enabled.

        :returns: The prepared USPTO (1976-2013) dataset by (2014, Lowe, D.M.).
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the preparation of the USPTO (1976-2013) dataset by (2014, Lowe, D.M.)."
                )

            grants_data = read_csv(
                filepath_or_buffer=join(
                    extracted_data_directory_path,
                    "1976-2013_USPTOgrants_reactionSmiles_feb2014filters.rsmi"
                ),
                delimiter="\t",
                header=None,
                dtype={
                    0: str,
                    1: str,
                    2: str
                }
            )

            grants_data.columns = [
                "reaction_smiles",
                "patent_document_id",
                "patent_document_paragraph_id"
            ]

            grants_data["patent_document_category"] = "grants"

            applications_data = read_csv(
                filepath_or_buffer=join(
                    extracted_data_directory_path,
                    "2001-2013_USPTOapplications_reactionSmiles_feb2014filters.rsmi"
                ),
                delimiter="\t",
                header=None,
                dtype={
                    0: str,
                    1: str,
                    2: str
                }
            )

            applications_data.columns = [
                "reaction_smiles",
                "patent_document_id",
                "patent_document_paragraph_id"
            ]

            applications_data["patent_document_category"] = "applications"

            prepared_data = concat([
                grants_data,
                applications_data
            ])[[
                "patent_document_category",
                "patent_document_id",
                "patent_document_paragraph_id",
                "reaction_smiles"
            ]].dropna(
                subset=[
                    "reaction_smiles"
                ]
            ).sort_values(
                by=[
                    "patent_document_category",
                    "patent_document_id",
                    "patent_document_paragraph_id"
                ],
                ascending=[
                    False,
                    True,
                    True
                ]
            ).drop_duplicates().reset_index(
                drop=True
            ).astype(
                dtype={
                    "patent_document_category": str,
                    "patent_document_id": str,
                    "patent_document_paragraph_id": str,
                    "reaction_smiles": str
                }
            )

            if output_directory_path is None:
                if enable_logger:
                    getLogger(__name__).info(
                        "Completed the preparation of the USPTO (1976-2013) dataset by (2014, Lowe, D.M.)."
                    )

                return prepared_data

            else:
                prepared_data.to_csv(
                    path_or_buf=join(output_directory_path, "uspto_1976_2013_2014_lowe_rsmi.csv"),
                    index=False
                )

                if enable_logger:
                    getLogger(__name__).info(
                        "Completed the preparation of the USPTO (1976-2013) dataset by (2014, Lowe, D.M.). "
                        "The prepared data is stored at: '{0}'.".format(
                            abspath(join(output_directory_path, "uspto_1976_2013_2014_lowe_rsmi.csv"))
                        )
                    )

            return prepared_data

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.UsptoDatasetPreparationUtils.prepare_1976_2013_2014_lowe".format(__name__)
                ).exception(exception_handle)

            raise

    @staticmethod
    def prepare_50k_2016_schneider_et_al(
            extracted_data_directory_path: str,
            output_directory_path: str = None,
            enable_logger: bool = False
    ) -> DataFrame:
        """
        Prepare the USPTO-50k dataset by (2016, Schneider, N., et al.).

        :parameter extracted_data_directory_path: The path to the directory where the extracted data is stored.
        :parameter output_directory_path: The path to the directory where the prepared data should be stored.
        :parameter enable_logger: The indicator whether the logger should be enabled.

        :returns: The prepared USPTO-50k dataset by (2016, Schneider, N., et al.).
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the preparation of the USPTO-50k dataset by (2016, Schneider, N., et al.)."
                )

            dataset_a_data = read_csv(
                filepath_or_buffer=join(extracted_data_directory_path, "dataSetA.csv")
            )[[
                "patentID",
                "rxn_Class",
                "rxn_Smiles"
            ]]

            dataset_a_data.columns = [
                "patent_document_id",
                "reaction_class",
                "reaction_smiles_name_rxn"
            ]

            dataset_a_data["dataset_name"] = "A"
            dataset_a_data["reaction_smiles_indigo"] = None
            dataset_a_data["reaction_smiles_indigo_knime"] = None

            dataset_b_data = read_csv(
                filepath_or_buffer=join(extracted_data_directory_path, "dataSetB.csv")
            )[[
                "patentID",
                "rxn_Class",
                "rxnSmiles_Mapping_NameRxn",
                "rxnSmiles_Mapping_IndigoTK",
                "rxnSmiles_IndigoAutoMapperKNIME"
            ]]

            dataset_b_data.columns = [
                "patent_document_id",
                "reaction_class",
                "reaction_smiles_name_rxn",
                "reaction_smiles_indigo",
                "reaction_smiles_indigo_knime"
            ]

            dataset_b_data["dataset_name"] = "B"

            prepared_data = concat([
                dataset_a_data,
                dataset_b_data
            ])[[
                "dataset_name",
                "patent_document_id",
                "reaction_class",
                "reaction_smiles_name_rxn",
                "reaction_smiles_indigo",
                "reaction_smiles_indigo_knime"
            ]].dropna(
                subset=[
                    "reaction_smiles_name_rxn",
                    "reaction_smiles_indigo",
                    "reaction_smiles_indigo_knime"
                ],
                how="all"
            ).sort_values(
                by=[
                    "dataset_name",
                    "patent_document_id",
                    "reaction_class"
                ]
            ).drop_duplicates().reset_index(
                drop=True
            ).astype(
                dtype={
                    "dataset_name": str,
                    "patent_document_id": str,
                    "reaction_class": int,
                    "reaction_smiles_name_rxn": str,
                    "reaction_smiles_indigo": str,
                    "reaction_smiles_indigo_knime": str
                }
            )

            if output_directory_path is None:
                if enable_logger:
                    getLogger(__name__).info(
                        "Completed the preparation of the USPTO-50k dataset by (2016, Schneider, N., et al.)."
                    )

                return prepared_data

            else:
                prepared_data.to_csv(
                    path_or_buf=join(output_directory_path, "uspto_50k_2016_schneider_et_al.csv"),
                    index=False
                )

                if enable_logger:
                    getLogger(__name__).info(
                        "Completed the preparation of the USPTO-50k dataset by (2016, Schneider, N., et al.). "
                        "The prepared data is stored at: '{0}'.".format(
                            abspath(join(output_directory_path, "uspto_50k_2016_schneider_et_al.csv"))
                        )
                    )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.UsptoDatasetPreparationUtils.prepare_50k_2016_schneider_et_al".format(__name__)
                ).exception(exception_handle)

            raise

    @staticmethod
    def prepare_15k_2017_coley_et_al(
            extracted_data_directory_path: str,
            output_directory_path: str = None,
            enable_logger: bool = False
    ) -> DataFrame:
        """
        Prepare the USPTO-15k dataset by (2017, Coley, C.W., et al.).

        :parameter extracted_data_directory_path: The path to the directory where the extracted data is stored.
        :parameter output_directory_path: The path to the directory where the prepared data should be stored.
        :parameter enable_logger: The indicator whether the logger should be enabled.

        :returns: The prepared USPTO-15k dataset by (2017, Coley, C.W., et al.).
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the preparation of the USPTO-15k dataset by (2017, Coley, C.W., et al.)."
                )

            train_data = read_csv(
                filepath_or_buffer=join(extracted_data_directory_path, "train.txt"),
                delimiter="\t",
                header=None
            ).iloc[:, [0]]

            train_data.columns = [
                "reaction_smiles"
            ]

            train_data["dataset_name"] = "train"

            valid_data = read_csv(
                filepath_or_buffer=join(extracted_data_directory_path, "valid.txt"),
                delimiter="\t",
                header=None
            ).iloc[:, [0]]

            valid_data.columns = [
                "reaction_smiles"
            ]

            valid_data["dataset_name"] = "valid"

            test_data = read_csv(
                filepath_or_buffer=join(extracted_data_directory_path, "test.txt"),
                delimiter="\t",
                header=None
            ).iloc[:, [0]]

            test_data.columns = [
                "reaction_smiles"
            ]

            test_data["dataset_name"] = "test"

            prepared_data = concat([
                train_data,
                valid_data,
                test_data
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
                        "Completed the preparation of the USPTO-15k dataset by (2017, Coley, C.W., et al.)."
                    )

                return prepared_data

            else:
                prepared_data.to_csv(
                    path_or_buf=join(output_directory_path, "uspto_15k_2017_coley_et_al.csv"),
                    index=False
                )

                if enable_logger:
                    getLogger(__name__).info(
                        "Completed the preparation of the USPTO-15k dataset by (2017, Coley, C.W., et al.). "
                        "The prepared data is stored at: '{0}'.".format(
                            abspath(join(output_directory_path, "uspto_15k_2017_coley_et_al.csv"))
                        )
                    )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.UsptoDatasetPreparationUtils.prepare_15k_2017_coley_et_al".format(__name__)
                ).exception(exception_handle)

            raise

    @staticmethod
    def prepare_1976_2016_2017_lowe(
            extracted_data_directory_path: str,
            output_directory_path: str = None,
            parse_xml_files: bool = True,
            number_of_cpu_cores: int = 1,
            enable_logger: bool = False
    ) -> DataFrame:
        """
        Prepare the USPTO (1976-2016) dataset by (2017, Lowe, D.M.).

        :parameter extracted_data_directory_path: The path to the directory where the extracted data is stored.
        :parameter output_directory_path: The path to the directory where the prepared data should be stored.
        :parameter parse_xml_files: The indicator whether '*.xml' files should be parsed instead of '*.rsmi' files.
        :parameter number_of_cpu_cores: The number of CPU cores that should be utilized.
        :parameter enable_logger: The indicator whether the logger should be enabled.

        :returns: The prepared USPTO (1976-2016) dataset by (2017, Lowe, D.M.).
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the preparation of the USPTO (1976-2016) dataset by (2017, Lowe, D.M.)."
                )

            if parse_xml_files:
                prepared_data_rows = list()

                for directory_path, _, file_names in walk(extracted_data_directory_path):
                    if any(file_name.endswith(".xml") for file_name in file_names):
                        for file_name in tqdm(
                                iterable=file_names,
                                total=len(file_names),
                                ascii=True,
                                ncols=150,
                                desc="Parsing the '{0}/{1}' directory '*.xml' files".format(
                                    directory_path.split("/")[-2],
                                    directory_path.split("/")[-1]
                                )
                        ):
                            xml_element_tree = parse(
                                source=join(directory_path, file_name)
                            )

                            xml_element_tree_contents = MultiprocessingUtilities.run(
                                processing_procedure=UsptoDatasetParsingUtilities.parse_xml_element,
                                primary_input_arguments=xml_element_tree.getroot(),
                                number_of_cpu_cores=number_of_cpu_cores,
                                enable_logger=enable_logger
                            )

                            prepared_data_rows.extend((
                                directory_path.split("/")[-2],
                                int(directory_path.split("/")[-1]),
                                xml_element_tree_content[0],
                                xml_element_tree_content[1],
                                xml_element_tree_content[2]
                            ) for xml_element_tree_content in xml_element_tree_contents)

                prepared_data = DataFrame(
                    data=prepared_data_rows,
                    columns=[
                        "patent_document_category",
                        "patent_document_publication_year",
                        "patent_document_id",
                        "patent_document_paragraph_id",
                        "reaction_smiles"
                    ]
                ).dropna(
                    subset=[
                        "reaction_smiles"
                    ]
                ).sort_values(
                    by=[
                        "patent_document_category",
                        "patent_document_publication_year",
                        "patent_document_id",
                        "patent_document_paragraph_id"
                    ],
                    ascending=[
                        False,
                        True,
                        True,
                        True
                    ]
                ).drop_duplicates().reset_index(
                    drop=True
                ).astype(
                    dtype={
                        "patent_document_category": str,
                        "patent_document_publication_year": int,
                        "patent_document_id": str,
                        "patent_document_paragraph_id": str,
                        "reaction_smiles": str
                    }
                )

                if output_directory_path is None:
                    if enable_logger:
                        getLogger(__name__).info(
                            "Completed the preparation of the USPTO (1976-2016) dataset by (2017, Lowe, D.M.)."
                        )

                    return prepared_data

                else:
                    prepared_data.to_csv(
                        path_or_buf=join(output_directory_path, "uspto_1976_2016_2017_lowe_xml.csv"),
                        index=False
                    )

                    if enable_logger:
                        getLogger(__name__).info(
                            "Completed the preparation of the USPTO (1976-2016) dataset by (2017, Lowe, D.M.). "
                            "The prepared data is stored at: '{0}'.".format(
                                abspath(join(output_directory_path, "uspto_1976_2016_2017_lowe_xml.csv"))
                            )
                        )

            else:
                grants_data = read_csv(
                    filepath_or_buffer=join(
                        extracted_data_directory_path,
                        "1976_Sep2016_USPTOgrants_smiles.rsmi"
                    ),
                    delimiter="\t",
                    dtype={
                        "ReactionSmiles": str,
                        "PatentNumber": str,
                        "ParagraphNum": str,
                        "Year": int,
                        "TextMinedYield": str,
                        "CalculatedYield": str
                    }
                )

                grants_data.columns = [
                    "reaction_smiles",
                    "patent_document_id",
                    "patent_document_paragraph_id",
                    "patent_document_publication_year",
                    "text_mined_yield",
                    "calculated_yield"
                ]

                grants_data["patent_document_category"] = "grants"

                applications_data = read_csv(
                    filepath_or_buffer=join(
                        extracted_data_directory_path,
                        "2001_Sep2016_USPTOapplications_smiles.rsmi"
                    ),
                    delimiter="\t",
                    dtype={
                        "ReactionSmiles": str,
                        "PatentNumber": str,
                        "ParagraphNum": str,
                        "Year": int,
                        "TextMinedYield": str,
                        "CalculatedYield": str
                    }
                )

                applications_data.columns = [
                    "reaction_smiles",
                    "patent_document_id",
                    "patent_document_paragraph_id",
                    "patent_document_publication_year",
                    "text_mined_yield",
                    "calculated_yield"
                ]

                applications_data["patent_document_category"] = "applications"

                prepared_data = concat([
                    grants_data,
                    applications_data
                ])[[
                    "patent_document_category",
                    "patent_document_publication_year",
                    "patent_document_id",
                    "patent_document_paragraph_id",
                    "reaction_smiles",
                    "text_mined_yield",
                    "calculated_yield"
                ]].dropna(
                    subset=[
                        "reaction_smiles"
                    ]
                ).sort_values(
                    by=[
                        "patent_document_category",
                        "patent_document_publication_year",
                        "patent_document_id",
                        "patent_document_paragraph_id"
                    ],
                    ascending=[
                        False,
                        True,
                        True,
                        True
                    ]
                ).drop_duplicates().reset_index(
                    drop=True
                ).astype(
                    dtype={
                        "patent_document_category": str,
                        "patent_document_publication_year": int,
                        "patent_document_id": str,
                        "patent_document_paragraph_id": str,
                        "reaction_smiles": str,
                        "text_mined_yield": str,
                        "calculated_yield": str
                    }
                )

                if output_directory_path is None:
                    if enable_logger:
                        getLogger(__name__).info(
                            "Completed the preparation of the USPTO (1976-2016) dataset by (2017, Lowe, D.M.)."
                        )

                    return prepared_data

                else:
                    prepared_data.to_csv(
                        path_or_buf=join(output_directory_path, "uspto_1976_2016_2017_lowe_rsmi.csv"),
                        index=False
                    )

                    if enable_logger:
                        getLogger(__name__).info(
                            "Completed the preparation of the USPTO (1976-2016) dataset by (2017, Lowe, D.M.). "
                            "The prepared data is stored at: '{0}'.".format(
                                abspath(join(output_directory_path, "uspto_1976_2016_2017_lowe_rsmi.csv"))
                            )
                        )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.UsptoDatasetPreparationUtils.prepare_1976_2016_2017_lowe".format(__name__)
                ).exception(exception_handle)

            raise

    @staticmethod
    def prepare_50k_2017_coley_et_al(
            extracted_data_directory_path: str,
            output_directory_path: str = None,
            enable_logger: bool = False
    ) -> DataFrame:
        """
        Prepare the USPTO-50k dataset by (2017, Coley, C.W. et al.).

        :parameter extracted_data_directory_path: The path to the directory where the extracted data is stored.
        :parameter output_directory_path: The path to the directory where the prepared data should be stored.
        :parameter enable_logger: The indicator whether the logger should be enabled.

        :returns: The prepared USPTO-50k dataset by (2017, Coley, C.W. et al.).
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the preparation of the USPTO-50k dataset by (2017, Coley, C.W. et al.)."
                )

            prepared_data = read_csv(
                filepath_or_buffer=join(extracted_data_directory_path, "data_processed.csv"),
                index_col=0
            )[[
                "id",
                "class",
                "rxn_smiles"
            ]]

            prepared_data.columns = [
                "patent_document_id",
                "reaction_class",
                "reaction_smiles"
            ]

            prepared_data = prepared_data.dropna(
                subset=[
                    "reaction_smiles"
                ]
            ).sort_values(
                by=[
                    "patent_document_id",
                    "reaction_class"
                ]
            ).drop_duplicates().reset_index(
                drop=True
            ).astype(
                dtype={
                    "patent_document_id": str,
                    "reaction_class": int,
                    "reaction_smiles": str
                }
            )

            if output_directory_path is None:
                if enable_logger:
                    getLogger(__name__).info(
                        "Completed the preparation of the USPTO-50k dataset by (2017, Coley, C.W. et al.)."
                    )

                return prepared_data

            else:
                prepared_data.to_csv(
                    path_or_buf=join(output_directory_path, "uspto_50k_2017_coley_et_al.csv"),
                    index=False
                )

                if enable_logger:
                    getLogger(__name__).info(
                        "Completed the preparation of the USPTO-50k dataset by (2017, Coley, C.W. et al.). "
                        "The prepared data is stored at: '{0}'.".format(
                            abspath(join(output_directory_path, "uspto_50k_2017_coley_et_al.csv"))
                        )
                    )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.UsptoDatasetPreparationUtils.prepare_50k_2017_coley_et_al".format(__name__)
                ).exception(exception_handle)

            raise

    @staticmethod
    def prepare_mit_2017_jin_et_al(
            extracted_data_directory_path: str,
            output_directory_path: str = None,
            enable_logger: bool = False
    ) -> DataFrame:
        """
        Prepare the USPTO-MIT dataset by (2017, Jin, W. et al.).

        :parameter extracted_data_directory_path: The path to the directory where the extracted data is stored.
        :parameter output_directory_path: The path to the directory where the prepared data should be stored.
        :parameter enable_logger: The indicator whether the logger should be enabled.

        :returns: The prepared USPTO-MIT dataset by (2017, Jin, W. et al.).
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the preparation of the USPTO-MIT dataset by (2017, Jin, W. et al.)."
                )

            train_data = read_csv(
                filepath_or_buffer=join(extracted_data_directory_path, "train.txt"),
                delimiter="\t",
                header=None
            ).iloc[:, [0]]

            train_data.columns = [
                "reaction_smiles"
            ]

            train_data["dataset_name"] = "train"

            valid_data = read_csv(
                filepath_or_buffer=join(extracted_data_directory_path, "valid.txt"),
                delimiter="\t",
                header=None
            ).iloc[:, [0]]

            valid_data.columns = [
                "reaction_smiles"
            ]

            valid_data["dataset_name"] = "valid"

            test_data = read_csv(
                filepath_or_buffer=join(extracted_data_directory_path, "test.txt"),
                delimiter="\t",
                header=None
            ).iloc[:, [0]]

            test_data.columns = [
                "reaction_smiles"
            ]

            test_data["dataset_name"] = "test"

            prepared_data = concat([
                train_data,
                valid_data,
                test_data
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
                        "Completed the preparation of the USPTO-MIT dataset by (2017, Jin, W. et al.)."
                    )

                return prepared_data

            else:
                prepared_data.to_csv(
                    path_or_buf=join(output_directory_path, "uspto_mit_2017_jin_et_al.csv"),
                    index=False
                )

                if enable_logger:
                    getLogger(__name__).info(
                        "Completed the preparation of the USPTO-MIT dataset by (2017, Jin, W. et al.). "
                        "The prepared data is stored at: '{0}'.".format(
                            abspath(join(output_directory_path, "uspto_mit_2017_jin_et_al.csv"))
                        )
                    )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.UsptoDatasetPreparationUtils.prepare_mit_2017_jin_et_al".format(__name__)
                ).exception(exception_handle)

            raise
