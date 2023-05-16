""" The 'chemical_reaction_data.uspto' package 'parsing' module. """

from typing import Optional, Tuple

from xml.etree.ElementTree import Element


class UsptoDatasetParsingUtilities:
    """ The United States Patent and Trademark Office (USPTO) dataset parsing utilities class. """

    @staticmethod
    def parse_xml_element(
            xml_element: Element
    ) -> Tuple[Optional[str], Optional[str], Optional[str]]:
        """
        Parse a '*.xml' file element Element object.

        :parameter xml_element: The '*.xml' file element Element object.

        :returns: The parsed '*.xml' file element Element object.
        """

        dl_prefix = "{http://bitbucket.org/dan2097}"

        document_id_xml_element = xml_element.find("{0}source/{0}documentId".format(dl_prefix))
        document_id = document_id_xml_element.text if document_id_xml_element is not None else None

        paragraph_number_xml_element = xml_element.find("{0}source/{0}paragraphNum".format(dl_prefix))
        paragraph_number = paragraph_number_xml_element.text if paragraph_number_xml_element is not None else None

        reaction_smiles_xml_element = xml_element.find("{0}reactionSmiles".format(dl_prefix))
        reaction_smiles = reaction_smiles_xml_element.text if reaction_smiles_xml_element is not None else None

        return document_id, paragraph_number, reaction_smiles
