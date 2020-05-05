

def strike_water_vol(grain_wt: float,
                     postboil_vol: float = 6,
                     boil_duration: float = 1.0,
                     grain_absorbtion: float = 0.1,
                     boil_off_rate: float = 1.0) -> float:
    """Computes BIAB strike water volume based primarily on grain weight.

    Calculation here:
    https://www.homebrewersassociation.org/wp-content/uploads/
    How-To-Brew-in-a-Bag.pdf.

    Args:
    grain_wt: Grain weight in lbs
    postboil_vol: Volume after boil in gal, typically batch vol + 1 (default 6)
    boil_duration: Boil duration in gal/hr (default 1)
    grain_absorbtion:  Grain absorbtion in gal/lbs (default 0.1)
    boil_off_rate: Boil off rate in gal/hr (default 1)
    Returns:
    Strike water volume in gal, i.e. fill volume before adding grain
    """
    return (grain_absorbtion * grain_wt +
            (postboil_vol + boil_duration * boil_off_rate))


def strike_water_temp(init_grain_temp: float,
                      strike_water_vol: float,
                      grain_wt: float,
                      target_mash_temp,
                      equip_temp_loss: float = 1) -> float:
    """Computes strike water temperature based primarily on initial mash temp.

    Calculation here http://howtobrew.com/book/section-3/
    the-methods-of-mashing/calculations-for-boiling-water-additions

    Args:
    init_grain_temp: Initial grain temp in F
    strike_water_vol: Strike water volume in gal
    grain_wt: Grain weight in lbs
    target_mash_temp: Target mash temp in F
    equip_temp_loss: Equipment temperature loss in F (default is 1)


    Returns:
    Strike water temperature in F i.e. temp to heat water before adding grain
    """
    # multiply vol by 4 to convert to quarts per pound
    r = strike_water_vol * 4.0/grain_wt
    t2 = target_mash_temp + equip_temp_loss
    return (0.2/r) * (t2 - init_grain_temp) + t2


def preboil_grav(target_og: float,
                 preboil_vol: float = 7,
                 postboil_vol: float = 6):
    """Computes preboil gravity to to verify before concluding mash

    Args:
    preboil_vol: Pre-boil volume in gal
    target_og: Target original gravity for primary fermentation e.g. 1.040
    postboil_vol: Postboil wort volume to be collected for primary fermentation
    """
    target_og = (target_og - 1.0) * 1000  # adjust to gravity points
    return (((postboil_vol * target_og) / preboil_vol)/1000) + 1.0
