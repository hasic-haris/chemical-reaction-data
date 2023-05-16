""" The 'scripts' directory 'prepare_ord' script. """

from argparse import ArgumentParser, BooleanOptionalAction, Namespace

from os.path import join

from chemical_reaction_data.ord import OrdDownloadUtilities, OrdExtractionUtilities, OrdPreparationUtilities


def parse_script_arguments() -> Namespace:
    """ Parse the 'prepare_ord' script arguments. """

    argument_parser = ArgumentParser()

    argument_parser.add_argument(
        "-v",
        "--version",
        type=str,
        choices=[
            "v_2021_kearnes_et_al"
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
        "-c",
        "--number_of_cpu_cores",
        type=int,
        default=1,
        help="The number of CPU cores that should be utilized."
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

    if script_arguments.version == "v_2021_kearnes_et_al":
        OrdDownloadUtilities.download_2021_kearnes_et_al(
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

        OrdExtractionUtilities.extract_2021_kearnes_et_al(
            downloaded_data_directory_path=script_arguments.output_directory_path,
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

        OrdPreparationUtilities.prepare_2021_kearnes_et_al(
            extracted_data_directory_path=join(script_arguments.output_directory_path, "ord-data-main", "data"),
            output_directory_path=script_arguments.output_directory_path,
            number_of_cpu_cores=script_arguments.number_of_cpu_cores,
            enable_logger=script_arguments.enable_logger
        )
