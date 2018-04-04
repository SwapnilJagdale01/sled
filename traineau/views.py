# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseForbidden, HttpResponse
import json
import time
import threading
#sched.shutdown()
def home(request):
    return render(request, "home.html")

#Bacth Variable
batch_var=1

#Stock variables
StkL1 = 2
StkL2 = 2
StkL3 = 2
StkL4 = 2
StkSKI1 = 2
StkSKI2 = 2
StkSEAT = 2
StkASS = 0
#Min stock variables
minStkL1 = 0
minStkL2 = 0
minStkL3 = 0
minStkL4 = 0
minStkSKI1 = 0
minStkSKI2 = 0
minStkSEAT = 0
#Maximum stock variables
maxStkL1 = 200
maxStkL2 = 200
maxStkL3 = 200
maxStkL4 = 200
maxStkSKI1 = 200
maxStkSKI2 = 200
maxStkSEAT = 200
#Produced qty
Prod1 = 0
Prod2 = 0
Prod3 = 0
Prod4 = 0
ProdSKI1 = 0
ProdSKI2 = 0
ProdSEAT = 0
ProdASS = 0

#Cycle time for each Work station (WS)
TCL1 = 0
TCL2 = 0
TCL3 = 0
TCL4 = 0
TCSKI1 = 0
TCSKI2 = 0
TCSEAT = 0
TCASS = 0
#Labor Cost per WS
CL1 = 0
CL2 = 0
CL3 = 0
CL4 = 0
CSKI1 = 0
CSKI2 = 0
CSEAT = 0
CASS = 0
#Number of Non-conformity per WS
NCL1 = 0
NCL2 = 0
NCL3 = 0
NCL4 = 0
NCSKI1 = 0
NCSKI2 = 0
NCSEAT = 0
NCASS = 0
#Number of employee for each workstation
MOL1 = 2
MOL2 = 2
MOL3 = 1
MOL4 = 1
MOSKI1 = 1
MOSKI2 = 1
MOSEAT = 1
MOASS = 2
#Raw material cost
MPL = 150 #sleigh
MPSEAT = 40 #SEAT
MPSKI = 40 #skis
#Labor rate (euros/seconds)
C = 12
#Other variables
sale = 10000
REV2 = 0 #revenu
CA = 0 #total sales
COUT = 0 #total cost
CNC = 0 #cost of non-conformities

# Graph list variables
TDP=[]
TDC=[]
P=[]
UI=[]
TK=[[0,55], [1,55], [2,55], [3,55], [4,55], [5,55], [6,55], [7,55], [8,55], [9,55], [10,55], [11,55], [12,55], [13,55], [14,55], [15,55], [16,55],[17,55], [18,55], [19,55], [20,55], [21,55], [22,55], [23,55], [24,55], [25,55], [26,55], [27,55], [28,55], [29,55], [30,55] ]
global gTime, pauseTime, resumeTime, diffTime

pauseTime=0.0
resumeTime=0.0
diffTime=0.0
gTime=0.0


def get_initial_data(request):

    global StkL1, StkL2, StkL3, StkL4, StkSKI1, StkSKI2, StkSEAT, StkASS, gTime, resumeTime, diffTime, pauseTime
    StkL1 = 2 
    StkL2 = 2 
    StkL3 = 2 
    StkL4 = 2 
    StkSKI1 = 2 
    StkSKI2 = 2 
    StkSEAT = 2 
    StkASS = 0 
    pauseTime=0.0
    resumeTime=0.0
    diffTime=0.0
    # timer=[0,0,0] 
    #Min stock variables 
    global minStkL1, minStkL2, minStkL3, minStkL4, minStkSKI1, minStkSKI2, minStkSEAT 
    minStkL1 = 3 
    minStkL2 = 3 
    minStkL3 = 3 
    minStkL4 = 3 
    minStkSKI1 = 3 
    minStkSKI2 = 3 
    minStkSEAT = 3 
    #Maximum stock variables 
    global maxStkL1, maxStkL2, maxStkL3, maxStkL4, maxStkSKI1, maxStkSKI2, maxStkSEAT 
    maxStkL1 = 10 
    maxStkL2 = 10 
    maxStkL3 = 10 
    maxStkL4 = 10 
    maxStkSKI1 = 10 
    maxStkSKI2 = 10 
    maxStkSEAT = 10 
    #Produced qty 
    global Prod1, Prod2, Prod3, Prod4, ProdSKI1, ProdSKI2, ProdSEAT, ProdASS 
    Prod1 = 0 
    Prod2 = 0 
    Prod3 = 0 
    Prod4 = 0 
    ProdSKI1 = 0 
    ProdSKI2 = 0 
    ProdSEAT = 0 
    ProdASS = 0 
    #Cycle time for each Work station (WS) 
    global TCL1, TCL2, TCL3, TCL4, TCSKI1, TCSKI2, TCSEAT, TCASS 
    TCL1 = 0 
    TCL2 = 0 
    TCL3 = 0 
    TCL4 = 0 
    TCSKI1 = 0 
    TCSKI2 = 0 
    TCSEAT = 0 
    TCASS = 0 
    #Labor Cost per WS 
    global CL1, CL2, CL3, CL4, CSKI1, CSKI2, CSEAT, CASS 
    CL1 = 0 
    CL2 = 0 
    CL3 = 0 
    CL4 = 0 
    CSKI1 = 0 
    CSKI2 = 0 
    CSEAT = 0 
    CASS = 0 
    #Number of Non-conformity per WS 
    global NCL1, NCL2, NCL3, NCL4, NCSKI1, NCSKI2, NCSEAT, NCASS 
    NCL1 = 0 
    NCL2 = 0 
    NCL3 = 0 
    NCL4 = 0 
    NCSKI1 = 0 
    NCSKI2 = 0 
    NCSEAT = 0 
    NCASS = 0 
    #Number of employee for each workstation 
    global MOL1, MOL2, MOL3, MOL4, MOSKI1, MOSKI2, MOSEAT, MOASS 
    MOL1 = 2 
    MOL2 = 2
    MOL3 = 1 
    MOL4 = 1 
    MOSKI1 = 1 
    OSKI2 = 1 
    MOSEAT = 1 
    MOASS = 2 
    #Raw material cost 
    global MPL, MPSEAT, MPSKI, C, sale, REV2, CA, COUT, CNC, TDC, TDP, batch_var, P, UI, TK
    MPL = 150 
    #sleigh 
    MPSEAT = 40 
    #SEAT
    MPSKI = 40 
    #skis #Labor rate (euros/seconds) 
    C = 12 
    #Other variables 
    sale = 10000 
    REV2 = 0 
    #revenu 
    CA = 0 
    #total sales 
    COUT = 0 
    #total cost 
    CNC = 0 
    TDC=[]
    TDP=[]
    batch_var=1
    P=[]
    UI=[]
    TK=[]
    print "TDP", TDP
    #cost of non-conformities
    
    raw_dict = {}

    raw_dict['MOL1'] = MOL1
    raw_dict['MOL2'] = MOL2
    raw_dict['MOL3'] = MOL3
    raw_dict['MOL4'] = MOL4
    raw_dict['MOSKI1'] = MOSKI1
    raw_dict['MOSKI2'] = MOSKI2
    raw_dict['MOSEAT'] = MOSEAT
    raw_dict['MOASS'] = MOASS

    raw_dict['StkL1'] = StkL1
    raw_dict['StkL2'] = StkL2
    raw_dict['StkL3'] = StkL3
    raw_dict['StkL4'] = StkL4
    raw_dict['StkSKI1'] = StkSKI1
    raw_dict['StkSKI2'] = StkSKI2
    raw_dict['StkSEAT'] = StkSEAT
    raw_dict['StkASS'] = StkASS  
    raw_dict['totalStack'] = int((StkL1+StkL2+StkL3+StkL4)*MPL)+ int(StkSKI2*MPSEAT) + int(StkSEAT*MPSKI)

    print "resumeTime", resumeTime
    print "pauseTime", pauseTime
    print "diffTime", diffTime
    
    return HttpResponse(json.dumps(raw_dict), content_type="application/json")

def getStartUpdate(request):
    global MOL1, MOL2, MOL3, MOL4, MOSKI1, MOSKI2, MOSEAT, MOASS, StkL1, StkL2, StkL3, StkL4, StkSKI1, StkSKI2, StkSEAT, StkASS
    raw_dict = {}
    raw_dict['MOL1'] = MOL1
    raw_dict['MOL2'] = MOL2
    raw_dict['MOL3'] = MOL3
    raw_dict['MOL4'] = MOL4
    raw_dict['MOSKI1'] = MOSKI1
    raw_dict['MOSKI2'] = MOSKI2
    raw_dict['MOSEAT'] = MOSEAT
    raw_dict['MOASS'] = MOASS

    raw_dict['StkL1'] = StkL1
    raw_dict['StkL2'] = StkL2
    raw_dict['StkL3'] = StkL3
    raw_dict['StkL4'] = StkL4
    raw_dict['StkSKI1'] = StkSKI1
    raw_dict['StkSKI2'] = StkSKI2
    raw_dict['StkSEAT'] = StkSEAT
    raw_dict['StkASS'] = StkASS   
    raw_dict['totalStack'] = int((StkL1+StkL2+StkL3+StkL4)*MPL)+ int(StkSKI2*MPSEAT) + int(StkSEAT*MPSKI)

    return HttpResponse(json.dumps(raw_dict), content_type="application/json")

def ProdL1(request):
    global StkL1, Prod1, CL1, TCL1, reload_page, timer, gTime, diffTime,batch_var

    raw_dict = {}
    Prod1 = Prod1 + batch_var
    raw_dict['L1Prod'] = int(Prod1)
    #TCL1 = int((timer[0] * 60 + timer[1] + timer[2] / 100) / (Prod1)) 
      
    print "resumeTime", resumeTime   
    print "pauseTime", pauseTime
    print "diffTime", diffTime    

    

    TCL1 = int(((time.time() -gTime)- diffTime)/(Prod1))

    print TCL1
    raw_dict['L1TC'] = TCL1
   
    CL1 = TCL1 * MOL1 * C
    raw_dict['L1Cost'] = CL1
    StkL1 = StkL1 + batch_var

    seconds= (time.time() -gTime)-diffTime
    m = seconds/ 60
    m= round(m ,2)
    temp=[m, TCL1]
    TDC.append(temp)
    print "TDC", TDC
   
    raw_dict['TP'] = (TCL1+(TCL2*StkL1)+(TCL3*StkL2)+(TCL4*StkL3)+(TCASS*StkL4),"s.")
    raw_dict['minStkL1'] = int(minStkL1)
    raw_dict['maxStkL1'] = int(maxStkL1)
    raw_dict['StkL1'] = int(StkL1)
    raw_dict['MOL1'] = MOL1
    raw_dict['MOL2'] = MOL2
    raw_dict['MOL3'] = MOL3
    raw_dict['MOL4'] = MOL4
    raw_dict['MOSKI1'] = MOSKI1
    raw_dict['MOSKI2'] = MOSKI2
    raw_dict['MOSEAT'] = MOSEAT
    raw_dict['MOASS'] = MOASS
    raw_dict['totalStack'] = int((StkL1+StkL2+StkL3+StkL4)*MPL)+ int(StkSKI2*MPSEAT) + int(StkSEAT*MPSKI)
    seconds=int((time.time() -gTime)- diffTime)
    minutes= round(seconds/60, 2)

    temp=[minutes, TCL1+(TCL2*StkL1)+(TCL3*StkL2)+(TCL4*StkL3)+(TCASS*StkL4)]
    TDP.append(temp);
    temp=[minutes, 55]
    TK.append(temp)

    #StkL1 + StkL2 + StkL3 + SkrL4) x SleighCost + StkSki x Skicost + StkSeat x SeatCost

    return HttpResponse(json.dumps(raw_dict), content_type="application/json")

def ProdL2(request):
    global StkL2, StkL1, Prod2, CL2, TCL2, gTime, diffTime,batch_var
    raw_dict = {}

    #start()
    print "resumeTime", resumeTime   
    print "pauseTime", pauseTime
    print "diffTime", diffTime  

    Prod2 = Prod2 + batch_var
    raw_dict['L2Prod'] = Prod2
    TCL2= int(((time.time() -gTime)-diffTime)/(Prod2))
    raw_dict['L2TC'] = TCL2
    CL2 = TCL2*MOL2*C
    raw_dict['L2Cost'] = CL2
    StkL2 = StkL2 + batch_var
    StkL1 = StkL1 - batch_var

    seconds= (time.time() -gTime)-diffTime
    m = seconds/ 60
    m= round(m ,2)
    temp=[m, TCL2]
    TDC.append(temp)
    print "TDC", TDC

    raw_dict['TP'] = (TCL1+(TCL2*StkL1)+(TCL3*StkL2)+(TCL4*StkL3)+(TCASS*StkL4),"s.")

    raw_dict['Prod2'] = int(Prod2)
    raw_dict['MOL2'] = int(MOL2)
    raw_dict['labL2'] = StkL2
    raw_dict['labL1'] = StkL1
    raw_dict['StkL1'] = StkL1
    raw_dict['StkL2'] = StkL2
    raw_dict['minStkL1'] = minStkL1
    raw_dict['maxStkL1'] = maxStkL1

    raw_dict['minStkL2'] = minStkL2
    raw_dict['maxStkL2'] = maxStkL2

    raw_dict['MOL1'] = MOL1
    raw_dict['MOL2'] = MOL2
    raw_dict['MOL3'] = MOL3
    raw_dict['MOL4'] = MOL4
    raw_dict['MOSKI1'] = MOSKI1
    raw_dict['MOSKI2'] = MOSKI2
    raw_dict['MOSEAT'] = MOSEAT
    raw_dict['MOASS'] = MOASS
    raw_dict['totalStack'] = int((StkL1+StkL2+StkL3+StkL4)*MPL)+ int(StkSKI2*MPSEAT) + int(StkSEAT*MPSKI)

    seconds=(time.time() -gTime)- diffTime
    minutes= round(seconds/60, 2)

    temp=[minutes, TCL1+(TCL2*StkL1)+(TCL3*StkL2)+(TCL4*StkL3)+(TCASS*StkL4)]
    TDP.append(temp);
    temp=[minutes, 55]
    TK.append(temp)

    return HttpResponse(json.dumps(raw_dict), content_type="application/json")

def ProdL3(request):
    global StkL3, StkL2, Prod3, CL3, TCL3, diffTime,batch_var
    raw_dict = {}

    #start()

    Prod3 = Prod3 + batch_var #Increases production of workstation3(WS3). Will be on the mobile app as well
    raw_dict['L3Prod'] = Prod3
    TCL3= int(((time.time() -gTime)-diffTime)/(Prod3)) # Cycle time of WS3 = actual Time / Qty produced at WS3
    raw_dict['L3TC'] = TCL3
    CL3 = TCL3*MOL3*C  # Labor Cost/piece produced WS3 = Cycle time WS3 * nb of employees WS3 * Rate
    raw_dict['L3Cost'] = CL3
    raw_dict['Prod3'] = int(Prod3)
    raw_dict['MOL3'] = int(MOL3)

    seconds= (time.time() -gTime)-diffTime
    m = seconds/ 60
    m= round(m ,2)
    temp=[m, TCL3]
    TDC.append(temp)
    print "TDC", TDC
    temp=[minutes, 55]
    TK.append(temp)

   
    StkL3 = StkL3 + batch_var #increase stock after WS3
    StkL2 = StkL2 - batch_var #reduces stock before WS3

    raw_dict['labL2'] = StkL2
    raw_dict['labL3'] = StkL3

    raw_dict['StkL2'] = StkL2
    raw_dict['StkL3'] = StkL3

    raw_dict['minStkL2'] = minStkL2
    raw_dict['maxStkL2'] = maxStkL2

    raw_dict['minStkL3'] = minStkL3
    raw_dict['maxStkL3'] = maxStkL3

    raw_dict['MOL1'] = MOL1
    raw_dict['MOL2'] = MOL2
    raw_dict['MOL3'] = MOL3
    raw_dict['MOL4'] = MOL4
    raw_dict['MOSKI1'] = MOSKI1
    raw_dict['MOSKI2'] = MOSKI2
    raw_dict['MOSEAT'] = MOSEAT
    raw_dict['MOASS'] = MOASS

    raw_dict['TP'] = (TCL1+(TCL2*StkL1)+(TCL3*StkL2)+(TCL4*StkL3)+(TCASS*StkL4),"s.")
    raw_dict['totalStack'] = int((StkL1+StkL2+StkL3+StkL4)*MPL)+ int(StkSKI2*MPSEAT) + int(StkSEAT*MPSKI)

    seconds=(time.time() -gTime)- diffTime
    minutes= round(seconds/60, 2)

    temp=[minutes, TCL1+(TCL2*StkL1)+(TCL3*StkL2)+(TCL4*StkL3)+(TCASS*StkL4)]
    TDP.append(temp);
    temp=[minutes, 55]
    TK.append(temp)

    return HttpResponse(json.dumps(raw_dict), content_type="application/json")

def ProdL4(request):
    global StkL4, StkL3, Prod4, CL4, TCL4, MOL4, diffTime,batch_var
    raw_dict = {}

    #start()

    Prod4 = Prod4 + batch_var #Increases production of workstation3(WS3). Will be on the mobile app as well
    raw_dict['L4Prod'] = Prod4
    TCL4= int(((time.time() -gTime)-diffTime)/(Prod4)) # Cycle time of WS3 = actual Time / Qty produced at WS3
    raw_dict['L4TC'] = TCL4
    CL4 = TCL4*MOL4*C  # Labor Cost/piece produced WS3 = Cycle time WS3 * nb of employees WS3 * Rate
    raw_dict['L4Cost'] = CL4
    StkL4 = StkL4 + batch_var #increase stock after WS3
    StkL3 = StkL3 - batch_var #reduces stock before WS3


    seconds= (time.time() -gTime)-diffTime
    m = seconds/ 60
    m= round(m ,2)
    temp=[m, TCL4]
    TDC.append(temp)
    temp=[minutes, 55]
    TK.append(temp)
    print "TDC", TDC


    raw_dict['StkL4'] = StkL4
    raw_dict['StkL3'] = StkL3

    raw_dict['StkSKI2'] = StkSKI2
    raw_dict['StkSEAT'] = StkSEAT


    raw_dict['minStkL4'] = minStkL4
    raw_dict['maxStkL4'] = maxStkL4

    raw_dict['minStkL3'] = minStkL3
    raw_dict['maxStkL3'] = maxStkL3
    raw_dict['MOL1'] = MOL1
    raw_dict['MOL2'] = MOL2
    raw_dict['MOL3'] = MOL3
    raw_dict['MOL4'] = MOL4
    raw_dict['MOSKI1'] = MOSKI1
    raw_dict['MOSKI2'] = MOSKI2
    raw_dict['MOSEAT'] = MOSEAT
    raw_dict['MOASS'] = MOASS
    raw_dict['TP'] = (TCL1+(TCL2*StkL1)+(TCL3*StkL2)+(TCL4*StkL3)+(TCASS*StkL4),"s.")
    #Turns the stock label to green if stock greater than the max qty or smaller than the min qty
    raw_dict['totalStack'] = int((StkL1+StkL2+StkL3+StkL4)*MPL)+ int(StkSKI2*MPSEAT) + int(StkSEAT*MPSKI)

    seconds=(time.time() -gTime)- diffTime
    minutes= round(seconds/60, 2)

    temp=[minutes, TCL1+(TCL2*StkL1)+(TCL3*StkL2)+(TCL4*StkL3)+(TCASS*StkL4)]
    TDP.append(temp);
    temp=[minutes, 55]
    TK.append(temp)

    return HttpResponse(json.dumps(raw_dict), content_type="application/json")

def fProdASS(request):
    global StkASS, StkL4,ProdASS,CASS,CA,COUT,REV2, TCASS,StkSKI2,StkSEAT, diffTime,batch_var, TCL1, TCL2, TCL3, TCL4
    raw_dict = {}

    #start()
    # if Prod1:
    #     TCL1= int(((time.time() -gTime)-diffTime)/(Prod1))

    # if Prod2:
    #     TCL2= int(((time.time() -gTime)-diffTime)/(Prod2))

    # if Prod3:
    #     TCL3= int(((time.time() -gTime)-diffTime)/(Prod3))

    # if Prod4:    
    #     TCL4= int(((time.time() -gTime)-diffTime)/(Prod4))
    
    ProdASS = ProdASS + batch_var
    raw_dict['ASSProd'] = ProdASS
    TCASS= int(((time.time() -gTime)-diffTime)/(ProdASS)) # Cycle time of WS3 = actual Time / Qty produced at WS3
    seconds= (time.time() -gTime)-diffTime
    m = seconds/ 60
    m= round(m ,2)
    temp=[m, TCASS]
    TDC.append(temp)
    print "TDC", TDC

    temp=[m, ProdASS]
    P.append(temp)
  
    raw_dict['TCASS'] = TCASS
    raw_dict['timestamp'] = TCASS
    CASS = TCASS*MOASS*C
    raw_dict['ASSCost'] = CASS
    StkASS = StkASS + batch_var
    StkL4 = StkL4 - batch_var
    StkSKI2 = StkSKI2 - batch_var
    StkSEAT = StkSEAT - batch_var
    raw_dict['StkL4'] = StkL4
    raw_dict['StkSKI2'] = StkSKI2
    raw_dict['StkSEAT'] = StkSEAT
    raw_dict['StkASS'] = StkASS

    raw_dict['TP'] = (TCL1+(TCL2*StkL1)+(TCL3*StkL2)+(TCL4*StkL3)+(TCASS*StkL4))
    CA = CA + sale #Total sales = Total Sales + New sale (here we use 10000euros for each sale)
    raw_dict['CA'] = CA
    COUT =  (MPL*(StkL1+StkL2+StkL3+StkL4+StkASS))+ MPSKI*(StkSKI1+StkSKI2) + MPSEAT * StkSEAT + C * (MOL1+MOL2+MOL3+MOL4+MOASS+MOSKI1+MOSKI2+MOSEAT)*((int(time.time() -gTime )-diffTime)) + CNC #Total cost = Cost of raw material(here 100euros)*total stock in the system + Rate*totalnumber of employees * time in seconds
    raw_dict['COUT'] = round(COUT, 2)
    REV2 = int((CA-COUT)/ProdASS) #Revenu/piece = (total sales-Total cost)/Production of last workstation
    raw_dict['REV2'] = REV2

    raw_dict['MOL1'] = MOL1
    raw_dict['MOL2'] = MOL2
    raw_dict['MOL3'] = MOL3
    raw_dict['MOL4'] = MOL4
    raw_dict['MOSKI1'] = MOSKI1
    raw_dict['MOSKI2'] = MOSKI2
    raw_dict['MOSEAT'] = MOSEAT
    raw_dict['MOASS'] = MOASS
    raw_dict['totalStack'] = int((StkL1+StkL2+StkL3+StkL4)*MPL)+ int(StkSKI2*MPSEAT) + int(StkSEAT*MPSKI)

    seconds=(time.time() -gTime)- diffTime
    minutes= round(seconds/60, 2)

    temp=[minutes, TCL1+(TCL2*StkL1)+(TCL3*StkL2)+(TCL4*StkL3)+(TCASS*StkL4)]
    TDP.append(temp);
    temp=[minutes, REV2]
    UI.append(temp)
    temp=[minutes, 55]
    TK.append(temp)

    return HttpResponse(json.dumps(raw_dict), content_type="application/json")



def fProdSKI1(request):
    global StkSKI1,ProdSKI1,CSKI1, TCSKI1,batch_var

    #start()

    raw_dict = {}
    ProdSKI1 = ProdSKI1 + batch_var
    TCSKI1= int(((time.time() -gTime)-diffTime)/(ProdSKI1))
    # SKI1TC.configure(text=(TCSKI1,"s."))
    raw_dict['ProdSKI1'] = ProdSKI1
    raw_dict['SKI1TC'] = TCSKI1
    CSKI1 = TCSKI1*MOSKI1*C
    StkSKI1 = StkSKI1 + batch_var

   
    raw_dict['CSKI1'] = CSKI1
    raw_dict['StkSKI1'] = StkSKI1

    raw_dict['minStkSKI1'] = minStkSKI1
    raw_dict['maxStkSKI1'] = maxStkSKI1

    raw_dict['MOL1'] = MOL1
    raw_dict['MOL2'] = MOL2
    raw_dict['MOL3'] = MOL3
    raw_dict['MOL4'] = MOL4
    raw_dict['MOSKI1'] = MOSKI1
    raw_dict['MOSKI2'] = MOSKI2
    raw_dict['MOSEAT'] = MOSEAT
    raw_dict['MOASS'] = MOASS
    raw_dict['totalStack'] = int((StkL1+StkL2+StkL3+StkL4)*MPL)+ int(StkSKI2*MPSEAT) + int(StkSEAT*MPSKI)

    return HttpResponse(json.dumps(raw_dict), content_type="application/json")

def fProdSKI2(request):
    global StkSKI1,StkSKI2,ProdSKI2,CSKI2, TCSKI2, diffTime,batch_var
    #start()

    raw_dict = {}
    ProdSKI2 = ProdSKI2 + batch_var
    TCSKI2= int(((time.time() -gTime)-diffTime)/(ProdSKI2))
    raw_dict['SKI2TC'] = TCSKI2
    raw_dict['ProdSKI2'] = ProdSKI2
    # SKI2TC.configure(text=(TCSKI2,"s."))

   
    CSKI2 = TCSKI2*MOSKI2*C
    StkSKI2 = StkSKI2 + batch_var
    StkSKI1 = StkSKI1 - batch_var

    raw_dict['CSKI2'] = CSKI2
    raw_dict['StkSKI1'] = StkSKI1
    raw_dict['StkSKI2'] = StkSKI2

    raw_dict['StkL4'] = StkL4
    raw_dict['StkSEAT'] = StkSEAT

    raw_dict['minStkSKI2'] = minStkSKI2
    raw_dict['maxStkSKI2'] = maxStkSKI2

    raw_dict['minStkSKI1'] = minStkSKI1
    raw_dict['maxStkSKI1'] = maxStkSKI1

    raw_dict['MOL1'] = MOL1
    raw_dict['MOL2'] = MOL2
    raw_dict['MOL3'] = MOL3
    raw_dict['MOL4'] = MOL4
    raw_dict['MOSKI1'] = MOSKI1
    raw_dict['MOSKI2'] = MOSKI2
    raw_dict['MOSEAT'] = MOSEAT
    raw_dict['MOASS'] = MOASS
    raw_dict['totalStack'] = int((StkL1+StkL2+StkL3+StkL4)*MPL)+ int(StkSKI2*MPSEAT) + int(StkSEAT*MPSKI)

    return HttpResponse(json.dumps(raw_dict), content_type="application/json")

def fProdSEAT(request):
    global StkSEAT,ProdSEAT,CSEAT, TCSEAT, diffTime,batch_var

    #start()
    raw_dict = {}
    ProdSEAT = ProdSEAT + batch_var
    TCSEAT= int(((time.time() -gTime)-diffTime)/(ProdSEAT))
    raw_dict['SEATTC'] = TCSEAT
    raw_dict['ProdSEAT'] = ProdSEAT
    CSEAT = TCSEAT*MOSEAT*C
    StkSEAT = StkSEAT + batch_var

  
    raw_dict['CSEAT'] = CSEAT
    raw_dict['StkSEAT'] = StkSEAT

    raw_dict['StkL4'] = StkL4
    raw_dict['StkSKI2'] = StkSKI2

    raw_dict['minStkSEAT'] = minStkSEAT
    raw_dict['maxStkSEAT'] = maxStkSEAT

    raw_dict['MOL1'] = MOL1
    raw_dict['MOL2'] = MOL2
    raw_dict['MOL3'] = MOL3
    raw_dict['MOL4'] = MOL4
    raw_dict['MOSKI1'] = MOSKI1
    raw_dict['MOSKI2'] = MOSKI2
    raw_dict['MOSEAT'] = MOSEAT
    raw_dict['MOASS'] = MOASS
    raw_dict['totalStack'] = int((StkL1+StkL2+StkL3+StkL4)*MPL)+ int(StkSKI2*MPSEAT) + int(StkSEAT*MPSKI)

    return HttpResponse(json.dumps(raw_dict), content_type="application/json")

def NC1(request):
    global NCL1,CNC,Prod1

    raw_dict = {}
    NCL1 = NCL1 + 1  #Increases the qty of Non-conformities for WS1 (button will be on mobile app as well)
    CNC = CNC + (MPL + CL1) #Total Cost of Non-conformity(in main dashboard) = Total Cost of non-conformity + (Raw material cost + Labor Cost/piece WS1)
    Prod1 = Prod1-1 #Reduces production for WS1
    raw_dict['L1Prod'] = Prod1
    raw_dict['L1NC'] = NCL1
    raw_dict['totNC'] = NCL1 + NCL2 + NCL3 + NCL4 + NCSKI1 + NCSKI2 + NCSEAT + NCASS
    raw_dict['CostNC'] = CNC
    raw_dict['MOL1'] = MOL1
    raw_dict['MOL2'] = MOL2
    raw_dict['MOL3'] = MOL3
    raw_dict['MOL4'] = MOL4
    raw_dict['MOSKI1'] = MOSKI1
    raw_dict['MOSKI2'] = MOSKI2
    raw_dict['MOSEAT'] = MOSEAT
    raw_dict['MOASS'] = MOASS
    raw_dict['totalStack'] = int((StkL1+StkL2+StkL3+StkL4)*MPL)+ int(StkSKI2*MPSEAT) + int(StkSEAT*MPSKI)

    return HttpResponse(json.dumps(raw_dict), content_type="application/json")

def NC2(request):
    global NCL2, CNC,Prod2
    raw_dict = {}
    NCL2 = NCL2 + 1
    CNC = CNC + (MPL + CL1+CL2)
    Prod2 = Prod2-1

    raw_dict['L2Prod'] = Prod2
    raw_dict['L2NC'] = NCL2
    raw_dict['totNC'] = NCL1 + NCL2 + NCL3 + NCL4 + NCSKI1 + NCSKI2 + NCSEAT + NCASS
    raw_dict['CostNC'] = CNC
    raw_dict['MOL1'] = MOL1
    raw_dict['MOL2'] = MOL2
    raw_dict['MOL3'] = MOL3
    raw_dict['MOL4'] = MOL4
    raw_dict['MOSKI1'] = MOSKI1
    raw_dict['MOSKI2'] = MOSKI2
    raw_dict['MOSEAT'] = MOSEAT
    raw_dict['MOASS'] = MOASS
    raw_dict['totalStack'] = int((StkL1+StkL2+StkL3+StkL4)*MPL)+ int(StkSKI2*MPSEAT) + int(StkSEAT*MPSKI)

    return HttpResponse(json.dumps(raw_dict), content_type="application/json")

def NC3(request):
    global NCL3, CNC,Prod3
    raw_dict = {}
    NCL3 = NCL3 + 1
    CNC = CNC + (MPL + CL1 + CL2 + CL3)
    Prod3 = Prod3 - 1

    raw_dict['L3Prod'] = Prod3
    raw_dict['L3NC'] = NCL3
    raw_dict['totNC'] = NCL1 + NCL2 + NCL3 + NCL4 + NCSKI1 + NCSKI2 + NCSEAT + NCASS
    raw_dict['CostNC'] = CNC
    raw_dict['MOL1'] = MOL1
    raw_dict['MOL2'] = MOL2
    raw_dict['MOL3'] = MOL3
    raw_dict['MOL4'] = MOL4
    raw_dict['MOSKI1'] = MOSKI1
    raw_dict['MOSKI2'] = MOSKI2
    raw_dict['MOSEAT'] = MOSEAT
    raw_dict['MOASS'] = MOASS
    raw_dict['totalStack'] = int((StkL1+StkL2+StkL3+StkL4)*MPL)+ int(StkSKI2*MPSEAT) + int(StkSEAT*MPSKI)

    return HttpResponse(json.dumps(raw_dict), content_type="application/json")

def NC4(request):
    global NCL4, CNC,Prod4
    raw_dict = {}
    NCL4 = NCL4 + 1
    CNC = CNC + (MPL + CL1+CL2 +CL3 + CL4)
    Prod4 = Prod4-1

    raw_dict['L4Prod'] = Prod4
    raw_dict['L4NC'] = NCL4
    raw_dict['totNC'] = NCL1 + NCL2 + NCL3 + NCL4 + NCSKI1 + NCSKI2 + NCSEAT + NCASS
    raw_dict['CostNC'] = CNC
    raw_dict['MOL1'] = MOL1
    raw_dict['MOL2'] = MOL2
    raw_dict['MOL3'] = MOL3
    raw_dict['MOL4'] = MOL4
    raw_dict['MOSKI1'] = MOSKI1
    raw_dict['MOSKI2'] = MOSKI2
    raw_dict['MOSEAT'] = MOSEAT
    raw_dict['MOASS'] = MOASS
    raw_dict['totalStack'] = int((StkL1+StkL2+StkL3+StkL4)*MPL)+ int(StkSKI2*MPSEAT) + int(StkSEAT*MPSKI)

    return HttpResponse(json.dumps(raw_dict), content_type="application/json")

def fNCSKI1(request):
    global NCSKI1, CNC,ProdSKI1
    raw_dict = {}
    NCSKI1 = NCSKI1 + 1
    CNC = CNC + (MPSKI + CSKI1)
    ProdSKI1 = ProdSKI1 - 1

    raw_dict['SKI1Prod'] = ProdSKI1
    raw_dict['SKI1NC'] = NCSKI1
    raw_dict['totNC'] = NCL1 + NCL2 + NCL3 + NCL4 + NCSKI1 + NCSKI2 + NCSEAT + NCASS
    raw_dict['CostNC'] = CNC
    raw_dict['MOL1'] = MOL1
    raw_dict['MOL2'] = MOL2
    raw_dict['MOL3'] = MOL3
    raw_dict['MOL4'] = MOL4
    raw_dict['MOSKI1'] = MOSKI1
    raw_dict['MOSKI2'] = MOSKI2
    raw_dict['MOSEAT'] = MOSEAT
    raw_dict['MOASS'] = MOASS
    raw_dict['totalStack'] = int((StkL1+StkL2+StkL3+StkL4)*MPL)+ int(StkSKI2*MPSEAT) + int(StkSEAT*MPSKI)

    return HttpResponse(json.dumps(raw_dict), content_type="application/json")

def fNCSKI2(request):
    global NCSKI2, CNC,ProdSKI2
    raw_dict = {}
    NCSKI2 = NCSKI2 + 1
    CNC = CNC + (MPSKI + CSKI1 + CSKI2)
    ProdSKI2 = ProdSKI2 - 1

    raw_dict['SKI2Prod'] = ProdSKI2
    raw_dict['SKI2NC'] = NCSKI2
    raw_dict['totNC'] = NCL1 + NCL2 + NCL3 + NCL4 + NCSKI1 + NCSKI2 + NCSEAT + NCASS
    raw_dict['CostNC'] = CNC
    raw_dict['MOL1'] = MOL1
    raw_dict['MOL2'] = MOL2
    raw_dict['MOL3'] = MOL3
    raw_dict['MOL4'] = MOL4
    raw_dict['MOSKI1'] = MOSKI1
    raw_dict['MOSKI2'] = MOSKI2
    raw_dict['MOSEAT'] = MOSEAT
    raw_dict['MOASS'] = MOASS
    raw_dict['totalStack'] = int((StkL1+StkL2+StkL3+StkL4)*MPL)+ int(StkSKI2*MPSEAT) + int(StkSEAT*MPSKI)

    return HttpResponse(json.dumps(raw_dict), content_type="application/json")

def fNCSEAT(request):
    global NCSEAT, CNC,ProdSEAT
    raw_dict = {}
    NCSEAT = NCSEAT + 1
    CNC = CNC + (MPSEAT + CSEAT)
    ProdSEAT = ProdSEAT - 1

    raw_dict['SEATProd'] = ProdSEAT
    raw_dict['SEATNC'] = NCSEAT
    raw_dict['totNC'] = NCL1 + NCL2 + NCL3 + NCL4 + NCSKI1 + NCSKI2 + NCSEAT + NCASS
    raw_dict['CostNC'] = CNC
    raw_dict['MOL1'] = MOL1
    raw_dict['MOL2'] = MOL2
    raw_dict['MOL3'] = MOL3
    raw_dict['MOL4'] = MOL4
    raw_dict['MOSKI1'] = MOSKI1
    raw_dict['MOSKI2'] = MOSKI2
    raw_dict['MOSEAT'] = MOSEAT
    raw_dict['MOASS'] = MOASS
    raw_dict['totalStack'] = int((StkL1+StkL2+StkL3+StkL4)*MPL)+ int(StkSKI2*MPSEAT) + int(StkSEAT*MPSKI)

    return HttpResponse(json.dumps(raw_dict), content_type="application/json")

def fNCASS(request):
    global NCASS, CNC,ProdASS
    raw_dict = {}
    NCASS = NCASS + 1
    CNC = CNC + (MPL + CL1+CL2 +CL3 + CL4) + (MPSEAT + CSEAT) + (MPSKI + CSKI1 + CSKI2)
    ProdASS = ProdASS-1

    raw_dict['ASSProd'] = ProdASS
    raw_dict['ASSNC'] = NCASS
    raw_dict['totNC'] = NCL1 + NCL2 + NCL3 + NCL4 + NCSKI1 + NCSKI2 + NCSEAT + NCASS
    raw_dict['CostNC'] = CNC
    raw_dict['MOL1'] = MOL1
    raw_dict['MOL2'] = MOL2
    raw_dict['MOL3'] = MOL3
    raw_dict['MOL4'] = MOL4
    raw_dict['MOSKI1'] = MOSKI1
    raw_dict['MOSKI2'] = MOSKI2
    raw_dict['MOSEAT'] = MOSEAT
    raw_dict['MOASS'] = MOASS
    raw_dict['totalStack'] = int((StkL1+StkL2+StkL3+StkL4)*MPL)+ int(StkSKI2*MPSEAT) + int(StkSEAT*MPSKI)

    return HttpResponse(json.dumps(raw_dict), content_type="application/json")


def init_data(request):
    raw_dict = update_timeText()

    return HttpResponse(raw_dict, content_type="application/json")

def resume_job(request):
    global resumeTime, pauseTime, diffTime
    print "resumeTime", resumeTime
    resumeTime= time.time()
    diffTime += resumeTime -pauseTime
    print "diffTime", diffTime

    raw_dict={}  
    raw_dict['MOL1'] = MOL1
    raw_dict['MOL2'] = MOL2
    raw_dict['MOL3'] = MOL3
    raw_dict['MOL4'] = MOL4
    raw_dict['MOSKI1'] = MOSKI1
    raw_dict['MOSKI2'] = MOSKI2
    raw_dict['MOSEAT'] = MOSEAT
    raw_dict['MOASS'] = MOASS
    raw_dict['totalStack'] = int((StkL1+StkL2+StkL3+StkL4)*MPL)+ int(StkSKI2*MPSEAT) + int(StkSEAT*MPSKI)

    return HttpResponse(json.dumps(raw_dict), content_type="application/json")   

def pause_job(request):
    global pauseTime, diffTime, resumeTime  
    pauseTime = time.time()    
    print "pauseTime", pauseTime
    print "diffTime", diffTime
    raw_dict={}    
     
    return HttpResponse(raw_dict, content_type="application/json")       

def start_job(request):
    global gTime
    raw_dict={}
    gTime=time.time()

    raw_dict['MOL1'] = MOL1
    raw_dict['MOL2'] = MOL2
    raw_dict['MOL3'] = MOL3
    raw_dict['MOL4'] = MOL4
    raw_dict['MOSKI1'] = MOSKI1
    raw_dict['MOSKI2'] = MOSKI2
    raw_dict['MOSEAT'] = MOSEAT
    raw_dict['MOASS'] = MOASS
    raw_dict['totalStack'] = int((StkL1+StkL2+StkL3+StkL4)*MPL)+ int(StkSKI2*MPSEAT) + int(StkSEAT*MPSKI)

    return HttpResponse(raw_dict, content_type="application/json")  

def stop_job(request):
    raw_dict={}
   
    return HttpResponse(raw_dict, content_type="application/json")             

#timer
# Our time structure [min, sec, centsec]
#timer = [0, 0, 0]
# The format is padding all the
def setting(request):
    return render(request, "setting.html")

def get_data(request):
    global MOL1, MOL2, MOL3, MOL4, MOSKI1, MOSKI2, MOSEAT, MOASS, StkL1, StkL2, StkL3, StkL4, StkSKI1, StkSKI2, StkSEAT, StkASS, minStkL1, minStkL2, minStkL3, minStkL4, minStkSKI1, minStkSKI2, minStkSEAT, maxStkL1, maxStkL2, maxStkL3, maxStkL4, maxStkSKI1, maxStkSKI2, maxStkSEAT
    raw_dict = {}
    raw_dict['MOL1'] = MOL1
    raw_dict['MOL2'] = MOL2
    raw_dict['MOL3'] = MOL3
    raw_dict['MOL4'] = MOL4
    raw_dict['MOSKI1'] = MOSKI1
    raw_dict['MOSKI2'] = MOSKI2
    raw_dict['MOSEAT'] = MOSEAT
    raw_dict['MOASS'] = MOASS

    raw_dict['StkL1'] = StkL1
    raw_dict['StkL2'] = StkL2
    raw_dict['StkL3'] = StkL3
    raw_dict['StkL4'] = StkL4
    raw_dict['StkSKI1'] = StkSKI1
    raw_dict['StkSKI2'] = StkSKI2
    raw_dict['StkSEAT'] = StkSEAT
    raw_dict['StkASS'] = StkASS

    raw_dict['minStkL1'] = minStkL1
    raw_dict['minStkL2'] = minStkL2
    raw_dict['minStkL3'] = minStkL3
    raw_dict['minStkL4'] = minStkL4
    raw_dict['minStkSKI1'] = minStkSKI1
    raw_dict['minStkSKI2'] = minStkSKI2
    raw_dict['minStkSEAT'] = minStkSEAT

    raw_dict['maxStkL1'] = maxStkL1
    raw_dict['maxStkL2'] = maxStkL2
    raw_dict['maxStkL3'] = maxStkL3
    raw_dict['maxStkL4'] = maxStkL4
    raw_dict['maxStkSKI1'] = maxStkSKI1
    raw_dict['maxStkSKI2'] = maxStkSKI2
    raw_dict['maxStkSEAT'] = maxStkSEAT
    raw_dict['totalStack'] = int((StkL1+StkL2+StkL3+StkL4)*MPL)+ int(StkSKI2*MPSEAT) + int(StkSEAT*MPSKI)

    return HttpResponse(json.dumps(raw_dict), content_type="application/json")

def update_data(request):
    global MOL1, MOL2, MOL3, MOL4, MOSKI1, MOSKI2, MOSEAT, MOASS, StkL1, StkL2, StkL3, StkL4, StkSKI1, StkSKI2, StkSEAT, StkASS, minStkL1, minStkL2, minStkL3, minStkL4, minStkSKI1, minStkSKI2, minStkSEAT, maxStkL1, maxStkL2, maxStkL3, maxStkL4, maxStkSKI1, maxStkSKI2, maxStkSEAT, batch_var
    variable_name = request.POST.get('name')
    variable_value = int(request.POST.get('value'))
    
    if(variable_name == 'MOL1'):
        MOL1 = variable_value
    if(variable_name == 'MOL2'):
        MOL2 = variable_value
    if(variable_name == 'MOL3'):
        MOL3 = variable_value
    if(variable_name == 'MOL4'):
        MOL4 = variable_value
    if(variable_name == 'MOSKI1'):
        MOSKI1 = variable_value
    if(variable_name == 'MOSKI2'):
        MOSKI2 = variable_value
    if(variable_name == 'MOSEAT'):
        MOSEAT = variable_value
    if(variable_name == 'MOASS'):
        MOASS = variable_value

    if(variable_name == 'StkL1'):
        StkL1 = variable_value
    if(variable_name == 'StkL2'):
        StkL2 = variable_value
    if(variable_name == 'StkL3'):
        StkL3 = variable_value
    if(variable_name == 'StkL4'):
        StkL4 = variable_value
    if(variable_name == 'StkSKI1'):
        StkSKI1 = variable_value
    if(variable_name == 'StkSKI2'):
        StkSKI2 = variable_value
    if(variable_name == 'StkSEAT'):
        StkSEAT = variable_value
    if(variable_name == 'StkASS'):
        StkASS = variable_value

    if(variable_name == 'minStkL1'):
        minStkL1 = variable_value
    if(variable_name == 'minStkL2'):
        minStkL2 = variable_value
    if(variable_name == 'minStkL3'):
        minStkL3 = variable_value
    if(variable_name == 'minStkL4'):
        minStkL4 = variable_value
    if(variable_name == 'minStkSKI1'):
        minStkSKI1 = variable_value
    if(variable_name == 'minStkSKI2'):
        minStkSKI2 = variable_value
    if(variable_name == 'minStkSEAT'):
        minStkSEAT = variable_value
    
    if(variable_name == 'maxStkL1'):
        maxStkL1 = variable_value
    if(variable_name == 'maxStkL2'):
        maxStkL2 = variable_value
    if(variable_name == 'maxStkL3'):
        maxStkL3 = variable_value
    if(variable_name == 'maxStkL4'):
        maxStkL4 = variable_value
    if(variable_name == 'maxStkSKI1'):
        maxStkSKI1 = variable_value
    if(variable_name == 'maxStkSKI2'):
        maxStkSKI2 = variable_value
    if(variable_name == 'maxStkSEAT'):
        maxStkSEAT = variable_value
    if(variable_name == 'batchvar'):
        batch_var = variable_value    

    return HttpResponse(content_type="application/json")



def charts(request):
    
    return render(request, "charts.html")

def temps_de_cycle(request):
    global TDC, TK
    raw_dict = {}
    raw_dict['temps'] = TDC
    raw_dict['takt'] = TK
       
    return HttpResponse(json.dumps(raw_dict), content_type="application/json")

def temps_de_passage(request):

    raw_dict = {}
    raw_dict['TDP'] = TDP
    raw_dict['TK'] = TK
    print TDP

    return HttpResponse(json.dumps(raw_dict), content_type="application/json")


def production_graph(request):

    raw_dict = {}
    raw_dict['P'] = P
    print P

    return HttpResponse(json.dumps(raw_dict), content_type="application/json")    

def unitIncome_graph(request):

    raw_dict = {}
    raw_dict['UI'] = UI
    print UI

    return HttpResponse(json.dumps(raw_dict), content_type="application/json")        