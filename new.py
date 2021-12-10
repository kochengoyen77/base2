#================================================================START OF SCRIPT================================================================

'''
===============================================TUGAS BESAR MATA KULIAH FLUIDA RESERVOIR KELOMPOK 20=============================================
12219013 AL-FATH SYAHALAM
12219037 DIFANS AFTA MUMIDDA MOHAN
12219054 MUHAMMAD ARYA PRATAMA
12219059 MUHAMMAD AZMI
12219081 RELIGIOUS MAHDA EDEN Haq

====================================================DILARANG MENYALIN SCRIPT MILIK KELOMPOK 20==================================================
'''



#IMPORT MODULE EXTERNAL
from tkinter import *
from math import log10, exp
from numpy import log as ln
from numpy import array
import matplotlib.pyplot as plt
plt.style.use("fast")

#MENDEFINISIKAN VARIABEL
tres = float()
pres = float()
psc = float()
sg = float()
api = float()
psep = float()
tsep = float()
rsb = float()
sgoil = float()
tds = float()
co2 = float()
h2s = float()
n2 = float()
pb = float()
p = float()
bo = float()
rs = float()
bg = float()
bw = float()
rsw = float()
condition = str()
z = float()
oildens = float()
gasdens = float()
brinedens = float()
oilvis = float()
gasvis = float()
brinevis = float()
co = float()
cg = float()
cw = float()


#GUI DECLARATION
root = Tk()
root.title("Oil Properties - Fluids Properties Correlation")
#root.iconbitmap("logo.ico")
root.geometry("1280x720+-10+0")
root.configure(bg="#10133a")

Grid.rowconfigure(root, 5, weight=1)
Grid.columnconfigure(root, 3, weight=1)

#FUNGSI UNTUK MENAMPILKAN TABEL DAN GRAFIK
def Tabel():
    global pres
    
    array_tekanan = [float(pres)]

    for i in range(200):
        if (array_tekanan[i]-(array_tekanan[0]-psc)/26) <=1:
            break
        array_tekanan.append(round(array_tekanan[i]-(array_tekanan[0]-psc)/26, 2))


    array_conditions = []
    for p in array_tekanan:
        array_conditions.append(Condition(p))


    array_rs = []
    for p in array_tekanan:
        array_rs.append(Rs(p, radiors.get()))


    array_co = []
    for p in array_tekanan:
        array_co.append(round(Co(p, Rs(p))*100000, 4))


    array_bo = []
    for p in array_tekanan:
        array_bo.append(Bo(Rs(p),radiobo.get()))

    array_oildens = []
    for p in array_tekanan:
        array_oildens.append(Oildens(Bo(Rs(p),radiobo.get()),Rs(p)))

    array_oilvis = []
    for p in array_tekanan:
        array_oilvis.append(Oilvis(p,Rs(p)))

    array_z = []
    for p in array_tekanan:
        array_z.append(Z(Ppr(p, ppccor)))

    array_gasdens = []
    for p in array_tekanan:
        array_gasdens.append(Gasdens(p,Z(Ppr(p, ppccor))))

    array_bg = []
    for p in array_tekanan:
        array_bg.append(Bg(p,Z(Ppr(p, ppccor))))

    array_gasvis = []
    for p in array_tekanan:
        array_gasvis.append(Gasvis(p,Z(Ppr(p, ppccor)),Gasdens(p,Z(Ppr(p, ppccor)))))

    array_cg = []
    for p in array_tekanan:
        array_cg.append(round(Cg(Z(Ppr(p, ppccor)), Ppr(p, ppccor))*100000, 4))

    array_rsw = []
    for p in array_tekanan:
        array_rsw.append(Rsw(p))

    array_bw = []
    for p in array_tekanan:
        array_bw.append(Bw(p))

    array_brinevis = []
    for p in array_tekanan:
        array_brinevis.append(Brinevis(p))

    array_cw = []
    for p in array_tekanan:
        array_cw.append(round(Cw(p, Rsw(p), radio2.get())*100000, 4))

    array_brinedens = []
    for p in array_tekanan:
        array_brinedens.append(Brinedens(Bw(p)))
    
    semuadata = array([array_tekanan,array_conditions,array_rs,array_co,array_bo,array_oildens,array_oilvis,array_z,array_gasdens,array_bg,array_gasvis,array_cg,array_rsw,array_bw,array_brinevis,array_cw,array_brinedens])
    judul_data = ["P\npsia","Conditions","Rs\nMSCF/STB","Co x 1e-5\n1/MMpsi","Bo\nRB/STB","Oil density\nlbm/cf","Oil viscosity\ncP","Z\nVol/Vol","Gas density\nlbm/scf","Bg\nRB/MSCF","Gas viscosity\ncP","Cg x 1e-5\n1/MMpsi","Rsw\nSCF/STB","Bw\nRB/STB","Brine viscosity\ncP","Cw x 1e-5\n1/MMpsi","Brine density\nlbm/cf"]


    tabel = Toplevel()
    tabel.title("Table and Chart")
    tabel.geometry("1280x720+-10+0")



    for kolom in range(0, 17):
        label = Label(tabel, text=judul_data[kolom], fg="#000000", font="times 10 bold")
        label.grid(row=0, column=kolom, sticky="nsew", padx=1, pady=1)
    for baris in range(len(array_tekanan)):
        for kolom in range(0, 17):
            label = Label(tabel, fg="#000000", font="times 10")
            label.config(text=semuadata[kolom][baris])
            label.grid(row=baris+1, column=kolom, sticky="nsew", padx=1, pady=1)
            tabel.grid_columnconfigure(kolom, weight=1)

    x = array_tekanan
    import numpy as np
    fig,a =  plt.subplots(2,3)
    a[0][0].plot(x, array_co,color="red")
    a[0][0].set_title('Oil Isothermal Compressibility (Co)')
    a[0][0].set(xlabel="psia", ylabel="1/MMpsi")
    a[0][1].plot(x, array_cg,color="green")
    a[0][1].set_title('Gas Isothermal Compressibility (Cg)')
    a[0][1].set(xlabel="psia", ylabel="1/MMpsi")
    a[0][2].plot(x, array_cw,color="blue")
    a[0][2].set_title('Water Isothermal Compressibility (Cw)')
    a[0][2].set(xlabel="psia", ylabel="1/MMpsi")
    a[1][0].plot(x, array_oildens,color="brown")
    a[1][0].set_title('Oil Density')
    a[1][0].set(xlabel="psia", ylabel="lbm/cf")
    a[1][1].plot(x, array_gasdens,color="purple")
    a[1][1].set_title('Gas Density')
    a[1][1].set(xlabel="psia", ylabel="lbm/cf")
    a[1][2].plot(x, array_brinedens,color="orange")
    a[1][2].set_title('Water Density')
    a[1][2].set(xlabel="psia", ylabel="lbm/cf")

    fig,a =  plt.subplots(2,3)
    a[0][0].plot(x, array_oilvis,color="red")
    a[0][0].set_title('Oil Viscosity')
    a[0][0].set(xlabel="psia", ylabel="cP")
    a[0][1].plot(x, array_gasvis,color="green")
    a[0][1].set_title('Gas Viscosity')
    a[0][1].set(xlabel="psia", ylabel="cP")
    a[0][2].plot(x, array_brinevis,color="blue")
    a[0][2].set_title('Water Viscosity')
    a[0][2].set(xlabel="psia", ylabel="cP")
    a[1][0].plot(x, array_bo,color="brown")
    a[1][0].set_title('Oil Formation Volume Factor (Bo)')
    a[1][0].set(xlabel="psia", ylabel="RB/STB")
    a[1][1].plot(x, array_bg,color="purple")
    a[1][1].set_title('Gas Formation Volume Factor (Bg)')
    a[1][1].set(xlabel="psia", ylabel="RB/MSCF")
    a[1][2].plot(x, array_bw,color="orange")
    a[1][2].set_title('Water Formation Volume Factor (Bw)')
    a[1][2].set(xlabel="psia", ylabel="RB/STB")

    fig,a =  plt.subplots(1,3)
    a[0].plot(x, array_rs,color="red")
    a[0].set_title('Gas Solubility (Rs)')
    a[0].set(xlabel="psia", ylabel="MSCF/STB")
    a[1].plot(x, array_rsw,color="green")
    a[1].set_title('Natural Gas in Water Solubility (Rsw)')
    a[1].set(xlabel="psia", ylabel="SCF/STB")
    a[2].plot(x, array_z,color="blue")
    a[2].set_title('Gas Compressibility Factor (Z)')
    a[2].set(xlabel="psia", ylabel="Vol/Vol")


    plt.show()



#TEKANAN DARI INPUT
def P(p=3000):
    poutput = Label(base, width=9, font="arial 10", fg="#86E2D5", bg=defaultbg, anchor="e")
    poutput.config(text=p)
    poutput.grid(row=2, column=2, sticky="E")
    return p
#OIL SPECIFIC GRAVITY
def Sgoil():
    global o5
    o5 = Label(oildata, font="arial 10", fg="#eeeeee", bg="#10133a",)
    o5.config(text=round(141.5/(float(o1.get())+131.5), 3))
    o5.grid(row=4, column=1, sticky="")
    return round(141.5/(float(o1.get())+131.5), 3)
#BUBBLE POINT PRESSURE, IF VALUE = 1 USING VASQUEZ-BEGGS, IF VALUE = 2 USING STANDING'S
def Pb(value=2):
    global tres,api,sg,rsb,psep,tsep
    rsb = float(rsb)
    sg = float(sg)
    api = float(api)
    tres = float(tres)
    psep = float(psep)
    tsep = float(tsep)
    if value == 1:
        SGgs = sg * (1 + 0.00005912 * api * tsep * log10(psep / 114.7))
        if api <= 30:
            C1 = 0.0362
            C2 = 1.0937
            C3 = 25.724
        else:
            C1 = 0.0178
            C2 = 1.187
            C3 = 23.931
        pb = (1000 * rsb / (C1 * SGgs * exp(C3 * api / (tsep + 460)))) ** (1 / C2)
    else:
        pb = 18.2 *  ( ( 1000 * rsb / sg )  ** 0.83 * 10 **  ( 0.00091 * tres - 0.0125 * api )  - 1.4 )
    pb = round(pb, 1)
    o6 = Label(oildata, font="arial 10", fg="#eeeeee", bg="#10133a",)
    o6.config(text=pb)
    o6.grid(row=6, column=1, sticky="")
    return pb
#CRITICAL PRESSURE
def Ppc(sg):
    if ( sg < 0.72 ) :
        ppc = 677 + 15 * sg - 37.5 *  ( sg ** 2 )
    else:
        ppc = 706 - 51.7 * sg - 11.1 *  ( sg ** 2 )
    ppc = round(ppc, 1)
    gas6 = Label(gasdata, font="arial 10", fg="#eeeeee", bg="#10133a",)
    gas6.config(text=ppc)
    gas6.grid(row=4, column=3, columnspan=2, sticky="")
    return ppc
#CRITICAL TEMPERATURE
def Tpc(sg):
    if ( sg < 0.72 ) :
        tpc = 168 + 325 * sg - 12.5 *  ( sg ** 2 )
    else:
        tpc = 187 + 330 * sg - 71.5 *  ( sg ** 2 )
    tpc = round(tpc, 1)
    gas7 = Label(gasdata, font="arial 10", fg="#eeeeee", bg="#10133a",)
    gas7.config(text=tpc)
    gas7.grid(row=5, column=3, columnspan=2, sticky="")
    return tpc
#PRESSURE WITH CORRECTION ON NON-HYDROCARBON EFFECT
def Ppccor(sg, co2, h2s, n2):
    co2 = float(co2)
    h2s = float(h2s)
    n2 = float(n2)
    ppccor = Ppc(sg) + 440 * co2 + 600 * h2s - 170 * n2
    ppccor = round(ppccor, 1)
    gas9 = Label(gasdata, font="arial 10", fg="#eeeeee", bg="#10133a",)
    gas9.config(text=ppccor)
    gas9.grid(row=7, column=3, columnspan=2, sticky="")
    return ppccor
#TEMPERATURE WITH CORRECTION ON NON-HYDROCARBON EFFECT
def Tpccor(sg, co2, h2s, n2):
    co2 = float(co2)
    h2s = float(h2s)
    n2 = float(n2)
    tpccor = Tpc(sg) - 80 * co2 + 130 * h2s - 250 * n2
    tpccor = round(tpccor, 1)
    gas10 = Label(gasdata, font="arial 10", fg="#eeeeee", bg="#10133a",)
    gas10.config(text=tpccor)
    gas10.grid(row=8, column=3, columnspan=2, sticky="")
    return tpccor
#PSEUDO-REDUCED PRESSURE
def Ppr(p, ppccor):
    p = float(p)
    ppccor = float(ppccor)
    ppr = p/ppccor
    ppr = round(ppr, 2)
    gas12 = Label(gasdata, font="arial 10", fg="#eeeeee", bg="#10133a",)
    gas12.config(text=ppr)
    gas12.grid(row=10, column=3, columnspan=2, sticky="")
    return ppr
#PSEUDO-REDUCED TEMPERATURE
def Tpr(tres, tpccor):
    tres = float(tres)
    tpccor = float(tpccor)
    tpr = (tres+460)/tpccor
    tpr = round(tpr, 2)
    gas13 = Label(gasdata, font="arial 10", fg="#eeeeee", bg="#10133a",)
    gas13.config(text=tpr)
    gas13.grid(row=11, column=3, columnspan=2, sticky="")
    return tpr

#OIL PROPERTIES

#RS, IF VALUE = 1 USING STANDING'S, IF VALUE = 2 USING VASQUEZ-BEGGS
def Rs(p,value=1):
    global pb, tres, api, sg, psep, tsep
    p = float(p)
    pb = float(pb)
    tres = float(tres)
    api = float(api)
    sg = float(sg)
    psep = float(psep)
    tsep = float(tsep)

    if value == 1:
        if ( p < pb ) :
            rs = ( sg / 1000 )  *  ( ( p / 18.2 + 1.4 )  / 10 **  ( 0.00091 * tres - 0.0125 * api ) )  **  ( 1 / 0.83 )
        else:
            rs = ( sg / 1000 )  *  ( ( pb / 18.2 + 1.4 )  / 10 **  ( 0.00091 * tres - 0.0125 * api ) )  **  ( 1 / 0.83 )
    else:
        sggs = sg *  ( 1 + 0.00005912 * api * tsep * log10(psep / 114.7) )
        if ( api <= 30 ) :
            C1 = 0.0362
            C2 = 1.0937
            C3 = 25.724
        else:
            C1 = 0.0178
            C2 = 1.187
            C3 = 23.931
        if ( p < pb ) :
            rs = ( ( C1 * sggs *  ( p ** C2 ) )  / 1000 )  * exp(C3 *  ( api /  ( tres + 460 ) ))
        else:
            rs = ( ( C1 * sggs *  ( pb ** C2 ) )  / 1000 )  * exp(C3 *  ( api /  ( tres + 460 ) ))
    rsoutput = Label(base, width=9, font="arial 10", fg="#86E2D5", bg="#10133a", anchor="e")
    rsoutput.config(text=round(rs, 4))
    rsoutput.grid(row=4, column=2, sticky="E")
    return round(rs, 4)
#OIL COMPRESSIBILITY USING GENERAL CORRELATION
def Co(p,rs):
    global tres, api, sg, pb, psep, tsep
    p = float(p)
    pb = float(pb)
    tres = float(tres)
    api = float(api)
    sg = float(sg)
    rs = float(rs)
    psep = float(psep)
    tsep = float(tsep)

    if p > pb:
        A1 = - 1433
        A2 = 5
        A3 = 17.2
        A4 = - 1180
        A5 = 12.61
        A6 = 100000

        sggs = sg *  ( 1 + 0.00005912 * api * tsep * log10(psep / 114.7) )
        co = ( A1 +  ( A2 * rs * 1000 )  +  ( A3 * tres )  +  ( A4 * sggs )  +  ( A5 * api ) )  /  ( A6 * p )
    else:
        A1 = - 7.114
        A2 = - 1.394
        A3 = 0.981
        A4 = 0.77
        A5 = 0.446

        co = exp(A1 + A2 * ln(p) + A3 * ln(tres + 459.6) + A4 * ln(api) + A5 * ln(sg))
    cooutput = Label(base, width=9, font="arial 10", fg="#86E2D5", bg=defaultbg, anchor="e")
    cooutput.config(text=round(co*100000, 4))
    cooutput.grid(row=16, column=2, sticky="E")
    return co
#OIL FVF, IF VALUE = 1 USING STANDING'S, IF VALUE = 2 USING VASQUEZ-BEGGS
def Bo(rs,value=1):
    global tres, api, sg, psep, tsep
    tres = float(tres)
    api = float(api)
    sg = float(sg)
    rs = float(rs)
    psep = float(psep)
    tsep = float(tsep)

    if value == 1:
        bo = 0.9759 + 0.00012 *  ( 1000 * rs *  ( sg *  ( api + 131.5 )  / 141.5 )  ** 0.5 + 1.25 * tres )  ** 1.2
    else:
        SGgs = sg *  ( 1 + 0.00005912 * api * tsep * log10(psep / 114.7) )
        #API value conditional
        if ( api <= 30 ) :
            C1 = 0.0004677
            C2 = 0.00001751
            C3 = - 0.00000001811
        else:
            C1 = 0.000467
            C2 = 0.000011
            C3 = 0.000000001337
        #Main Function of VB FVF Correlation
        bo = 1 + 1000 * C1 * rs +  ( C2 + C3 * rs * 1000 )  *  ( tres - 60 )  * api / SGgs
    booutput = Label(base, width=9, font="arial 10", fg="#86E2D5", bg=defaultbg, anchor="e")
    booutput.config(text=round(bo, 4))
    booutput.grid(row=3, column=2, sticky="E")
    return round(bo, 4)
#OIL DENSITY USING GENERAL CORRELATION
def Oildens(bo,rs):
    global sg, api
    sg = float(sg)
    bo = float(bo)
    rs = float(rs)
    api = float(api)

    sgoil = 141.5/(api+ 131.5)

    oildens=((62.4 * sgoil * 5.615) + 0.0765 * rs * sg * 1000) / (5.615 * bo)
    oildensoutput = Label(base, width=9, font="arial 10", fg="#86E2D5", bg=defaultbg, anchor="e")
    oildensoutput.config(text=round(oildens, 4))
    oildensoutput.grid(row=10, column=2, sticky="E")
    return round(oildens, 4)
#OIL VISCOSITY USING GENERAL CORRELATION
def Oilvis(p, rs):
    global tres, api, pb
    p = float(p)
    tres = float(tres)
    api = float(api)
    pb = float(pb)
    rs = float(rs)
    #Dead Oil Viscosity
    A1 = 1.8653
    A2 = - 0.025086
    A3 = - 0.5644
    Z = A1 +  ( A2 * api )
    Y = 10 ** Z
    X = Y *  ( tres ** A3 )
    DeadVIscos = ( 10 ** X )  - 1
    #Bubble Point Viscosity
    A = 10.715 *  ( 1000 * rs + 100 )  **  ( - 0.515 )
    B = 5.44 *  ( 1000 * rs + 150 )  **  ( - 0.338 )
    BubbleViscos = A *  ( DeadVIscos ** B )
    if ( p > pb ) :
        C1 = 2.6
        C2 = 1.187
        C3 = -11.513
        C4 = -0.0000898
        m = C1 *  ( p ** C2 )  * exp(C3 + C4 * p)
        oilvis = BubbleViscos *  ( p / pb )  ** m
    else:
        oilvis = BubbleViscos
    oilvisoutput = Label(base, width=9, font="arial 10", fg="#86E2D5", bg=defaultbg, anchor="e")
    oilvisoutput.config(text=round(oilvis, 4))
    oilvisoutput.grid(row=13, column=2, sticky="E")
    return round(oilvis, 4)

#GAS PROPERTIES

#Z FACTOR USING DRANCHUK CORRELATION
def Z(ppr):
    global tpr
    A1 = 0.3265
    A2 = - 1.07
    A3 = - 0.5339
    A4 = 0.01569
    A5 = - 0.05165
    A6 = 0.5475
    A7 = - 0.7361
    A8 = 0.1844
    A9 = 0.1056
    A10 = 0.6134
    A11 = 0.721
    EPSILON = 0.00001

    TprSqr = tpr * tpr
    TprCube = TprSqr * tpr
    TprFourth = TprCube * tpr
    TprFifth = TprFourth * tpr
    C0 = ( A7 / tpr )  +  ( A8 / TprSqr )
    C1 = A1 +  ( A2 / tpr )  +  ( A3 / TprCube )  +  ( A4 / TprFourth )  +  ( A5 / TprFifth )
    C2 = A6 + C0
    C3 = A9 * C0
    zEst = 0
    z = 1
    count = 1
    while ( abs(z - zEst) > EPSILON ):
        zEst = z
        z = zCalc(ppr, tpr, zEst, A10, A11, C1, C2, C3)
        if ( count > 15 ) :
            z = - 999999
            break
        count = count + 1

    zoutput = Label(base, width=9, font="arial 10", fg="#86E2D5", bg=defaultbg, anchor="e")
    zoutput.config(text=round(z, 4))
    zoutput.grid(row=9, column=2, sticky="E")
    return round(z, 4)

def zCalc(ppr, tpr, zEst, A10, A11, C1, C2, C3):
    zc = 0.27
    rhoR = zc * ppr /  ( zEst * tpr )          
    rhoR_Sqr = rhoR * rhoR
    rhoR_Fifth = rhoR_Sqr * rhoR_Sqr * rhoR
    TprCube = tpr * tpr * tpr
    TprFifth = TprCube * tpr * tpr
    C4 = A10 *  ( 1 + A11 * rhoR_Sqr )  *  ( rhoR_Sqr / TprCube )  * exp(- A11 * rhoR_Sqr)
    F = zEst -  ( 1 + C1 * rhoR + C2 * rhoR_Sqr - C3 * rhoR_Fifth + C4 )
    Fprime = 1 +  ( C1 * rhoR + 2 * C2 * rhoR_Sqr - 5 * C3 * rhoR_Fifth ) / zEst + 2 * A10 * rhoR_Sqr /  ( TprCube * zEst )  *  ( 1 + A11 * rhoR_Sqr -  ( A11 * rhoR_Sqr )  ** 2 ) * exp(- A11 * rhoR_Sqr)
    return zEst -  ( F / Fprime )
#GAS DENSITY USING GENERAL CORRELATION
def Gasdens(p, z):
    global tres, sg
    p = float(p)
    tres = float(tres)
    sg = float(sg)
    z = float(z)

    R = 10.732
    AirMW = 28.965

    gasdens = sg * AirMW * p / (z * R * (tres + 460))
    gasdensoutput = Label(base, text="12.5251", width=9, font="arial 10", fg="#86E2D5", bg=defaultbg, anchor="e")
    gasdensoutput.config(text=round(gasdens, 4))
    gasdensoutput.grid(row=11, column=2, sticky="E")
    return round(gasdens, 4)
#GAS FVF USING GENERAL CORRECTION
def Bg(p, z):
    global psc, tres
    psc = float(psc)
    z = float(z)
    tres = float(tres)
    p = float(p)

    bg = 1000 * psc * z * (tres + 460) / (5.61458 * (60 + 460) * p)
    bgoutput = Label(base, width=9, font="arial 10", fg="#86E2D5", bg=defaultbg, anchor="e")
    bgoutput.config(text=round(bg, 4))
    bgoutput.grid(row=5, column=2, sticky="E")
    return round(bg, 4)
#GAS VISCOSITY USING LEE-GONZALES-EAKIN CORRELATION
def Gasvis(p,z,gasdens):
    global sg, tres
    gasdens = float(gasdens)
    sg = float(sg)
    z = float(z)
    tres = float(tres)
    p = float(p)

    MWair = 28.964
    Ma = sg * MWair
    K = ( ( 9.4 + 0.02 * Ma )  *  ( tres + 460 )  ** 1.5 )  /  ( 209 + 19 * Ma +  ( tres + 460 ) )
    X = 3.5 +  ( 986 /  ( tres + 460 ) )  + 0.01 * Ma
    Y = 2.4 - 0.2 * X
    gasvis = ( 10 **  ( - 4 ) )  * K * exp(X *  ( ( gasdens / 62.4 )  ** Y ))
    gasvisoutput = Label(base, width=9, font="arial 10", fg="#86E2D5", bg=defaultbg, anchor="e")
    gasvisoutput.config(text=round(gasvis, 4))
    gasvisoutput.grid(row=14, column=2, sticky="E")
    return round(gasvis, 4)
#GAS COMPRESSIBILITY USING BENEDICT-WEBB CORRELATION
def Cg(z,ppr):
    global tpr, ppc
    ppr = float(ppr)
    tpr = float(tpr)
    z = float(z)
    ppc = float(ppc)

    if ( ppr < 5 ) :
        A1 = 0.001290236
        A2 = 0.38193005
        A3 = 0.022199287
        A4 = 0.12215481
        A5 = - 0.015674794
        A6 = 0.027271364
        A7 = 0.023834219
        A8 = 0.4361778
    else:
        A1 = 0.0014507882
        A2 = 0.37922269
        A3 = 0.024181399
        A4 = 0.1182287
        A5 = - 0.037905663
        A6 = 0.19845016
        A7 = 0.048911693
        A8 = 0.0631425417
    RedDens = ( 0.27 * ppr )  /  ( z * tpr )
    B1 = A1 +  ( A2 / tpr )  +  ( A3 / tpr ** 3 )
    B2 = 2 *  ( A4 +  ( A5 / tpr ) )  * RedDens
    B3 = 5 * A5 * A6 *  ( ( RedDens ** 4 )  / tpr )
    B4 = 2 * A7 * RedDens /  ( tpr ** 3 )
    B5 = 1 + A8 *  ( RedDens ** 2 )  -  ( A8 ** 2 )  *  ( RedDens ** 4 )
    B6 = - A8 *  ( RedDens ** 2 )
    dzdr = B1 + B2 + B3 + B4 * B5 * exp(B6)
    Cr = ( 1 / ppr )  -  ( 0.27 /  ( ( z ** 2 )  * tpr ) )  *  ( dzdr /  ( 1 +  ( RedDens / z )  * dzdr ) )
    cg = Cr / ppc
    cgoutput = Label(base, width=9, font="arial 10", fg="#86E2D5", bg=defaultbg, anchor="e")
    cgoutput.config(text=round(cg*100000, 4))
    cgoutput.grid(row=17, column=2, sticky="E")
    return cg

#BRINE/WATER PROPERTIES


#GAS SOLUTION IN BRINE USING GENERAL CORRELATION
def Rsw(p):
    global tres, tds
    p = float(p)
    tres = float(tres)
    tds = float(tds)

    A0 = 8.15839
    A1 = - 6.12265 *  ( 10 ** - 2 )
    A2 = 1.91663 *  ( 10 ** - 4 )
    A3 = - 2.1654 *  ( 10 ** - 7 )
    B0 = 1.01021 *  ( 10 ** - 2 )
    B1 = - 7.44241 *  ( 10 ** - 5 )
    B2 = 3.05553 *  ( 10 ** - 7 )
    B3 = - 2.94883 *  ( 10 ** - 10 )
    C0 = - 9.02505
    C1 = 0.130237
    C2 = - 8.53425 *  ( 10 ** - 4 )
    C3 = 2.34122 *  ( 10 ** - 6 )
    C4 = - 2.37049 *  ( 10 ** - 9 )


    A = A0 +  ( A1 * tres )  +  ( A2 * tres ** 2 )  +  ( A3 * tres ** 3 )
    B = B0 +  ( B1 * tres )  +  ( B2 * tres ** 2 )  +  ( B3 * tres ** 3 )
    C = ( C0 +  ( C1 * tres )  +  ( C2 * tres ** 2 )  +  ( C3 * tres ** 3 )  +  ( C4 * tres ** 4 ) )  *  ( 10 ** - 7 )
    RswMurni = ( A +  ( B * p )  +  ( C * p ** 2 ) )  / 1000
    rsw = RswMurni * 10 **  ( - 0.0840655 * tds * tres ** - 0.285854 )
    rswoutput = Label(base, width=9, font="arial 10", fg="#86E2D5", bg=defaultbg, anchor="e")
    rswoutput.config(text=round(rsw, 4))
    rswoutput.grid(row=7, column=2, sticky="E")

    return round(rsw, 4)
#BRINE FVF USING GENERAL CORRELATION
def Bw(p):
    global tres
    tres = float(tres)
    p = float(p)

    VwP = - 1.0001 *  ( 10 ** - 2 )  + 1.33391 *  ( 10 ** - 4 )  * tres + 5.50654 *  ( 10 ** - 7 )  * tres ** 2
    VwT = - 1.95301 *  ( 10 ** - 9 )  * p * tres - 1.72834 *  ( 10 ** - 13 )  * p ** 2 * tres - 3.58922 *  ( 10 ** - 7 )  * p - 2.25341 *  ( 10 ** - 10 )  * p ** 2
    bw = ( 1 + VwP )  *  ( 1 + VwT )
    bwoutput = Label(base, width=9, font="arial 10", fg="#86E2D5", bg=defaultbg, anchor="e")
    bwoutput.config(text=round(bw, 4))
    bwoutput.grid(row=6, column=2, sticky="E")
    return round(bw, 4)
#BRINE VISCOSITY USING GENERAL CORRELATION
def Brinevis(p):
    global tds, tres
    tds = float(tds)
    tres = float(tres)
    p = float(p)

    A = 109.574 - 8.40564 * tds + 0.313314 * tds ** 2 + 8.72213 * 10 **  ( - 3 )  * tds ** 3
    B = 1.12166 - 2.63951 * 10 **  ( - 2 )  * tds + 6.79461 * 10 **  ( - 4 )  * tds ** 2 + 5.47119 * 10 **  ( - 5 )  * tds ** 3 - 1.55586 * 10 **  ( - 6 )  * tds ** 4
    BrineVisc1 = A * tres **  ( - B )
    brinevis = BrineVisc1 *  ( 0.994 + 4.0295 * 10 **  ( - 5 )  * p * 3.1062 * 10 **  ( - 9 )  * p ** 2 )
    brinevisoutput = Label(base, width=9, font="arial 10", fg="#86E2D5", bg=defaultbg, anchor="e")
    brinevisoutput.config(text=round(brinevis, 4))
    brinevisoutput.grid(row=15, column=2, sticky="E")
    return round(brinevis, 4)
#BRINE COMPRESSIBILITY USING MEEHAN CORRELATION
def Cw(p, rsw, value=1):
    global tres, tds
    p= float(p)
    tres = float(tres)
    rsw = float(rsw)
    tds = float(tds)

    A = 3.8546 - 0.000134 * p
    B = - 0.01052 + 4.77 *  ( 10 ** - 7 )  * p
    C = 3.9267 *  ( 10 ** - 5 )  - 8.8 *  ( 10 ** - 10 )  * p
    Cwf = ( A +  ( B * tres )  +  ( C * tres ** 2 ) )  /  ( 1 *  ( 10 ** 6 ) )

    if value == 2:
        Cwg = Cwf
    else:
        Cwg = Cwf *  ( 1 + 8.9 *( 10 **   - 3 )  * rsw * 1000 )

    Cz = ( ( - 0.052 + 2.7 *  ( 10 ** - 4 )  * tres - 1.14 *  ( 10 ** - 6 )  * tres ** 2 + 1.121 *  ( 10 ** - 9 )  * tres ** 3 )  * tds ** 0.7 + 1 )
    cw = Cwg * Cz
    cwoutput = Label(base, width=9, font="arial 10", fg="#86E2D5", bg=defaultbg, anchor="e")
    cwoutput.config(text=round(cw*100000, 4))
    cwoutput.grid(row=18, column=2, sticky="E")
    return cw
#BRINE DENSITY USING GENERAL CORRELATION
def Brinedens(bw):
    global tds
    BrineDensSc = 62.368 + 0.438603 * tds + 1.60074 *  ( 10 ** - 3 )  *  ( tds ** 2 )
    brinedens = BrineDensSc / bw
    brinedensoutput = Label(base, width=9, font="arial 10", fg="#86E2D5", bg=defaultbg, anchor="e")
    brinedensoutput.config(text=round(brinedens, 4))
    brinedensoutput.grid(row=12, column=2, sticky="E")
    return round(brinedens, 4)
#PROPERTY CONDITION
def Condition(p):
    global pb
    p = float(p)
    if p > pb:
        condition = "U. Saturated"
    else:
        condition = "Saturated"
    conditionoutput = Label(base, width=9, font="arial 10", fg="#86E2D5", bg=defaultbg, anchor="e")
    conditionoutput.config(text=condition)
    conditionoutput.grid(row=8, column=2, sticky="E")
    return condition


#SAVING THE VALUES
def submit():
    global tres,pres,psc,sg,api,psep,tsep,rsb,sgoil,tds,co2,h2s,n2
    global pb,ppc,tpc,ppccor,tpccor,ppr,tpr,p,rs,co,bo,oildens,oilvis,z
    global gasdens, bg, gasvis, cg, rsw, bw, brinevis, cw, brinedens, condition
    global array_conditions,array_rs,array_co,array_bo,array_oildens,array_oilvis,array_z,array_gasdens,array_bg,array_gasvis,array_cg,array_rsw,array_bw,array_brinevis,array_cw,array_brinedens
    p = P(PVTCalculatorP.get())
    tres = g1.get()
    pres = g2.get()
    psc = g3.get()
    sg = g4.get()
    api = o1.get()
    psep = o2.get()
    tsep = o3.get()
    rsb = o4.get()
    sgoil = Sgoil()
    tds = b1.get()
    co2 = gas2.get()
    h2s = gas3.get()
    n2 = gas4.get()
    pb = Pb(radio1.get())
    ppc = Ppc(sg)
    tpc = Tpc(sg)
    ppccor = Ppccor(sg, co2, h2s, n2)
    tpccor = Tpccor(sg, co2, h2s, n2)
    ppr = Ppr(p, ppccor)
    tpr = Tpr(tres, tpccor)
    rs = Rs(p,radiors.get())
    co = Co(p,rs)
    bo = Bo(rs, radiobo.get())
    oildens = Oildens(bo, rs)
    oilvis = Oilvis(p, rs)
    z = Z(ppr)
    gasdens = Gasdens(p, z)
    bg = Bg(p, z)
    gasvis = Gasvis(p,z, gasdens)
    cg = Cg(z,ppr)
    rsw = Rsw(p)
    bw = Bw(p)
    brinevis = Brinevis(p)
    cw = Cw(p, rsw,radio2.get())
    brinedens = Brinedens(bw)
    condition = Condition(p)

#================================================================GUI DEVELOPMENT================================================================
judul = Label(root,
    text="OIL PROPERTIES\nFLUIDS PROPERTIES CORRELATION",
    width=1,
    height=5,
    fg="#1b96f3",
    bg="#10133a",
    font="arial 21 bold",
    justify="center",
)
judul.grid(row=0, column=0, columnspan=4, sticky="news")

informations = LabelFrame(root, text="Informations", font="arial 13", fg="#fcdf87", bg="#10133a", )
informations.grid(row=1 , column=0, sticky="news")

information1 = Label(informations, text=" Field Name :", font="arial 10", fg="#eeeeee", bg="#10133a", )
information1.grid(row=0, column=0, sticky="E")
information2 = Label(informations, text="Company :", font="arial 10", fg="#eeeeee", bg="#10133a", )
information2.grid(row=1, column=0, sticky="E")
information3 = Label(informations, text="Location :", font="arial 10", fg="#eeeeee", bg="#10133a", )
information3.grid(row=2, column=0, sticky="E")
information4 = Label(informations, text="Engineer :", font="arial 10", fg="#eeeeee", bg="#10133a", )
information4.grid(row=3, column=0, sticky="E")

i1 = Entry(informations)
i1.insert(END, "Blok East Natuna")
i2 = Entry(informations)
i2.insert(END, "Pertamina")
i3 = Entry(informations)
i3.insert(END, "Natuna")
i4 = Entry(informations)
i4.insert(END, "Religious Mohan")

i1.grid(row=0, column=1)
i2.grid(row=1, column=1)
i3.grid(row=2, column=1)
i4.grid(row=3, column=1)

generaldata = LabelFrame(root, text="General Data", font="arial 13", fg="#fcdf87", bg="#10133a", )
generaldata.grid(row=2, column=0, sticky="news")

generaldata1 = Label(generaldata, text="Reservoir Temperature (Tres) :", font="arial 10", fg="#eeeeee", bg="#10133a",  )
generaldata1.grid(row=0, column=0, sticky="E")
generaldata2 = Label(generaldata, text="Initial Reservoir Pressure (Pres) :", font="arial 10", fg="#eeeeee", bg="#10133a", )
generaldata2.grid(row=1, column=0, sticky="E")
generaldata3 = Label(generaldata, text=" Standard Condition Pressure (Psc) :", font="arial 10", fg="#eeeeee", bg="#10133a", )
generaldata3.grid(row=2, column=0, sticky="E")
generaldata4 = Label(generaldata, text="Specific Gravity Gas (SG) :", font="arial 10", fg="#eeeeee", bg="#10133a", )
generaldata4.grid(row=3, column=0, sticky="E")

g1 = Entry(generaldata, width=8, justify=RIGHT)
g1.insert(END, "200")
g2 = Entry(generaldata, width=8, justify=RIGHT)
g2.insert(END, "4500")
g3 = Entry(generaldata, width=8, justify=RIGHT)
g3.insert(END, "14.56")
g4 = Entry(generaldata, width=8, justify=RIGHT)
g4.insert(END, "0.87")

g1.grid(row=0, column=1)
g2.grid(row=1, column=1)
g3.grid(row=2, column=1)
g4.grid(row=3, column=1)

generaldata1 = Label(generaldata, text="⁰F", font="arial 10", fg="#eeeeee", bg="#10133a", )
generaldata1.grid(row=0, column=2, sticky="W")
generaldata2 = Label(generaldata, text="psia", font="arial 10", fg="#eeeeee", bg="#10133a", )
generaldata2.grid(row=1, column=2, sticky="W")
generaldata3 = Label(generaldata, text="psia", font="arial 10", fg="#eeeeee", bg="#10133a", )
generaldata3.grid(row=2, column=2, sticky="W")
generaldata4 = Label(generaldata, text=" ", font="arial 10", fg="#eeeeee", bg="#10133a", )
generaldata4.grid(row=3, column=2, sticky="W")

oildata = LabelFrame(root, text="Oil Data", font="arial 13", fg="#fcdf87", bg="#10133a", )
oildata.grid(row=3, column=0, sticky="news")

oildata1 = Label(oildata, text="Oil API :", font="arial 10", fg="#eeeeee", bg="#10133a", )
oildata1.grid(row=0, column=0, sticky="E")
oildata2 = Label(oildata, text="Separator Pressure (Psep) :", font="arial 10", fg="#eeeeee", bg="#10133a", )
oildata2.grid(row=1, column=0, sticky="E")
oildata3 = Label(oildata, text=" Separator Temperature (Tsep) :", font="arial 10", fg="#eeeeee", bg="#10133a", )
oildata3.grid(row=2, column=0, sticky="E")
oildata4 = Label(oildata, text="Gas Solubility at Bubble Point (Rsb) :", font="arial 10", fg="#eeeeee", bg="#10133a", )
oildata4.grid(row=3, column=0, sticky="E")

o1 = Entry(oildata, width=8, justify=RIGHT)
o1.insert(END, "54")
o2 = Entry(oildata, width=8, justify=RIGHT)
o2.insert(END, "150")
o3 = Entry(oildata, width=8, justify=RIGHT)
o3.insert(END, "60")
o4 = Entry(oildata, width=8, justify=RIGHT)
o4.insert(END, "1.459")

o1.grid(row=0, column=1)
o2.grid(row=1, column=1)
o3.grid(row=2, column=1)
o4.grid(row=3, column=1)

oildata1 = Label(oildata, text=" ", font="arial 10", fg="#eeeeee", bg="#10133a", )
oildata1.grid(row=0, column=2, sticky="W")
oildata2 = Label(oildata, text="psia", font="arial 10", fg="#eeeeee", bg="#10133a", )
oildata2.grid(row=1, column=2, sticky="W")
oildata3 = Label(oildata, text="⁰F", font="arial 10", fg="#eeeeee", bg="#10133a", )
oildata3.grid(row=2, column=2, sticky="W")
oildata4 = Label(oildata, text="MSCF/STB", font="arial 10", fg="#eeeeee", bg="#10133a", )
oildata4.grid(row=3, column=2, sticky="W")


oildata5 = Label(oildata, text="Specific Gravity Oil (SGoil) :", font="arial 10", fg="#eeeeee", bg="#10133a", )
oildata5.grid(row=4, column=0, sticky="E")
o5 = Label(oildata, text=round(141.5/(float(o1.get())+131.5), 3), font="arial 10", fg="#eeeeee", bg="#10133a",)
o5.grid(row=4, column=1, sticky="")


oildata6 = Label(oildata, text="Bubble Point Pressure (Pb) :", font="arial 10", fg="#eeeeee", bg="#10133a", )
oildata6.grid(row=6, column=0, sticky="E")
o6 = Label(oildata, text=round(141.5/(float(o1.get())+131.5), 3), font="arial 10", fg="#eeeeee", bg="#10133a",)
o6.grid(row=6, column=1, sticky="")
oildata4 = Label(oildata, text="psia", font="arial 10", fg="#eeeeee", bg="#10133a", )
oildata4.grid(row=6, column=2, sticky="W")


radio1 = IntVar()
radio1.set("2")
Radiobutton(oildata, text="Vasquez-Beggs", variable=radio1, value=1, font="arial 10", fg="#eeeeee", bg="#10133a", selectcolor="#10133a", command=lambda: Pb(radio1.get())).grid(row=5, column=0, sticky="E")
Radiobutton(oildata, text="Standing's  ", variable=radio1, value=2, font="arial 10", fg="#eeeeee", bg="#10133a", selectcolor="#10133a", command=lambda: Pb(radio1.get())).grid(row=5, column=1, columnspan=2, sticky="W")


brinedata = LabelFrame(root, text="Brine Data", font="arial 13", fg="#fcdf87", bg="#10133a", )
brinedata.grid(row=1, column=1, sticky="news")

brinedata1 = Label(brinedata, text=" Total Dissolved Solid (TDS) :", font="arial 10", fg="#eeeeee", bg="#10133a", )
brinedata1.grid(row=0, column=0, sticky="E")

b1 = Entry(brinedata, width=4, justify=CENTER)
b1.insert(END, "5")

b1.grid(row=0, column=1)

brinedata1 = Label(brinedata, text="%", font="arial 10", fg="#eeeeee", bg="#10133a", )
brinedata1.grid(row=0, column=2, sticky="W")

radio2 = IntVar()
radio2.set("1")
Radiobutton(brinedata, text="Gas-Saturated Brine", variable=radio2, value=1, font="arial 10", fg="#eeeeee", bg="#10133a", selectcolor="#10133a", width=15, anchor="w").grid(row=1, column=0, sticky="E")
Radiobutton(brinedata, text="Gas-Free Brine", variable=radio2, value=2, font="arial 10", fg="#eeeeee", bg="#10133a", selectcolor="#10133a", width=15, anchor="w").grid(row=2, column=0, sticky="E")


gasdata = LabelFrame(root, text="Gas Data", font="arial 13", fg="#fcdf87", bg="#10133a", )
gasdata.grid(row=2, column=1, rowspan=2, sticky="news")

gasdata1 = Label(gasdata, text="Mole Percentage", font="arial 10", fg="#eeeeee", bg="#10133a", )
gasdata1.grid(row=0, column=0, columnspan=6, sticky="")
gasdata2 = Label(gasdata, text=" CO2 ", font="arial 10", fg="#eeeeee", bg="#10133a", )
gasdata2.grid(row=1, column=0, columnspan=2, sticky="")
gasdata3 = Label(gasdata, text=" H2S ", font="arial 10", fg="#eeeeee", bg="#10133a", )
gasdata3.grid(row=1, column=2, columnspan=2, sticky="")
gasdata4 = Label(gasdata, text=" N2 ", font="arial 10", fg="#eeeeee", bg="#10133a", )
gasdata4.grid(row=1, column=4, columnspan=2, sticky="")



gas2 = Entry(gasdata, width=8, justify=CENTER)
gas2.insert(END, "0.25")
gas3 = Entry(gasdata, width=8, justify=CENTER)
gas3.insert(END, "0")
gas4 = Entry(gasdata, width=8, justify=CENTER)
gas4.insert(END, "0")

gas2.grid(row=2, column=0, columnspan=2,)
gas3.grid(row=2, column=2, columnspan=2,)
gas4.grid(row=2, column=4, columnspan=2,)



gasdata5 = Label(gasdata, text="Critical Properties", font="arial 10 bold", fg="#dda0dd", bg="#10133a", height=2, anchor="s" )
gasdata5.grid(row=3, column=0, columnspan=6, sticky="ws")
gasdata6 = Label(gasdata, text="Pressure (Ppc) :", font="arial 10", fg="#eeeeee", bg="#10133a", )
gasdata6.grid(row=4, column=0, columnspan=3, sticky="W")
gasdata7 = Label(gasdata, text="Temperature (Tpc) :", font="arial 10", fg="#eeeeee", bg="#10133a", )
gasdata7.grid(row=5, column=0, columnspan=3, sticky="W")
gasdata8 = Label(gasdata, text="Correction on Non-Hydrocarbon Effect", font="arial 10 bold", fg="#dda0dd", bg="#10133a", )
gasdata8.grid(row=6, column=0, columnspan=6, sticky="w")
gasdata9 = Label(gasdata, text="Pressure (Ppc'):", font="arial 10", fg="#eeeeee", bg="#10133a", )
gasdata9.grid(row=7, column=0, columnspan=3, sticky="W")
gasdata10 = Label(gasdata, text="Temperature (Tpc'):", font="arial 10", fg="#eeeeee", bg="#10133a", )
gasdata10.grid(row=8, column=0, columnspan=3, sticky="W")
gasdata11 = Label(gasdata, text="Pseudo-Reduced Properties", font="arial 10 bold", fg="#dda0dd", bg="#10133a", )
gasdata11.grid(row=9, column=0, columnspan=6, sticky="W")
gasdata12 = Label(gasdata, text="Pressure (Ppr):", font="arial 10", fg="#eeeeee", bg="#10133a", )
gasdata12.grid(row=10, column=0, columnspan=3, sticky="W")
gasdata13 = Label(gasdata, text="Temperature (Tpr):", font="arial 10", fg="#eeeeee", bg="#10133a", )
gasdata13.grid(row=11, column=0, columnspan=3, sticky="W")

gas6 = Label(gasdata, text="0", font="arial 10", fg="#eeeeee", bg="#10133a",)
gas6.grid(row=4, column=3, columnspan=2, sticky="")
gasdata6 = Label(gasdata, text="psia", font="arial 10", fg="#eeeeee", bg="#10133a", )
gasdata6.grid(row=4, column=5, columnspan=2, sticky="W")
gas7 = Label(gasdata, text="0", font="arial 10", fg="#eeeeee", bg="#10133a",)
gas7.grid(row=5, column=3, columnspan=2, sticky="")
gasdata7 = Label(gasdata, text="⁰F", font="arial 10", fg="#eeeeee", bg="#10133a", )
gasdata7.grid(row=5, column=5, columnspan=2, sticky="W")
gas9 = Label(gasdata, text="0", font="arial 10", fg="#eeeeee", bg="#10133a",)
gas9.grid(row=7, column=3, columnspan=2, sticky="")
gasdata9 = Label(gasdata, text="psia", font="arial 10", fg="#eeeeee", bg="#10133a", )
gasdata9.grid(row=7, column=5, columnspan=2, sticky="W")
gas10 = Label(gasdata, text="0", font="arial 10", fg="#eeeeee", bg="#10133a",)
gas10.grid(row=8, column=3, columnspan=2, sticky="")
gasdata10 = Label(gasdata, text="⁰F", font="arial 10", fg="#eeeeee", bg="#10133a", )
gasdata10.grid(row=8, column=5, columnspan=2, sticky="W")




base = LabelFrame(root, text="PVT Calculator")
defaultbg = "#10133a"
base.configure(bg=defaultbg, highlightthickness=0, fg="#eeeeee", font="arial 15 bold",)
base.grid(row=1, column=2, rowspan=3, sticky="news")


ppvt = Label(base, text="P :", width=13, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="e")
ppvt.grid(row=2, column=1, sticky="E")
bopvt = Label(base, text="Bo :", width=13, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="e")
bopvt.grid(row=3, column=1, sticky="E")
rspvt = Label(base, text="Rs :", width=13, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="e")
rspvt.grid(row=4, column=1, sticky="E")
bgpvt = Label(base, text="Bg :", width=13, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="e")
bgpvt.grid(row=5, column=1, sticky="E")
bwpvt = Label(base, text="Bw :", width=13, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="e")
bwpvt.grid(row=6, column=1, sticky="E")
rswpvt = Label(base, text="Rsw :", width=13, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="e")
rswpvt.grid(row=7, column=1, sticky="E")
conditionpvt = Label(base, text="Condition :", width=13, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="e")
conditionpvt.grid(row=8, column=1, sticky="E")
zpvt = Label(base, text="Z :", width=13, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="e")
zpvt.grid(row=9, column=1, sticky="E")
oildenspvt = Label(base, text="Oil Density :", width=13, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="e")
oildenspvt.grid(row=10, column=1, sticky="E")
gasdenspvt = Label(base, text="Gas Density :", width=13, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="e")
gasdenspvt.grid(row=11, column=1, sticky="E")
brinedenspvt = Label(base, text="Brine Density :", width=13, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="e")
brinedenspvt.grid(row=12, column=1, sticky="E")
oilvispvt = Label(base, text="Oil Viscosity :", width=13, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="e")
oilvispvt.grid(row=13, column=1, sticky="E")
gasvispvt = Label(base, text="Gas Viscosity :", width=13, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="e")
gasvispvt.grid(row=14, column=1, sticky="E")
brinevispvt = Label(base, text="Brine Viscosity :", width=13, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="e")
brinevispvt.grid(row=15, column=1, sticky="E")
copvt = Label(base, text="Co x 1E-5 :", width=13, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="e")
copvt.grid(row=16, column=1, sticky="E")
cgpvt = Label(base, text="Cg x 1E-5 :", width=13, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="e")
cgpvt.grid(row=17, column=1, sticky="E")
cwpvt = Label(base, text="Cw x 1E-5 :", width=13, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="e")
cwpvt.grid(row=18, column=1, sticky="E")


poutput = Label(base, text="3000", width=9, font="arial 10", fg="#86E2D5", bg=defaultbg, anchor="e")
poutput.grid(row=2, column=2, sticky="E")
booutput = Label(base, text="1.7186", width=9, font="arial 10", fg="#86E2D5", bg=defaultbg, anchor="e")
booutput.grid(row=3, column=2, sticky="E")
rsoutput = Label(base, text="1.3563", width=9, font="arial 10", fg="#86E2D5", bg=defaultbg, anchor="e")
rsoutput.grid(row=4, column=2, sticky="E")
bgoutput = Label(base, text="0.866", width=9, font="arial 10", fg="#86E2D5", bg=defaultbg, anchor="e")
bgoutput.grid(row=5, column=2, sticky="E")
bwoutput = Label(base, text="1.03447", width=9, font="arial 10", fg="#86E2D5", bg=defaultbg, anchor="e")
bwoutput.grid(row=6, column=2, sticky="E")
rswoutput = Label(base, text="0.01223", width=9, font="arial 10", fg="#86E2D5", bg=defaultbg, anchor="e")
rswoutput.grid(row=7, column=2, sticky="E")
conditionoutput = Label(base, text="Under Saturated", width=9, font="arial 10", fg="#86E2D5", bg=defaultbg, anchor="e")
conditionoutput.grid(row=8, column=2, sticky="E")
zoutput = Label(base, text="0.7895", width=9, font="arial 10", fg="#86E2D5", bg=defaultbg, anchor="e")
zoutput.grid(row=9, column=2, sticky="E")
oildensoutput = Label(base, text="36.9269", width=9, font="arial 10", fg="#86E2D5", bg=defaultbg, anchor="e")
oildensoutput.grid(row=10, column=2, sticky="E")
gasdensoutput = Label(base, text="12.5251", width=9, font="arial 10", fg="#86E2D5", bg=defaultbg, anchor="e")
gasdensoutput.grid(row=11, column=2, sticky="E")
brinedensoutput = Label(base, text="62.4482", width=9, font="arial 10", fg="#86E2D5", bg=defaultbg, anchor="e")
brinedensoutput.grid(row=12, column=2, sticky="E")
oilvisoutput = Label(base, text="0.1796", width=9, font="arial 10", fg="#86E2D5", bg=defaultbg, anchor="e")
oilvisoutput.grid(row=13, column=2, sticky="E")
gasvisoutput = Label(base, text="0.0242", width=9, font="arial 10", fg="#86E2D5", bg=defaultbg, anchor="e")
gasvisoutput.grid(row=14, column=2, sticky="E")
brinevisoutput = Label(base, text="0.3408", width=9, font="arial 10", fg="#86E2D5", bg=defaultbg, anchor="e")
brinevisoutput.grid(row=15, column=2, sticky="E")
cooutput = Label(base, text="2.8067", width=9, font="arial 10", fg="#86E2D5", bg=defaultbg, anchor="e")
cooutput.grid(row=16, column=2, sticky="E")
cgoutput = Label(base, text="26.7247", width=9, font="arial 10", fg="#86E2D5", bg=defaultbg, anchor="e")
cgoutput.grid(row=17, column=2, sticky="E")
cwoutput = Label(base, text="0.3070", width=9, font="arial 10", fg="#86E2D5", bg=defaultbg, anchor="e")
cwoutput.grid(row=18, column=2, sticky="E")



punit = Label(base, text=" psia", width=10, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="w")
punit.grid(row=2, column=3, sticky="E")
bounit = Label(base, text=" RB/STB", width=10, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="w")
bounit.grid(row=3, column=3, sticky="E")
rsunit = Label(base, text=" MSCF/STB", width=10, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="w")
rsunit.grid(row=4, column=3, sticky="E")
bgunit = Label(base, text=" RB/MSCF", width=10, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="w")
bgunit.grid(row=5, column=3, sticky="E")
bwunit = Label(base, text=" RB/MSCF", width=10, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="w")
bwunit.grid(row=6, column=3, sticky="E")
rswunit = Label(base, text=" SCF/STB", width=10, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="w")
rswunit.grid(row=7, column=3, sticky="E")
conditionunit = Label(base, text=" Oil Sat", width=10, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="w")
conditionunit.grid(row=8, column=3, sticky="E")
zunit = Label(base, text=" Vol/Vol", width=10, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="w")
zunit.grid(row=9, column=3, sticky="E")
oildensunit = Label(base, text=" lbm/CF", width=10, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="w")
oildensunit.grid(row=10, column=3, sticky="E")
gasdensunit = Label(base, text=" lbm/CF", width=10, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="w")
gasdensunit.grid(row=11, column=3, sticky="E")
brinedensunit = Label(base, text=" lbm/CF", width=10, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="w")
brinedensunit.grid(row=12, column=3, sticky="E")
oilvisunit = Label(base, text=" cP", width=10, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="w")
oilvisunit.grid(row=13, column=3, sticky="E")
gasvisunit = Label(base, text=" cP", width=10, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="w")
gasvisunit.grid(row=14, column=3, sticky="E")
brinevisunit = Label(base, text=" cP", width=10, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="w")
brinevisunit.grid(row=15, column=3, sticky="E")
counit = Label(base, text=" 1/MMpsi", width=10, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="w")
counit.grid(row=16, column=3, sticky="E")
cgunit = Label(base, text=" 1/MMpsi", width=10, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="w")
cgunit.grid(row=17, column=3, sticky="E")
cwunit = Label(base, text=" 1/MMpsi", width=10, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="w")
cwunit.grid(row=18, column=3, sticky="E")

radiobo = IntVar()
radiobo.set("1")
Radiobutton(base, text=" Standing's", variable=radiobo, value=1, font="arial 10", fg="#eeeeee", bg=defaultbg, selectcolor=defaultbg, ).grid(row=3, column=4, sticky="w")
Radiobutton(base, text=" Vasquez-Beggs", variable=radiobo, value=2, font="arial 10", fg="#eeeeee", bg=defaultbg, selectcolor=defaultbg, ).grid(row=3, column=5, sticky="w")

radiors = IntVar()
radiors.set("1")
Radiobutton(base, text=" Standing's", variable=radiors, value=1, font="arial 10", fg="#eeeeee", bg=defaultbg, selectcolor=defaultbg,).grid(row=4, column=4, sticky="w")
Radiobutton(base, text=" Vasquez-Beggs", variable=radiors, value=2, font="arial 10", fg="#eeeeee", bg=defaultbg, selectcolor=defaultbg,).grid(row=4, column=5, sticky="w")

bgcorrel = Label(base, text=" General Correlation", width=15, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="w")
bgcorrel.grid(row=5, column=4, columnspan=2, sticky="")
bwcorrel = Label(base, text=" General Correlation", width=15, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="w")
bwcorrel.grid(row=6, column=4, columnspan=2, sticky="")
rswcorrel = Label(base, text=" General Correlation", width=15, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="w")
rswcorrel.grid(row=7, column=4, columnspan=2, sticky="")
zcorrel = Label(base, text=" Dranchuk Correlation", width=15, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="w")
zcorrel.grid(row=9, column=4, columnspan=2, sticky="")
oildenscorrel = Label(base, text=" General Correlation", width=15, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="w")
oildenscorrel.grid(row=10, column=4, columnspan=2, sticky="")
gasdenscorrel = Label(base, text=" General Correlation", width=15, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="w")
gasdenscorrel.grid(row=11, column=4, columnspan=2, sticky="")
brinedenscorrel = Label(base, text=" General Correlation", width=15, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="w")
brinedenscorrel.grid(row=12, column=4, columnspan=2, sticky="")
oilviscorrel = Label(base, text=" Beggs-Robinson Correlation", width=15, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="w")
oilviscorrel.grid(row=13, column=4, columnspan=2, sticky="")
gasviscorrel = Label(base, text=" Lee-Gonzales-Eakin Corr.", width=15, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="w")
gasviscorrel.grid(row=14, column=4, columnspan=2, sticky="")
brineviscorrel = Label(base, text=" General Correlation", width=15, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="w")
brineviscorrel.grid(row=15, column=4, columnspan=2, sticky="")
cocorrel = Label(base, text=" General Correlation", width=15, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="w")
cocorrel.grid(row=16, column=4, columnspan=2, sticky="")
cgcorrel = Label(base, text=" Benedict-Webb-Rubin Corr.", width=15, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="w")
cgcorrel.grid(row=17, column=4, columnspan=2, sticky="")
cwcorrel = Label(base, text=" Meehan Correlation", width=15, font="arial 10", fg="#eeeeee", bg=defaultbg, anchor="w")
cwcorrel.grid(row=18, column=4, columnspan=2, sticky="")







tombol_tabel = Button(root, 
    text="View Table\nand\nChart", 
    width=17,
    height=1,
    fg="#90EE90",
    bg="#8859b6",
    font="arial 18 bold", 
    relief=FLAT,
    command=Tabel
)
tombol_tabel.grid(row=1, column=3, sticky="news")

label_PVT = LabelFrame(root, text="P for PVT Calculator", font="arial 13", fg="#fcdf87", bg="#10133a",)
label_PVT.grid(row=2, column=3, sticky="news")
Grid.rowconfigure(label_PVT, 0, weight=1)
Grid.columnconfigure(label_PVT, 0, weight=1)

PVTCalculatorP = Entry(label_PVT,
    width=14,
    fg="#fff7e2",
    bg="#8859b6",
    font="arial 25 bold",
    justify=CENTER,
    relief=FLAT,
)
PVTCalculatorP.insert(END, "3000")
PVTCalculatorP.grid(row=0, column=0, sticky="news")
PVTCalculatorlabel = Label(label_PVT, text="psia", font="arial 13", fg="#eeeeee", bg="#10133a",)
PVTCalculatorlabel.grid(row=0, column=1, sticky="news")


tombol_submit = Button(root, 
    text="SUBMIT", 
    width=17,
    height=1,
    fg="#F1F227",
    bg="#8859b6",
    font="arial 30 bold", 
    relief=FLAT,
    command=submit
)
tombol_submit.grid(row=3, column=3, sticky="news")

submit()


kosongan = Canvas(root, width=50, height=200, background="#10133a", highlightthickness=0)
kosongan.grid(row=5, column=0, columnspan=4, sticky="news")
kosongan = Canvas(root, width=50, height=5, background="#10133a")
kosongan.grid(row=6, column=0, columnspan=4, sticky="news")

pesansubmit = Label(root, text="After updating data, always click SUBMIT",height=1, bg="#10133a", fg = "#f1f227", font="times 14 bold", justify="center")
pesansubmit.grid(row=7, column=0, columnspan=4, sticky="news")
NamaNim = Label(root, text="Al-Fath Syahalam 12219013      Difans Afta Mumidda Mohan 12219037      Muhammad Arya Pratama 12219054      Muhammad Azmi 12219059      Religious Mahda Eden Haq 12219081",height=1, bg="#10133a", fg = "#2ecc91", font="times 11", justify="center",)
NamaNim.grid(row=8, column=0, columnspan=4, sticky="news" )



root.mainloop()
#============================================================END OF SCRIPT=============================================================