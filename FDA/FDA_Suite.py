'''
Created on 28-Mar-2018

@author: dsarath
'''
import FDA.Utilities as fda_gen_util
import FDA.Punctual_Stress as calc_punc_stress

class FDA_Suite(object):
    '''
    classdocs
    '''
    def __init__(self, metafile,folder,end_time,with_sign=True,dump_files=False,debug=False):
        '''
        Constructor
        '''
        self._with_sign=with_sign;      self._metafile=metafile;    self._end_time=end_time;
        self._dump_files=dump_files;    self._debug=debug;          self._folder=folder;
        
        self.META_PER_RESID_STATS={};
    
        self._process_meta_file()
    
    def _process_meta_file(self):

        fda_gen_util.check_file(self._metafile);
        meta_open=open(self._metafile,'r');
        
        for i in meta_open:
            grofile=self._folder+"/"+i.split()[0]; #indi pfa
            pfa_file=self._folder+"/"+i.split()[1]; #indi gro
            
            f_label=i.split()[2]; #indi file label
            fda_gen_util.check_file(grofile);
            fda_gen_util.check_file(pfa_file); 
            punc_stress_object=calc_punc_stress.Punctual_Stress(grofile,pfa_file,f_label,self._folder)

