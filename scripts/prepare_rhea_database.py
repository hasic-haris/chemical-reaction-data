""" The 'scripts' directory 'prepare_rhea_database' script. """

from argparse import ArgumentParser, BooleanOptionalAction, Namespace

from chemical_reaction_data.rhea import RheaDatabaseDownloadUtilities, RheaDatabasePreparationUtilities


def parse_script_arguments() -> Namespace:
    """ Parse the 'prepare_rhea_database' script arguments. """

    argument_parser = ArgumentParser()

    argument_parser.add_argument(
        "-v",
        "--version",
        type=str,
        choices=[
            "v_2022_bansal_et_al"
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

    if script_arguments.version == "v_2022_bansal_et_al":
        RheaDatabaseDownloadUtilities.download_2022_bansal_et_al(
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

        RheaDatabasePreparationUtilities.prepare_2022_bansal_et_al(
            extracted_data_directory_path=script_arguments.output_directory_path,
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )
