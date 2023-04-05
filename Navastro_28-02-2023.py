#Module import
import math
import time
import matplotlib.pyplot as plt
  

#Timer start
start = time.time()

#CONVERSIONS & CONSTANTS
DegRad=math.pi/180 #degrees to radians
cd=2 #decimal places for rounded values


"""
#DATA INPUT
obsYear= eval(input("Year of observation: "))
obsMonth= eval(input("Month of observation: "))
obsDay= eval(input("Day of observation: "))
obsHour= eval(input("Hour of observation: "))
obsMinute= eval(input("Minute of observation: "))
obsSecond= eval(input("Second of observation: "))
obsAltitude= eval(input("Altitude of observation (m): "))
obsDeg= eval(input("Sextant angle degrees: "))
obsCorr= eval(input("Sextant correction minutes: "))
obsTemp= eval(input("Ambient temperature (ºC): "))
obsPress= eval(input("Ambient pressure (mbar): "))
estLat= eval(input("Estimated latitude degrees(+N, -S): "))
estLon= eval(input("Estimated longitude degrees (+E, -W): "))
obsLimb= eval(input("Observed limb of the sun (1 upper, 0 lower): "))
"""

#TEST DATA INPUT 1972
# obsYear= 1972
# obsMonth= 6
# obsDay= 23
# obsHour= 0
# obsMinute= 17
# obsSecond= 52
# obsAltitude= 3.4
# obsDeg= 50.02
# obsCorr= 10.2
# obsTemp= 22
# obsPress= 1010
# estLat= -16.1
# estLon= 172
# obsLimb= 0


#TEST DATA INPUT 1994
# obsYear= 1994
# obsMonth= 4
# obsDay= 8
# obsHour= 21
# obsMinute= 54
# obsSecond= 9
# obsAltitude= 2.2
# obsDeg= 2.53
# obsCorr= -5.8
# obsTemp= 40
# obsPress= 1030
# estLat= 13
# estLon= -58
# obsLimb= 1


#TEST INPUT DATA ANDREW EVANS
#OBS 1
obsYear= 2005
obsMonth= 8
obsDay= 21
obsHour= 20
obsMinute= 2
obsSecond= 15
obsAltitude= 0
obsDeg= 53.23
obsCorr= 8
obsTemp= 24
obsPress= 1030
estLat= 48
estLon= -123.81
obsLimb= 0
#OBS2
obsHour2= 22
obsMinute2= 48
obsSecond2= 7
obsDeg2= 41.57
estLon2= -123.29
#CALCULATE UTC CENTURIES
Tu= (367*obsYear-math.trunc(7*(obsYear+math.trunc((obsMonth+9)/12))/4)+math.trunc(275*obsMonth/9)+obsDay+(obsHour+(obsMinute+(obsSecond/60))/60)/24-730531.5)/36525
Tu2= (367*obsYear-math.trunc(7*(obsYear+math.trunc((obsMonth+9)/12))/4)+math.trunc(275*obsMonth/9)+obsDay+(obsHour2+(obsMinute2+(obsSecond2/60))/60)/24-730531.5)/36525
#CALCULATE EPHEMERIES TIME
Te= Tu+((63+60*Tu)/3200000000)
Te2= Tu2+((63+60*Tu2)/3200000000)
#CALCULATE POSITIONS FOR VENUS, EARTH, MARS and JUPITER
V=50+58517*Te
V2=50+58517*Te2
E=357.52558+35999.04974*Te
E2=357.52558+35999.04974*Te2
M=20+19140*Te
M2=20+19140*Te2
J=19.9+3034.6*Te
J2=19.9+3034.6*Te2
#CALCULATE MOON'S ASCENDING NODE AND 2*SUN MEAN LONGITUDE
N=125-1934.1*Te
N2=125-1934.1*Te2
L=200.9+72001.7*Te
L2=200.9+72001.7*Te2
#CALCULATE APPARENT ECLIPTIC LONGITUDE OF THE SUN
EL = E+(1018585.1+(6191.2*Te)+(1.1*Te**2) 
     +6892.8*math.sin(((E-0.0018)*DegRad))
     +72.0*math.sin((2*E)*DegRad) 
     -17.4*Te*math.sin(E*DegRad) 
     +7.2*math.sin((E-J-90.5)*DegRad)
     +6.5*math.sin(((445267.1*Te)-62.1)*DegRad)
     -6.4*math.sin(((20.2*Te)+71.4)*DegRad)
     +5.5*math.sin(((2*E)-(2*V)-58)*DegRad)
     -4.8*math.sin((E-V-29)*DegRad)
     -2.7*math.sin(((2*E)-(2*J)-3)*DegRad)
     -2.6*math.sin((J+7)*DegRad)
     -2.5*math.sin(((3*E)-(2*V)-46)*DegRad)
     +2.0*math.sin(((2*E)-(2*M)+74)*DegRad)
     -1.9*math.sin(((150*Te)+28)*DegRad)
     +1.8*math.sin((E-(2*M)-70)*DegRad)
     -1.6*math.sin((E-(2*J)+20)*DegRad)
     -1.6*math.sin(((4*E)-(3*V)-75)*DegRad)
     +1.0*math.sin((3*E)*DegRad)
     -1.0*math.sin(((5*E)-(3*V)-48)*DegRad)
     -20.5 
     -17.2*math.sin(N*DegRad) 
     -1.3*(math.sin(L))*DegRad)/3600

EL2 = E2+(1018585.1+(6191.2*Te2)+(1.1*Te2**2) 
     +6892.8*math.sin(((E2-0.0018)*DegRad))
     +72.0*math.sin((2*E2)*DegRad) 
     -17.4*Te2*math.sin(E2*DegRad) 
     +7.2*math.sin((E2-J2-90.5)*DegRad)
     +6.5*math.sin(((445267.1*Te2)-62.1)*DegRad)
     -6.4*math.sin(((20.2*Te2)+71.4)*DegRad)
     +5.5*math.sin(((2*E2)-(2*V2)-58)*DegRad)
     -4.8*math.sin((E2-V2-29)*DegRad)
     -2.7*math.sin(((2*E2)-(2*J2)-3)*DegRad)
     -2.6*math.sin((J2+7)*DegRad)
     -2.5*math.sin(((3*E2)-(2*V2)-46)*DegRad)
     +2.0*math.sin(((2*E2)-(2*M2)+74)*DegRad)
     -1.9*math.sin(((150*Te2)+28)*DegRad)
     +1.8*math.sin((E2-(2*M2)-70)*DegRad)
     -1.6*math.sin((E2-(2*J2)+20)*DegRad)
     -1.6*math.sin(((4*E2)-(3*V2)-75)*DegRad)
     +1.0*math.sin((3*E2)*DegRad)
     -1.0*math.sin(((5*E2)-(3*V2)-48)*DegRad)
     -20.5 
     -17.2*math.sin(N2*DegRad) 
     -1.3*(math.sin(L2))*DegRad)/3600

#CONVERT ECLIPTIC TO EQUATORIAL COORDINATES
Ob=23.43929-(0.01300*Te)+(0.00256*math.cos(N*DegRad))+(0.00016*math.cos(L*DegRad))
Ob2=23.43929-(0.01300*Te2)+(0.00256*math.cos(N2*DegRad))+(0.00016*math.cos(L2*DegRad))
RA=math.degrees(math.atan(math.tan(EL*DegRad)*math.cos(Ob*DegRad)))
RA2=math.degrees(math.atan(math.tan(EL2*DegRad)*math.cos(Ob2*DegRad)))
if abs(EL-(math.trunc(EL/360))*360)>90 and abs(EL-(math.trunc(EL/360))*360)<270:
    RAcorr=180+RA
else:
    RAcorr=RA
if abs(EL2-(math.trunc(EL2/360))*360)>90 and abs(EL2-(math.trunc(EL2/360))*360)<270:
    RAcorr2=180+RA2
else:
    RAcorr2=RA2
#CALCULATE DECLINATION
Dec=math.degrees(math.asin(math.sin(EL*DegRad)*math.sin(Ob*DegRad)))
Dec2=math.degrees(math.asin(math.sin(EL2*DegRad)*math.sin(Ob2*DegRad)))
#CALCULATE GHA of ARIES
ARIES=360*(0.7790573+36625.002139*Tu+0.0000011*Tu*Tu-0.0000122*math.sin(N*DegRad)-0.0000009*math.sin(L*DegRad))
ARIES2=360*(0.7790573+36625.002139*Tu2+0.0000011*Tu2*Tu2-0.0000122*math.sin(N2*DegRad)-0.0000009*math.sin(L2*DegRad))
ARIEScorr=360+ARIES-(math.trunc(ARIES/360))*360
ARIEScorr2=360+ARIES2-(math.trunc(ARIES2/360))*360
#CALCULATE GHA of the SUN
GHA1=ARIEScorr-RAcorr
GHA1_2=ARIEScorr2-RAcorr2
GHA=GHA1-(math.trunc(GHA1/360))*360
GHA2=GHA1_2-(math.trunc(GHA1_2/360))*360
#CALCULATE SEMIDIAMETER OF THE SUN
SD=math.degrees(math.asin(0.004659/(1-0.0167*math.cos(DegRad*(E)))))
SD2=math.degrees(math.asin(0.004659/(1-0.0167*math.cos(DegRad*(E2)))))
#CALCULATE HEIGHT OF EYE CORRECTION
D=0.0198*obsAltitude #original value of 0.0293 corrected P.Cabral)
#CALCULATE APPARENT ALTITUDE OF THE SUN
Ha=obsDeg+(obsCorr/60)-D
Ha2=obsDeg2+(obsCorr/60)-D
#CALCULATE REFRACTIVE CORRECTION
Rc=(0.28*obsPress/(obsTemp+273))*0.0167/math.tan((Ha+(7.31/(Ha+4.4)))*DegRad)
Rc2=(0.28*obsPress/(obsTemp+273))*0.0167/math.tan((Ha2+(7.31/(Ha2+4.4)))*DegRad)
#CALCULATE PARALLAX CORRECTION
PA=0.0024*math.cos(Ha*DegRad)
PA2=0.0024*math.cos(Ha2*DegRad)
#CALCULATE LHA
LHA=GHA+estLon
LHA2=GHA2+estLon2
#CALCULATE HC
Hc=math.degrees(math.asin((math.cos(LHA*DegRad)*math.cos(estLat*DegRad)*math.cos(Dec*DegRad))+(math.sin(estLat*DegRad)*math.sin(Dec*DegRad))))
Hc2=math.degrees(math.asin((math.cos(LHA2*DegRad)*math.cos(estLat*DegRad)*math.cos(Dec2*DegRad))+(math.sin(estLat*DegRad)*math.sin(Dec2*DegRad))))
#CALCULATE ZC
Zc = math.degrees(math.acos((math.sin(Dec*DegRad)-(math.sin(estLat*DegRad)*math.sin(Hc*DegRad)))/(math.cos(estLat*DegRad)*math.cos(Hc*DegRad))))
Zc2 = math.degrees(math.acos((math.sin(Dec2*DegRad)-(math.sin(estLat*DegRad)*math.sin(Hc2*DegRad)))/(math.cos(estLat*DegRad)*math.cos(Hc2*DegRad))))
#CALCULATE ZN
if LHA>0 and LHA<180:
    Zn=360-Zc
else:
    Zn=Zc
if LHA2>0 and LHA2<180:
    Zn2=360-Zc2
else:
    Zn2=Zc2  
#CALCULATE INTERCEPT
 #p = 60*(Ha-Rc+PA±S-HC)  
if obsLimb==0:
    p=60*(Ha-Rc+PA+SD-Hc)
else:
    p=60*(Ha-Rc+PA-SD-Hc)
if obsLimb==0:
    p2=60*(Ha2-Rc2+PA2+SD2-Hc2)
else:
    p2=60*(Ha2-Rc2+PA2-SD2-Hc2)
#Print intermediate results
print(" ")
print("***** INTERMEDIATE RESULTS *****")
print ("UTC centuries: ",Tu,"-",Tu2)
print ("Ephemeries time: ",Te,"-",Te)
print ("Venus position: ",V,"-",V2)
print ("Earth position: ",E,"-",E2)
print ("Jupiter position: ",J,"-",J2)
print ("Mars position: ",M,"-",M2)
print ("Moon ascending node: ",N,"-",N2)
print ("2*Sun mean longitude: ",L,"-",L2)
print ("Apparent ecliptic longitude of the sun: ",EL,"-",EL2)
print ("Ecliptic oliquity: ",Ob,"-",Ob2)
print ("Vertical ascention: ",RA,"-",RA2)
print ("Corrected vertical ascention: ",RAcorr,"-",RAcorr2)
print ("Declination: ",Dec,"-",Dec2)
print ("Greenwich hour angle of Aries: ",ARIES,"-",ARIES2)
print ("Corrected Greenwich hour angle of Aries: ",ARIEScorr,"-",ARIEScorr2)
print ("Greenwich hour angle of the Sun: ",GHA,"-",GHA2)
print ("Semidiameter of the Sun: ", SD,"-",SD2)
print ("Height of eye correction: ",D)
print ("Apparent altitude of the Sun: ",Ha,"-",Ha2)
print ("Refractive correction: ",Rc,"-",Rc2)
print ("Parallax correction: ",PA,"-",PA2)
#Print final results
print ("\n",
       "***** FINAL RESULTS *****","\n",
       "Date:","\t","\t","\t","\t","\t",obsDay,"/",obsMonth,"/",obsYear,"\n","\n",
       "\t","\t","\t","\t","\t","OBSERVATION 1: ","\t","OBSERVATION 2: ","\n",
       "Time:","\t","\t","\t","\t","\t",obsHour,"h",obsMinute,"m",obsSecond,"s","\t","\t",obsHour2,"h",obsMinute2,"m",obsSecond2,"s","\n",
       "Sun declination (Dec):","\t","\t",round(Dec,cd),"º","\t","\t",round(Dec2,cd),"º","\n",
       "Sun Greenwich hour angle (GHA):","\t",round(GHA,cd),"º","\t","\t",round(GHA2,cd),"º","\n",
       "Sextant height (Hs):","\t","\t","\t",obsDeg,"º","\t","\t",obsDeg2,"º","\n",
       "Azimuth (Zn): ","\t","\t","\t",round(Zn,cd),"º","\t","\t",round(Zn2,cd),"º","\n",
       "Intercept (P): ","\t","\t","\t",round(p,cd),"nm","\t","\t",round(p2,cd),"nm")
#Plot
#Corrected Zn angles
ZnCorr=(Zn)*DegRad
Zn2Corr=(Zn2)*DegRad
#Limits
Range=8
limx1=estLon+Range
limx2=estLon-Range
limy1=estLat-Range
limy2=estLat+Range
plt.xlim(limx1, limx2) 
plt.ylim(limy1, limy2)
#Titles
plt.xlabel('LONGITUDE',weight='bold') 
plt.ylabel('LATITUDE',weight='bold') 
plt.title("POSITION PLOT",weight='bold')
#Ap1 point 
plt.text(estLon, estLat,"  Ap 1",color='blue')
plt.scatter(estLon, estLat, s=25 ,  facecolors='none', edgecolors='blue' ,linewidth=2 )
#Ap2 point
plt.text(estLon2, estLat,"  Ap 2",color='magenta')
plt.scatter(estLon2, estLat, s=25 ,  facecolors='none', edgecolors='magenta' ,linewidth=2 )
#Ap1 line
m1=math.tan(ZnCorr)
b1=estLat-m1*estLon
x_valuesAp1=[((estLat-1)-b1)/m1,((estLat+1)-b1)/m1]
y_valuesAp1=[estLat-1,estLat+1]
plt.plot(x_valuesAp1, y_valuesAp1,linestyle="-",color='blue',linewidth=1)
#Lop1 line
mLop1=m1
p1x=estLon - (math.sin((180-ZnCorr)*DegRad))*p
p1y=estLat +  (math.cos((180-ZnCorr)*DegRad))*p
bLop1=p1y-mLop1*p1x
plt.text(p1x,p1y ,"  Lop 1",color='green')
plt.scatter(p1x, p1y, s=25 ,  facecolors='none', edgecolors='green' ,linewidth=2 )
x_valuesLop1=[estLon+Range,estLon-Range]
y_valuesLop1=[mLop1*(estLon+Range)+bLop1,mLop1*(estLon+Range)+bLop1]
plt.plot(x_valuesLop1, y_valuesLop1,linestyle="-",color='green',linewidth=1)
#Ap2 line
m2=math.tan(Zn2Corr)
b2=estLat-m2*estLon2
x_valuesAp2=[((estLat-1)-b2)/m2,((estLat+1)-b2)/m2]
y_valuesAp2=[estLat-1,estLat+1]
plt.plot(x_valuesAp2, y_valuesAp2,linestyle="-",color='magenta',linewidth=1)
#Lop2 line
#Stop timer
end = time.time()
#Calculate execution time
total_time = end - start
print("\n",
      "***** EXECUTION TIME *****","\n",
      "Execution time:",
      str(round (total_time,3)),"s")
#Print plot
plt.show()
"""          
The formulas for calculating the GHA, dec, and SD of the sun are short enough to enter easily (?)
by hand into a programmable calculator.
I wrote two articles for doing that.
The first "A Sun Sight Calculator for UKL 17", was published by Practical Boat Owner in February 1994.
A month or two later there was a correction of a typesetting error that covered part of the program with a photo.
The second, "Create Your Own Sun-Sight Reduction Program", was published by Cruising World in March 1996.
It too was bitten by the typesetting bug and has corrections in a later issue.
The English article was written for the TI-67 and the American for the TI-81.
In those days when hand held programmable calculators were "the thing", I wrote a "does everything" program
for the TI-82 and sold it by word of mouth for several years.
The real fun of these things, at least for me, was figuring out how the calculations are made and accomplishing them myself.
If you want to do that, here is a little bit to get you started or at least show you what is involved.
The internet will no doubt butcher the layout of the tables, but here goes. 
 
In order to reduce a sight of the sun it is necessary to know three astronomical values and two corrections.
The astro values are the sun's Greenwich hour angle, declination, and semidiameter.
The corrections are the refraction correction and the dip of the horizon.
All can be found in the Nautical Almanac, but they can also be calculated directly.
The necessary calculations are too long to be done by hand, but they can be easily done with a
programmable calculator or computer program.
After finding these five numbers, the sight reduction formulas can be used to reduce a sun sight to an azimuth and intercept. 
 
The problem is broken into six parts.
The common units of time are reduced to a single unit of time.
The position of the sun is calculated in the ecliptic coordinates of celestial latitude and longitude.
The celestial coordinates are converted to right ascension and declination.
The Greenwich hour angle of Aries is calculated and used to convert the right ascension of the sun to Greenwich hour angle.
Values are found for the semidiameter of the sun, the refraction correction, and the dip of the horizon.
Finally, the azimuth and intercept are calculated. 
 
The common units of time are hopelessly complicated.
There are too many of them; years, months, days, hours, minutes, and seconds.
Time must be changed into a single unit.
The chosen unit is the number of centuries after noon 1 January 2000.
Time has a value of -.5 at 1200 on 1 January 1950, 0 at 1200 on 1 January 2000, and +.5 at 1200 on 1 January 2050. 
 
Van Flandern and Pulkkinen give a short formula for converting common UTC (or GMT) time to UTC centuries
that is valid from March 1900 to February 2100. 
Tu = (367*yr-trunc(7*(yr+trunc((mo+9)/12))/4)+trunc(275*mo/9)+day+(hr+(min+(sec/60))/60)/24-730531.5)/36525 
 
The formula fails outside those dates because 1900 and 2100 are both years divisible by 4 which are not leap years.
The function trunc is the integer part of the number within the brackets; any fractional part is dropped.
To have an accuracy of one second, the value of time must have 11 significant digits
because there are over 6 billion seconds in two centuries. 
 
The way the formula works is a little vague and is best explained working backwards.
At the end of the formula, 36525 converts the units from days to centuries.
The 730531.5 makes the formula have a value of 0 at noon on 1 January 2000.
The term "day+(hr+(min+(sec/60))/60)/24" converts the date of the month and time into the number of days
since the beginning of the last day of the previous month.
The remaining part of the formula handles the changing number of days in the months and accounts for leap years.
You can get an idea of how it works by solving it for the first day of each month
for four consecutive years writing down the numbers from within each set of parentheses. 
 
We must keep up with two kinds of time.
One is UTC and is related to the rotation of the earth.
The other is ephemeris time which is related to the speed with which the earth revolves around the sun.
These two kinds of time are slowly drifting apart because the earth's rotational speed has been slowing down
for the last several decades.
Every time a leap second is inserted into UTC the two get farther apart. 
 
An equation for converting centuries of UTC time to ephemeris time is 
Te = Tu+((63+60*Tu)/3,200,000,000) 
 
This says that the difference between the two kinds of time is 63 seconds in January 2000 and is increasing by 60 seconds per century.
The formula has been accurate for the last few decades and will probably be accurate for several more. 
 
With time out of the way, the next step is to calculate the apparent ecliptic longitude of the sun.
Because the orbit of the earth around the sun is perturbed by the nearby planets and because the earth is pulled about by the moon,
we must first make rough estimates of the positions of the earth, moon, and planets. 
 
The positions of venus, earth, mars, and jupiter are each calculated as
the mean anomaly which is the angle between the planet's perihelion and position.
The results are in degrees with values oftentimes greater than 360º or less than 0º.
That does not matter to most calculators, but you may find it necessary to subtract the extra revolutions
before taking the sines of the angles in later calculations. 
V = 50+(58517*Te) 
E = 357.52558+(35999.04974*Te) 
M = 20+(19140*Te) 
J = 19.9+(3034.6*Te) 
 
A few more short formulas give the longitude of the moon's ascending node and twice the sun's mean longitude. 
N = 125.0-(1934.1*Te) 
L = 200.9+(72001.7*Te) 
 
With these intermediate values in hand, it is possible to calculate the apparent ecliptic longitude of the sun.  The formula is long and somewhat repetitious.
EL = E+(1018585.1+(6191.2*Te)+(1.1*Te2) 
     +6892.8*sin(E-0.0018) 
     +72.0*sin(2*E) 
     -17.4*Te*sin(E) 
     +7.2*sin(E-J-90.5) 
     +6.5*sin((445267.1*Te)-62.1) 
     -6.4*sin((20.2*Te)+71.4) 
     +5.5*sin((2*E)-(2*V)-58) 
     -4.8*sin(E-V-29) 
     -2.7*sin((2*E)-(2*J)-3) 
     -2.6*sin(J+7) 
     -2.5*sin((3*E)-(2*V)-46) 
     +2.0*sin((2*E)-(2*M)+74) 
     -1.9*sin((150*Te)+28) 
     +1.8*sin(E-(2*M)-70) 
     -1.6*sin(E-(2*J)+20) 
     -1.6*sin((4*E)-(3*V)-75) 
     +1.0*sin(3*E) 
     -1.0*sin((5*E)-(3*V)-48) 
     -20.5 
     -17.2*sin(N) 
     -1.3*sin(L))3600 
 
The result is in degrees, but the units of each of the summed elements are seconds of arc.
The first line calculates the mean ecliptic longitude of the sun.
The next eighteen lines move the sun in an elliptical orbit and correct for the tugs and pulls of the moon and planets.
Because we see the sun where it was about 8 minutes ago, 20.5 seconds of arc must be subtracted.
The last two lines correct for the nutation of the earth's axis. 
 
The next task is to change from ecliptic to equatorial coordinates.
If we assume that the sun's celestial latitude is zero, the formulas for right ascension and declination are short
and we need only know the obliquity of the ecliptic.
Ob = 23.43929-(0.01300*Te)+(0.00256*cos(N))+(0.00016*cos(L)) 
RA = tan-1(tan(EL)*cos(Ob)) 
if 90º<EL<270º, then RA = 180+RA 
Dec = sin-1(sin(EL)*sin(Ob)) 
 
The GHA of Aries can be calculated from the universal time in centuries with a relatively short formula.
The answer is in degrees and may need to be reduced to an angle between 0 and 360º.
This formula requires at least 12 significant digits to keep an accuracy of 0.1' between 1900 and 2100.
The GHA of the sun is the difference between the GHA of Aries and the right ascension of the sun. 
ARIES = 360*(0.7790573+(36625.0021390*Tu)+(0.0000011*Tu2) -(0.0000122*sin(N))-(0.0000009*sin(L))) 
GHA = ARIES-RA 
 
The semidiameter of the sun varies with its distance from the earth and that depends on the position of the sun.
The semidiameter of the sun can be calculated from its mean anomaly. 
SD = sin-1 (0.004659/(1-0.0167*cos(E))) 
 
The almanac has a formula for the height of eye correction with the height of eye in meters and the dip of the horizon in degrees. 
D = 0.0293*HE 
 
The sun's apparent altitude is the total of the sextant altitude, the index correction, and the negative of the dip.
The apparent altitude, sextant altitude, and dip are all in degrees.  The index correction is in minutes of arc. 
Ha = Hs+(IC/60)-D 
 
The almanac also has a formula for the refractive correction. 
The pressure is in millibar, and the temperature is in Celsius. 
Rc = (0.28*Pres/(Temp+273))*0.0167/tan(Ha+(7.31/(Ha+4.4))) 
 
The horizontal parallax of the sun is small and can be ignored, but for completeness we can include it.
Both the parallax in altitude and apparent altitude are in degrees. 
PA = 0.0024*cos(Ha) 
 
With all the usual Nautical Almanac data now in hand, the well known sight reduction formulas can be used
to find the calculated altitude and azimuth.
The latitude and longitude of the dead reckoning position are in degrees with north and east positive and with south and west negative. 
LHA = GHA+Long 
Hc = sin-1((cos(LHA)*cos(Lat)*cos(Dec))+(sin(Lat)*sin(Dec))) 
Zc = cos-1((sin(Dec)-(sin(Lat)*sin(Hc)))/(cos(Lat)cos(Hc))) 
if 0°<LHA<180°, Zn = 360-Zc 
if 180°<LHA<360°, Zn = Zc 
 
The intercept in nautical miles is finally calculated.
The sign of the semidiameter depends on the limb observed.
The sign is + for the lower limb and - for the upper limb. 
p = 60*(Ha-Rc+PA±S-HC) 
 
It is easy to incorporate the formulas in a calculator program, a spreadsheet, or a PC program.
To help in debugging such a program, two examples are given in the table below.
They were calculated with an Excel spreadsheet.
The results might be slightly different with other calculators or programs. 
 
The astro formulas give results that closely match the Nautical Almanac.
The accuracy seems to be 0.1' or better.
In December and January the results for the sun's GHA may appear worse, but remember that
the Nautical Almanac entries are slightly in error then to avoid a 'v' correction for the sun. 
 
The formulas used in this article came from the from the Nautical Almanac,
from Van Flandern and Pulkkinen, "Low Precision Formulae for Planetary Positions",
The Astrophysical Supplement Series, vol 41, p 391, (1979)
and from Montenbruck and Phleger, Astronomy on the Personal Computer, Springer-Verlag, Berlin, 1991.
They were put into the form used by B. Emerson in N.A.O. Technical Note Number 47 - Approximate Solar Coordinates
Her Majesty's Nautical Almanac Office, November 1978. 
 
Test Problems 
 
yr 1972 1994 
mo 6 4 
day 23 8 
hr 0 21 
min 17 54 
sec 52 9 
Tu -0.275249489 -0.057319299 
Te -0.275249475 -0.05731928 
V -16056.77351 -3304.15233 
E -9551.193949 -1705.914046 
M -5248.274945 -1077.091027 
J -815.3720558 -154.0410883 
N 657.3600089 235.8612202 
L -19617.5301 -3926.18563 
EL -9268.363115 -1421.172693  
Ob 23.44388492 23.43873142 
RA -88.21592359 17.37102545 
RA 91.78407641 17.37102545 
Dec 23.43374638 7.375208356 
ARIES -3628884.262 -755474.5373 
ARIES 275.7376754 165.4626822 
GHA 183.953599 148.0916567 
SD  0.262639337 0.266624737 
HE 3.4 2.2 
D 0.054026531 0.043458923 
Hs 50.02000000 2.53000000 
IC 10.2 -5.8 
Ha 50.13597347 2.38987441 
Pres 1010 1030 
Temp 22 40 
Rc 0.013305383 0.254021969 
PA 0.001538323 0.002397913 
Long 172 -58 
LHA 355.953599 90.0916567 
Lat -16.1 13 
Hc 50.2688665 1.566109477 
Zc 5.813557565 82.79151131 
Zn 5.813557565 277.2084887 
Limb lower upper 
p 7.078755034 18.33096838 
 A Comparison of the Calculator Almanac and the Nautical Almanac 
 
                                     Sun                                        Aries                Date   Time        G.H.A.             Declination        Semidiameter        G.H.A. 
               N.A.     Calc.  Error  N.A.     Calc. Error N.A. Calc. Error   N.A.  Calc.  Error 
                °    '   °    '        °    '   °    '   '     '    '      °    '   °    '   ' 
 1 Jan 95 0000 179 12.0 179 12.2 +.2  S23 03.2 S23 03.3 +.1  16.3 16.3 0  100 10.7 100 10.7  0 
 2 Jun 94 0100 195 32.5 195 32.6 +.1  N22 07.9 N22 07.9  0   15.8 15.8 0  265 16.6 265 16.6  0 
27 Feb 93 0200 206 48.0 206 48.0  0   S 8 23.2 S 8 23.2  0   16.2 16.2 0  186 55.3 186 55.3  0 
 3 Sep 93 0300 225 08.4 225 08.4  0   N 7 34.8 N 7 34.8  0   15.9 15.9 0   27 15.8  27 15.9 +.1 
20 Mar 92 0400 238 07.5 238 07.4 -.1  S 0 04.7 S 0 04.7  0   16.1 16.1 0  237 56.5 237 56.5  0 
10 Oct 92 0500 258 15.1 258 15.0 -.1  S 6 44.1 S 6 44.1  0   16.0 16.0 0   94 03.2  94 03.2  0 
23 Apl 91 0600 270 23.5 270 23.4 -.1  N12 22.5 N12 22.5  0   15.9 15.9 0  300 47.3 300 47.3  0 
16 Nov 91 0700 288 49.7 288 49.7  0   S18 37.7 S18 37.7  0   16.2 16.2 0  159 51.5 159 51.5  0 
 8 May 90 0800 300 52.9 300 52.9  0   N17 03.0 N17 02.9 -.1  15.9 15.9 0  345 53.6 345 53.5 -.1 
13 Dec 90 0900 316 29.5 316 29.5  0   S23 08.5 S23 08.5  0   16.3 16.3 0  216 47.5 216 47.4 -.1 
26 May 89 1000 330 45.6 330 45.7 +.1  N21 09.5 N21 09.5  0   15.8 15.8 0   33 57.2  33 57.2  0 
 6 Jun 84 1100 345 20.2 345 20.3 +.1  N22 41.8 N22 41.8  0   15.8 15.8 0   60 02.3  60 02.3  0 
 
Bill Murdoch 
 
(My wife and I have a Crealock 34 in Northwest Creek Marina not far from you.)
"""
