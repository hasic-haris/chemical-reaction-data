""" The 'chemical_reaction_data.ord' package 'parsing' module. """

from typing import Iterable, List, Optional, Tuple

from ord_schema import message_helpers

from ord_schema.proto.reaction_pb2 import Reaction, ReactionIdentifier, ReactionInput, ReactionOutcome

from ..utilities.chemistry.compounds import CompoundFormatConversionUtilities
from ..utilities.chemistry.reactions import ReactionFormatConversionUtilities


class OrdParsingUtilities:
    """ The Open Reaction Database (ORD) parsing utilities class. """

    @staticmethod
    def _parse_reaction_identifier_messages(
            reaction_identifier_messages: Iterable[ReactionIdentifier]
    ) -> Optional[str]:
        """
        Parse chemical reaction identifier message ReactionIdentifier objects.

        :parameter reaction_identifier_messages: The chemical reaction identifier message ReactionIdentifier objects.

        :returns: The parsed chemical reaction identifier message ReactionIdentifier objects.
        """

        reaction_identifiers = list()

        for reaction_identifier_message in reaction_identifier_messages:
            reaction_identifier = message_helpers.message_to_row(
                message=reaction_identifier_message
            )

            # ----------------------------------------------------------------------------------------------------------
            #  Parse the chemical reaction SMILES string from a 'REACTION_CXSMILES' or 'REACTION_SMILES' identifier.
            # ----------------------------------------------------------------------------------------------------------

            if "type" in reaction_identifier.keys() and "value" in reaction_identifier.keys():
                if reaction_identifier["type"] in ["REACTION_CXSMILES", "REACTION_SMILES"]:
                    return reaction_identifier["value"]

                reaction_identifiers.append((
                    reaction_identifier["type"],
                    reaction_identifier["value"]
                ))

        # --------------------------------------------------------------------------------------------------------------
        #  Parse the chemical reaction SMILES string from a 'CUSTOM' or 'UNSPECIFIED' identifier.
        # --------------------------------------------------------------------------------------------------------------

        for reaction_identifier in reaction_identifiers:
            if reaction_identifier[0] in ["CUSTOM", "UNSPECIFIED"]:
                reaction_rxn = ReactionFormatConversionUtilities.smiles_to_rxn(
                    reaction_smiles=reaction_identifier[1]
                )

                if reaction_rxn is not None:
                    return reaction_identifier[1]

        return None

    @staticmethod
    def _parse_reaction_input_messages(
            reaction_input_messages: Iterable[ReactionInput]
    ) -> Tuple[List[str], List[str]]:
        """
        Parse chemical reaction input message ReactionInput objects.

        :parameter reaction_input_messages: The chemical reaction input message ReactionInput objects.

        :returns: The parsed chemical reaction input message ReactionInput objects.
        """

        reaction_input_reactant_smiles_strings, reaction_input_spectator_smiles_strings = list(), list()

        for reaction_input_message in reaction_input_messages:
            for reaction_input_component_message in reaction_input_message.components:
                reaction_input_component = message_helpers.message_to_row(
                    message=reaction_input_component_message
                )

                reaction_input_component_identifier_keys = [
                    reaction_input_component_key.split(".")[0]
                    for reaction_input_component_key in reaction_input_component.keys()
                    if "identifiers" in reaction_input_component_key and (
                        "type" in reaction_input_component_key or "value" in reaction_input_component_key
                    )
                ]

                reaction_input_component_identifiers = list()

                # ------------------------------------------------------------------------------------------------------
                #  Parse the chemical reaction reactant and spectator compound SMILES strings from the 'CXSMILES' or
                #  'SMILES' input component identifiers.
                # ------------------------------------------------------------------------------------------------------

                for reaction_input_component_identifier_key in reaction_input_component_identifier_keys:
                    if reaction_input_component[".".join([reaction_input_component_identifier_key, "type"])] in [
                        "CXSMILES", "SMILES"
                    ]:
                        if "reaction_role" in reaction_input_component.keys() and \
                                reaction_input_component["reaction_role"] in ["CATALYST", "REAGENT", "SOLVENT"]:
                            reaction_input_spectator_smiles_strings.append(
                                reaction_input_component[".".join([reaction_input_component_identifier_key, "value"])]
                            )

                        else:
                            reaction_input_reactant_smiles_strings.append(
                                reaction_input_component[".".join([reaction_input_component_identifier_key, "value"])]
                            )

                        reaction_input_component_identifiers = None

                        break

                    reaction_input_component_identifiers.append((
                        reaction_input_component["reaction_role"]
                        if "reaction_role" in reaction_input_component.keys() else None,
                        reaction_input_component[".".join([reaction_input_component_identifier_key, "type"])],
                        reaction_input_component[".".join([reaction_input_component_identifier_key, "value"])]
                    ))

                # ------------------------------------------------------------------------------------------------------
                #  Parse the chemical reaction reactant and spectator compound SMILES strings from the 'INCHI' input
                #  component identifiers.
                # ------------------------------------------------------------------------------------------------------

                if reaction_input_component_identifiers is not None:
                    for reaction_input_component_identifier in reaction_input_component_identifiers:
                        if reaction_input_component_identifier[1] == "INCHI":
                            compound_mol = CompoundFormatConversionUtilities.inchi_to_mol(
                                compound_inchi=reaction_input_component_identifier[2]
                            )

                            if compound_mol is not None:
                                if reaction_input_component_identifier[0] in ["CATALYST", "REAGENT", "SOLVENT"]:
                                    reaction_input_spectator_smiles_strings.append(
                                        CompoundFormatConversionUtilities.mol_to_smiles(
                                            compound_mol=compound_mol
                                        )
                                    )

                                else:
                                    reaction_input_reactant_smiles_strings.append(
                                        CompoundFormatConversionUtilities.mol_to_smiles(
                                            compound_mol=compound_mol
                                        )
                                    )

                                reaction_input_component_identifiers = None

                                break

                # ------------------------------------------------------------------------------------------------------
                #  Parse the chemical reaction reactant and spectator compound SMILES strings from the 'CUSTOM' or
                #  'UNSPECIFIED' input component identifiers.
                # ------------------------------------------------------------------------------------------------------

                if reaction_input_component_identifiers is not None:
                    for reaction_input_component_identifier in reaction_input_component_identifiers:
                        if reaction_input_component_identifier[1] in ["CUSTOM", "UNSPECIFIED"]:
                            compound_mol = CompoundFormatConversionUtilities.smiles_to_mol(
                                compound_smiles=reaction_input_component_identifier[2]
                            )

                            if compound_mol is not None:
                                compound_mol = CompoundFormatConversionUtilities.inchi_to_mol(
                                    compound_inchi=reaction_input_component_identifier[2]
                                )

                            if compound_mol is not None:
                                if reaction_input_component_identifier[0] in ["CATALYST", "REAGENT", "SOLVENT"]:
                                    reaction_input_spectator_smiles_strings.append(
                                        CompoundFormatConversionUtilities.mol_to_smiles(
                                            compound_mol=compound_mol
                                        )
                                    )

                                else:
                                    reaction_input_reactant_smiles_strings.append(
                                        CompoundFormatConversionUtilities.mol_to_smiles(
                                            compound_mol=compound_mol
                                        )
                                    )

                                break

        return reaction_input_reactant_smiles_strings, reaction_input_spectator_smiles_strings

    @staticmethod
    def _parse_reaction_outcome_messages(
            reaction_outcome_messages: Iterable[ReactionOutcome]
    ) -> List[str]:
        """
        Parse chemical reaction outcome message ReactionOutcome objects.

        :parameter reaction_outcome_messages: The chemical reaction outcome message ReactionOutcome objects.

        :returns: The parsed chemical reaction outcome message ReactionOutcome objects.
        """

        reaction_outcome_product_smiles_strings = list()

        for reaction_outcome_message in reaction_outcome_messages:
            for reaction_outcome_product_message in reaction_outcome_message.products:
                reaction_outcome_product = message_helpers.message_to_row(
                    message=reaction_outcome_product_message
                )

                reaction_outcome_product_identifier_keys = [
                    reaction_outcome_product_key.split(".")[0]
                    for reaction_outcome_product_key in reaction_outcome_product.keys()
                    if "identifiers" in reaction_outcome_product_key and (
                        "type" in reaction_outcome_product_key or "value" in reaction_outcome_product_key
                    )
                ]

                reaction_outcome_product_identifiers = list()

                # ------------------------------------------------------------------------------------------------------
                #  Parse the chemical reaction product compound SMILES strings from the 'CXSMILES' or 'SMILES' input
                #  component identifiers.
                # ------------------------------------------------------------------------------------------------------

                for reaction_outcome_product_identifier_key in reaction_outcome_product_identifier_keys:
                    if reaction_outcome_product[".".join([reaction_outcome_product_identifier_key, "type"])] in [
                        "CXSMILES", "SMILES"
                    ]:
                        reaction_outcome_product_smiles_strings.append(
                            reaction_outcome_product[".".join([reaction_outcome_product_identifier_key, "value"])]
                        )

                        reaction_outcome_product_identifiers = None

                        break

                    reaction_outcome_product_identifiers.append((
                        reaction_outcome_product[".".join([reaction_outcome_product_identifier_key, "type"])],
                        reaction_outcome_product[".".join([reaction_outcome_product_identifier_key, "value"])]
                    ))

                # ------------------------------------------------------------------------------------------------------
                #  Parse the chemical reaction product compound SMILES strings from the 'INCHI' input component
                #  identifiers.
                # ------------------------------------------------------------------------------------------------------

                if reaction_outcome_product_identifiers is not None:
                    for reaction_outcome_product_identifier in reaction_outcome_product_identifiers:
                        if reaction_outcome_product_identifier[0] == "INCHI":
                            compound_mol = CompoundFormatConversionUtilities.inchi_to_mol(
                                compound_inchi=reaction_outcome_product_identifier[1]
                            )

                            if compound_mol is not None:
                                reaction_outcome_product_smiles_strings.append(
                                    CompoundFormatConversionUtilities.mol_to_smiles(
                                        compound_mol=compound_mol
                                    )
                                )

                                reaction_outcome_product_identifiers = None

                                break

                # ------------------------------------------------------------------------------------------------------
                #  Parse the chemical reaction product compound SMILES strings from the 'CUSTOM' or 'UNSPECIFIED' input
                #  component identifiers.
                # ------------------------------------------------------------------------------------------------------

                if reaction_outcome_product_identifiers is not None:
                    for reaction_outcome_product_identifier in reaction_outcome_product_identifiers:
                        if reaction_outcome_product_identifier[0] in ["CUSTOM", "UNSPECIFIED"]:
                            compound_mol = CompoundFormatConversionUtilities.smiles_to_mol(
                                compound_smiles=reaction_outcome_product_identifier[1]
                            )

                            if compound_mol is not None:
                                compound_mol = CompoundFormatConversionUtilities.inchi_to_mol(
                                    compound_inchi=reaction_outcome_product_identifier[1]
                                )

                            if compound_mol is not None:
                                reaction_outcome_product_smiles_strings.append(
                                    CompoundFormatConversionUtilities.mol_to_smiles(
                                        compound_mol=compound_mol
                                    )
                                )

                                break

        return reaction_outcome_product_smiles_strings

    @staticmethod
    def parse_reaction_message(
            reaction_message: Reaction
    ) -> Tuple[str, str, str]:
        """
        Parse a chemical reaction message Reaction object.

        :parameter reaction_message: The chemical reaction message Reaction object.

        :returns: The parsed chemical reaction message Reaction object.
        """

        reaction_id = reaction_message.reaction_id

        reaction_smiles = OrdParsingUtilities._parse_reaction_identifier_messages(
            reaction_identifier_messages=reaction_message.identifiers
        )

        reactant_smiles_strings, spectator_smiles_strings = OrdParsingUtilities._parse_reaction_input_messages(
            reaction_input_messages=reaction_message.inputs.values()
        )

        product_smiles_strings = OrdParsingUtilities._parse_reaction_outcome_messages(
            reaction_outcome_messages=reaction_message.outcomes
        )

        return reaction_id, reaction_smiles, ">".join([
            ".".join(reactant_smiles_strings) if len(reactant_smiles_strings) > 0 else "",
            ".".join(spectator_smiles_strings) if len(spectator_smiles_strings) > 0 else "",
            ".".join(product_smiles_strings) if len(product_smiles_strings) > 0 else ""
        ])
