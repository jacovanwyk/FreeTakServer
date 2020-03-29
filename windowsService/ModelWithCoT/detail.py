#######################################################
#
# detail.py
# Python implementation of the Class detail
# Generated by Enterprise Architect
# Created on: 11-Feb-2020 11:08:07 AM
# Original author: Corvo
#
#######################################################
from Model.status import status as status1
from Model.color import color as color1
from Model.link import link as link1
from Model.contact import contact as contact1
from Model.usericon import usericon as usericon1
from Model.remarks import remarks as remarks1
from Model.takv import takv as takv1
from Model.track import track as track1
from Model.Precisionlocation import Precisionlocation as Precisionlocation1 
from Model.__chat import __chat as chat1
from Model.__serverdestination import __serverdestination as serverdestination1
from Model.uid import uid as uid1
from Model.__group import __group as info

class detail:
    """An optional element used to hold CoT sub-schema. empty element
    """
    def __init__(self):
        self.Precisionlocation = Precisionlocation1()
        self.__chat = chat1()
        self.__serverdestination = serverdestination1()
        self.track = track1()
        self.status = status1() 
        self.takv = takv1()
        self.remarks = remarks1()
        self.usericon = usericon1()
        self.contact = contact1()
        self.link = link1()
        self.color = color1()
        self.uid = uid1()
        self.__group = info()