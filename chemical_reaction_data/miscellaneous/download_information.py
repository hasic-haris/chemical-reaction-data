""" The 'chemical_reaction_data.miscellaneous' package 'download_information' module. """


MISCELLANEOUS_DATA_DOWNLOAD_INFORMATION = {
    # ------------------------------------------------------------------------------------------------------------------
    #  The chemical reaction classification dataset by (2013, Kraut, H., et al.).
    #  DOI: https://doi.org/10.1021/ci400442f.
    # ------------------------------------------------------------------------------------------------------------------

    "v_2013_kraut_et_al": {
        "official_acs": {
            "base_url": "https://ndownloader.figstatic.com/collections/2375332/versions",
            "url_file_paths": [
                "/1"
            ]
        }
    },

    # ------------------------------------------------------------------------------------------------------------------
    #  The organic chemistry textbook questions dataset by (2016, Wei, J.N., et al.).
    #  DOI: https://doi.org/10.1021/acscentsci.6b00219.
    # ------------------------------------------------------------------------------------------------------------------

    "v_2016_wei_et_al": {
        "official_github": {
            "base_url": "https://raw.githubusercontent.com/jnwei/neural_reaction_fingerprint/master/data",
            "url_file_paths": [
                "/test_questions/Wade8_47.ans_smi.txt",
                "/test_questions/Wade8_48.ans_smi.txt"
            ]
        }
    },

    # ------------------------------------------------------------------------------------------------------------------
    #  The RetroTransformDB dataset by (2018, Avramova, S., et al.).
    #  DOI: https://doi.org/10.5281/zenodo.1209312.
    # ------------------------------------------------------------------------------------------------------------------

    "v_2018_avramova_et_al": {
        "official_zenodo": {
            "base_url": "https://zenodo.org/record/1209313/files",
            "url_file_paths": [
                "/RetroTransformDB-v-1-0.txt"
            ]
        }
    },

    # ------------------------------------------------------------------------------------------------------------------
    #  The Grambow dataset by (2022, Wen, M., et al.).
    #  DOI: https://doi.org/10.1039/D1SC06515G.
    # ------------------------------------------------------------------------------------------------------------------

    "v_grambow_2022_wen_et_al": {
        "official_github": {
            "base_url": "https://raw.githubusercontent.com/mjwen/rxnrep/master/dataset/grambow",
            "url_file_paths": [
                "/grambow_test.tsv",
                "/grambow_train.tsv",
                "/grambow_val.tsv"
            ]
        }
    },

    # ------------------------------------------------------------------------------------------------------------------
    #  The TPL100 dataset by (2022, Wen, M., et al.).
    #  DOI: https://doi.org/10.1039/D1SC06515G.
    # ------------------------------------------------------------------------------------------------------------------

    "v_tpl100_2022_wen_et_al": {
        "official_github": {
            "base_url": "https://raw.githubusercontent.com/mjwen/rxnrep/master/dataset/tpl100",
            "url_file_paths": [
                "/tpl100_test.tsv",
                "/tpl100_train.tsv",
                "/tpl100_val.tsv"
            ]
        }
    }

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------
}
