#!usr/bin/python
import numpy as np
import FDA.Utilities as fda_gen_util
import FDA.Plot_Utilities as plot_util
from scipy import stats
import os,sys,timeit
import math

DUMP_FILES=True;
FASTA="SSVLASCPKKPVSSYLRFSKEQLPIFKAQNPDAKTTELIRRIAQRWRELPDSKKKIYQDAYRAEWQVYKEEISRFKEQLTPSQIMSLEKEIMDKHLKRKAMTKKKELTLLGKPKRPRSAYNVYVAERFQEAKGDSPQEKLKTVKENWKNLSDSEKELYIQHAKEDETRYHNEMKSWEEQMIEVGRKDLLRRTIKK"

def avg_force_per_frame(force_list):

    FORCE_LIST=[];
    N_FRAMES=len(force_list)

    for i in range(N_FRAMES):
        frame_num=force_list[i][0];
        i_resid_force_list=force_list[i][1];
        #resid,forces=extract_resid_forces(i_resid_force_list);
        resid,forces=fda_gen_util.extract_2d_list(i_resid_force_list);
        ave_force=np.average(forces)
        d=[frame_num,ave_force]
        print (ave_force[0])
        exit()
        FORCE_LIST.append(d)
    return FORCE_LIST

def mode_per_resid(force_list,label):
    global DUMP_FILES
    res_force_list=[];
    FORCE_LIST=[];
    N_FRAMES=len(force_list)

    for x in range(1):
        frame_num=force_list[x][0];
        i_resid_force_list=force_list[x][1];
        #resid,forces=extract_resid_forces(i_resid_force_list);
        resid,forces=fda_gen_util.extract_2d_list(i_resid_force_list);

    N_resid=len(resid); count=0;
    FOL="/home/mugdha/Projects/TFAM/analysis/fda/dat";
    for i in range(N_resid):
        cur_resid=resid[i];
        res_force=[]; time_data=[];
        for j in range(N_FRAMES):
            i_data=force_list[j][1][i];

            #print force_list
            i_resid=int(i_data[0]);  i_force=float(i_data[1]);
            if(i_resid==cur_resid):
                res_force.append(i_force)
                d=[j,i_force]
                time_data.append(d)
        #contains time series data per residue can be dumped
        #write a dump function for this
        #print time_data
        '''''
        if(DUMP_FILES==True):
            osd=fda_gen_util.prep_2d_list_for_writing(time_data)
            fname="%s/%s-TvF-%d-TFAM.dat"%(FOL,label,cur_resid)
            fda_gen_util.write_file(fname,osd)
            new_lab="%s-%s-TimeVsForce"%(label,cur_resid)
            a,b=fda_gen_util.extract_2d_list(time_data)
            plot_util.plot_fun(a,b,FOL,new_lab)
            '''''
        #modforce=stats.mode(res_force)
        #d=[cur_resid,modforce[0][0]]
        modforce=np.average(res_force)
        d=[cur_resid,modforce]

        FORCE_LIST.append(d)
    return FORCE_LIST

def calc_diff_mode_forces(res_mode_forces_1,res_mode_forces_2,label):
    FOL="/home/mugdha/Projects/TFAM/analysis/fda/png";
    print ("abra ka dabra")
    diff_force_list=[];
    file_force_list=[];
    N_1=len(res_mode_forces_1)
    N_2=len(res_mode_forces_2)
    if(N_1!=N_2):
        print ("Residue numbers of PFA1 and PFA2 files are not the ssame. Please check.")
        exit()
    for i in range(N_1):
        force_diff=res_mode_forces_1[i][1]-res_mode_forces_2[i][1]
        diff_force_list.append([res_mode_forces_1[i][0],force_diff])
        d=[i+1,res_mode_forces_1[i][1],res_mode_forces_2[i][1],force_diff]
        file_force_list.append(d)
    osd=fda_gen_util.prep_4d_list_for_writing(file_force_list)
    fname="%s/%s-diff_force_list.dat"%(FOL,label)
    fda_gen_util.write_file(fname,osd)
    return diff_force_list

def average_force_per_forcefile(a,b,c):
    N=len(a)
    ave_force_list=[];
    std_force_list=[];
    for i in range(N):
        all_traj_force=[a[i][1],b[i][1],c[i][1]]
        #total_ave_force=all_traj_force/3
        #print all_traj_force
        total_ave_force=np.average(all_traj_force)
        error=np.std(all_traj_force)
        #print error
        #print total_ave_force#, all_traj_force
        d=[a[i][0],error]
        s=[a[i][0],total_ave_force]
        std_force_list.append(d)
        ave_force_list.append(s)
    osd=fda_gen_util.prep_2d_list_for_writing(ave_force_list)
    #print ave_force_list
    #fname="%s/protein-dna-wt_forces.dat"%(os.getcwd());
    #fda_gen_util.write_file(fname,osd)
    return std_force_list, ave_force_list


def net_force_calc(ave_force_ref,ave_force_pert,std_ref,std_pert,label,diff_res):
    global FASTA
    N=len(ave_force_ref)
    net_force_list=[];

    fac=1.0/math.sqrt(N);
    wout_data="%4s %12s %12s %12s %12s\n"%("ResI","Net Force","DELTA F","E Ref","E Pert");
    for i in range(N):
        error_ref=std_ref[i]*fac
        error_pert=1 #std_pert[i]*fac;
        #e_fac=1.0/error_ref
        e_fac=1
        i_resid=diff_res[i];
        #C=ave_force_pert[i];
        D=ave_force_ref[i];
        i_diff=1#(ave_force_pert[i]-ave_force_ref[i]);

        #print i_resid,ave_force_pert[i], ave_force_ref[i]
        #wout_data+="%12d %12.2f %12.2f\n"%(diff_res[i],diff_data[i],diff_err[i])
        i_net_force=D*e_fac
        wout_data+="%4d %12.2f %12.2f %12.2f %12.2f\n"%(i_resid,i_net_force,i_diff,error_ref,error_pert);
        #wout_data+="%4d %12.2f %12.2f %12.2f %12.2f %12.2f\n"%(i_resid,ave_force_ref,ave_force_pert,i_diff,error_ref,error_pert);
        if (0>=i_net_force) or (i_net_force>=0):
            d=[diff_res[i],D]
        else:
            #d=[FASTA[i],diff_res[i],0]
            d=[diff_res[i],0]
        #d=[diff_res[i],i_net_force]


        net_force_list.append(d)


    osd=fda_gen_util.prep_2d_list_for_writing(net_force_list)
    fname="%s/Net_force-%s.dat"%(os.getcwd(),label);
    fda_gen_util.write_file(fname,osd)
    return net_force_list
