""" The 'chemical_reaction_data.retro_rules' package 'preparation' module. """

from logging import getLogger
from pandas import DataFrame, read_csv

from os.path import abspath, join


class RetroRulesDatabasePreparationUtilities:
    """ The RetroRules database preparation utilities class. """

    @staticmethod
    def prepare_rr01_rp2_hs_2018_duigou_et_al(
            extracted_data_directory_path: str,
            output_directory_path: str = None,
            enable_logger: bool = False
    ) -> DataFrame:
        """
        Prepare the RetroRules (rr01.rp2.hs) database by (2018, Duigou, T., et al.).

        :parameter extracted_data_directory_path: The path to the directory where the extracted data is stored.
        :parameter output_directory_path: The path to the directory where the prepared data should be stored.
        :parameter enable_logger: The indicator whether the logger should be enabled.

        :returns: The prepared RetroRules (rr01.rp2.hs) database by (2018, Duigou, T., et al.).
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the preparation of the RetroRules (rr01.rp2.hs) database by (2018, Duigou, T., et al.)."
                )

            prepared_data = read_csv(
                filepath_or_buffer=join(extracted_data_directory_path, "retrorules_rr01_rp2_flat_all.csv")
            )[[
                "Rule ID",
                "Rule",
                "Rule usage"
            ]]

            prepared_data.columns = [
                "reaction_rule_id",
                "reaction_rule_smarts",
                "reaction_rule_usage"
            ]

            prepared_data = prepared_data.dropna(
                subset=[
                    "reaction_rule_smarts"
                ]
            ).sort_values(
                by=[
                    "reaction_rule_id"
                ]
            ).drop_duplicates().reset_index(
                drop=True
            ).astype(
                dtype={
                    "reaction_rule_id": str,
                    "reaction_rule_smarts": str,
                    "reaction_rule_usage": str
                }
            )

            if output_directory_path is None:
                if enable_logger:
                    getLogger(__name__).info(
                        "Completed the preparation of the RetroRules (rr01.rp2.hs) database by "
                        "(2018, Duigou, T., et al.)."
                    )

                return prepared_data

            else:
                prepared_data.to_csv(
                    path_or_buf=join(output_directory_path, "retro_rules_rr01_rp2_hs_2018_duigou_et_al.csv"),
                    index=False
                )

                if enable_logger:
                    getLogger(__name__).info(
                        "Completed the preparation of the RetroRules (rr01.rp2.hs) database by "
                        "(2018, Duigou, T., et al.). The prepared data is stored at: '{0}'.".format(
                            abspath(join(output_directory_path, "retro_rules_rr01_rp2_hs_2018_duigou_et_al.csv"))
                        )
                    )

                return prepared_data

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.RetroRulesDatabasePreparationUtilities.prepare_rr01_rp2_hs_2018_duigou_et_al".format(__name__)
                ).exception(exception_handle)

            raise

    @staticmethod
    def prepare_rr02_rp2_hs_2018_duigou_et_al(
            extracted_data_directory_path: str,
            output_directory_path: str = None,
            enable_logger: bool = False
    ) -> DataFrame:
        """
        Prepare the RetroRules (rr02.rp2.hs) database by (2018, Duigou, T., et al.).

        :parameter extracted_data_directory_path: The path to the directory where the extracted data is stored.
        :parameter output_directory_path: The path to the directory where the prepared data should be stored.
        :parameter enable_logger: The indicator whether the logger should be enabled.

        :returns: The prepared RetroRules (rr02.rp2.hs) database by (2018, Duigou, T., et al.).
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the preparation of the RetroRules (rr02.rp2.hs) database by (2018, Duigou, T., et al.)."
                )

            prepared_data = read_csv(
                filepath_or_buffer=join(extracted_data_directory_path, "retrorules_rr02_rp2_flat_all.csv")
            )[[
                "Rule ID",
                "Rule",
                "Rule usage"
            ]]

            prepared_data.columns = [
                "reaction_rule_id",
                "reaction_rule_smarts",
                "reaction_rule_usage"
            ]

            prepared_data = prepared_data.dropna(
                subset=[
                    "reaction_rule_smarts"
                ]
            ).sort_values(
                by=[
                    "reaction_rule_id"
                ]
            ).drop_duplicates().reset_index(
                drop=True
            ).astype(
                dtype={
                    "reaction_rule_id": str,
                    "reaction_rule_smarts": str,
                    "reaction_rule_usage": str
                }
            )

            if output_directory_path is None:
                if enable_logger:
                    getLogger(__name__).info(
                        "Completed the preparation of the RetroRules (rr02.rp2.hs) database by "
                        "(2018, Duigou, T., et al.)."
                    )

                return prepared_data

            else:
                prepared_data.to_csv(
                    path_or_buf=join(output_directory_path, "retro_rules_rr02_rp2_hs_2018_duigou_et_al.csv"),
                    index=False
                )

                if enable_logger:
                    getLogger(__name__).info(
                        "Completed the preparation of the RetroRules (rr02.rp2.hs) database by "
                        "(2018, Duigou, T., et al.). The prepared data is stored at: '{0}'.".format(
                            abspath(join(output_directory_path, "retro_rules_rr02_rp2_hs_2018_duigou_et_al.csv"))
                        )
                    )

                return prepared_data

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.RetroRulesDatabasePreparationUtilities.prepare_rr02_rp2_hs_2018_duigou_et_al".format(__name__)
                ).exception(exception_handle)

            raise

    @staticmethod
    def prepare_rr02_rp3_hs_2018_duigou_et_al(
            extracted_data_directory_path: str,
            output_directory_path: str = None,
            enable_logger: bool = False
    ) -> DataFrame:
        """
        Prepare the RetroRules (rr02.rp3.hs) database by (2018, Duigou, T., et al.).

        :parameter extracted_data_directory_path: The path to the directory where the extracted data is stored.
        :parameter output_directory_path: The path to the directory where the prepared data should be stored.
        :parameter enable_logger: The indicator whether the logger should be enabled.

        :returns: The prepared RetroRules (rr02.rp3.hs) database by (2018, Duigou, T., et al.).
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the preparation of the RetroRules (rr02.rp3.hs) database by (2018, Duigou, T., et al.)."
                )

            prepared_data = read_csv(
                filepath_or_buffer=join(extracted_data_directory_path, "retrorules_rr02_flat_all.tsv"),
                delimiter="\t"
            )[[
                "# Rule_ID",
                "Rule_SMARTS",
                "Rule_usage"
            ]]

            prepared_data.columns = [
                "reaction_rule_id",
                "reaction_rule_smarts",
                "reaction_rule_usage"
            ]

            prepared_data = prepared_data.dropna(
                subset=[
                    "reaction_rule_smarts"
                ]
            ).sort_values(
                by=[
                    "reaction_rule_id"
                ]
            ).drop_duplicates().reset_index(
                drop=True
            ).astype(
                dtype={
                    "reaction_rule_id": str,
                    "reaction_rule_smarts": str,
                    "reaction_rule_usage": str
                }
            )

            if output_directory_path is None:
                if enable_logger:
                    getLogger(__name__).info(
                        "Completed the preparation of the RetroRules (rr02.rp3.hs) database by "
                        "(2018, Duigou, T., et al.)."
                    )

                return prepared_data

            else:
                prepared_data.to_csv(
                    path_or_buf=join(output_directory_path, "retro_rules_rr02_rp3_hs_2018_duigou_et_al.csv"),
                    index=False
                )

                if enable_logger:
                    getLogger(__name__).info(
                        "Completed the preparation of the RetroRules (rr02.rp3.hs) database by "
                        "(2018, Duigou, T., et al.). The prepared data is stored at: '{0}'.".format(
                            abspath(join(output_directory_path, "retro_rules_rr02_rp3_hs_2018_duigou_et_al.csv"))
                        )
                    )

                return prepared_data

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.RetroRulesDatabasePreparationUtilities.prepare_rr02_rp3_hs_2018_duigou_et_al".format(__name__)
                ).exception(exception_handle)

            raise

    @staticmethod
    def prepare_rr02_rp3_nohs_2018_duigou_et_al(
            extracted_data_directory_path: str,
            output_directory_path: str = None,
            enable_logger: bool = False
    ) -> DataFrame:
        """
        Prepare the RetroRules (rr02.rp3.nohs) database by (2018, Duigou, T., et al.).

        :parameter extracted_data_directory_path: The path to the directory where the extracted data is stored.
        :parameter output_directory_path: The path to the directory where the prepared data should be stored.
        :parameter enable_logger: The indicator whether the logger should be enabled.

        :returns: The prepared RetroRules (rr02.rp3.nohs) database by (2018, Duigou, T., et al.).
        """

        try:
            if enable_logger:
                getLogger(__name__).info(
                    "Started the preparation of the RetroRules (rr02.rp3.nohs) database by (2018, Duigou, T., et al.)."
                )

            prepared_data = read_csv(
                filepath_or_buffer=join(extracted_data_directory_path, "retrorules_rr02_flat_all.tsv"),
                delimiter="\t"
            )[[
                "# Rule_ID",
                "Rule_SMARTS",
                "Rule_usage"
            ]]

            prepared_data.columns = [
                "reaction_rule_id",
                "reaction_rule_smarts",
                "reaction_rule_usage"
            ]

            prepared_data = prepared_data.dropna(
                subset=[
                    "reaction_rule_smarts"
                ]
            ).sort_values(
                by=[
                    "reaction_rule_id"
                ]
            ).drop_duplicates().reset_index(
                drop=True
            ).astype(
                dtype={
                    "reaction_rule_id": str,
                    "reaction_rule_smarts": str,
                    "reaction_rule_usage": str
                }
            )

            if output_directory_path is None:
                if enable_logger:
                    getLogger(__name__).info(
                        "Completed the preparation of the RetroRules (rr02.rp3.nohs) database by "
                        "(2018, Duigou, T., et al.)."
                    )

                return prepared_data

            else:
                prepared_data.to_csv(
                    path_or_buf=join(output_directory_path, "retro_rules_rr02_rp3_nohs_2018_duigou_et_al.csv"),
                    index=False
                )

                if enable_logger:
                    getLogger(__name__).info(
                        "Completed the preparation of the RetroRules (rr02.rp3.nohs) database by "
                        "(2018, Duigou, T., et al.). The prepared data is stored at: '{0}'.".format(
                            abspath(join(output_directory_path, "retro_rules_rr02_rp3_nohs_2018_duigou_et_al.csv"))
                        )
                    )

                return prepared_data

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.RetroRulesDatabasePreparationUtilities.prepare_rr02_rp3_nohs_2018_duigou_et_al".format(
                        __name__
                    )
                ).exception(exception_handle)

            raise
