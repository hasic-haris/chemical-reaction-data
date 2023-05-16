#!/bin/bash

export PYTHONPATH=$PYTHONPATH:"/path/to/project/directory"

export VERSION="v_rr01_rp2_hs_2018_duigou_et_al"
export OUTPUT_DIRECTORY_PATH="/path/to/output/directory"


python "$(cd -P "$(dirname "${BASH_SOURCE[0]}")" && pwd)"/prepare_retro_rules_database.py \
        --version $VERSION \
        --output_directory_path $OUTPUT_DIRECTORY_PATH \
        --enable_logger
