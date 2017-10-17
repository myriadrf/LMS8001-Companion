Contact Details
---------------

Lime Microsystems Ltd.
Surrey Technology Centre, Occam Road,             
The Surrey Research Park,
Guilford, Surrey.
GU2 7YG 
United Kingdom

http: www.limemicro.com

contact person:
  Ignas Skudrickas
  email: i.skudrickas@limemicro.com



Board Description
-----------------

board designation           : LMS8001-Companion Board 2v1
board type                  : Lead Free
board size                  : 147.754 x 67.00 mm
board thickness             : 1.6 mm +/- 10 %
board material              : Rogers RO4350B + FR4

number of layers            : 4

Top layer copper foil thickness: 0.5 oz (18 um)+plating
Dielectric thickness between Top layer and 2nd layer: 20.00 mil
Dielectric between Top layer and 2nd layer relative permittivity (Er): 3.66

minimum finished hole size  : 200 um
minimum spacing             : 100 um
minimum track width         : 100 um


drill diameters             : finished hole

plating finish (both sides) : immersion gold
                              0.08-0.20 um of gold over
                              2.50-5.00 um of nickel


Important Notes
---------------
0.35mm ring and 0.2mm drill via-in-pads must be resin filled with metal cap

DRCs must be run on Gerber files before building boards.

Solder mask : black, both sides, halogen free.

Silkscreen : white epoxy ink, halogen free, both sides. No silkscreen on pads.

Electrical test : 100 % netlist.

Boards are to be individually bagged.

Design software used:  KiCad 2013-june-11 stable



Controlled Impedance
--------------------

  * 50 Ohm uncoated RF GCPW lines (Top layer: 
         track width for GCPW line 0.79 mm, gap 0.25 mm
    Rogers 4350, 20.00 mil (between F.RO and B.RO Layers), metal thickness 0.5 oz (18 um)+plating


Board Stackup
------------
-F_Paste.gtp
-F_SilkS.gto
-F_Mask.gts
-F_RO.gtl
-B_RO.gbr
-F_FR4.gbr
-B_FR4.gbl
-B_Mask.gbs
-B_SilkS.gbo
-B_Paste.gbp

Additional gerbs:
-----------------
-Edge_Cuts.gbr
-Dwgs_User.gbr
-drl_map.pho
-NPTH-drl_map.pho
.drl
-NPTH.drl

Reports folder
--------------             
.drc.rpt (DRC Errors Report)			 
.rpt (Drill Size Table Report)               
.net (netlist)  
.rpt (module report)
.erc (Electric rules check)     



