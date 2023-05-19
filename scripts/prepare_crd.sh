#!/bin/bash

export PYTHONPATH=$PYTHONPATH:"/path/to/project/root/directory"

export VERSION="v_2022_van_der_lingen"
export OUTPUT_DIRECTORY_PATH="/path/to/output/directory"


python "$(cd -P "$(dirname "${BASH_SOURCE[0]}")" && pwd)"/prepare_crd.py \
        --version $VERSION \
        --output_directory_path $OUTPUT_DIRECTORY_PATH \
        --enable_logger
