###############################################################################
#
# Copyright 2019, University of Stuttgart: Institute for Natural Language Processing (IMS)
#
# This file is part of Adviser.
# Adviser is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3.
#
# Adviser is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Adviser.  If not, see <https://www.gnu.org/licenses/>.
#
###############################################################################


import json
import os
import sqlite3
from io import StringIO
from typing import List, Iterable

from utils.domain import Domain


class SpaceJamDomain(Domain):
    """ Abstract class for linking a domain based on a JSON-ontology with a database
       access method (sqllite).
    """

    def __init__(self, name: str, json_ontology_file: str = None, \
                 display_name: str = None):
        """ Loads the ontology from a json file and the data from a sqllite
            database.

            To create a new domain using this format, inherit from this class
            and overwrite the _get_domain_name_()-method to return your
            domain's name.

        Arguments:
            name (str): the domain's name used as an identifier
            json_ontology_file (str): relative path to the ontology file
                                (from the top-level adviser directory, e.g. resources/ontologies)
            sqllite_db_file (str): relative path to the database file
                                (from the top-level adviser directory, e.g. resources/databases)
            display_name (str): the domain's name as it appears on the screen
                                (e.g. containing whitespaces)
        """
        super(SpaceJamDomain, self).__init__(name)

        root_dir = self._get_root_dir()
        # make sure to set default values in case of None
        json_ontology_file = json_ontology_file or os.path.join('resources', 'ontologies',
                                                                name + '.json')
        self.ontology_json = json.load(open(root_dir + '/' + json_ontology_file))
        self.display_name = display_name if display_name is not None else name

    def _get_root_dir(self):
        """ Returns the path to the root directory """
        return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    def get_display_name(self):
        return self.display_name

    def get_requestable_slots(self) -> List[str]:
        """ Returns a list of all slots requestable by the user. """
        return self.ontology_json['requestable']

    def get_system_requestable_slots(self) -> List[str]:
        """ Returns a list of all slots requestable by the system. """
        return self.ontology_json['system_requestable']

    def get_informable_slots(self) -> List[str]:
        """ Returns a list of all informable slots. """
        return self.ontology_json['informable'].keys()

    def get_possible_values(self, slot: str) -> List[str]:
        """ Returns all possible values for an informable slot

        Args:
            slot (str): name of the slot

        Returns:
            a list of strings, each string representing one possible value for
            the specified slot.
         """
        return self.ontology_json['informable'][slot]


        if slot in self.ontology_json['pronoun_map']:
            return self.ontology_json['pronoun_map'][slot]
        else:
            return []

    def get_discourse_acts(self):
        """ Returns list of all discourse acts """
        return self.ontology_json["discourseAct"]

    def get_describable_slots(self):
        """ Returns list of all describable slots """
        return self.ontology_json["describable"]

    def get_keyword(self):
        """ Returns keyword that identifies the domain """
        return self.ontology_json["keyword"]