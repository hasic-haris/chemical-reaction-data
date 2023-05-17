# Chemical Reaction Data
The computer-assisted synthesis field grew to become one of the most active fields in chemoinformatics, with new and
improved approaches centered around chemical reactions being published on a regular basis. Unfortunately, the chemical
reaction data necessary to develop and test the practicality of such approaches is not easy to come by, given the
potential value it holds. The data that is available is often times of poor quality and quantity, stored in various
different formats, or published behind a paywall, which can be a significant barrier of entry for many scientists.
Taking all of this into account, the goal of this project is to systematically curate, categorize and facilitate the
access to existing open-source chemical reaction data in one place.


## Setup
To use the ***chemical_reaction_data*** package, please ensure that the
[ord-schema](https://github.com/open-reaction-database/ord-schema), [py7zr](https://github.com/miurahr/py7zr),
[tqdm](https://github.com/tqdm/tqdm) and [rdkit](https://github.com/rdkit/rdkit) libraries are available. A minimal
execution environment can be set up using [conda](https://docs.conda.io/en/latest/) and
[pip](https://pip.pypa.io/en/stable/) as follows:

```shell
conda create -c conda-forge -n chemical-reaction-data rdkit -y

conda activate chemical-reaction-data

pip install ord-schema py7zr tqdm
```


## Scripts
The ***scripts*** directory is primarily meant to illustrate how to utilize the ***chemical_reaction_data*** package to
download, extract and prepare open-source chemical reaction data. The line
`export PYTHONPATH=$PYTHONPATH:"/path/to/project/root/directory"` is a reminder to add the path to the project root
directory to the `PYTHONPATH` variable to make the package visible before running the scripts.


## Supported Data Sources
Currently, the ***chemical_reaction_data*** package supports the following open-source chemical reaction data sources:

1. [The United States Patent and Trademark Office Dataset](#the-united-states-patent-and-trademark-office-dataset)
2. [The Open Reaction Database](#the-open-reaction-database)
3. [The Rhea Database](#the-rhea-database)
4. [The RetroRules Database](#the-retrorules-database)
5. [Miscellaneous Data Sources](#miscellaneous-data-sources)


### The United States Patent and Trademark Office Dataset
The **United States Patent and Trademark Office** (USPTO) dataset [[1]](#References) is an open-source chemical
reaction dataset constructed by text-mining patent grant and patent application documents.

![uspto_dataset_versions.png](resources/uspto_dataset_versions.png)

Currently, the ***chemical_reaction_data*** package supports the following USPTO dataset versions:

| Version           | Reference                                                                 | Status                                                          |
|-------------------|---------------------------------------------------------------------------|-----------------------------------------------------------------|
| USPTO (1976-2013) | [(2014, Lowe, D.M.)](https://doi.org/10.6084/m9.figshare.12084729.v1)     | :orange_circle: Partially Implemented (Performance Limitations) |
| USPTO-50k         | [(2016, Schneider, N., et al.)](https://doi.org/10.1021/acs.jcim.6b00564) | :green_circle: Implemented                                      |
| USPTO-15k         | [(2017, Coley, C.W., et al.)](https://doi.org/10.1021/acscentsci.7b00064) | :green_circle: Implemented                                      |
| USPTO (1976-2016) | [(2017, Lowe, D.M.)](https://doi.org/10.6084/m9.figshare.5104873.v1)      | :green_circle: Implemented                                      |
| USPTO-50k         | [(2017, Liu, B., et al.)](https://doi.org/10.1021/acscentsci.7b00303)     | :red_circle: Not Implemented                                    |
| USPTO-50k         | [(2017, Coley, C.W., et al.)](https://doi.org/10.1021/acscentsci.7b00355) | :green_circle: Implemented                                      |
| USPTO-MIT         | [(2017, Jin, W., et al.)](https://doi.org/10.48550/arXiv.1709.04555)      | :green_circle: Implemented                                      |
| USPTO-MIT         | [(2018, Schwaller, P., et al.)](https://doi.org/10.1039/C8SC02339E)       | :red_circle: Not Implemented (Download Limitations)             |
| USPTO-Stereo      | [(2018, Schwaller, P., et al.)](https://doi.org/10.1039/C8SC02339E)       | :red_circle: Not Implemented (Download Limitations)             |


### The Open Reaction Database
The **Open Reaction Database** [[2]](#References) (ORD) is an open-source chemical reaction database designed to
support machine learning and related efforts in chemical reaction prediction, chemical synthesis planning, and
experiment design. Currently, the ***chemical_reaction_data*** package supports the following ORD versions:

| Version | Reference                                                             | Status                     |
|---------|-----------------------------------------------------------------------|----------------------------|
| ORD     | [(2021, Kearnes, S.M., et al.)](https://doi.org/10.1021/jacs.1c09820) | :green_circle: Implemented |


### The Rhea Database
The **Rhea** database [[3]](#References) is an open-source expert-curated knowledgebase of chemical and transport
reactions of biological interest. Currently, the ***chemical_reaction_data*** package supports the following Rhea
database versions:

| Version | Reference                                                          | Status                     |
|---------|--------------------------------------------------------------------|----------------------------|
| Rhea    | [(2022, Bansal, P., et al.)](https://doi.org/10.1093/nar/gkab1016) | :green_circle: Implemented |


### The RetroRules Database
The **RetroRules** database [[4]](#References) is an open-source database of chemical reaction rules for metabolic
pathway discovery and metabolic engineering. Currently, the ***chemical_reaction_data*** package supports the following
RetroRules database versions:

| Version                    | Reference                                                            | Status                     |
|----------------------------|----------------------------------------------------------------------|----------------------------|
| RetroRules (rr01.rp2.hs)   | [(2018, Duigou, T., et al.)](https://doi.org/10.5281/zenodo.5827427) | :green_circle: Implemented |
| RetroRules (rr02.rp2.hs)   | [(2018, Duigou, T., et al.)](https://doi.org/10.5281/zenodo.5828017) | :green_circle: Implemented |
| RetroRules (rr02.rp3.hs)   | [(2018, Duigou, T., et al.)](https://doi.org/10.5281/zenodo.5827977) | :green_circle: Implemented |
| RetroRules (rr02.rp3.nohs) | [(2018, Duigou, T., et al.)](https://doi.org/10.5281/zenodo.5827969) | :green_circle: Implemented |


### Miscellaneous Data Sources
Currently, the ***chemical_reaction_data*** package supports the following miscellaneous data sources:

| Data Source                                                     | Reference                                                               | Status                     |
|-----------------------------------------------------------------|-------------------------------------------------------------------------|----------------------------|
| Chemical Reaction Classification Dataset [[5]](#References)     | [(2013, Kraut, H., et al.)](https://doi.org/10.1021/ci400442f)          | :green_circle: Implemented |
| Organic Chemistry Textbook Questions Dataset [[6]](#References) | [(2016, Wei, J.N., et al.)](https://doi.org/10.1021/acscentsci.6b00219) | :green_circle: Implemented |
| RetroTransformDB Dataset [[7]](#References)                     | [(2018, Avramova, S., et al.)](https://doi.org/10.5281/zenodo.1209312)  | :green_circle: Implemented |


## License Information
This project is published under the [MIT License](/LICENSE). For more details on the license information of individual
data sources, please refer to the original publications.


## Contact
If you are interested in contributing to this project by reporting bugs, submitting feedback or anything else that
might be beneficial, please feel free to do so via GitHub issues or [e-mail](mailto:hasic@cb.cs.titech.ac.jp). Also,
feel free to check the latest research at [Elix, Inc.](https://www.elix-inc.com/). 


## References
1. Lowe, D.M. **Extraction of Chemical Structures and Reactions from the Literature**. *Ph.D. Thesis, University of
   Cambridge, Department of Chemistry, Pembroke College*, 2012. DOI: https://doi.org/10.17863/CAM.16293.
2. Kearnes, S.M., Maser, M.R., Wleklinski, M., Kast, A., Doyle, A.G., Dreher, S.D., Hawkins, J.M., Jensen, K.F., and
   Coley, C.W. **The Open Reaction Database**. *J. Am. Chem. Soc.*, 2021, 143, 45, 18820–18826.
   DOI: https://doi.org/10.1021/jacs.1c09820.
3. Bansal, P., Morgat, A., Axelsen, K.B., Muthukrishnan, V., Coudert, E., Aimo, L., Hyka-Nouspikel, N., Gasteiger, E.,
   Kerhornou, A., Neto, T.B., Pozzato, M., Blatter, M., Ignatchenko, A., Redaschi, N., and Bridge, A. **Rhea, the
   Reaction Knowledgebase in 2022**, *Nucleic Acids Research*, 2022, 50, D1, D693–D700.
   DOI: https://doi.org/10.1093/nar/gkab1016.
4. Duigou, T., du Lac, M., Carbonell, P., and Faulon, J. **RetroRules: A Database of Reaction Rules for Engineering
   Biology**, *Nucleic Acids Research*, 2018, 47, D1, D1229–D1235. DOI: https://doi.org/10.1093/nar/gky940.
5. Kraut, H., Eiblmaier, J., Grethe, G., Löw, P., Matuszczyk, H., and Saller, H. **Algorithm for Reaction
   Classification**, *J. Chem. Inf. Model.*, 2013, 53, 11, 2884–2895. DOI: https://doi.org/10.1021/ci400442f.
6. Wei, J.N., Duvenaud, D., and Aspuru-Guzik, A. **Neural Networks for the Prediction of Organic Chemistry 
   Reactions**, *ACS Cent. Sci.*, 2016, 2, 10, 725–732. DOI: https://doi.org/10.1021/acscentsci.6b00219.
7. Avramova, S., Kochev, N., and Angelov, P. **RetroTransformDB: A Dataset of Generic Transforms for Retrosynthetic 
   Analysis**, *Data*, 2018, 3, 2. DOI: https://doi.org/10.3390/data3020014.
