#!/bin/bash

export PYTHONPATH=$PYTHONPATH:"/path/to/project/root/directory"

export VERSION="v_2022_bansal_et_al"
export OUTPUT_DIRECTORY_PATH="/path/to/output/directory"


python "$(cd -P "$(dirname "${BASH_SOURCE[0]}")" && pwd)"/prepare_rhea_database.py \
        --version $VERSION \
        --output_directory_path $OUTPUT_DIRECTORY_PATH \
        --enable_logger
