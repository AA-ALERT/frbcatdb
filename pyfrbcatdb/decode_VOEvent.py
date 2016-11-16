'''
description:    Decode VOEvent db entry to xml
license:        APACHE 2.0
author:         Ronald van Haren, NLeSC (r.vanharen@esciencecenter.nl)
'''
from pyfrbcatdb import dbase
from pyfrbcatdb.FRBCat import *


def decode_FRBCat_entry(frb_ids):
    '''
    Decode FRBCat entry
    '''
    # load mapping VOEvent -> FRBCat
    # connect to database
    # TODO: add connection details
    connection, cursor = dbase.connectToDB()

    for frb_id in frb_ids:
        FRBCat = FRBCat_decode(connection, cursor, frb_id)
        FRBCat.decode_VOEvent_from_FRBCat()