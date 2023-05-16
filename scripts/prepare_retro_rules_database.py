""" The 'scripts' directory 'prepare_retro_rules_database' script. """

from argparse import ArgumentParser, BooleanOptionalAction, Namespace

from os.path import join

from chemical_reaction_data.retro_rules import RetroRulesDatabaseDownloadUtilities
from chemical_reaction_data.retro_rules import RetroRulesDatabaseExtractionUtilities
from chemical_reaction_data.retro_rules import RetroRulesDatabasePreparationUtilities


def parse_script_arguments() -> Namespace:
    """ Parse the 'prepare_retro_rules_database' script arguments. """

    argument_parser = ArgumentParser()

    argument_parser.add_argument(
        "-v",
        "--version",
        type=str,
        choices=[
            "v_rr01_rp2_hs_2018_duigou_et_al",
            "v_rr02_rp2_hs_2018_duigou_et_al",
            "v_rr02_rp3_hs_2018_duigou_et_al",
            "v_rr02_rp3_nohs_2018_duigou_et_al"
        ],
        required=True,
        help="The indicator of the data source version that should be prepared."
    )

    argument_parser.add_argument(
        "-o",
        "--output_directory_path",
        type=str,
        required=True,
        help="The path to the directory where the prepared data should be stored."
    )

    argument_parser.add_argument(
        "-l",
        "--enable_logger",
        action=BooleanOptionalAction,
        help="The indicator whether the logger should be enabled."
    )

    return argument_parser.parse_args()


if __name__ == "__main__":
    script_arguments = parse_script_arguments()

    if script_arguments.version == "v_rr01_rp2_hs_2018_duigou_et_al":
        RetroRulesDatabaseDownloadUtilities.download_rr01_rp2_hs_2018_duigou_et_al(
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

        RetroRulesDatabaseExtractionUtilities.extract_rr01_rp2_hs_2018_duigou_et_al(
            downloaded_data_directory_path=script_arguments.output_directory_path,
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

        RetroRulesDatabasePreparationUtilities.prepare_rr01_rp2_hs_2018_duigou_et_al(
            extracted_data_directory_path=join(script_arguments.output_directory_path, "retrorules_rr01_rp2"),
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

    elif script_arguments.version == "v_rr02_rp2_hs_2018_duigou_et_al":
        RetroRulesDatabaseDownloadUtilities.download_rr02_rp2_hs_2018_duigou_et_al(
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

        RetroRulesDatabaseExtractionUtilities.extract_rr02_rp2_hs_2018_duigou_et_al(
            downloaded_data_directory_path=script_arguments.output_directory_path,
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

        RetroRulesDatabasePreparationUtilities.prepare_rr02_rp2_hs_2018_duigou_et_al(
            extracted_data_directory_path=join(script_arguments.output_directory_path, "retrorules_rr02_rp2_hs"),
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

    elif script_arguments.version == "v_rr02_rp3_hs_2018_duigou_et_al":
        RetroRulesDatabaseDownloadUtilities.download_rr02_rp3_hs_2018_duigou_et_al(
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

        RetroRulesDatabaseExtractionUtilities.extract_rr02_rp3_hs_2018_duigou_et_al(
            downloaded_data_directory_path=script_arguments.output_directory_path,
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

        RetroRulesDatabasePreparationUtilities.prepare_rr02_rp3_hs_2018_duigou_et_al(
            extracted_data_directory_path=join(script_arguments.output_directory_path, "retrorules_rr02_rp3_hs"),
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

    elif script_arguments.version == "v_rr02_rp3_nohs_2018_duigou_et_al":
        RetroRulesDatabaseDownloadUtilities.download_rr02_rp3_nohs_2018_duigou_et_al(
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

        RetroRulesDatabaseExtractionUtilities.extract_rr02_rp3_nohs_2018_duigou_et_al(
            downloaded_data_directory_path=script_arguments.output_directory_path,
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

        RetroRulesDatabasePreparationUtilities.prepare_rr02_rp3_nohs_2018_duigou_et_al(
            extracted_data_directory_path=join(script_arguments.output_directory_path, "retrorules_rr02_rp3_nohs"),
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )
