#!/usr/bin/python
import FDA.Utilities as utils
class Gro_Reader(object):

    def __init__(self,gro_file):
        self.ATOM_ID=[];    self.ATOM_NAME=[];
        self.RES_NAME={};           self.X_Y_Z=[];
        
        self.RESID_ATOMS={};        
        
        self._gro_file=gro_file;
        
        self._read_gro();
        self.NUM_RESIDUES=len(self.RES_NAME)
        
        print("GRO file read \t\t %s"%(gro_file))
        print("No. of resid \t\t %12d"%(self.NUM_RESIDUES))
        print("No. of atoms \t\t %12d"%(len(self.ATOM_ID)))
        
    def _read_gro(self):
        
        fopen=open(self._gro_file,"r");
        count=0;    
        # should not read coord line from gro
        #implement store CA lines
        line="";
        for line in fopen:
            if(count>1):
                jk= line.split()
                n_col=len(jk);
                if(n_col==5)or(n_col==6):
                    self._proc_line_punc_stress(line);
                    #GRO_RESID.append(temp_resid)
                    #GRO_ATOMID.append(temp_atomid);
                    #gro_data[ATOM_ID]=RESID;
            count= count+1    
        
    def _proc_line(self,line):
        resid=int(line[0:5].strip());
        x=line[20:28].strip();  y=line[28:36].strip();        z=line[36:44].strip();
        coord=[x,y,z]
        
        atom_name=line[10:15].strip();      atom_id=int(line[15:20].strip());
        res_name=line[5:10].strip();        res_name=utils.aa_map(res_name);    
        
        
        self.ATOM_NAME.append(atom_name);        self.ATOM_ID.append(atom_id);          self.X_Y_Z.append(coord)
        self.RES_NAME[resid]=res_name;
        self._mapping(resid,atom_id)
    
    
    def _mapping(self,resid,atom_id):
        doom=False;
        if(resid in self.RESID_ATOMS)==False:
            t=[atom_id]
            self.RESID_ATOMS[resid]=t
            doom=True;
        if((resid in self.RESID_ATOMS)==True)and(doom==False):
            t=self.RESID_ATOMS[resid];
            self.RESID_ATOMS[resid]=0;
            new_t=[];
            for i in range(len(t)):
                new_t.append(t[i])
            new_t.append(atom_id)
            self.RESID_ATOMS[resid]=new_t

    def _proc_line_punc_stress(self,line):
        split_line=line.split()
        N=len(split_line);
        if(N==5)or(N==6):
            self._proc_line(line)
        ##if gro is dumped from trr, might throw errors as they contain V and F
        if(N<5)or(N>6):
            print ("Gro file line is messed up. Check input file")
            print ("Error at the following line")
            print (line)
            print ("Exiting programm")
            exit(1)
