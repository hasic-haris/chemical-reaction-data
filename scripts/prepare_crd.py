""" The 'scripts' directory 'prepare_crd' script. """

from argparse import ArgumentParser, BooleanOptionalAction, Namespace

from chemical_reaction_data.crd import CrdDownloadUtilities, CrdPreparationUtilities


def parse_script_arguments() -> Namespace:
    """ Parse the 'prepare_crd' script arguments. """

    argument_parser = ArgumentParser()

    argument_parser.add_argument(
        "-v",
        "--version",
        type=str,
        choices=[
            "v_2022_van_der_lingen"
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

    if script_arguments.version == "v_2022_van_der_lingen":
        CrdDownloadUtilities.download_2022_van_der_lingen(
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

        CrdPreparationUtilities.prepare_2022_van_der_lingen(
            extracted_data_directory_path=script_arguments.output_directory_path,
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )
