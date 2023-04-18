import numpy as np

# If the filter names and central wavelength are different from
# the global definitions in gemini_instruments/gemini/lookup.py
# redefine them here in filter_wavelengths.

filter_wavelengths = {
#    'r' : 0.60,
}

array_properties = {
    # EDIT AS NEEDED
    # somehow the gain needs to be a list
    "gain"  :  np.array([3]),   # electrons/ADU  (MADE UP VALUE for example)
    "read_noise"  :  np.array([5]),   # electrons/ADU  (MADE UP VALUE for example)

}
