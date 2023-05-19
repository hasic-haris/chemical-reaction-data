""" The 'chemical_reaction_data' package initialization module. """

from logging import Formatter, getLogger, INFO, StreamHandler

from rdkit.RDLogger import DisableLog


__author__, __institution__, __version__ = (
    "Haris Hasic",
    "Ishida Laboratory, Department of Computer Science, Tokyo Institute of Technology && Elix, Inc.",
    "2023.1.1"
)


DisableLog("rdApp.*")

chemical_reaction_data_logger = getLogger(__name__)
chemical_reaction_data_logger.setLevel(INFO)

chemical_reaction_data_stream_handler = StreamHandler()
chemical_reaction_data_stream_handler.setLevel(INFO)
chemical_reaction_data_stream_handler.setFormatter(Formatter("%(asctime)s (%(levelname)s @ %(name)s): %(message)s"))

chemical_reaction_data_logger.addHandler(chemical_reaction_data_stream_handler)
