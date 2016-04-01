#SMURFF: Simple Module adjUstments for Real-ish Fuel-mass Fractions

*For people who want real-ish fuel mass fractions without too much hassle.  Formerly "Simple Mass adjUstments for Real-ish Fuel-mass Fractions."*

![SMURFF logo](https://github.com/Kerbas-ad-astra/SMURFF/raw/master/SMURFF%20logo.png)

##Features

SMURFF is a Module Manager patch that reduces the dry masses of fuel tanks and engines and improves engine performance so that KSP rockets can have fuel mass fractions closer to what we make in the real world, without going into per-part configurations like e.g. Realism Overhaul.

Most of a real rocket's structural strength comes from the fuel inside of it, rather than the tanks themselves -- the "tank" is just a metal shell to hold the fuel together.  KSP fuel tanks, on the other hand, seem to be made of lead plates and rebar.  This is all well and good for a planet where you only need 3.5 km/s to get to orbit, but it's not a lot of fun for the real solar system.  To help ease the transition to RSS (without requiring per-part configurations, thus allowing *any* mods to be supported), SMURFF makes several adjustments to engines, tanks, crew modules, and heat shields.  These adjustments are calibrated so that stock and stockalike-balanced parts will have their performance (TWR, fuel mass fraction, and ballistic coefficient) improved to be "real-ish" -- representative of typical aerospace technology of the last few decades, so that rockets built in RSS or 10X have mass fractions similar to real rockets.  You can reduce the buffs applied to parts (without tinkering with the mathematics) by reducing the values of "**tanklever**", "**enginelever**", and "**podlever**" at the top of SMURFF.cfg (or with a patch).  When they're set to 1 (as they are by default), the adjustments are made at their full values, and when they're set to 0, parts are left at stock performance values.  In-between is in-between, so those interested in intermediate-difficulty solar systems may want to experiment with setting the values to 0.5.

There are some built-in protections to prevent part masses from being sent into negative values, but otherwise, SMURFF will patch parts as if their mass and thrust values are balanced with stock parts.  If you want to exclude parts from being patched (e.g. because they already have real-ish TWR), include "**SMURFFExclude = true**" in the top-level config.  To avoid griping from KSP when SMURFF is not installed, you can use a patch like this one:

```
@PART[whatever_parts]:NEEDS[SMURFF]
{
	%SMURFFExclude = true
}
```

The specific adjustments are as follows:

* Stock and stockalike liquid fuel tanks (LFO, LF, Monoprop) have a fuel mass fraction of 87-89%; SMURFF increases this to 96-97% by reducing dry mass by 75%, putting them in line with real spacecraft fuel tanks.
	* Tanks that have fuel-switching patches from Stock Fuel Switch or Cryogenic Engines will get the appropriate mass buff for their equivalent Liquid Fuel and Oxidizer contents.
	* "Lifter" liquid-hydrogen tanks from CryoTanks get their LH2 mass fractions adjusted from 74% to 63% (65% *increase* in dry mass).  Because of the LFO buff, hydrolox "lifter" fuel tanks still go from 86% to 89% fuel by mass.
	* Zero boiloff LH2 tanks get their LH2 mass fractions adjusted from 69% to 46% (166% *increase* in dry mass).
	* Other parts with switchable fuel tanks get their dry masses divided by 4, except for parts which are switchable in-flight, which only get a 50% dry mass reduction.
* Xenon gas tanks are adjusted from 56% to 90% (86% reduction in dry mass).  I've seen some NASA sources saying xenon tanks are 95% fuel (or suggesting that they will soon be so), others suggesting 85%, so I went with 90%.
	* Argon gas tanks from Near Future Propulsion are adjusted from 56% to 62% fuel (20% reduction in dry mass).  They match the efficiency of stock xenon tanks for gameplay balance reasons, but in reality, xenon tanks are much more efficient, and argon not nearly as much (xenon atoms are heavier, so a much greater mass of xenon can be packed into a given tank design).  The benefit of argon is that it is more abundant (and thus cheaper) than xenon by orders of magnitude.  For large missions, the reduced fuel cost may be enough to make up for the mass penalty.
	* If anyone has a reference for the mass-efficiency of lithium storage and vaporization systems for spacecraft, I'd be happy to hear it.  :)  Until then, I'm leaving the lithium tanks as-is.
* Bipropellant (LFO and LH2/Ox -- or anything with Oxidizer) rocket engines' thrusts are increased by 50%.  Any that are not crew containers or multi-mode engines also get a 62.5% reduction in mass.  Comparing the stock LFO engines to real RP-1/LOX rockets (as opposed to the LH2/LOX SSME, as I did previously), the "orbital" (i.e. stackable) stock engines have TWRs from 15-25, while real engines have TWRs from 60-100 (and getting up to 150 nowadays), so the TWRs need to be quadrupled.  The Skipper is actually a pretty good analog to the Merlin (several hundred kN of thrust, 2-3 meters tall), but rather than just cutting the weight to match TWRs, I increase the thrust so that stock rockets don't need ridiculous numbers of engines (recall that SpaceX uses nine Merlins on their first stages -- and incidentally, it turns out that SpaceY engines get their TWRs pushed into the 120-150 range, just like SpaceX's).
	* SRBs (baselining with the Kickback compared to the Space Shuttle SRBs) get their dry masses reduced by 40% and specific impulses get buffed by 40 seconds.  Their thrusts are left unchanged -- fuel density and TWR are already close to reality.
	* Nuclear thermal rockets, jet engines, monopropellant rockets, and ion thrusters are left alone.  (Oxidizer-burning modes of multi-mode engines still get the thrust buff.)
* Crew containers (pods, cockpits, cabins, etc.) and heat shields have their masses reduced by half (and their pyrolysisLossFactor doubled).  I justify this by looking at the mass-per-passenger of space capsules and jet liners, ballistic coefficents, and comparing crew cabins to fuel tanks of the same size.  For example, the Mk1-2 command pod weighs as much as the Apollo Command Module despite being nearly 40% smaller (by diameter -- 26% of the volume) and carrying half-sized astronauts.  The Mk1 and Mk2 crew cabins weigh as much as a full fuel tank of the same size, despite being mostly air-filled.  Same for heat shields -- the Apollo heat shield was 3.9 meters across and weighed 850 kg, vs. 2800 kg for the stock 3.75m heat shield.  (The reason that I didn't cut heat shield masses by 70% is so that shields can still be used for landing larger masses than just a capsule.)
* Most of the patches stack (e.g. a service module with both monoprop and liquid fuel will have its mass reduced appropriately), but not the ones that divide tank mass by a factor (crew capsule, bipropellant engine, and general-purpose switchable tank) -- only one of those may apply to any part, and they get applied in that order.

The result is that rockets have more Earth-like mass fractions and thus are able to achieve Earth-like payload masses without requiring the construction of horrible asparagus monsters.  To compare: with stock part masses, to get the Mk1-2 capsule (plus parachute and heat shield) up into space, I need to convert the Kerbal X into the "Kerbal X Triple-Heavy" (or "Kerbal 7"), with 6 asparagus-staged size 2 boosters identical to the core (actually, identical plus the round X200-6R tank from TurboNisuReloaded) and an extended upper-stage tank (an X200-32 instead of the stock -16).  It gets just shy of 7 tons into LEO (not counting the spent upper stage) with a 465-ton rocket (not counting the payload -- almost 70 times as much rocket as payload) which blows up the launchpad at takeoff.  With SMURFF, I just have to make the Kerbal X into the "Kerbal Xtended" by doubling the upper-stage fuel tank (the stock Kerbal X is entirely capable of getting into orbit on its own, but the extension is necessary to add the heat shield...), putting 3.5 tons into orbit (not counting the spent upper stage) with a 114-ton rocket (not counting the payload -- 33 times as much rocket as payload).   The Falcon 9 v1 got 10.5 tons into orbit and weighed 335 tons (32 times as much rocket as payload), using slightly less efficient engines than the Skipper and Poodle, so I figure I'm close enough for Kerbal work.



##Dependencies

SMURFF depends on [**Module Manager**](http://forum.kerbalspaceprogram.com/threads/55219) version **2.6.16 or later** to function.

##Recommendations

SMURFF is mainly intended for use with [**Real Solar System**](http://forum.kerbalspaceprogram.com/threads/55145).  It's why I made it, and that's where the default balance is set.  Try setting the levers to 0.5 for intermediate solar systems, like 64K or SKY.

Big rocket fractions (i.e. 1 kg into LEO = 25+ kg of rocket) call for big rockets, so [**SpaceY**](http://forum.kerbalspaceprogram.com/threads/100408) and [**SpaceY Expanded**](http://forum.kerbalspaceprogram.com/threads/133301) (alternatively, [**Behemoth Aerospace Engineering**](http://forum.kerbalspaceprogram.com/threads/124064)) are recommended to get big rockets without big part counts.  [**Home-Grown Rockets**](http://forum.kerbalspaceprogram.com/threads/60974) is also great for large upper stages and for payloads that are just too big for 1.25m rockets, but where 2.5m is overkill.  (Since thrust increases with the square of scale, and mass with the cube, all else being equal, the jump from 1.25 to 2.5 is actually much steeper than the jump from 2.5 to 3.75, so I've found 1.875m parts to be surprisingly handy.)

If you want higher real-ish specific impulses as well as mass fractions, there's Nertea's [**Cryogenic Engines pack**](http://forum.kerbalspaceprogram.com/threads/117766).  (Note that there is now no need to replace its fuel-switch patch, if you choose to use it -- in fact, you should probably make sure that you have the original patch, if you think you might have replaced it with the modified one I provided for the initial release, to ensure that tanks don't get double-buffed.)

##Suggestions

Other addons that bring "real-ish" capabilities and challenges to Kerbal Space Program include:

* [**AntennaRange**](http://forum.kerbalspaceprogram.com/threads/56440), to "enforce and encourage antenna diversity".  Relaying is handled automatically, but only if you've used the right antennas for the job.  (We'll see how the 1.1 antenna system is when that comes.)
	* I'll also advertise my [**AntennaRange Relays**](http://forum.kerbalspaceprogram.com/threads/129704) contract pack (for [**Contract Configurator**](http://forum.kerbalspaceprogram.com/threads/101604)), to give some guidance and financial support for deploying relays.
* [**SCANSat**](http://forum.kerbalspaceprogram.com/threads/80369), to make biome and elevation maps (handy for planning landings) and require just a bit more effort when scanning for resources.
* [**USI Life Support**](http://forum.kerbalspaceprogram.com/threads/116790), for a life support system which is simple and forgiving (unless you configure it to kill Kerbals).
	* [**USI Kolonization Systems**](http://forum.kerbalspaceprogram.com/threads/79588), for ISRU that allows self-sustaining colonies (with some effort).
	* You should also consider picking up [**Extraplanetary Launchpads**](http://forum.kerbalspaceprogram.com/threads/59545) and [**OSE Workshop**](http://forum.kerbalspaceprogram.com/threads/108234) (and [**Kerbal Inventory System**](http://forum.kerbalspaceprogram.com/threads/113111), OSE's dependency), as an extension of NASA's real-world interest in in-situ manufacturing and repair.  (And to give your bases something new to do.)

Feel free to suggest other "real-ish" addons!  To give you some idea of what I'm looking for, addons suggested with SMURFF shall adhere to the following criteria:

1. They shall not require individual parts to be configured in order to function (as e.g. RealFuels does) -- if an addon can't work out-of-the-box with any other addons that people use, it doesn't belong on the list.  (I guess AntennaRange could be said to violate this, since antennas do need their ranges configured individually, but antennas aren't that common and AR doesn't stop non-patched antennas from working, so I'm okay with including it.)
2. They shall improve the realism of some aspect of KSP that is not very or not at all realistic.  (KSP has no life support whatsoever, so USI-LS is included, but it has mildly realistic aerodynamic and heating systems, so FAR and Deadly Reentry are not.)

Of course, criterion zero is that I won't suggest an addon that I don't like and use (or have used or considered using) myself.  :)

##Download and install

* [**GitHub**](https://github.com/Kerbas-ad-astra/SMURFF/releases)
* CurseForge

From there, just unzip the "SMURFF" folder into your GameData directory.

##Known and anticipated issues

None at this time.  Please let me know in [**the forum thread**](http://forum.kerbalspaceprogram.com/threads/131023) or on [**the GitHub issue tracker**](https://github.com/Kerbas-ad-astra/SMURFF/issues) if you find any!

##Version history and changelog

* 2015 08 08: Initial release.
* 2015 11 19 (1.1): Renamed to Simple **Module** adjUstments for Real-ish Fuel-mass Fractions (since we're not just touching mass anymore).
	* +50% to non-SRB engine thrusts and -62.5% to mass, to bring TWRs in line with RP-1/LOX engines and reduce need for ridiculous engine clusters.
	* +40 seconds to SRB Isp, to bring Kickbacks in line with Space Shuttle SRBs.
	* Mass reduction of resource containers is now proportional to their contents, so parts which have resources and do other things (e.g. command pods, wings with fuel) only get mass reduction corresponding to the part of them which holds resources (e.g. command pods are now slightly lighter because of their monopropellant storage, but not by a factor of 4).
	* New patch to act on Procedural Parts.
	* Based on RealFuels data and further research, LH2 and argon mass fractions no longer improved.
	* Adjusted patch to properly grab all engine modules.
	* Compatible with Stock Fuel Switch and Cryogenic Engines.
		* **If you replaced or modified Cryogenic Engines's fuel switcher patch, make sure you restore it to the original -- otherwise, tanks might get double-buffed.**
* 2015 11 20 (1.1.1): Minor bug fixes.
	* Fixed Procedural Parts patch (thanks to speedwaystar).
	* Excluded air-breathing jets, nuclear thermal rockets, monopropellant engines, and ion engines from TWR buffs.  (They're close enough to reality already.)
* 2015 11 22 (1.1.2): More compatibility (inspired by Atomic Age).
	* Improved selectivity of engine mass buff by excluding multi-mode engines and IntakeAtm-breathing engines.  (All Oxidizer-burning engine modes will still get a thrust increase.)
* 2015 12 07 (1.1.3): More selection adjustments.
	* Changed engine mass buffs to apply to engines which only have oxidizer-burning modes (so that SpaceY's engines get buffed -- they use a MultiModeEngine module to simulate the all-nozzle vs. center-out/center-only modes of operation, so excluding all multi-mode engines wasn't fair.)
* 2016 01 08 (1.1.4): Argon adaptation
	* New ArgonGas patch for the tank efficiency changes made in Near Future Propulsion 0.6.0.
	* **I've made some slight changes in the backend for handling Cryogenic Engines.** In my testing, I haven't noticed any changes in spacecraft mass (either in the VAB or in flight), but please be careful!
* 2016 01 27 (1.2): Entry, Descent, and Landing
	* Masses of crew containers and heat shields are reduced by half, to permit reduced (and reasonable) capsule ballistic coefficients.  Now pods are more likely slow down in time to get their chutes open.
	* Added a "reserved mass" system so that engines and pods only modify mass which is not accounted for by fuel tanks and batteries.
	* Added a "SMURFFCONFIG" section -- adjust the "tanklever", "enginelever", and "podlever" variables to control how much of a buff is applied.  1 for real-ish performance (default), 0 to leave stock values alone, and everything in between is in between.  Try 0.5 for the likes of 64k or SKY.
	* Changed patches to run FOR[zSMURFF], so that the patches run later.  SpaceY's engines now get properly buffed when Cryogenic Engines is installed.  (SpaceY replaces the ModuleEnginesFX modules of some engines in that circumstance, and since SpaceY comes after SMURFF, the thrust buff was being overwritten.)
	* Added a "fix" for parts whose mass gets sent into the negatives (i.e. any part which weighs less than it "should" by stockalike standards): their masses get restored to their initial values.
	* Added support for "SMURFFExclude" -- add "SMURFFExclude = true" to any part you don't want to get buffed.
* 2016 02 02 (1.2.1): De-icing
	* Adapted to new Cryogenic Tanks LH2 mass fractions and tank setups.  (LH2 tanks actually get hit with the nerf-bat.)
* 2016 02 20 (1.2.2): Sore throat
	* Added some new patch logic to catch ablative engines.
* 2016 03 17 (1.3): Wild Blue Yonder
	* Parts with WBIResourceSwitcher (e.g. the Titan fuel tanks from MOLE) are now included in the switchable-tanks patches.
	* Switchable (FS and Interstellar Fuel Switch) tanks with different tankMasses now get proper mass buffs, thanks to the new array-editing features in Module Manager.
		* This feature is only present in MM version 2.6.16 or later, so **this version and later versions are not compatible with KSP 1.0.4.**

##Roadmap

As I get the time, I'll publish to CurseForge and CKAN.

If you find any classes of parts (i.e. anything that can be described by using Module Manager to filter by module, resource, mass, etc.) that get horribly mistreated, I'll make an adjustment.  That being said, I'm not planning to make special patches for parts that are already themselves outliers -- the whole point of SMURFF is to avoid that level of complication.

##Credits

Thanks are owed to NathanKell and the entire Realism Overhaul team for making an incredibly detailed, thoroughly researched and calculated system...and convincing me to make something simpler.  :wink:  The tank-mass spreadsheet was a handy resource!

Even more thanks to ialdeboath and sarbian for the power of Module Manager.  Seriously, half of my addons wouldn't exist if not for them.

##License

Simple Module adjUstments for Real-ish Fuel-mass Fractions ("SMURFF") is copyright 2015 Kerbas_ad_astra.  Configuration files are released under the [**Apache 2.0 license**](https://www.apache.org/licenses/LICENSE-2.0).  All other rights (e.g. the SMURFF logo) reserved.