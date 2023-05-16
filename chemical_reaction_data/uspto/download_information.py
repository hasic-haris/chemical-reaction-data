""" The 'chemical_reaction_data.uspto' package 'download_information' module. """


USPTO_DATASET_DOWNLOAD_INFORMATION = {
    # ------------------------------------------------------------------------------------------------------------------
    #  The USPTO (1976-2013) dataset by (2014, Lowe, D.M.).
    #  DOI: https://doi.org/10.6084/m9.figshare.12084729.v1.
    # ------------------------------------------------------------------------------------------------------------------

    "v_1976_2013_2014_lowe": {
        "official_figshare": {
            "base_url": "https://www.figshare.com/ndownloader/articles/12084729/versions",
            "url_file_paths": [
                "/1"
            ]
        }
    },

    # ------------------------------------------------------------------------------------------------------------------
    #  The USPTO-50k dataset by (2016, Schneider, N., et al.).
    #  DOI: https://doi.org/10.1021/acs.jcim.6b00564.
    # ------------------------------------------------------------------------------------------------------------------

    "v_50k_2016_schneider_et_al": {
        "official_acs": {
            "base_url": "https://ndownloader.figstatic.com/collections/3591299/versions",
            "url_file_paths": [
                "/1"
            ]
        },
        "unofficial_github": {
            "base_url": "https://raw.githubusercontent.com/connorcoley/retrosim/master/retrosim/data/from_schneider",
            "url_file_paths": [
                "/dataSetA.csv",
                "/dataSetB.csv"
            ]
        }
    },

    # ------------------------------------------------------------------------------------------------------------------
    #  The USPTO-15k dataset by (2017, Coley, C.W., et al.).
    #  DOI: https://doi.org/10.1021/acscentsci.7b00064.
    # ------------------------------------------------------------------------------------------------------------------

    "v_15k_2017_coley_et_al": {
        "unofficial_github": {
            "base_url": "https://raw.githubusercontent.com/wengong-jin/nips17-rexgen/master/USPTO-15K",
            "url_file_paths": [
                "/data.zip"
            ]
        }
    },

    # ------------------------------------------------------------------------------------------------------------------
    #  The USPTO (1976-2016) dataset by (2017, Lowe, D.M.).
    #  DOI: https://doi.org/10.6084/m9.figshare.5104873.v1.
    # ------------------------------------------------------------------------------------------------------------------

    "v_1976_2016_2017_lowe": {
        "official_figshare": {
            "base_url": "https://www.figshare.com/ndownloader/articles/5104873/versions",
            "url_file_paths": [
                "/1"
            ]
        }
    },

    # ------------------------------------------------------------------------------------------------------------------
    #  The USPTO-50k dataset by (2017, Coley, C.W., et al.).
    #  DOI: https://doi.org/10.1021/acscentsci.7b00355.
    # ------------------------------------------------------------------------------------------------------------------

    "v_50k_2017_coley_et_al": {
        "official_github": {
            "base_url": "https://raw.githubusercontent.com/connorcoley/retrosim/master/retrosim/data",
            "url_file_paths": [
                "/data_processed.csv"
            ]
        }
    },

    # ------------------------------------------------------------------------------------------------------------------
    #  The USPTO-MIT dataset by (2017, Jin, W., et al.).
    #  DOI: https://doi.org/10.48550/arXiv.1709.04555.
    # ------------------------------------------------------------------------------------------------------------------

    "v_mit_2017_jin_et_al": {
        "official_github": {
            "base_url": "https://raw.githubusercontent.com/wengong-jin/nips17-rexgen/master/USPTO",
            "url_file_paths": [
                "/data.zip"
            ]
        }
    }

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------
}
