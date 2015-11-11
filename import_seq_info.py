# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from imgdb.wsgi import *
from utils.models import SequenceInfo
from pyeasy import OpenExcel



def main():
    f = OpenExcel('seqinfo.xls')
    for index in xrange(1, f.getRows()+1):
        si = SequenceInfo(id=index)
        #si.document_file = f.read('A%s'%index)
        si.strain = f.read('B%s'%index)
        si.sequence_type = f.read('C%s'%index)
        si.public_type = f.read('D%s'%index)
        si.strain_owner = f.read('E%s'%index)
        si.industrial_application = f.read('F%s'%index)
        si.save()


'''
['strain', 'sequence_type', 'public_type', 'strain_owner',
    'industrial_application', 'document_file']
'''
if __name__ == '__main__':
    main()
