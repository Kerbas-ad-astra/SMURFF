#KSP-RishA: Real-ish Adjustments

*For people who want real-ish fuel mass fractions and engine performance without too much hassle.  Formerly SMURFF: Simple Mass adjUstments for Real-ish Fuel-mass Fractions.*

![KSP-RishA logo](https://github.com/Kerbas-ad-astra/KSP-RishA/raw/master/KSP-RishA%20logo.png)

##Features

KSP-RishA is a Module Manager patch that reduces the dry masses of fuel tanks and engines and improves engine performance so that KSP rockets can have fuel mass fractions closer to what we make in the real world, without going into per-part configurations like e.g. Realism Overhaul.

Most of a real rocket's structural strength comes from the fuel inside of it, rather than the tanks themselves -- the "tank" is just a metal shell to hold the fuel together.  KSP fuel tanks, on the other hand, seem to be made of lead plates and rebar.  This is all well and good for a planet where you only need 3.5 km/s to get to orbit, but it's not a lot of fun for the real solar system.  To help ease the transition to RSS (without requiring per-part configurations, thus allowing *any* mods to be installed), KSP-RishA makes the following adjustments:

* Stock and stockalike liquid fuel tanks (LFO, LF, Monoprop) have a fuel mass fraction of 87-89%; KSP-RishA increases this to 96-97% by reducing dry mass by 75%, putting them in line with the Space Shuttle external tank.
* Xenon gas tanks are adjusted from 56% to 90% (86% reduction in dry mass).  I've seen some NASA sources saying xenon tanks are 95% fuel (or suggesting that they will soon be so), others suggesting 85%, so I went with 90%.
	* Note that Near Future Propulsion xenon gas tanks are going to get buffed to better than 90% (closer to 95%).  I figure that this is fair enough, given that they're bigger.
	* Speaking of NFP, its argon and liquid-hydrogen tanks are already at real or predicted tank-mass fractions, so I'm not going to touch them.  (My comparison to the Space Shuttle External Tank in a previous version was unfair, because the ET just had to store fuel for a few minutes to get into orbit, while NFP's tanks are meant for long-term "cryogenic" storage.)
	* However, Cryogenic Engines takes something of a penalty for its LH2 tank mass fraction, and it inherits the stock LFO storage penalties, so I'll still keep the modified fuel-switching patch available.
* Liquid Hydrogen tanks (from Near Future Propulsion -- Freight Transportation Technology tanks are less efficient) are adjusted from 75% to 86% (50% reduction in dry mass), in line with the ET's hydrogen tank (it's about 2/3 the length, so its mass is thus estimated as 2/3 of the tank's dry mass, which combined with hydrogen's lightness makes it "only" 86% fuel).
* Parts that use the fuel-switching modules from Firespitter or Interstellar Fuel Switch have their dry mass reduced by only a factor of 2 (vs. 4 or 7 for LF/O/MP and Xenon/Argon, respectively); I figure the interchangeable-tank hardware hurts their fuel mass fraction.
	* Parts which use the "tankMass" variable won't get even that buff.  See "Known and anticipated issues" for more details.
* Engines' masses (excluding SRBs or LFBs, which get patched separately) reduced by 62.5% and (including LFBs) their thrusts are increased by 50%.  Comparing the stock engines to real RP-1/LOX rockets (as opposed to the LH2/LOX SSME, as I did previously), the "orbital" (i.e. stackable) stock engines have TWRs from 15-25, while real engines have TWRs from 60-100 (and getting up to 150 nowadays), so the TWRs need to be quadrupled.  The Skipper is actually a pretty good analog to the Merlin (several hundred kN of thrust, 2-3 meters tall), but rather than just cut the weight to match TWRs, I increase the thrust so that stock rockets don't need ridiculous numbers of engines (recall that SpaceX uses nine Merlins on their first stages -- and incidentally, it turns out that SpaceY engines get their TWRs pushed into the 120-150 range, just like SpaceX's.)
	* SRBs (baselining with the Kickback compared to the Space Shuttle SRBs) get their dry masses reduced by 40% and specific impulses get buffed by 40 seconds.  Their thrusts are left unchanged -- fuel density and TWR are already close to reality.
* Probes, command pods, and cargo bays are excluded from getting their masses straight-up cut in half by the fuel-switching or engine patches.  (If they have engines, their thrusts still get doubled.)

The result is that rockets have more Earth-like mass fractions and thus are able to achieve Earth-like payload masses without requiring the construction of horrible asparagus monsters.  To compare: with stock part masses, to get the Mk1-2 capsule (plus parachute and heat shield) up into space, I need to convert the Kerbal X into the "Kerbal X Triple-Heavy" (or "Kerbal 7"), with 6 asparagus-staged size 2 boosters identical to the core (actually, identical plus the round X200-6R tank from TurboNisuReloaded) and an extended upper-stage tank (an X200-32 instead of the stock -16).  It gets just shy of 7 tons into LEO (not counting the spent upper stage) with a 465-ton rocket (not counting the payload) which blows up the launchpad at takeoff.  With KSP-RishA, I can lose two of those boosters and get 9.5 tons into orbit (not counting the spent upper stage) with a 296-ton rocket (not counting the payload).   The Falcon 9 v1 got 10.5 tons into orbit and weighed 335 tons, using slightly less efficient engines than the Skipper and Poodle, so I figure I'm close enough for Kerbal work.

##Dependencies

KSP-RishA depends on [**Module Manager**](http://forum.kerbalspaceprogram.com/threads/55219) to function.

##Recommendations

KSP-RishA is mainly intended for use with [**Real Solar System**](http://forum.kerbalspaceprogram.com/threads/55145).  It's why I made it!

Big rocket fractions (i.e. 1 kg into LEO = 25+ kg of rocket) call for big rockets, so [**SpaceY**](http://forum.kerbalspaceprogram.com/threads/100408) and [**SpaceY Expanded**](http://forum.kerbalspaceprogram.com/threads/133301) and/or [**Behemoth Aerospace Engineering**](http://forum.kerbalspaceprogram.com/threads/124064) are recommended to get big rockets without big part counts.  [**Home-Grown Rockets**](http://forum.kerbalspaceprogram.com/threads/60974) is also great for payloads that are just too big for 1.25m rockets, but where 2.5m is overkill.  (Since thrust increases with the square of scale, and mass with the cube, all else being equal, the jump from 1.25 to 2.5 is actually much steeper than from 2.5 to 3.75, so I've found 1.875m surprisingly handy.)

If you want higher real-ish specific impulses as well as mass fractions, there's Nertea's [**Cryogenic Engines pack**](http://forum.kerbalspaceprogram.com/threads/117766), but be careful! By default, the pack will patch all LFO fuel tanks to be switchable to LH2/LO2 via InterstellarFuelSwitch, and because it uses the tankMass variable, KSP-RishA won't be able to give them a buff.  The relative penalty to tank mass outweighs the boost from the increased specific impulse.  To get a benefit from Cryogenic Engines, you have two options:

1. Delete the CryoEnginesFuelTankSwitcher patch, install the CryoEnginesLFO patch from the "Extras" folder (so the ISRU patch can also be deleted), and then open that patch, look for **cryoEngine-375-1** and fix the typo to **cryoengine-375-1** (make the "E" lowercase).  Their specific impulses get knocked down a bit from when they burn hydrolox, but they're still more efficient than the stock engines (if a little heavier and a hair less powerful).
2. Replace the CryoEnginesFuelTankSwitcher patch with the one I made in [**this post**](http://forum.kerbalspaceprogram.com/threads/131023?p=2136847&viewfull=1#post2136847).  As I demonstrate later in that post, you won't get quite as good mass for delta-V as in option 1 (because I don't improve the mass fraction quite as much), but you will have switchable fuel tanks (which is why I improve the mass fraction to 94-95% instead of 96-97%).

*(So, whoever it is that decides to index this mod on CKAN, you probably shouldn't actually put Cryogenic Engines in as a recommendation, since either option requires deleting or modifying Cryogenic Engines's files, which CKAN doesn't allow.)*

##Suggestions

Other addons that bring "real-ish" capabilities and challenges to Kerbal Space Program include:

* [**AntennaRange**](http://forum.kerbalspaceprogram.com/threads/56440), to "enforce and encourage antenna diversity".  Relaying is handled automatically, but only if you've used the right antennas for the job.  (We'll see how the 1.1 antenna system is when that comes.)
	* If you use this with Real Solar System, be sure to grab [**my range-extending patch**](https://github.com/Kerbas-ad-astra/RealSolarSystem/blob/master/GameData/RealSolarSystem/Compatibility/AntennaRangeExtender.cfg).
	* I'll also advertise my [**AntennaRange Relays**](http://forum.kerbalspaceprogram.com/threads/129704) contract pack (for [**Contract Configurator**](http://forum.kerbalspaceprogram.com/threads/101604)), to give some guidance and financial support for deploying relays.
* [**SCANSat**](http://forum.kerbalspaceprogram.com/threads/80369), to make biome and elevation maps (handy for planning landings) and require just a bit more effort when scanning for resources.
* [**USI Life Support**](http://forum.kerbalspaceprogram.com/threads/116790), for a life support system which is simple and forgiving (unless you configure it to kill Kerbals).
	* [**USI Kolonization Systems**](http://forum.kerbalspaceprogram.com/threads/79588), for ISRU that allows self-sustaining colonies (with some effort).
	* You should also consider picking up [**Extraplanetary Launchpads**](http://forum.kerbalspaceprogram.com/threads/59545) and [**OSE Workshop**](http://forum.kerbalspaceprogram.com/threads/108234) (and [**Kerbal Inventory System**](http://forum.kerbalspaceprogram.com/threads/113111), OSE's dependency), as an extension of NASA's real-world interest in in-situ manufacturing and repair.  (And to give your bases something new to do.)

Feel free to suggest other "real-ish" addons!  To give you some idea of what I'm looking for, addons suggested with KSP-RishA shall adhere to the following criteria:

1. They shall not require individual parts to be configured in order to function (as e.g. RealFuels does) -- if an addon can't work out-of-the-box with any other addons that people use, it doesn't belong in RishA.  (I guess AntennaRange could be said to violate this, since antennas do need their ranges configured individually, but antennas aren't that common and AR doesn't stop non-patched antennas from working, so I'm okay with including it.)
2. They shall improve the realism of some aspect of KSP that is not very or not at all realistic.  (KSP has no life support whatsoever, so USI-LS is included, but it has mildly realistic aerodynamic and heating systems, so FAR and Deadly Reentry are not.)

Of course, criterion zero is that I won't suggest an addon that I don't like and use (or have used or considered using) myself.  :)

##Download and install

* [**GitHub**](https://github.com/Kerbas-ad-astra/KSP-RishA/releases)
* CurseForge
* KerbalStuff

From there, just unzip the "KSP-RishA" folder into your GameData directory.

##Known and anticipated issues

Data that isn't stored as a straight-up number can't be easily modified by Module Manager.  This includes atmosphereCurve keys.  At the moment, if an SRB's atmosphereCurve has tangents defined (to my knowledge, this only affects the Boostertrons from RLA Stockalike), the tangents get squashed.  After Sarbian returns from vacation and formally releases an update to Module Manager with a fix I've contributed (version 2.6.10 or later), I'll be able to release a version of RishA that properly retains tangents and all will be well.

This also includes tankMass from FS/Interstellar Fuel Switch, which is stored as an arbitrarily-long series of semicolon-separated values.  There's a super-hacky technique to pick it apart into individual masses (again, using MM 2.6.10+ when it's released), do math on them, and put the results back together, but it results in ModuleManager reporting errors, so I'm not going to use it, and it's not really necessary since most switchable fuel tanks don't set individual tank masses (i.e. they're all zero).  However, this means that **you will get no benefit from SMURFF if you use Cryogenic Engines without removing or replacing the CryoEnginesFuelTankSwitcher patch** as I describe above.

Please let me know in the forum thread or on [**the GitHub issue tracker**](https://github.com/Kerbas-ad-astra/KSP-RishA/issues) if you find any others!

[SPOILER=Technical details on the tankMass issue]
Module Manager can query individual values from a character-separated list, but it doesn't have a way to figure out in advance how many list members there are, and even if it did (and it's certainly possible from a technical perspective), it doesn't have for-loops or the like, so it wouldn't be able to make use of that knowledge.  The answer is to query as many values as can possibly exist.  I believe that the record-holder for "most fuel-switch variants" is USI Kontainers, with 16 variants, so we'll use that.

We thus define sixteen temporary variables, tankMass0 to 15.  Each asks for the 0-15th member of tankMass.  When tankMass has fewer than 16 elements, the requests for variables which don't exist are left blank.  For example, if a part only has 8 variants, then tankMass8 to 15 will be blank, or "tankMass8 = " and so on in the config.

After breaking out tankMass, we buff the mass fraction by dividing each tankMassX variable by 2.  Since "blank" cannot resolve into a number, Module Manager throws errors for trying to divide any blank tankMassX by 2, and leaves them blank.

The modified tankMassX values are then reassembled into tankMass.  Parts that started with fewer than 16 tank masses end up with lots of semicolons in a row at the end, separating blank values.  These are easily trimmed by a regular expression replacement in the final cleanup patch.

In the end, the technique works as intended, but it leaves an ugly error message, which is why I'm not interested in using it.
[/SPOILER]

##Version history and changelog

* 2015 08 08: Initial release.
* 2015 09 XX: Renamed to KSP-RishA: Real-ish Adjustments (since we're not just touching mass anymore).
	* +50% to non-SRB engine thrusts and -62.5% to mass, to bring TWRs in line with RP-1/LOX engines and reduce need for ridiculous engine clusters.
	* +40 seconds to SRB Isp, to bring Kickbacks in line with Space Shuttle SRBs.
	* Mass reduction of resource containers is now proportional to their contents, so parts which have resources and do other things (e.g. command pods, wings with fuel) only get mass reduction corresponding to the part of them which holds resources (e.g. command pods are now slightly lighter, but not by a factor of 4).
	* New patch to act on Procedural Parts.

##Roadmap

As I get the time, I'll publish to CurseForge and KerbalStuff.

If you find any classes of parts (i.e. anything that can be described by using Module Manager to filter by module, resource, mass, etc.) that get horribly mistreated (either too much mass reduction or too little), I'll make an adjustment, but I have zero interest in making adjustments for individual parts -- the whole point of KSP-RishA is to avoid that level of complication.

##Credits

Thanks are owed to NathanKell and the entire Realism Overhaul team for making an incredibly detailed, thoroughly researched and calculated system...and convincing me to make something simpler.  :wink:

Even more thanks are owed to ialdeboath and sarbian for the power of Module Manager.  Seriously, half of my addons wouldn't exist if not for them.

##License

KSP Real-ish Adjustments ("KSP-RishA") is copyright 2015 Kerbas_ad_astra.  Configuration files are released under the [**Apache 2.0 license**](https://www.apache.org/licenses/LICENSE-2.0).  All other rights (e.g. the KSP-RishA logo) reserved.