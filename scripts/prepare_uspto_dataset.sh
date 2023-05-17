#!/bin/bash

export PYTHONPATH=$PYTHONPATH:"/path/to/project/root/directory"

export VERSION="v_1976_2013_2014_lowe"
export OUTPUT_DIRECTORY_PATH="/path/to/output/directory"
export NUMBER_OF_CPU_CORES=1


python "$(cd -P "$(dirname "${BASH_SOURCE[0]}")" && pwd)"/prepare_uspto_dataset.py \
        --version $VERSION \
        --output_directory_path $OUTPUT_DIRECTORY_PATH \
        --number_of_cpu_cores $NUMBER_OF_CPU_CORES \
        --enable_logger
