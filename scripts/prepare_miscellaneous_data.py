""" The 'scripts' directory 'prepare_miscellaneous_data' script. """

from argparse import ArgumentParser, BooleanOptionalAction, Namespace

from chemical_reaction_data.miscellaneous import MiscellaneousDataDownloadUtilities
from chemical_reaction_data.miscellaneous import MiscellaneousDataExtractionUtilities
from chemical_reaction_data.miscellaneous import MiscellaneousDataPreparationUtilities


def parse_script_arguments() -> Namespace:
    """ Parse the 'prepare_miscellaneous_data' script arguments. """

    argument_parser = ArgumentParser()

    argument_parser.add_argument(
        "-v",
        "--version",
        type=str,
        choices=[
            "v_2013_kraut_et_al",
            "v_2016_wei_et_al",
            "v_2018_avramova_et_al",
            "v_grambow_2022_wen_et_al",
            "v_tpl100_2022_wen_et_al"
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

    if script_arguments.version == "v_2013_kraut_et_al":
        MiscellaneousDataDownloadUtilities.download_2013_kraut_et_al(
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

        MiscellaneousDataExtractionUtilities.extract_2013_kraut_et_al(
            downloaded_data_directory_path=script_arguments.output_directory_path,
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

        MiscellaneousDataPreparationUtilities.prepare_2013_kraut_et_al(
            extracted_data_directory_path=script_arguments.output_directory_path,
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

    elif script_arguments.version == "v_2016_wei_et_al":
        MiscellaneousDataDownloadUtilities.download_2016_wei_et_al(
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

        MiscellaneousDataPreparationUtilities.prepare_2016_wei_et_al_dataset(
            extracted_data_directory_path=script_arguments.output_directory_path,
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

    elif script_arguments.version == "v_grambow_2022_wen_et_al":
        MiscellaneousDataDownloadUtilities.download_grambow_2022_wen_et_al(
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

        MiscellaneousDataPreparationUtilities.prepare_grambow_2022_wen_et_al(
            extracted_data_directory_path=script_arguments.output_directory_path,
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

    elif script_arguments.version == "v_tpl100_2022_wen_et_al":
        MiscellaneousDataDownloadUtilities.download_tpl100_2022_wen_et_al(
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

        MiscellaneousDataPreparationUtilities.prepare_tpl100_2022_wen_et_al(
            extracted_data_directory_path=script_arguments.output_directory_path,
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )
