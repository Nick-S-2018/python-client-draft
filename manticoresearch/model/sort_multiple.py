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

class SortMultiple(object):
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
        'attrs': '{str: (bool, date, datetime, dict, float, int, list, str, none_type)}',
        'replace': 'bool'
    }

    attribute_map = {
        'attrs': 'attrs',
        'replace': 'replace'
    }

    def __init__(self, attrs=None, replace=None, local_vars_configuration=None):  # noqa: E501
        """SortMultiple - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._attrs = None
        self._replace = None
        self.discriminator = None

        self.attrs = attrs
        self.replace = replace

    @property
    def attrs(self):
        """Gets the attrs of this SortMultiple.  # noqa: E501


        :return: The attrs of this SortMultiple.  # noqa: E501
        :rtype: {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
        """
        return self._attrs
    @attrs.setter
    def attrs(self, attrs):
        """Sets the attrs of this SortMultiple.


        :param attrs: The attrs of this SortMultiple.  # noqa: E501
        :type attrs: {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
        """
        if self.local_vars_configuration.client_side_validation and attrs is None:  # noqa: E501
            raise ValueError("Invalid value for `attrs`, must not be `None`")  # noqa: E501

        self._attrs = attrs
    @property
    def replace(self):
        """Gets the replace of this SortMultiple.  # noqa: E501


        :return: The replace of this SortMultiple.  # noqa: E501
        :rtype: bool
        """
        return self._replace
    @replace.setter
    def replace(self, replace):
        """Sets the replace of this SortMultiple.


        :param replace: The replace of this SortMultiple.  # noqa: E501
        :type replace: bool
        """
        if self.local_vars_configuration.client_side_validation and replace is None:  # noqa: E501
            raise ValueError("Invalid value for `replace`, must not be `None`")  # noqa: E501

        self._replace = replace

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



        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SortMultiple):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SortMultiple):
            return True

        return self.to_dict() != other.to_dict()