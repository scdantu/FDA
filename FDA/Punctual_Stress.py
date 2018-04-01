#!/usr/bin/python
import FDA.Gro_Reader as gro_reader
import FDA.PFA as pfa
import FDA.Utilities as fda_utils

class Punctual_Stress(object):
    '''
    Attributes:
        PER_ATOM_FORCE [atomid]=force
        PER_RESIDUE_FORCE [resid]=force
        
    '''
    
    def __init__(self,grofile,pfafile,label,folder):
        
        self.PER_ATOM_FORCE={}; self.PER_RESIDUE_FORCE={};
        
        self._folder=folder;    self._out_file=self._folder+"/"+"PRF-"+label+".prf"
        
        self._out_forces="";
        
        '''
        create gro object
        create pfa object
        '''
        self.gro_object=gro_reader.Gro_Reader(grofile);
        self.pfa_object=pfa.PFA(pfafile,label)
        
        '''
        making a copy of PER_ATOM_FORCE
        '''
        self.PER_ATOM_FORCE=self.pfa_object.PER_ATOM_FORCE;
        '''
        map forces to each residue
        '''
        self._per_resid_force();
        
        '''
        dump forces to a file
        '''
        fda_utils.write_file(self._out_file, self._out_forces)
        
    def _per_resid_force(self):
        for i in range(self.gro_object.NUM_RESIDUES):
            current_resid=i+1;
            if ((current_resid in self.gro_object.RESID_ATOMS)==True):
                atoms_list=self.gro_object.RESID_ATOMS[current_resid];
                sum_force=self._get_forces_list(atoms_list);
                self._out_forces+="%12d %12.5f\n"%(current_resid,sum_force)
                self.PER_RESIDUE_FORCE[current_resid]=sum_force;
        
    def _get_forces_list(self,atoms_list):
        sum_force=0;

        for atom in atoms_list:
            if((atom in self.PER_ATOM_FORCE)==True):
                sum_force+=self.PER_ATOM_FORCE[atom]
        return sum_force;
    
    