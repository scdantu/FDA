'''
Created on 01-Mar-2018

@author: mugdhaD, sarathD
'''
import FDA.FDA_Suite as fda_suite
import FDA.Punctual_Stress as punc_stress
import timeit
def main():
    
    '''
    Dependencies:
        *python3,matplotlib,numpy
    '''
    start_t=timeit.default_timer();
    folder="/home/dsarath/Projects/tfam/pfa_gro";
    
    pfa_file=folder+"/"+"NSS.pfa";   gro_file=folder+"/"+"NSS.gro"; 
    
    metafile=folder+"/"+"meta.dat";
    
    with_sign=True; dump_files=True;    debug=True; end_time=500;   label="NSS"
     
    #pfa_object=punc_stress.process_manager(gro_file,pfa_file,with_sign,dump_files,end_time,debug,label,folder)
    #pfa_object=punc_stress.process_manager(gro_file,pfa_file,with_sign,dump_files,end_time,debug,label,folder)
    
    pfa_object=fda_suite.FDA_Suite(metafile,folder,end_time,with_sign,dump_files,debug);
    
    '''
    metafile=folder+"/"+"hsp.dat";
    pfa_object=fda_suite.FDA_Suite(metafile,folder,end_time,with_sign,dump_files,debug);
    #print (pfa_object.META_PER_RESID_STATS)
    
    DEBUG_OUT=calc_punc_stress.DUMP_DEBUG_OUTPUT;
    #DEBUG_OUT+="START TIME %s\n"(str(start_t));
    #DEBUG_OUT+="END   TIME %s\n"(str(end_t));
    DEBUG_OUT+="TOTAL TIME %12.2d (s)\n"%((end_t-start_t));
    if(debug==True):
        fname="%s/Log_PS_FDA.log"%(os.getcwd());
        fda_gen_util.write_file(fname,DEBUG_OUT)

     options=fda_po.parse_options();
    with_sign=bool(options.wsign)
    DUMP_FILES=bool(options.ddump)
    DEBUG=bool(options.debug)
    end_time=int(options.end_time)
    metafile1=options.mmeta1 #array of files for input
        #store ending time of the prog. call
    '''
    end_t=timeit.default_timer();
    print (end_t-start_t, "\t (s)");

    #tim.protein()
    
if __name__ == '__main__':
    main()
    pass
