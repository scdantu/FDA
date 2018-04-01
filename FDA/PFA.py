'''
Created on 01-Apr-2018

@author: dsarath
'''
class PFA(object):
    '''
    reads pfa file (_read_pfa)
    and then maps forces per each atom using _per_atom_force function
    
    for now use only PER_ATOM_FORCE dictionary
    to access force on atom 
    print (self.PER_ATOM_FORCE[atomid])

    '''
    def __init__(self, pfa_file,label):
        '''
        Constructor
        '''
        self.NUM_OF_FRAMES=[];
        
        self.ATOM_A=[];    self.ATOM_B=[];  self.FORCES=[]; self.FORCE_TYPE=[];
        
        self.PER_ATOM_FORCE={}
        self._pfa_file=pfa_file;    self._label=label;
        self._read_pfa()
        
        print("Read pfa file %s"%(pfa_file));
        print("No. of atoms with forces: %12d"%(len(self.PER_ATOM_FORCE)));
        
    def _read_pfa(self):
        
        pfopen=open(self._pfa_file,'r');
        for pfa_line in pfopen:
            pfal_split=pfa_line.split()
            n_cols=len(pfal_split);
            if(n_cols==2):
                frame_no=int(pfal_split[1]);
                self.NUM_OF_FRAMES.append(frame_no)
                  
            if(n_cols==4):
                atom_a=int(pfal_split[0]);  atom_b=int(pfal_split[1])
                atom_f=float(pfal_split[2]);
                '''
                NOT INTERESTED IN THESE YET
                
                self.ATOM_A.append(atom_a); self.ATOM_B.append(atom_b)
                self.FORCES.append(atom_f)
                self.FORCE_TYPE.append(float(pfal_split[3]))
                '''
                self._per_atom_force(atom_a,atom_f)
            #if(frame_no==FIN_TIME):
            #    break
            if(n_cols>4):
                print (pfal_split)
                exit()
    '''
    checks if an atom is present in the dictionary PER_ATOM_FORCE
    if not store it and F:atom_f on it
    if atom_a is present 
    get the old_force+atom_f and store it for atom_a
    '''
    def _per_atom_force(self,atom_a,atom_f):
        doom=False;
        if(atom_a in self.PER_ATOM_FORCE)==False:
            self.PER_ATOM_FORCE[atom_a]=atom_f
            doom=True;
        if((atom_a in self.PER_ATOM_FORCE)==True)and(doom==False):
            old_force=self.PER_ATOM_FORCE[atom_a];
            self.PER_ATOM_FORCE[atom_a]=0;
            atom_f=old_force+atom_f
            self.PER_ATOM_FORCE[atom_a]=atom_f
            