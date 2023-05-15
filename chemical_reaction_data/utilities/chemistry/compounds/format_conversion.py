""" The 'chemical_reaction_data.utilities.chemistry.compounds' package 'format_conversion' module. """

from logging import getLogger
from typing import Optional

from rdkit.Chem.inchi import MolFromInchi
from rdkit.Chem.rdchem import Mol
from rdkit.Chem.rdmolfiles import MolFromSmiles, MolToSmiles


class CompoundFormatConversionUtilities:
    """ The chemical compound format conversion utilities class. """

    @staticmethod
    def inchi_to_mol(
            compound_inchi: str,
            enable_logger: bool = False,
            **kwargs
    ) -> Optional[Mol]:
        """
        Convert a chemical compound InChI string to a Mol object.

        :parameter compound_inchi: The chemical compound InChI string.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        :parameter kwargs: The default keyword arguments for the adjustment of underlying functions.

        :returns: The chemical compound Mol object.
        """

        try:
            return MolFromInchi(
                compound_inchi,
                sanitize=kwargs["sanitize"] if "sanitize" in kwargs.keys() else True,
                removeHs=kwargs["removeHs"] if "removeHs" in kwargs.keys() else True,
                logLevel=kwargs["logLevel"] if "logLevel" in kwargs.keys() else None,
                treatWarningAsError=kwargs["treatWarningAsError"] if "treatWarningAsError" in kwargs.keys() else False
            )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.CompoundFormatConversionUtilities.inchi_to_mol".format(__name__)
                ).debug(exception_handle)

            return None

    @staticmethod
    def mol_to_smiles(
            compound_mol: Mol,
            enable_logger: bool = False,
            **kwargs
    ) -> Optional[str]:
        """
        Convert a chemical compound Mol object to a SMILES string.

        :parameter compound_mol: The chemical compound Mol object.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        :parameter kwargs: The default keyword arguments for the adjustment of underlying functions.

        :returns: The chemical compound SMILES string.
        """

        try:
            return MolToSmiles(
                compound_mol,
                isomericSmiles=kwargs["isomericSmiles"] if "isomericSmiles" in kwargs.keys() else True,
                kekuleSmiles=kwargs["kekuleSmiles"] if "kekuleSmiles" in kwargs.keys() else False,
                rootedAtAtom=kwargs["rootedAtAtom"] if "rootedAtAtom" in kwargs.keys() else -1,
                canonical=kwargs["canonical"] if "canonical" in kwargs.keys() else True,
                allBondsExplicit=kwargs["allBondsExplicit"] if "allBondsExplicit" in kwargs.keys() else False,
                allHsExplicit=kwargs["allHsExplicit"] if "allHsExplicit" in kwargs.keys() else False,
                doRandom=kwargs["doRandom"] if "doRandom" in kwargs.keys() else False
            )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.CompoundFormatConversionUtilities.mol_to_smiles".format(__name__)
                ).debug(exception_handle)

            return None

    @staticmethod
    def smiles_to_mol(
            compound_smiles: str,
            enable_logger: bool = False,
            **kwargs
    ) -> Optional[Mol]:
        """
        Convert a chemical compound SMILES string to a Mol object.

        :parameter compound_smiles: The chemical compound SMILES string.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        :parameter kwargs: The default keyword arguments for the adjustment of underlying functions.

        :returns: The chemical compound Mol object.
        """

        try:
            return MolFromSmiles(
                compound_smiles,
                sanitize=kwargs["sanitize"] if "sanitize" in kwargs.keys() else True,
                replacements=kwargs["replacements"] if "replacements" in kwargs.keys() else {}
            )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.CompoundFormatConversionUtilities.smiles_to_mol".format(__name__)
                ).debug(exception_handle)

            return None
