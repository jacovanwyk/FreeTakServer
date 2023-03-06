# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.delivery_rate_limiter import DeliveryRateLimiter  # noqa: F401,E501
from swagger_server.models.dos_rate_limiter import DosRateLimiter  # noqa: F401,E501
from swagger_server.models.read_rate_limiter import ReadRateLimiter  # noqa: F401,E501
from swagger_server import util


class Qos(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, delivery_rate_limiter: DeliveryRateLimiter=None, read_rate_limiter: ReadRateLimiter=None, dos_rate_limiter: DosRateLimiter=None):  # noqa: E501
        """Qos - a model defined in Swagger

        :param delivery_rate_limiter: The delivery_rate_limiter of this Qos.  # noqa: E501
        :type delivery_rate_limiter: DeliveryRateLimiter
        :param read_rate_limiter: The read_rate_limiter of this Qos.  # noqa: E501
        :type read_rate_limiter: ReadRateLimiter
        :param dos_rate_limiter: The dos_rate_limiter of this Qos.  # noqa: E501
        :type dos_rate_limiter: DosRateLimiter
        """
        self.swagger_types = {
            'delivery_rate_limiter': DeliveryRateLimiter,
            'read_rate_limiter': ReadRateLimiter,
            'dos_rate_limiter': DosRateLimiter
        }

        self.attribute_map = {
            'delivery_rate_limiter': 'deliveryRateLimiter',
            'read_rate_limiter': 'readRateLimiter',
            'dos_rate_limiter': 'dosRateLimiter'
        }
        self._delivery_rate_limiter = delivery_rate_limiter
        self._read_rate_limiter = read_rate_limiter
        self._dos_rate_limiter = dos_rate_limiter

    @classmethod
    def from_dict(cls, dikt) -> 'Qos':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Qos of this Qos.  # noqa: E501
        :rtype: Qos
        """
        return util.deserialize_model(dikt, cls)

    @property
    def delivery_rate_limiter(self) -> DeliveryRateLimiter:
        """Gets the delivery_rate_limiter of this Qos.


        :return: The delivery_rate_limiter of this Qos.
        :rtype: DeliveryRateLimiter
        """
        return self._delivery_rate_limiter

    @delivery_rate_limiter.setter
    def delivery_rate_limiter(self, delivery_rate_limiter: DeliveryRateLimiter):
        """Sets the delivery_rate_limiter of this Qos.


        :param delivery_rate_limiter: The delivery_rate_limiter of this Qos.
        :type delivery_rate_limiter: DeliveryRateLimiter
        """

        self._delivery_rate_limiter = delivery_rate_limiter

    @property
    def read_rate_limiter(self) -> ReadRateLimiter:
        """Gets the read_rate_limiter of this Qos.


        :return: The read_rate_limiter of this Qos.
        :rtype: ReadRateLimiter
        """
        return self._read_rate_limiter

    @read_rate_limiter.setter
    def read_rate_limiter(self, read_rate_limiter: ReadRateLimiter):
        """Sets the read_rate_limiter of this Qos.


        :param read_rate_limiter: The read_rate_limiter of this Qos.
        :type read_rate_limiter: ReadRateLimiter
        """

        self._read_rate_limiter = read_rate_limiter

    @property
    def dos_rate_limiter(self) -> DosRateLimiter:
        """Gets the dos_rate_limiter of this Qos.


        :return: The dos_rate_limiter of this Qos.
        :rtype: DosRateLimiter
        """
        return self._dos_rate_limiter

    @dos_rate_limiter.setter
    def dos_rate_limiter(self, dos_rate_limiter: DosRateLimiter):
        """Sets the dos_rate_limiter of this Qos.


        :param dos_rate_limiter: The dos_rate_limiter of this Qos.
        :type dos_rate_limiter: DosRateLimiter
        """

        self._dos_rate_limiter = dos_rate_limiter
