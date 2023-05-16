""" The 'scripts' directory 'prepare_uspto_dataset' script. """

from argparse import ArgumentParser, BooleanOptionalAction, Namespace

from os.path import join

from chemical_reaction_data.uspto import UsptoDatasetDownloadUtilities, UsptoDatasetExtractionUtilities
from chemical_reaction_data.uspto import UsptoDatasetPreparationUtils


def parse_script_arguments() -> Namespace:
    """ Parse the 'prepare_uspto_dataset' script arguments. """

    argument_parser = ArgumentParser()

    argument_parser.add_argument(
        "-v",
        "--version",
        type=str,
        choices=[
            "v_1976_2013_2014_lowe",
            "v_50k_2016_schneider_et_al",
            "v_15k_2017_coley_et_al",
            "v_1976_2016_2017_lowe",
            "v_50k_2017_coley_et_al",
            "v_mit_2017_jin_et_al"
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

    if script_arguments.version == "v_1976_2013_2014_lowe":
        UsptoDatasetDownloadUtilities.download_1976_2013_2014_lowe(
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

        UsptoDatasetExtractionUtilities.extract_1976_2013_2014_lowe(
            downloaded_data_directory_path=script_arguments.output_directory_path,
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

        UsptoDatasetPreparationUtils.prepare_1976_2013_2014_lowe(
            extracted_data_directory_path=script_arguments.output_directory_path,
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

    elif script_arguments.version == "v_50k_2016_schneider_et_al":
        UsptoDatasetDownloadUtilities.download_50k_2016_schneider_et_al(
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

        UsptoDatasetExtractionUtilities.extract_50k_2016_schneider_et_al(
            downloaded_data_directory_path=script_arguments.output_directory_path,
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

        UsptoDatasetPreparationUtils.prepare_50k_2016_schneider_et_al(
            extracted_data_directory_path=join(script_arguments.output_directory_path, "data"),
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

    elif script_arguments.version == "v_15k_2017_coley_et_al":
        UsptoDatasetDownloadUtilities.download_15k_2017_coley_et_al(
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

        UsptoDatasetExtractionUtilities.extract_15k_2017_coley_et_al(
            downloaded_data_directory_path=script_arguments.output_directory_path,
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

        UsptoDatasetPreparationUtils.prepare_15k_2017_coley_et_al(
            extracted_data_directory_path=join(script_arguments.output_directory_path, "data"),
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

    elif script_arguments.version == "v_1976_2016_2017_lowe":
        UsptoDatasetDownloadUtilities.download_1976_2016_2017_lowe(
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

        UsptoDatasetExtractionUtilities.extract_1976_2016_2017_lowe(
            downloaded_data_directory_path=script_arguments.output_directory_path,
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

        UsptoDatasetPreparationUtils.prepare_1976_2016_2017_lowe(
            extracted_data_directory_path=script_arguments.output_directory_path,
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

    elif script_arguments.version == "v_50k_2017_coley_et_al":
        UsptoDatasetDownloadUtilities.download_50k_2017_coley_et_al(
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

        UsptoDatasetPreparationUtils.prepare_50k_2017_coley_et_al(
            extracted_data_directory_path=script_arguments.output_directory_path,
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

    elif script_arguments.version == "v_mit_2017_jin_et_al":
        UsptoDatasetDownloadUtilities.download_mit_2017_jin_et_al(
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

        UsptoDatasetExtractionUtilities.extract_mit_2017_jin_et_al(
            downloaded_data_directory_path=script_arguments.output_directory_path,
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )

        UsptoDatasetPreparationUtils.prepare_mit_2017_jin_et_al(
            extracted_data_directory_path=join(script_arguments.output_directory_path, "data"),
            output_directory_path=script_arguments.output_directory_path,
            enable_logger=script_arguments.enable_logger
        )
