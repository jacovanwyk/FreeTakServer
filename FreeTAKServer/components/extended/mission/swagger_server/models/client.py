# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Client(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, client_id: str=None, secret: str=None, redirect_uri: str=None, resource_ids: str=None, scope: str=None, authorized_grant_types: str=None, authorities: str=None, autoapprove: str=None, refresh_token_validity: int=None):  # noqa: E501
        """Client - a model defined in Swagger

        :param client_id: The client_id of this Client.  # noqa: E501
        :type client_id: str
        :param secret: The secret of this Client.  # noqa: E501
        :type secret: str
        :param redirect_uri: The redirect_uri of this Client.  # noqa: E501
        :type redirect_uri: str
        :param resource_ids: The resource_ids of this Client.  # noqa: E501
        :type resource_ids: str
        :param scope: The scope of this Client.  # noqa: E501
        :type scope: str
        :param authorized_grant_types: The authorized_grant_types of this Client.  # noqa: E501
        :type authorized_grant_types: str
        :param authorities: The authorities of this Client.  # noqa: E501
        :type authorities: str
        :param autoapprove: The autoapprove of this Client.  # noqa: E501
        :type autoapprove: str
        :param refresh_token_validity: The refresh_token_validity of this Client.  # noqa: E501
        :type refresh_token_validity: int
        """
        self.swagger_types = {
            'client_id': str,
            'secret': str,
            'redirect_uri': str,
            'resource_ids': str,
            'scope': str,
            'authorized_grant_types': str,
            'authorities': str,
            'autoapprove': str,
            'refresh_token_validity': int
        }

        self.attribute_map = {
            'client_id': 'clientId',
            'secret': 'secret',
            'redirect_uri': 'redirectUri',
            'resource_ids': 'resourceIds',
            'scope': 'scope',
            'authorized_grant_types': 'authorizedGrantTypes',
            'authorities': 'authorities',
            'autoapprove': 'autoapprove',
            'refresh_token_validity': 'refreshTokenValidity'
        }
        self._client_id = client_id
        self._secret = secret
        self._redirect_uri = redirect_uri
        self._resource_ids = resource_ids
        self._scope = scope
        self._authorized_grant_types = authorized_grant_types
        self._authorities = authorities
        self._autoapprove = autoapprove
        self._refresh_token_validity = refresh_token_validity

    @classmethod
    def from_dict(cls, dikt) -> 'Client':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Client of this Client.  # noqa: E501
        :rtype: Client
        """
        return util.deserialize_model(dikt, cls)

    @property
    def client_id(self) -> str:
        """Gets the client_id of this Client.


        :return: The client_id of this Client.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id: str):
        """Sets the client_id of this Client.


        :param client_id: The client_id of this Client.
        :type client_id: str
        """

        self._client_id = client_id

    @property
    def secret(self) -> str:
        """Gets the secret of this Client.


        :return: The secret of this Client.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret: str):
        """Sets the secret of this Client.


        :param secret: The secret of this Client.
        :type secret: str
        """

        self._secret = secret

    @property
    def redirect_uri(self) -> str:
        """Gets the redirect_uri of this Client.


        :return: The redirect_uri of this Client.
        :rtype: str
        """
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, redirect_uri: str):
        """Sets the redirect_uri of this Client.


        :param redirect_uri: The redirect_uri of this Client.
        :type redirect_uri: str
        """

        self._redirect_uri = redirect_uri

    @property
    def resource_ids(self) -> str:
        """Gets the resource_ids of this Client.


        :return: The resource_ids of this Client.
        :rtype: str
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids: str):
        """Sets the resource_ids of this Client.


        :param resource_ids: The resource_ids of this Client.
        :type resource_ids: str
        """

        self._resource_ids = resource_ids

    @property
    def scope(self) -> str:
        """Gets the scope of this Client.


        :return: The scope of this Client.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope: str):
        """Sets the scope of this Client.


        :param scope: The scope of this Client.
        :type scope: str
        """

        self._scope = scope

    @property
    def authorized_grant_types(self) -> str:
        """Gets the authorized_grant_types of this Client.


        :return: The authorized_grant_types of this Client.
        :rtype: str
        """
        return self._authorized_grant_types

    @authorized_grant_types.setter
    def authorized_grant_types(self, authorized_grant_types: str):
        """Sets the authorized_grant_types of this Client.


        :param authorized_grant_types: The authorized_grant_types of this Client.
        :type authorized_grant_types: str
        """

        self._authorized_grant_types = authorized_grant_types

    @property
    def authorities(self) -> str:
        """Gets the authorities of this Client.


        :return: The authorities of this Client.
        :rtype: str
        """
        return self._authorities

    @authorities.setter
    def authorities(self, authorities: str):
        """Sets the authorities of this Client.


        :param authorities: The authorities of this Client.
        :type authorities: str
        """

        self._authorities = authorities

    @property
    def autoapprove(self) -> str:
        """Gets the autoapprove of this Client.


        :return: The autoapprove of this Client.
        :rtype: str
        """
        return self._autoapprove

    @autoapprove.setter
    def autoapprove(self, autoapprove: str):
        """Sets the autoapprove of this Client.


        :param autoapprove: The autoapprove of this Client.
        :type autoapprove: str
        """

        self._autoapprove = autoapprove

    @property
    def refresh_token_validity(self) -> int:
        """Gets the refresh_token_validity of this Client.


        :return: The refresh_token_validity of this Client.
        :rtype: int
        """
        return self._refresh_token_validity

    @refresh_token_validity.setter
    def refresh_token_validity(self, refresh_token_validity: int):
        """Sets the refresh_token_validity of this Client.


        :param refresh_token_validity: The refresh_token_validity of this Client.
        :type refresh_token_validity: int
        """

        self._refresh_token_validity = refresh_token_validity
