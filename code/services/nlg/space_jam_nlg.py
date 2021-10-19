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

"""Handcrafted (i.e. template-based) Natural Language Generation Module"""

import inspect
import os

from services.nlg.templates.templatefile import TemplateFile
from services.service import PublishSubscribe
from services.service import Service
from utils.common import Language
from utils.domain.domain import Domain
from utils.logger import DiasysLogger
from utils.sysact import SysAct, SysActionType
from typing import Dict
import string

class SpaceJamHandcraftedNLG(Service):
    """Handcrafted (i.e. template-based) Natural Language Generation Module

    A rule-based approach on natural language generation.
    The rules have to be specified within a template file using the ADVISER NLG syntax.
    Python methods that are called within a template file must be specified in the
    HandcraftedNLG class by using the prefix "_template_". For example, the method
    "_template_genitive_s" can be accessed in the template file via calling {genitive_s(name)}

    Attributes:
        domain (Domain): the domain
        template_filename (str): the NLG template filename
        templates (TemplateFile): the parsed and ready-to-go NLG template file
        template_english (str): the name of the English NLG template file
        template_german (str): the name of the German NLG template file
        language (Language): the language of the dialogue
    """
    def __init__(self, domain: Domain, sub_topic_domains: Dict[str, str] = {},
                 logger: DiasysLogger = DiasysLogger()):
        """Constructor mainly extracts methods and rules from the template file"""
        Service.__init__(self, domain=domain, sub_topic_domains=sub_topic_domains)

        self.templates_human = None
        self.templates_factual = None
        self.user_lookup = {'factual': set(), 'human': set()}       
        self.domain = domain
        self.template_filename = None
        self.logger = logger

        self.language = Language.ENGLISH
        self._initialise_templates(self.language)

    @PublishSubscribe(sub_topics=["sys_acts"], pub_topics=["sys_utterance"])
    def generate_system_utterance(self, user_id: str = "default", sys_acts: SysAct = None) -> dict(sys_utterance=str):
        """

        Takes a system act, searches for a fitting rule, applies it
        and returns the message.

        Args:
            sys_act (SysAct): The system act, to check whether the dialogue was finished

        Returns:
            dict: a dict containing the system utterance
        """
        # message = str(sys_acts)
        rule_found = True
        message = ""
        bad_act = None
        templates = self.get_template(user_id)
        # TODO: go back to policy and put acts in correct order
        # put acts in wrong order in policy and it's much easier to fix that here --LV
        if SysActionType.Explain in [act.type for act in sys_acts]:
            sys_acts = sys_acts[::-1]

        for act in sys_acts:
            try:
                message += templates.create_message(act)
            except BaseException as error:
                rule_found = False
                self.logger.error(error)
                bad_act = act
                # raise(error)

        # inform if no applicable rule could be found in the template file
        if not rule_found:
            self.logger.info(f'# USER {user_id} # NLG-ERROR ({self.domain.get_domain_name()}) - Could not find a fitting rule for the given system act!')
            self.logger.info(f"# USER {user_id} # NLG-ERROR ({self.domain.get_domain_name()}) - System Action: {str(bad_act.type)} - Slots: {str(bad_act.slot_values)}")

        self.logger.dialog_turn(f"# USER {user_id} # NLG-MSG ({self.domain.get_domain_name()}) - {message}")
        return {'sys_utterance': message}

    def _initialise_templates(self, language: Language):
        """
            Loads the correct template file based on which language has been selected
            this should only be called on the first turn of the dialog

            Args:
                language (Language): Enum representing the language the user has selected
        """
        template_filename_factual = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '../../resources/nlg_templates/%sMessagesFactual.nlg' % self.domain.get_domain_name())
        template_filename_human = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '../../resources/nlg_templates/%sMessagesPersonal.nlg' % self.domain.get_domain_name())

        self.templates_factual = TemplateFile(template_filename_factual, self.domain)
        self.templates_human = TemplateFile(template_filename_human, self.domain)
        self._add_additional_methods_for_template_file()

    def _add_additional_methods_for_template_file(self):
        """add the function prefixed by "_template_" to the template file interpreter"""
        for (method_name, method) in inspect.getmembers(type(self), inspect.isfunction):
            if method_name.startswith('_template_'):
                self.templates_human.add_python_function(method_name[10:], method, [self])
                self.templates_factual.add_python_function(method_name[10:], method, [self])

    def _template_genitive_s(self, name: str) -> str:
        if name[-1] == 's':
            return f"{name}'"
        else:
            return f"{name}'s"

    def _template_genitive_s_german(self, name: str) -> str:
        if name[-1] in ('s', 'x', 'ß', 'z'):
            return f"{name}'"
        else:
            return f"{name}s"

    def _template_plural_s(self, name: str) -> str:
        if name[-1] in ('m', 'e'): # capturing (repeat) exam = (repeat) exams, requirements modules
            return f"{name}s"
        else:
            return f"{name}"

    def _template_cap_name(self, name: str) -> str:
        return string.capwords(name)

    def get_template(self, user_id):
        """
            looks up which template set to user for each user, if the user has not yet been assigned a group, tries
            to balance user pools, alternating between human and factual
        """
        if user_id in self.user_lookup['human']:
            return self.templates_human
        elif user_id in self.user_lookup['factual']:
            return self.templates_factual
        else:
            num_human = len(self.user_lookup['human'])
            num_factual = len(self.user_lookup['factual'])
            if num_human <= num_factual:
                self.user_lookup['human'].add(user_id)
                self.logger.info(f'# USER {user_id} # CONDITION: personal')
                return self.templates_human
            else:
                self.user_lookup['factual'].add(user_id)
                self.logger.info(f'# USER {user_id} # CONDITION: factual')
                return self.templates_factual