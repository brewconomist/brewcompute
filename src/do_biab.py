#! /usr/bin/env python3
import argparse
import biab_eq as be


def main():
    parser = argparse.ArgumentParser(
        description='Prints vital measurements of BIAB recipe')
    parser.add_argument('-gw', '--grain_wt',
                        help='Weight of grain in lbs',
                        required=True)
    parser.add_argument('-igt', '--init_grain_temp',
                        help='Initial temperature of grain in F',
                        required=True)
    parser.add_argument('-tmt', '--target_mash_temp',
                        help='Target mash temperature of grain in F',
                        required=True)
    parser.add_argument('-tog', '--target_og',
                        help='Target original gravity',
                        required=True)

    args = vars(parser.parse_args())

    grain_wt = float(args['grain_wt'])
    init_grain_temp = float(args['init_grain_temp'])
    target_mash_temp = float(args['target_mash_temp'])
    target_og = float(args['target_og'])

    strike_water_vol = be.strike_water_vol(grain_wt=grain_wt)
    strike_water_temp = be.strike_water_temp(init_grain_temp=init_grain_temp,
                                             strike_water_vol=strike_water_vol,
                                             grain_wt=grain_wt,
                                             target_mash_temp=target_mash_temp)
    preboil_grav = be.preboil_grav(target_og=target_og)

    print("Hello there.\n\nYour Brew-in-a-bag recipe assumes")
    print(f"{grain_wt} lbs of grain.")
    print(f"{init_grain_temp} F room grain temperature.")
    print(f"{target_mash_temp} F target mash temp.")
    print(f"{target_og} target OG.\n")
    print("Resulting process metrics")
    print(f"1. Fill strike water volume to {strike_water_vol:.2f} gallons.")
    print(f"2. Heat strike water temp to {strike_water_temp:.2f} F.")
    print(f"3. Verify preboil gravity is {preboil_grav:.3f} after mash.")


if __name__ == '__main__':
    main()
