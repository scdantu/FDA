#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mplot
import FDA.Utilities as fda_gen_util
import os,sys

import matplotlib.font_manager as fm

#mplot.rcParams['font.sans-serif']=['Arial']
FOL=os.getcwd();
BPFOL="%s/png/barplots"%(FOL)
PNGFOL="%s/png"%(FOL)
BAR_PLOT_DATA=[];
#BLACK,RED,DARK GREEN,BLUE,ORANGE,BROWN,CYAN,LIME,FUCHSIA,PURPLE
PLOT_COLOR = ('#000000','#FF0000','#008000','#0000FF', '#FFA500','#A52A2A','#00FFFF','#00FF00','#FF00FF','#800080')
PLOT_LINE_STYLE=['-','-','-','-','-','-','-','-','-','-','-','-']
PLOT_MARKER_STYLE=[' ',' ',' ','o','D','H','s','v','x']
PLOT_MARKER_SIZE=[1,1,3,3,3,3,3,3,3,3,3,3,3,3]
PLOT_MARKER_SHAPE=['o','s','^','8','p','*','h','H','D','d','-','-']; #http://matplotlib.org/api/markers_api.html#module-matplotlib.markers

def plot_fun(a,b,FOL,label):
    global PNGFOL
    fda_gen_util.check_folder(PNGFOL)
    xmin=0; xmax=200;   xgap=5;
    fig=plt.figure();
    fig.set_size_inches(12,4)
    #N=len(a);
    #ind=np.arange(N);
    width=0.5
    plt.plot(a,b,color="#02FF00")
    #plt.show()
    ylab=r'$\Delta\hspace{0.5}\mathrm{Avg.}\hspace{0.5}\mathrm{Force}\hspace{0.5}\mathrm{(pN)}$'
    plt.xlabel("Residue id");
    plt.ylabel(ylab)
    plt.xticks(np.arange(xmin,xmax+xgap,xgap))
    plt.xlim(xmin,xmax)
    sfname="%s/%s.png"%(FOL,label)
    plt.savefig(sfname,dpi=300)
    print ("%s saved"%(sfname))

#def bar_plots(BAR_PLOT_DATA,resid):
def bar_plots(BAR_PLOT_DATA):
    #Fol="/home/mugdha/Projects/TFAM/analysis/fda/png/barplots";
    global PNGFOL,BPFOL
    bar_color="#0000FF"
    fda_gen_util.check_folder(PNGFOL); #This is a redundant check since BPFOL is nested in PNGFOL
    fda_gen_util.check_folder(BPFOL);

    fig=plt.figure();
    #fig.set_size_inches(12,4)
    bar_width=0.50;  opacity=0.9;
    labels=[];  lab_pos=[];
    prop = fm.FontProperties(fname='/usr/share/matplotlib/mpl-data/fonts/ttf/cmb10.ttf')
    #prop=fm.FontProperties(fname='/home/mugdha/Downloads/arial.ttf')
    N=len(BAR_PLOT_DATA);

    ymin=-4000;   ymax=3000;   ygap=1000;   title_fs=12;    y_fs=10;

    ax1=plt.subplot(321);
    ax_c_data=BAR_PLOT_DATA[0];
    ax_label=ax_c_data[0];    ax_plot_data=ax_c_data[1];
    N=len(ax_plot_data);
    pos_array=[];   labels=[];
    index=np.arange(0,len(ax_plot_data));

    for i in range(N):
        i_data=ax_plot_data[i];
        pos=index[i]+(bar_width*i);
        labels.append(i_data[0]);       pos_array.append(pos);
        plt.bar(pos,i_data[1],bar_width,alpha=opacity,color=bar_color,label=i_data[0],yerr=i_data[2],ecolor="#000000",align='center')
    plt.xticks(pos_array, labels,fontproperties=prop,fontsize=0)
    plt.yticks(np.arange(ymin,ymax+ygap,ygap),fontproperties=prop,fontsize=y_fs)
    plt.title(ax_label,fontproperties=prop,fontsize=title_fs);

    ax2=plt.subplot(322);
    ax_c_data=BAR_PLOT_DATA[1];
    ax_label=ax_c_data[0];    ax_plot_data=ax_c_data[1];
    N=len(ax_plot_data);
    pos_array=[];   labels=[];
    index=np.arange(0,len(ax_plot_data));

    for i in range(N):
        i_data=ax_plot_data[i];
        pos=index[i]+(bar_width*i);

        labels.append(i_data[0]);       pos_array.append(pos);
        plt.bar(pos,i_data[1],bar_width,alpha=opacity,color=bar_color,label=i_data[0],yerr=i_data[2],ecolor="#000000",align='center')
    plt.xticks(pos_array, labels,fontproperties=prop,fontsize=0)
    plt.yticks(np.arange(ymin,ymax+ygap,ygap),fontsize=0)
    plt.title(ax_label,fontproperties=prop,fontsize=title_fs);

    ax3=plt.subplot(323);
    ax_c_data=BAR_PLOT_DATA[2];
    ax_label=ax_c_data[0];    ax_plot_data=ax_c_data[1];
    N=len(ax_plot_data);
    pos_array=[];   labels=[];
    index=np.arange(0,len(ax_plot_data));

    for i in range(N):
        i_data=ax_plot_data[i];
        pos=index[i]+(bar_width*i);

        labels.append(i_data[0]);       pos_array.append(pos);
        plt.bar(pos,i_data[1],bar_width,alpha=opacity,color=bar_color,label=i_data[0],yerr=i_data[2],ecolor="#000000",align='center')
    plt.xticks(pos_array, labels,fontproperties=prop,fontsize=0)
    plt.yticks(np.arange(ymin,ymax+ygap,ygap),fontproperties=prop,fontsize=y_fs)
    plt.title(ax_label,fontproperties=prop,fontsize=title_fs);

    ax4=plt.subplot(324);
    ax_c_data=BAR_PLOT_DATA[3];
    ax_label=ax_c_data[0];    ax_plot_data=ax_c_data[1];
    N=len(ax_plot_data);
    pos_array=[];   labels=[];
    index=np.arange(0,len(ax_plot_data));

    for i in range(N):
        i_data=ax_plot_data[i];
        pos=index[i]+(bar_width*i);
        labels.append(i_data[0]);       pos_array.append(pos);
        plt.bar(pos,i_data[1],bar_width,alpha=opacity,color=bar_color,label=i_data[0],yerr=i_data[2],ecolor="#000000",align='center')
    plt.xticks(pos_array, labels,fontproperties=prop,fontsize=0)
    plt.yticks(np.arange(ymin,ymax+ygap,ygap),fontsize=0)
    plt.title(ax_label,fontproperties=prop,fontsize=title_fs);

    ax5=plt.subplot(325);
    ax_c_data=BAR_PLOT_DATA[4];
    ax_label=ax_c_data[0];    ax_plot_data=ax_c_data[1];
    N=len(ax_plot_data);
    pos_array=[];   labels=[];
    index=np.arange(0,len(ax_plot_data));

    for i in range(N):
        i_data=ax_plot_data[i];
        pos=index[i]+(bar_width*i);
        labels.append(i_data[0]);       pos_array.append(pos);
        plt.bar(pos,i_data[1],bar_width,alpha=opacity,color=bar_color,label=i_data[0],yerr=i_data[2],ecolor="#000000",align='center')
    plt.title(ax_label,fontproperties=prop,fontsize=title_fs);

    plt.xticks(pos_array, labels,fontproperties=prop,fontsize=10)
    plt.yticks(np.arange(ymin,ymax+ygap,ygap),fontproperties=prop,fontsize=y_fs)
    plt.ylim(ymin,ymax)

    ax6=plt.subplot(326);
    ax_c_data=BAR_PLOT_DATA[5];
    ax_label=ax_c_data[0];    ax_plot_data=ax_c_data[1];
    N=len(ax_plot_data);
    pos_array=[];   labels=[];
    index=np.arange(0,len(ax_plot_data));

    for i in range(N):
        i_data=ax_plot_data[i];
        pos=index[i]+(bar_width*i);
        labels.append(i_data[0]);       pos_array.append(pos);
        plt.bar(pos,i_data[1],bar_width,alpha=opacity,color=bar_color,label=i_data[0],yerr=i_data[2],ecolor="#000000",align='center')
    plt.xticks(pos_array, labels,fontproperties=prop,fontsize=10)
    plt.yticks(np.arange(ymin,ymax+ygap,ygap),fontsize=0)
    #plt.setp(ax6.get_yticklabels(),visible=False);
    plt.title(ax_label,fontproperties=prop,fontsize=title_fs);

    #plt.legend(prop=mplot.font_manager.FontProperties(size=10),frameon=False,ncol=2,mode="expand")
    plt.tight_layout()
    sfname="%s/MutationL6-barPlot.png"%(BPFOL)
    plt.savefig(sfname,dpi=300)
    #plt.show()
    ''''
    for i in range(N):
        i_label=BAR_PLOT_DATA[i][0];
        lab_pos=[]; pos_array=[];   data_array=[];  err_array=[];   labels=[];
        DATA=BAR_PLOT_DATA[i][1]
        index=np.arange(0,len(DATA));

        for j in range(len(DATA)):
            j_data=DATA[j]

            pos=index[j]+(bar_width*j);     l_pos=pos+(bar_width/2);

            labels.append(j_data[0]);       pos_array.append(pos);
            data_array.append(j_data[1]);   err_array.append(j_data[2]);

            lab_pos.append(l_pos)
            #axs[i].bar(pos,j_data[1],bar_width,alpha=opacity,color='b',label=j_data[0],yerr=j_data[2],ecolor="#000000",align='center')
        #ymin=min(data_array);   ymax=max(data_array);   ygap=1000;
        axs[i].bar(pos_array,data_array,bar_width,alpha=opacity,color='b',label=labels,yerr=err_array,ecolor="#000000")
        print lab_pos
        print labels
        axs[i].set_xticks(lab_pos, labels)
        axs[i].set_yticks(np.arange(ymin,ymax+ygap,ygap))
        #axs[i].set_xlabel('Mutations')
        #axs[i].set_ylabel('Avg. Force (pN)')

    #title="Avg. forces on %d"%(resid)


    '''

    #title="Avg. forces on %d"%(resid)


    #plt.title(title)
    #plt.legend()
    #plt.legend(bbox_to_anchor=(0., 1.02, 1., .102),prop=mplot.font_manager.FontProperties(size=10),frameon=False,ncol=2,mode="expand")

    #print "saved %s"%(sfname)
''''
BAR_PLOT_DATA.append(["A",20,5]);
BAR_PLOT_DATA.append(["B",10,5]);
BAR_PLOT_DATA.append(["C",25,7.5]);
BAR_PLOT_DATA.append(["D",10,15]);
bar_plots(BAR_PLOT_DATA,98)
'''''

def plot_1_bar(plotdata):
    X=plotdata[0];
    Y=plotdata[1];
    plt.bar(1,Y,width=0.5)
    plt.show()
