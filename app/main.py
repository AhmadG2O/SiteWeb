from flask import Flask
from flask import render_template
from flask import request
import sqlite3
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
app = Flask(__name__)

@app.route("/") 
def index():
    return render_template('accueil.html')

@app.route('/patient', methods=['POST'])
def patient():
    L=[]
    X=[]
    i=0
    Prenom=request.form['Prenom']
    Pin=request.form['Pin']
    with sqlite3.connect("etudiant.db") as con:
        cur = con.cursor()
        #cur.execute("CREATE TABLE IF NOT EXISTS users(ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,Nom TEXT,Pin TEXT)")
        #cur.execute("INSERT INTO users(Nom, Pin) VALUES(?, ?)", (Nom, Pin))
        
        cur.execute("SELECT Prenom FROM users")
        con.commit()
        utilisateurs = cur.fetchall()
        for users in utilisateurs:
             L.append(utilisateurs[i][0])
             i=i+1
        taille=len(L)
        
        cur.execute("SELECT Pin FROM users")
        con.commit()
        mdp = cur.fetchall()
        
        i=0
        cur.execute("SELECT * FROM users")
        con.commit()
        donnees = cur.fetchall()
        j=0
        for i in range (len(donnees)):
            for donnee in donnees[i]:
                X.append(donnees[i][j])
                j+=j
        i=0
        j=0
        long=int(len(X)/len(donnees))
        for i in range (len(donnees)):
            for j in range (long):
                if donnees[i][j]==Prenom:
                    Nom=(donnees[i][j+1])
                    Age=(donnees[i][j+2])
                    Sexe=(donnees[i][j+3])
                    Adresse=(donnees[i][j+4])
                    Code_Postal=(donnees[i][j+5])
                    Ville=(donnees[i][j+6])
                    Adresse_Mail=(donnees[i][j+7])
                    Num_tel=(donnees[i][j+8])
                    Num_SS=(donnees[i][j+9])
                    leuco=(donnees[i][j+11])
                    hemati=(donnees[i][j+12])
                    hemo=(donnees[i][j+13])
                    hemato=(donnees[i][j+14])
                    vgm=(donnees[i][j+15])
                    ccmh=(donnees[i][j+16]) 
                    tcmh=(donnees[i][j+17])
                    rdw=(donnees[i][j+18])
                    polynp=(donnees[i][j+19])
                    polyep=(donnees[i][j+20])
                    polybp=(donnees[i][j+21])
                    lympp=(donnees[i][j+22])
                    monop=(donnees[i][j+23])
                    polyn=(donnees[i][j+24])
                    polye=(donnees[i][j+25])
                    polyb=(donnees[i][j+26])
                    lymp=(donnees[i][j+27])
                    mono=(donnees[i][j+28])
                    numplaq=(donnees[i][j+29])
                    gly=(donnees[i][j+30])
                    glym=(donnees[i][j+31])
                    crea=(donnees[i][j+32])
                    creat=(donnees[i][j+33])
                    mdrd=(donnees[i][j+34])
                    ckd=(donnees[i][j+35])
                    aspect=(donnees[i][j+36]) 
                    chotot=(donnees[i][j+37])
                    chotott=(donnees[i][j+38])
                    chohdl=(donnees[i][j+39])
                    chohdll=(donnees[i][j+40])
                    ccholdl=(donnees[i][j+41])
                    cchodll=(donnees[i][j+42])
                    triglyc=(donnees[i][j+43])
                    triglyce=(donnees[i][j+44])
                    asat=(donnees[i][j+45])
                    alat=(donnees[i][j+46])
                    gamglu=(donnees[i][j+47])
                    phospha=(donnees[i][j+48])
                    TSH=(donnees[i][j+49])
                    VIH=(donnees[i][j+50])
                    SCO=(donnees[i][j+51])
                    ACHB=(donnees[i][j+52])
                    EVS=(donnees[i][j+53])
                    font = "Helvetica"
                    font_size = 26
                    text = "Hemogramme"
                    x = 5.4 * inch
                    y = 11.0 * inch
                    destination_file = "first.pdf"
                    my_canvas = canvas.Canvas(destination_file)
                    my_canvas.setFont(font, font_size)
                    my_canvas.drawRightString(x, y, text)
                        
                        
                    text1="NUMERATION GLOBULAIRE"
                    my_canvas.drawRightString(5.0*inch, 10.5*inch, text1)
                    my_canvas.setFont(font, font_size)
                        
                     
                    my_canvas.drawRightString(3.5*inch, 10.0*inch, "Leucocytes:"+leuco)
                    my_canvas.setFont(font, font_size)
                    
                    my_canvas.drawRightString(3.5*inch, 9.5*inch, "Hématies:"+hemati)
                    my_canvas.setFont(font, font_size)
                        
                    my_canvas.drawRightString(3.5*inch, 9.0*inch, "Hémoglobine:"+hemo)
                    my_canvas.setFont(font, font_size)
                        
                    my_canvas.drawRightString(3.5*inch, 8.5*inch, "Hématocrite:"+hemato)
                    my_canvas.setFont(font, font_size)
                        
                    my_canvas.drawRightString(3.5*inch, 8.0*inch, "V.G.M.:"+vgm)
                    my_canvas.setFont(font, font_size)
                        
                    my_canvas.drawRightString(3.5*inch, 7.5*inch, "C.C.M.H.:"+ccmh)
                    my_canvas.setFont(font, font_size)
                        
                    my_canvas.drawRightString(3.5*inch, 7.0*inch, "T.C.M.H.:"+tcmh)
                    my_canvas.setFont(font, font_size)
                        
                    my_canvas.drawRightString(3.5*inch, 6.5*inch, "R.D.W.:"+rdw)
                    my_canvas.setFont(font, font_size)
                        
                    text2="FORMULE SANGUINE"
                    my_canvas.drawRightString(4.0*inch, 6.0*inch, text2)
                    my_canvas.setFont(font, font_size)
                        
                    my_canvas.drawRightString(5.5*inch, 5.5*inch, "Polynucléaires neutrophiles:"+polyn)
                    my_canvas.setFont(font, font_size)
                        
                    my_canvas.drawRightString(5.5*inch, 5.0*inch, "Polynucléaires éosinophiles:"+polye)
                    my_canvas.setFont(font, font_size)
                        
                    my_canvas.drawRightString(5.5*inch, 4.5*inch, "Polynucléaires basophiles:"+polyb)
                    my_canvas.setFont(font, font_size)
                        
                    my_canvas.drawRightString(3.5*inch, 4.0*inch, "Lymphocytes:"+lymp)
                    my_canvas.setFont(font, font_size)
                        
                    my_canvas.drawRightString(3.5*inch, 3.5*inch," Monocytes:"+mono)
                    my_canvas.setFont(font, font_size)
                        
                    text3="NUMERATION DES PLAQUETTES"
                    my_canvas.drawRightString(6.0*inch, 3.0*inch, text3)
                    my_canvas.setFont(font, font_size)
                        
                    my_canvas.drawRightString(5.5*inch, 2.5*inch, "Numération des plaquettes:"+numplaq)
                    my_canvas.setFont(font, font_size)
            
                    my_canvas.save()
                    break;
                    
        i=0
        for i in range (taille):
            if Prenom=="Admin" and Pin=="Administration":
                texte=render_template('rendu_2.html',Prenom="Admin")
                break;
            else:
                if utilisateurs[i][0]==Prenom and mdp[i][0]==Pin:
                    texte=render_template('rendu_1.html',Prenom=Prenom,Nom=Nom, Age=Age, Sexe=Sexe, Adresse=Adresse, Code_Postal=Code_Postal, Ville=Ville,Adresse_Mail=Adresse_Mail, Num_tel=Num_tel, Num_SS=Num_SS, leuco=leuco,hemati=hemati,hemo=hemo,
                hemato=hemato, vgm=vgm, ccmh=ccmh,tcmh=tcmh,rdw=rdw,polynp=polynp, polyep=polyep,
                polybp=polybp,lympp=lympp, monop=monop, polyn=polyn, polye=polye, polyb=polyb,
                lymp=lymp,mono=mono, numplaq=numplaq,
                gly=gly,glym=glym,crea=crea,creat=creat,mdrd=mdrd,ckd=ckd,aspect=aspect, chotot=chotot, 
                chotott=chotott,chohdl=chohdl,chohdll=chohdll,ccholdl=ccholdl,cchodll=cchodll,
                triglyc=triglyc,triglyce=triglyce,asat=asat,alat=alat,gamglu=gamglu,phospha=phospha,TSH=TSH,VIH=VIH,SCO=SCO,ACHB=ACHB,EVS=EVS)
                    break;
                else:
                    Erreur="Mauvais Password"
                    texte=render_template('accueil.html',Erreur=Erreur)
        return(texte)


@app.route('/Admin', methods=['POST'])
def Admin():
    with sqlite3.connect("etudiant.db") as con:
        cur = con.cursor()
        Prenom=request.form['CPrenom']
        Nom=request.form['CNom']
        Age=request.form['CAge']
        Sexe=request.form['CSexe']
        Adresse=request.form['CAdresse']
        Code_Postal=request.form['CCode_Postal']
        Ville=request.form['CVille']
        Adresse_Mail=request.form['CAdresse_Mail']
        Num_tel=request.form['CNum_tel']
        Num_SS=request.form['CNum_SS']
        Pin=request.form['CPi']
        leuco=request.form['Cleuco']
        hemati=request.form['Chemati']
        hemo=request.form['Chemo']
        hemato=request.form['Chemato']
        vgm=request.form['Cvgm']
        ccmh=request.form['Cccmh']
        tcmh=request.form['Ctcmh']
        rdw=request.form['Crdw']
        polynp=request.form['Cpolynp']
        polyep=request.form['Cpolyep']
        polybp=request.form['Cpolybp']
        lympp=request.form['Clympp']
        monop=request.form['Cmonop']
        polyn=request.form['Cpolyn']
        polye=request.form['Cpolye']
        polyb=request.form['Cpolyb']
        lymp=request.form['Clymp']
        mono=request.form['Cmono']
        numplaq=request.form['Cnumplaq']
        gly=request.form['Cgly']
        glym=request.form['Cglym']
        crea=request.form['Ccrea']
        creat=request.form['Ccreat']
        mdrd=request.form['Cmdrd']
        ckd=request.form['Cckd']
        aspect=request.form['Caspect']
        chotot=request.form['Cchotot']
        chotott=request.form['Cchotott']
        chohdl=request.form['Cchohdl']
        chohdll=request.form['Cchohdll']
        ccholdl=request.form['Cccholdl']
        cchodll=request.form['Ccchodll']
        triglyc=request.form['Ctriglyc']
        triglyce=request.form['Ctriglyce']
        asat=request.form['Casat']
        alat=request.form['Calat']
        gamglu=request.form['Cgamglu']
        phospha=request.form['Cphospha']
        TSH=request.form['CTSH']
        VIH=request.form['CVIH']
        SCO=request.form['CSCO']
        ACHB=request.form['CACHB']
        EVS=request.form['CEVS']
        
        cur.execute("INSERT INTO users(Prenom,Nom,Age,Sexe,Adresse,Code_Postal,Ville,Adresse_Mail,Num_tel,Num_SS, Pin, leuco, hemati, hemo, hemato, vgm, ccmh, tcmh, rdw, polynp, polyep, polybp, lympp, monop, polyn, polye, polyb, lymp, mono, numplaq,gly, glym, crea, creat, mdrd, ckd, aspect, chotot, chotott, chohdl, chohdll, ccholdl, cchodll, triglyc, triglyce, asat, alat, gamglu, phospha, TSH, VIH, SCO, ACHB, EVS) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(Prenom,Nom,Age,Sexe,Adresse,Code_Postal,Ville,Adresse_Mail,Num_tel,Num_SS, Pin, leuco, hemati, hemo, hemato, vgm, ccmh, tcmh, rdw, polynp, polyep, polybp, lympp, monop, polyn, polye, polyb, lymp, mono, numplaq,gly, glym, crea, creat, mdrd, ckd, aspect, chotot, chotott, chohdl, chohdll, ccholdl, cchodll, triglyc, triglyce, asat, alat, gamglu, phospha, TSH, VIH, SCO, ACHB, EVS))
        
    return(render_template('accueil.html'))

@app.route('/Modification', methods=['POST'])
def Modif():
    with sqlite3.connect("etudiant.db") as con:
        cur = con.cursor()
        X=[]
        i=0
        Entree=request.form['entree']
        cur.execute("SELECT * FROM users")
        con.commit()
        donnees = cur.fetchall()
        j=0
        for i in range (len(donnees)):
            for donnee in donnees[i]:
                X.append(donnees[i][j])
                j+=j
        i=0
        j=0
                          
        Prenom=request.form['MPrenom']
        Nom=request.form['MNom']
        Age=request.form['MAge']
        Sexe=request.form['MSexe']
        Adresse=request.form['MAdresse']
        Code_Postal=request.form['MCode_Postal']
        Ville=request.form['MVille']
        Adresse_Mail=request.form['MAdresse_Mail']
        Num_tel=request.form['MNum_tel']
        Num_SS=request.form['MNum_SS']
        Pin=request.form['MPi']
        leuco=request.form['Mleuco']
        hemati=request.form['Mhemati']
        hemo=request.form['Mhemo']
        hemato=request.form['Mhemato']
        vgm=request.form['Mvgm']
        ccmh=request.form['Mccmh']
        tcmh=request.form['Mtcmh']
        rdw=request.form['Mrdw']
        polynp=request.form['Mpolynp']
        polyep=request.form['Mpolyep']
        polybp=request.form['Mpolybp']
        lympp=request.form['Mlympp']
        monop=request.form['Mmonop']
        polyn=request.form['Mpolyn']
        polye=request.form['Mpolye']
        polyb=request.form['Mpolyb']
        lymp=request.form['Mlymp']
        mono=request.form['Mmono']
        numplaq=request.form['Mnumplaq']
        gly=request.form['Mgly']
        glym=request.form['Mglym']
        crea=request.form['Mcrea']
        creat=request.form['Mcreat']
        mdrd=request.form['Mmdrd']
        ckd=request.form['Mckd']
        aspect=request.form['Maspect']
        chotot=request.form['Mchotot']
        chotott=request.form['Mchotott']
        chohdl=request.form['Mchohdl']
        chohdll=request.form['Mchohdll']
        ccholdl=request.form['Mccholdl']
        cchodll=request.form['Mcchodll']
        triglyc=request.form['Mtriglyc']
        triglyce=request.form['Mtriglyce']
        asat=request.form['Masat']
        alat=request.form['Malat']
        gamglu=request.form['Mgamglu']
        phospha=request.form['Mphospha']
        TSH=request.form['MTSH']
        VIH=request.form['MVIH']
        SCO=request.form['MSCO']
        ACHB=request.form['MACHB']
        EVS=request.form['MEVS']
        
        long=int(len(X)/len(donnees))
        for i in range (len(donnees)):
            for j in range (long):
                if donnees[i][j]==Entree:
                    ids=donnees[i][j-1]
                    cur.execute("UPDATE users SET Prenom='"+Prenom+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET Nom='"+Nom+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET Age='"+Age+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET Sexe='"+Sexe+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET Adresse='"+Adresse+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET Code_Postal='"+Code_Postal+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET Ville='"+Ville+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET Adresse_Mail='"+Adresse_Mail+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET Num_tel='"+Num_tel+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET Num_SS='"+Num_SS+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET Pin='"+Pin+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET leuco='"+leuco+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET hemati='"+hemati+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET hemo='"+hemo+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET hemato='"+hemato+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET vgm='"+vgm+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET ccmh='"+ccmh+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET tcmh='"+tcmh+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET rdw='"+rdw+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET polynp='"+polynp+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET polyep='"+polyep+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET polybp='"+polybp+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET lympp='"+lympp+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET monop='"+monop+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET polyn='"+polyn+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET polye='"+polye+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET polyb='"+polyb+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET lymp='"+lymp+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET mono='"+mono+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET numplaq='"+numplaq+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET gly='"+gly+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET glym='"+glym+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET crea='"+crea+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET creat='"+creat+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET mdrd='"+mdrd+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET ckd='"+ckd+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET aspect='"+aspect+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET chotot='"+chotot+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET chotott='"+chotott+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET chohdl='"+chohdl+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET chohdll='"+chohdll+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET ccholdl='"+ccholdl+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET cchodll='"+cchodll+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET triglyc='"+triglyc+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET triglyce='"+triglyce+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET asat='"+asat+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET alat='"+alat+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET gamglu='"+gamglu+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET phospha='"+phospha+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET TSH='"+TSH+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET VIH='"+VIH+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET SCO='"+SCO+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET ACHB='"+ACHB+"' WHERE ID="+str(ids))
                    cur.execute("UPDATE users SET EVS='"+EVS+"' WHERE ID="+str(ids))
                    test=" Modifié avec succès"
                    break;
                else:
                    test=" invalide veuillez réessayer"       
        
    return(render_template('rendu_2.html',test=test))

@app.route('/patientv2', methods=['POST'])
def maj():
    with sqlite3.connect("etudiant.db") as con:
        cur = con.cursor()
        X=[]
        i=0
        Vno=request.form['Vpreno']
        cur.execute("SELECT * FROM users")
        con.commit()
        donnees = cur.fetchall()
        j=0
        for i in range (len(donnees)):
            for donnee in donnees[i]:
                X.append(donnees[i][j])
                j+=j
        i=0
        j=0
        long=int(len(X)/len(donnees))
        for i in range (len(donnees)):
            for j in range (long):
                if donnees[i][j]==Vno:
                    ids=donnees[i][j-1]
                    Nom=(donnees[i][j+1])
                    Age=(donnees[i][j+2])
                    Sexe=(donnees[i][j+3])
                    Adresse=(donnees[i][j+4])
                    Code_Postal=(donnees[i][j+5])
                    Ville=(donnees[i][j+6])
                    Adresse_Mail=(donnees[i][j+7])
                    Num_tel=(donnees[i][j+8])
                    Num_SS=(donnees[i][j+9])
                    leuco=(donnees[i][j+11])
                    hemati=(donnees[i][j+12])
                    hemo=(donnees[i][j+13])
                    hemato=(donnees[i][j+14])
                    vgm=(donnees[i][j+15])
                    ccmh=(donnees[i][j+16]) 
                    tcmh=(donnees[i][j+17])
                    rdw=(donnees[i][j+18])
                    polynp=(donnees[i][j+19])
                    polyep=(donnees[i][j+20])
                    polybp=(donnees[i][j+21])
                    lympp=(donnees[i][j+22])
                    monop=(donnees[i][j+23])
                    polyn=(donnees[i][j+24])
                    polye=(donnees[i][j+25])
                    polyb=(donnees[i][j+26])
                    lymp=(donnees[i][j+27])
                    mono=(donnees[i][j+28])
                    numplaq=(donnees[i][j+29])
                    gly=(donnees[i][j+30])
                    glym=(donnees[i][j+31])
                    crea=(donnees[i][j+32])
                    creat=(donnees[i][j+33])
                    mdrd=(donnees[i][j+34])
                    ckd=(donnees[i][j+35])
                    aspect=(donnees[i][j+36]) 
                    chotot=(donnees[i][j+37])
                    chotott=(donnees[i][j+38])
                    chohdl=(donnees[i][j+39])
                    chohdll=(donnees[i][j+40])
                    ccholdl=(donnees[i][j+41])
                    cchodll=(donnees[i][j+42])
                    triglyc=(donnees[i][j+43])
                    triglyce=(donnees[i][j+44])
                    asat=(donnees[i][j+45])
                    alat=(donnees[i][j+46])
                    gamglu=(donnees[i][j+47])
                    phospha=(donnees[i][j+48])
                    TSH=(donnees[i][j+49])
                    VIH=(donnees[i][j+50])
                    SCO=(donnees[i][j+51])
                    ACHB=(donnees[i][j+52])
                    EVS=(donnees[i][j+53])
                    break;
                    
        Prenom=request.form['Preno']
        Nom=request.form['Nom']
        Age=request.form['Age']
        Sexe=request.form['Sexe']
        Adresse=request.form['Adresse']
        Code_Postal=request.form['Code_Postal']
        Ville=request.form['Ville']
        Adresse_Mail=request.form['Adresse_Mail']
        Num_tel=request.form['Num_tel']
        Num_SS=request.form['Num_SS']
        Pin=request.form['Pi']
        
        cur.execute("UPDATE users SET Prenom='"+Prenom+"' WHERE ID="+str(ids))
        cur.execute("UPDATE users SET Nom='"+Nom+"' WHERE ID="+str(ids))
        cur.execute("UPDATE users SET Age='"+Age+"' WHERE ID="+str(ids))
        cur.execute("UPDATE users SET Sexe='"+Sexe+"' WHERE ID="+str(ids))
        cur.execute("UPDATE users SET Adresse='"+Adresse+"' WHERE ID="+str(ids))
        cur.execute("UPDATE users SET Code_Postal='"+Code_Postal+"' WHERE ID="+str(ids))
        cur.execute("UPDATE users SET Ville='"+Ville+"' WHERE ID="+str(ids))
        cur.execute("UPDATE users SET Adresse_Mail='"+Adresse_Mail+"' WHERE ID="+str(ids))
        cur.execute("UPDATE users SET Num_tel='"+Num_tel+"' WHERE ID="+str(ids))
        cur.execute("UPDATE users SET Num_SS='"+Num_SS+"' WHERE ID="+str(ids))
        cur.execute("UPDATE users SET Pin='"+Pin+"' WHERE ID="+str(ids))
        con.commit()
        
        texte=render_template('rendu_1.html',Prenom=Prenom,Nom=Nom, Age=Age, Sexe=Sexe, Adresse=Adresse, Code_Postal=Code_Postal, Ville=Ville,Adresse_Mail=Adresse_Mail, Num_tel=Num_tel, Num_SS=Num_SS, leuco=leuco,hemati=hemati,hemo=hemo,
                hemato=hemato, vgm=vgm, ccmh=ccmh,tcmh=tcmh,rdw=rdw,polynp=polynp, polyep=polyep,
                polybp=polybp,lympp=lympp, monop=monop, polyn=polyn, polye=polye, polyb=polyb,
                lymp=lymp,mono=mono, numplaq=numplaq,
                gly=gly,glym=glym,crea=crea,creat=creat,
       mdrd=mdrd,
        ckd=ckd,
        aspect=aspect, 
        chotot=chotot,
        chotott=chotott,
        chohdl=chohdl,
        chohdll=chohdll,
        ccholdl=ccholdl,
        cchodll=cchodll,
        triglyc=triglyc,
        triglyce=triglyce,
        asat=asat,
        alat=alat,
        gamglu=gamglu,
        phospha=phospha,
        TSH=TSH,
        VIH=VIH,
        SCO=SCO,
        ACHB=ACHB,
        EVS=EVS)
        
    return(texte)