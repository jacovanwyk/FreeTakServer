# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.coordinate import Coordinate  # noqa: F401,E501
from swagger_server import util


class Coordinate(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, x: float=None, y: float=None, z: float=None, m: float=None, coordinate: Coordinate=None):  # noqa: E501
        """Coordinate - a model defined in Swagger

        :param x: The x of this Coordinate.  # noqa: E501
        :type x: float
        :param y: The y of this Coordinate.  # noqa: E501
        :type y: float
        :param z: The z of this Coordinate.  # noqa: E501
        :type z: float
        :param m: The m of this Coordinate.  # noqa: E501
        :type m: float
        :param coordinate: The coordinate of this Coordinate.  # noqa: E501
        :type coordinate: Coordinate
        """
        self.swagger_types = {
            'x': float,
            'y': float,
            'z': float,
            'm': float,
            'coordinate': Coordinate
        }

        self.attribute_map = {
            'x': 'x',
            'y': 'y',
            'z': 'z',
            'm': 'm',
            'coordinate': 'coordinate'
        }
        self._x = x
        self._y = y
        self._z = z
        self._m = m
        self._coordinate = coordinate

    @classmethod
    def from_dict(cls, dikt) -> 'Coordinate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Coordinate of this Coordinate.  # noqa: E501
        :rtype: Coordinate
        """
        return util.deserialize_model(dikt, cls)

    @property
    def x(self) -> float:
        """Gets the x of this Coordinate.


        :return: The x of this Coordinate.
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x: float):
        """Sets the x of this Coordinate.


        :param x: The x of this Coordinate.
        :type x: float
        """

        self._x = x

    @property
    def y(self) -> float:
        """Gets the y of this Coordinate.


        :return: The y of this Coordinate.
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y: float):
        """Sets the y of this Coordinate.


        :param y: The y of this Coordinate.
        :type y: float
        """

        self._y = y

    @property
    def z(self) -> float:
        """Gets the z of this Coordinate.


        :return: The z of this Coordinate.
        :rtype: float
        """
        return self._z

    @z.setter
    def z(self, z: float):
        """Sets the z of this Coordinate.


        :param z: The z of this Coordinate.
        :type z: float
        """

        self._z = z

    @property
    def m(self) -> float:
        """Gets the m of this Coordinate.


        :return: The m of this Coordinate.
        :rtype: float
        """
        return self._m

    @m.setter
    def m(self, m: float):
        """Sets the m of this Coordinate.


        :param m: The m of this Coordinate.
        :type m: float
        """

        self._m = m

    @property
    def coordinate(self) -> Coordinate:
        """Gets the coordinate of this Coordinate.


        :return: The coordinate of this Coordinate.
        :rtype: Coordinate
        """
        return self._coordinate

    @coordinate.setter
    def coordinate(self, coordinate: Coordinate):
        """Sets the coordinate of this Coordinate.


        :param coordinate: The coordinate of this Coordinate.
        :type coordinate: Coordinate
        """

        self._coordinate = coordinate
