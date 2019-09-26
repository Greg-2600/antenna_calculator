#!/usr/bin/python
import argparse

def antenna_calculator(frequency):
    light_speed_meters = float('299792458')
    light_speed_meters_via_copper = light_speed_meters * 0.95

    frequency_in_kilo = frequency * 1000

    wave_length_meters = light_speed_meters_via_copper / frequency_in_kilo / 1000
    wave_length_feet = wave_length_meters / 0.3048

    quarter_wave_length_meters = wave_length_meters * 0.25
    quarter_wave_length_feet = quarter_wave_length_meters / 0.3048

    dipole_element_meters = wave_length_meters / 2
    dipole_element_feet = dipole_element_meters / 0.3048

    #inches = float(wave_length) / .3048 % 1 * 12

    print ('light speed: %s' % light_speed_meters)
    print ('light speed via copper: %s' % light_speed_meters_via_copper)
    print ('input frequency: %s' % frequency)
    print ('frequency in kilocycles: %s' % frequency_in_kilo)
    print ('wave length in meters: %s' % wave_length_meters)
    print ('wave length in feet: %s' % wave_length_feet)
    print ('quarter wave length in meters: %s' % quarter_wave_length_meters)
    print ('quarter wave length in feet: %s' % quarter_wave_length_feet)
    print ('dipole element length in meters: %s' % dipole_element_meters)
    print ('dipole element length in feet: %s' % dipole_element_feet)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='calculate antenna properties by frequency')
    parser.add_argument('frequency', type=float, help='transmission frequency')
    args = parser.parse_args()
    antenna_calculator(args.frequency)
