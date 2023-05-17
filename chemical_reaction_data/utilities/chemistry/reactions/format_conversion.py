""" The 'chemical_reaction_data.utilities.chemistry.reactions' package 'format_conversion' module. """

from logging import getLogger
from typing import Optional

from rdkit.Chem.rdChemReactions import ChemicalReaction, ReactionFromRxnBlock, ReactionFromSmarts, ReactionToSmiles


class ReactionFormatConversionUtilities:
    """ The chemical reaction format conversion utilities class. """

    @staticmethod
    def rxn_block_to_rxn(
            reaction_rxn_block: str,
            enable_logger: bool = False,
            **kwargs
    ) -> Optional[ChemicalReaction]:
        """
        Convert a chemical reaction MDL RXNfile block string to a ChemicalReaction object.

        :parameter reaction_rxn_block: The chemical reaction MDL RXNfile block string.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        :parameter kwargs: The default keyword arguments for the adjustment of underlying functions:
                           'rdkit.Chem.rdChemReactions.{ReactionFromRxnBlock}'.

        :returns: The chemical reaction ChemicalReaction object.
        """

        try:
            return ReactionFromRxnBlock(
                reaction_rxn_block,
                sanitize=kwargs["sanitize"] if "sanitize" in kwargs.keys() else False,
                removeHs=kwargs["removeHs"] if "removeHs" in kwargs.keys() else False,
                strictParsing=kwargs["strictParsing"] if "strictParsing" in kwargs.keys() else True
            )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.ReactionFormatConversionUtilities.rxn_block_to_rxn".format(__name__)
                ).debug(exception_handle)

            return None

    @staticmethod
    def rxn_to_smiles(
            reaction_rxn: ChemicalReaction,
            enable_logger: bool = False,
            **kwargs
    ) -> Optional[str]:
        """
        Convert a chemical reaction ChemicalReaction object to a SMILES string.

        :parameter reaction_rxn: The chemical reaction ChemicalReaction object.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        :parameter kwargs: The default keyword arguments for the adjustment of underlying functions:
                           'rdkit.Chem.rdChemReactions.{ReactionToSmiles}'.

        :returns: The chemical reaction SMILES string.
        """

        try:
            return ReactionToSmiles(
                reaction_rxn,
                canonical=kwargs["canonical"] if "canonical" in kwargs.keys() else True
            )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.ReactionFormatConversionUtilities.rxn_to_smiles".format(__name__)
                ).debug(exception_handle)

            return None

    @staticmethod
    def smiles_to_rxn(
            reaction_smiles: str,
            enable_logger: bool = False,
            **kwargs
    ) -> Optional[ChemicalReaction]:
        """
        Convert a chemical reaction SMILES string to a ChemicalReaction object.

        :parameter reaction_smiles: The chemical reaction SMILES string.
        :parameter enable_logger: The indicator whether the logger should be enabled.
        :parameter kwargs: The default keyword arguments for the adjustment of underlying functions:
                           'rdkit.Chem.rdChemReactions.{ReactionFromSmarts}'.

        :returns: The chemical reaction ChemicalReaction object.
        """

        try:
            return ReactionFromSmarts(
                reaction_smiles,
                replacements=kwargs["replacements"] if "replacements" in kwargs.keys() else {},
                useSmiles=kwargs["useSmiles"] if "useSmiles" in kwargs.keys() else False
            )

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.ReactionFormatConversionUtilities.smiles_to_rxn".format(__name__)
                ).debug(exception_handle)

            return None
