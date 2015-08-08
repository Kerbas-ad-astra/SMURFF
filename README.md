#SMURFF: Simple Mass adjUstments for Real-ish Fuel-mass Fractions

*For people who want real-ish fuel mass fractions without too much hassle.*

![SMURFF logo](https://raw.githubusercontent.com/Kerbas-ad-astra/SMURFF/master/SMURFF%20logo.png)

##Features

SMURFF is a Module Manager patch that reduces the dry masses of fuel tanks and engines so that KSP rockets can have fuel mass fractions closer to what we make in the real world, without going into per-part configurations like e.g. Realism Overhaul.

Most of a real rocket's structural strength comes from the fuel inside of it, rather than the tanks themselves -- the "tank" is just a metal shell to hold the fuel together.  KSP fuel tanks, on the other hand, seem to be made of lead plates and rebar.  This is all well and good for a planet where you only need 3.5 km/s to get to orbit, but it's not a lot of fun for the real solar system.  To help ease the transition to RSS (without requiring per-part configurations, thus allowing *any* mods to be installed), SMURFF makes the following adjustments:

* Stock and stockalike liquid fuel tanks (LFO, LF, Monoprop) have a fuel mass fraction of 87-89%; SMURFF increases this to 96-97% by dividing fuel tank mass by 4, putting them in line with the Space Shuttle external tank.
* Xenon and argon gas tanks are adjusted from 56% to 90% by dividing their mass by 7.  I've seen some NASA sources saying xenon tanks are 95% fuel (or suggesting that they will soon be so), others suggesting 85%, so I went with 90%.
* Liquid Hydrogen tanks (from Near Future Propulsion -- Freight Transportation Technology tanks are less efficient) are adjusted from 75% to 85% by dividing their mass by 2, in line with the ET's hydrogen tank (it's about 2/3 the length, so its mass is thus estimated as 2/3 of the tank's dry mass, which combined with hydrogen's lightness makes it "only" 85% fuel).
* Parts that use the fuel-switching modules from Firespitter or Interstellar Fuel Switch have their dry mass reduced by only a factor of 2; I figure the interchangeable-tank hardware hurts their fuel mass fraction.
	* Parts which use the "tankMass" variable won't get even that buff, since the switcher module will overwrite the stock mass in that case.
* SRBs are adjusted from 79% to 88% by dividing their mass by 2, in line with the Space Shuttle SRBs.
* Engines' masses (excluding SRBs) are reduced by a factor of 2 (SSMEs mass 3.5 tons each, diameter of 2.5 meters, thrust of 2,000 kN; compare to the Mainsail, diameter of 2.5 meters, thrust 1500 kN, mass 6 tons -- cutting it in half to 3 tons feels about right).
* Command pods (and probes) and cargo bays are excluded from getting buffed.  (Engines are also excluded from some patches, but that's only because they get buffed later by a different amount.)

(Even though they use the same numerical factor, SRBs, non-SRBs, and fuel-switching tanks are considered and patched separately because they're based on different comparisons.)

The result is that rockets have more Earth-like mass fractions and thus are able to achieve Earth-like payload masses without requiring the construction of horrible asparagus monsters.  To compare: with stock part masses, to get the Kerbal X capsule (plus heat shield) up into space, I need to convert the Kerbal X into the "Kerbal X Triple-Heavy" (or "Kerbal 7"), with 6 asparagus-staged size 2 boosters identical to the core (actually, identical plus the round X200-6R tank from TurboNisuReloaded) and an extended upper-stage tank (an X200-32 instead of the stock -16).  It gets just shy of 7 tons into LEO (not counting the spent upper stage) with a 465-ton rocket (not counting the payload) which blows up the launchpad at takeoff.  With SMURFF, I can lose two of those boosters and get 9.5 tons into orbit (not counting the spent upper stage) with a 296-ton rocket (not counting the payload).   The Falcon 9 v1 got 10.5 tons into orbit and weighed 335 tons, using slightly less efficient engines than the Skipper and Poodle, so I figure I'm close enough for Kerbal work.

##Dependencies

SMURFF depends on [**Module Manager**](http://forum.kerbalspaceprogram.com/threads/55219) to function.

##Recommendations

SMURFF is mainly intended for use with [**Real Solar System**](http://forum.kerbalspaceprogram.com/threads/55145).  It's why I made it!

If you want higher real-ish specific impulses as well as mass fractions (though 300-350 seconds is real-ish enough for kerolox engines), there's Nertea's [**Cryogenic Engines pack**](http://forum.kerbalspaceprogram.com/threads/117766), but be careful! By default, the pack will patch all LFO fuel tanks to be switchable to LH2/LO2 via InterstellarFuelSwitch, and because it uses the tankMass variable, SMURFF won't be able to give them a buff.  The relative penalty to tank mass outweighs the boost from the increased specific impulse.  To get a benefit from Cryogenic Engines, delete the CryoEnginesFuelTankSwitcher patch, and install the CryoEnginesLFO patch from the "Extras" folder (so the ISRU patch can also be deleted).  Their specific impulses get knocked down a bit from when they burn hydrolox, but they're still more efficient than the stock engines (if a little heavier and a hair less powerful).  *(So, whoever it is that decides to index this mod on CKAN, you shouldn't actually put Cryogenic Engines in as a recommendation.  Not even CryoEngines-LFO, since that still installs the FuelSwitch patch!)*

##Download and install

* [**GitHub**](https://github.com/Kerbas-ad-astra/SMURFF/releases)
* CurseForge
* KerbalStuff

From there, just unzip the "SMURFF" folder into your GameData directory.

##Known and anticipated issues

Mass data that isn't stored as a straight-up number can't be modified by this version of SMURFF.  This includes tankMass from FS/Interstellar Fuel Switch, which is stored as a series of semicolon-separated values.  If you know how to modify them with a ModuleManager patch, please tell me!  Otherwise, tanks that use that variable (**all fuel tanks** if you use Cryogenic Engines without removing the CryoEnginesFuelTankSwitcher patch!) will receive no buff from SMURFF.

Please let me know in the forum thread or on [**the GitHub issue tracker**](https://github.com/Kerbas-ad-astra/SMURFF/issues) if you find any others!

##Version history and changelog

* 2015 08 08: Initial release.

##Roadmap

As I get the time, I'll publish to CurseForge and KerbalStuff.  (Probably going to wait on KerbalStuff, since I'm thinking about renaming SMURFF and KS doesn't let mod authors rename things.)

I had been content to leave SMURFF with just mass adjustments, since I didn't know of a way to modify specific impulses in a simple, universal way with Module Manager (since "0 350" or whatever isn't a number, I can't just add to it), but I've had a brainwave: MM *can* do regex replacement, so I can make a patch that says "if an atmoCurve entry starts with "0 3", replace it with "0 4", and the LFO motors will go from 300-something seconds to 400-something seconds, just like real rocket motors do.  I've got some more thinking and testing to do before I release that (for one thing, 300-something seconds is in line with kerosene-fueled rockets, which is arguably a better match for Liquid Fuel), and since it's not an adjustment to mass, I wouldn't be able to call this thing SMURFF anymore, so let me know if you're interested in **KSP-RishA: Real-ish Adjustments**.  (I'm also open to suggestions for the name.)

Until then, if you find any classes of parts (i.e. anything that can be described by using Module Manager to filter by module, resource, mass, etc.) that get horribly mistreated (either too much mass reduction or too little), I'll make an adjustment, but I have zero interest in making adjustments for individual parts -- the whole point of SMURFF is to avoid that level of complication.

##Credits

Thanks are owed to NathanKell and the entire Realism Overhaul team for making an incredibly detailed, thoroughly researched and calculated system...and convincing me to make something simpler.  :wink:

Even more thanks are owed to ialdeboath and sarbian for the power of Module Manager.  Seriously, half of my addons wouldn't exist if not for them.

##License

Simple Mass adjUstments for Real-ish Fuel-mass Fractions ("SMURFF") is copyright 2015 Kerbas_ad_astra.  Configuration files are released under the [**Apache 2.0 license**](https://www.apache.org/licenses/LICENSE-2.0).  All other rights (e.g. the SMURFF logo) reserved.