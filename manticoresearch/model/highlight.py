# coding: utf-8

# Manticore Search Client
# Copyright (c) 2020-2021, Manticore Software LTD (https://manticoresearch.com)
# 
# All rights reserved
#



import pprint
import re  # noqa: F401

import six

from manticoresearch.configuration import Configuration

class Highlight(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'fieldnames': '[str]',
        'fields': '[HighlightField]',
        'encoder': 'str',
        'highlight_query': 'FulltextFilter',
        'pre_tags': 'str',
        'post_tags': 'str',
        'no_match_size': 'int',
        'fragment_size': 'int',
        'number_of_fragments': 'int',
        'limits_per_field': 'bool',
        'use_boundaries': 'bool',
        'force_all_words': 'bool',
        'allow_empty': 'bool',
        'emit_zones': 'bool',
        'force_snippets': 'bool',
        'around': 'int',
        'start_snippet_id': 'int',
        'html_strip_mode': 'str',
        'snippet_boundary': 'str'
    }

    attribute_map = {
        'fieldnames': 'fieldnames',
        'fields': 'fields',
        'encoder': 'encoder',
        'highlight_query': 'highlight_query',
        'pre_tags': 'pre_tags',
        'post_tags': 'post_tags',
        'no_match_size': 'no_match_size',
        'fragment_size': 'fragment_size',
        'number_of_fragments': 'number_of_fragments',
        'limits_per_field': 'limits_per_field',
        'use_boundaries': 'use_boundaries',
        'force_all_words': 'force_all_words',
        'allow_empty': 'allow_empty',
        'emit_zones': 'emit_zones',
        'force_snippets': 'force_snippets',
        'around': 'around',
        'start_snippet_id': 'start_snippet_id',
        'html_strip_mode': 'html_strip_mode',
        'snippet_boundary': 'snippet_boundary'
    }

    def __init__(self, fieldnames=None, fields=None, encoder=None, highlight_query=None, pre_tags="<strong>", post_tags="</strong>", no_match_size=1, fragment_size=256, number_of_fragments=0, limits_per_field=False, use_boundaries=False, force_all_words=False, allow_empty=False, emit_zones=False, force_snippets=False, around=5, start_snippet_id=1, html_strip_mode=None, snippet_boundary=None, local_vars_configuration=None):  # noqa: E501
        """Highlight - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._fieldnames = None
        self._fields = None
        self._encoder = None
        self._highlight_query = None
        self._pre_tags = None
        self._post_tags = None
        self._no_match_size = None
        self._fragment_size = None
        self._number_of_fragments = None
        self._limits_per_field = None
        self._use_boundaries = None
        self._force_all_words = None
        self._allow_empty = None
        self._emit_zones = None
        self._force_snippets = None
        self._around = None
        self._start_snippet_id = None
        self._html_strip_mode = None
        self._snippet_boundary = None
        self.discriminator = None

        if fieldnames is not None:
            self.fieldnames = fieldnames
        if fields is not None:
            self.fields = fields
        if encoder is not None:
            self.encoder = encoder
        if highlight_query is not None:
            self.highlight_query = highlight_query
        if pre_tags is not None:
            self.pre_tags = pre_tags
        if post_tags is not None:
            self.post_tags = post_tags
        if no_match_size is not None:
            self.no_match_size = no_match_size
        if fragment_size is not None:
            self.fragment_size = fragment_size
        if number_of_fragments is not None:
            self.number_of_fragments = number_of_fragments
        if limits_per_field is not None:
            self.limits_per_field = limits_per_field
        if use_boundaries is not None:
            self.use_boundaries = use_boundaries
        if force_all_words is not None:
            self.force_all_words = force_all_words
        if allow_empty is not None:
            self.allow_empty = allow_empty
        if emit_zones is not None:
            self.emit_zones = emit_zones
        if force_snippets is not None:
            self.force_snippets = force_snippets
        if around is not None:
            self.around = around
        if start_snippet_id is not None:
            self.start_snippet_id = start_snippet_id
        if html_strip_mode is not None:
            self.html_strip_mode = html_strip_mode
        if snippet_boundary is not None:
            self.snippet_boundary = snippet_boundary

    @property
    def fieldnames(self):
        """Gets the fieldnames of this Highlight.  # noqa: E501


        :return: The fieldnames of this Highlight.  # noqa: E501
        :rtype: [str]
        """
        return self._fieldnames
    @fieldnames.setter
    def fieldnames(self, fieldnames):
        """Sets the fieldnames of this Highlight.


        :param fieldnames: The fieldnames of this Highlight.  # noqa: E501
        :type fieldnames: [str]
        """

        self._fieldnames = fieldnames
    @property
    def fields(self):
        """Gets the fields of this Highlight.  # noqa: E501


        :return: The fields of this Highlight.  # noqa: E501
        :rtype: [HighlightField]
        """
        return self._fields
    @fields.setter
    def fields(self, fields):
        """Sets the fields of this Highlight.


        :param fields: The fields of this Highlight.  # noqa: E501
        :type fields: [HighlightField]
        """

        self._fields = fields
    @property
    def encoder(self):
        """Gets the encoder of this Highlight.  # noqa: E501


        :return: The encoder of this Highlight.  # noqa: E501
        :rtype: str
        """
        return self._encoder
    @encoder.setter
    def encoder(self, encoder):
        """Sets the encoder of this Highlight.


        :param encoder: The encoder of this Highlight.  # noqa: E501
        :type encoder: str
        """
        allowed_values = ["default", "html"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and encoder not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `encoder` ({0}), must be one of {1}"  # noqa: E501
                .format(encoder, allowed_values)
            )

        self._encoder = encoder
    @property
    def highlight_query(self):
        """Gets the highlight_query of this Highlight.  # noqa: E501


        :return: The highlight_query of this Highlight.  # noqa: E501
        :rtype: FulltextFilter
        """
        return self._highlight_query
    @highlight_query.setter
    def highlight_query(self, highlight_query):
        """Sets the highlight_query of this Highlight.


        :param highlight_query: The highlight_query of this Highlight.  # noqa: E501
        :type highlight_query: FulltextFilter
        """

        self._highlight_query = highlight_query
    @property
    def pre_tags(self):
        """Gets the pre_tags of this Highlight.  # noqa: E501


        :return: The pre_tags of this Highlight.  # noqa: E501
        :rtype: str
        """
        return self._pre_tags
    @pre_tags.setter
    def pre_tags(self, pre_tags):
        """Sets the pre_tags of this Highlight.


        :param pre_tags: The pre_tags of this Highlight.  # noqa: E501
        :type pre_tags: str
        """

        self._pre_tags = pre_tags
    @property
    def post_tags(self):
        """Gets the post_tags of this Highlight.  # noqa: E501


        :return: The post_tags of this Highlight.  # noqa: E501
        :rtype: str
        """
        return self._post_tags
    @post_tags.setter
    def post_tags(self, post_tags):
        """Sets the post_tags of this Highlight.


        :param post_tags: The post_tags of this Highlight.  # noqa: E501
        :type post_tags: str
        """

        self._post_tags = post_tags
    @property
    def no_match_size(self):
        """Gets the no_match_size of this Highlight.  # noqa: E501


        :return: The no_match_size of this Highlight.  # noqa: E501
        :rtype: int
        """
        return self._no_match_size
    @no_match_size.setter
    def no_match_size(self, no_match_size):
        """Sets the no_match_size of this Highlight.


        :param no_match_size: The no_match_size of this Highlight.  # noqa: E501
        :type no_match_size: int
        """
        allowed_values = [0, 1]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and no_match_size not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `no_match_size` ({0}), must be one of {1}"  # noqa: E501
                .format(no_match_size, allowed_values)
            )

        self._no_match_size = no_match_size
    @property
    def fragment_size(self):
        """Gets the fragment_size of this Highlight.  # noqa: E501


        :return: The fragment_size of this Highlight.  # noqa: E501
        :rtype: int
        """
        return self._fragment_size
    @fragment_size.setter
    def fragment_size(self, fragment_size):
        """Sets the fragment_size of this Highlight.


        :param fragment_size: The fragment_size of this Highlight.  # noqa: E501
        :type fragment_size: int
        """

        self._fragment_size = fragment_size
    @property
    def number_of_fragments(self):
        """Gets the number_of_fragments of this Highlight.  # noqa: E501


        :return: The number_of_fragments of this Highlight.  # noqa: E501
        :rtype: int
        """
        return self._number_of_fragments
    @number_of_fragments.setter
    def number_of_fragments(self, number_of_fragments):
        """Sets the number_of_fragments of this Highlight.


        :param number_of_fragments: The number_of_fragments of this Highlight.  # noqa: E501
        :type number_of_fragments: int
        """

        self._number_of_fragments = number_of_fragments
    @property
    def limits_per_field(self):
        """Gets the limits_per_field of this Highlight.  # noqa: E501


        :return: The limits_per_field of this Highlight.  # noqa: E501
        :rtype: bool
        """
        return self._limits_per_field
    @limits_per_field.setter
    def limits_per_field(self, limits_per_field):
        """Sets the limits_per_field of this Highlight.


        :param limits_per_field: The limits_per_field of this Highlight.  # noqa: E501
        :type limits_per_field: bool
        """

        self._limits_per_field = limits_per_field
    @property
    def use_boundaries(self):
        """Gets the use_boundaries of this Highlight.  # noqa: E501


        :return: The use_boundaries of this Highlight.  # noqa: E501
        :rtype: bool
        """
        return self._use_boundaries
    @use_boundaries.setter
    def use_boundaries(self, use_boundaries):
        """Sets the use_boundaries of this Highlight.


        :param use_boundaries: The use_boundaries of this Highlight.  # noqa: E501
        :type use_boundaries: bool
        """

        self._use_boundaries = use_boundaries
    @property
    def force_all_words(self):
        """Gets the force_all_words of this Highlight.  # noqa: E501


        :return: The force_all_words of this Highlight.  # noqa: E501
        :rtype: bool
        """
        return self._force_all_words
    @force_all_words.setter
    def force_all_words(self, force_all_words):
        """Sets the force_all_words of this Highlight.


        :param force_all_words: The force_all_words of this Highlight.  # noqa: E501
        :type force_all_words: bool
        """

        self._force_all_words = force_all_words
    @property
    def allow_empty(self):
        """Gets the allow_empty of this Highlight.  # noqa: E501


        :return: The allow_empty of this Highlight.  # noqa: E501
        :rtype: bool
        """
        return self._allow_empty
    @allow_empty.setter
    def allow_empty(self, allow_empty):
        """Sets the allow_empty of this Highlight.


        :param allow_empty: The allow_empty of this Highlight.  # noqa: E501
        :type allow_empty: bool
        """

        self._allow_empty = allow_empty
    @property
    def emit_zones(self):
        """Gets the emit_zones of this Highlight.  # noqa: E501


        :return: The emit_zones of this Highlight.  # noqa: E501
        :rtype: bool
        """
        return self._emit_zones
    @emit_zones.setter
    def emit_zones(self, emit_zones):
        """Sets the emit_zones of this Highlight.


        :param emit_zones: The emit_zones of this Highlight.  # noqa: E501
        :type emit_zones: bool
        """

        self._emit_zones = emit_zones
    @property
    def force_snippets(self):
        """Gets the force_snippets of this Highlight.  # noqa: E501


        :return: The force_snippets of this Highlight.  # noqa: E501
        :rtype: bool
        """
        return self._force_snippets
    @force_snippets.setter
    def force_snippets(self, force_snippets):
        """Sets the force_snippets of this Highlight.


        :param force_snippets: The force_snippets of this Highlight.  # noqa: E501
        :type force_snippets: bool
        """

        self._force_snippets = force_snippets
    @property
    def around(self):
        """Gets the around of this Highlight.  # noqa: E501


        :return: The around of this Highlight.  # noqa: E501
        :rtype: int
        """
        return self._around
    @around.setter
    def around(self, around):
        """Sets the around of this Highlight.


        :param around: The around of this Highlight.  # noqa: E501
        :type around: int
        """

        self._around = around
    @property
    def start_snippet_id(self):
        """Gets the start_snippet_id of this Highlight.  # noqa: E501


        :return: The start_snippet_id of this Highlight.  # noqa: E501
        :rtype: int
        """
        return self._start_snippet_id
    @start_snippet_id.setter
    def start_snippet_id(self, start_snippet_id):
        """Sets the start_snippet_id of this Highlight.


        :param start_snippet_id: The start_snippet_id of this Highlight.  # noqa: E501
        :type start_snippet_id: int
        """

        self._start_snippet_id = start_snippet_id
    @property
    def html_strip_mode(self):
        """Gets the html_strip_mode of this Highlight.  # noqa: E501


        :return: The html_strip_mode of this Highlight.  # noqa: E501
        :rtype: str
        """
        return self._html_strip_mode
    @html_strip_mode.setter
    def html_strip_mode(self, html_strip_mode):
        """Sets the html_strip_mode of this Highlight.


        :param html_strip_mode: The html_strip_mode of this Highlight.  # noqa: E501
        :type html_strip_mode: str
        """
        allowed_values = ["none", "strip", "index", "retain"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and html_strip_mode not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `html_strip_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(html_strip_mode, allowed_values)
            )

        self._html_strip_mode = html_strip_mode
    @property
    def snippet_boundary(self):
        """Gets the snippet_boundary of this Highlight.  # noqa: E501


        :return: The snippet_boundary of this Highlight.  # noqa: E501
        :rtype: str
        """
        return self._snippet_boundary
    @snippet_boundary.setter
    def snippet_boundary(self, snippet_boundary):
        """Sets the snippet_boundary of this Highlight.


        :param snippet_boundary: The snippet_boundary of this Highlight.  # noqa: E501
        :type snippet_boundary: str
        """
        allowed_values = ["sentence", "paragraph", "zone"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and snippet_boundary not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `snippet_boundary` ({0}), must be one of {1}"  # noqa: E501
                .format(snippet_boundary, allowed_values)
            )

        self._snippet_boundary = snippet_boundary

    def to_dict(self):
        """Returns the model properties as a dict"""

        result = {}		
        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        if result['fields'] is not None:
            result['fields'] = {k:v for i in result['fields'] for k,v in i.items() if v is not None}


        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Highlight):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Highlight):
            return True

        return self.to_dict() != other.to_dict()