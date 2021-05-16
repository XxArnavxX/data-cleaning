import pandas as pd

rd = pd.read_csv("./cleaning.csv")
print(rd.shape)
del rd["hyperlink"]
print(rd.shape)
del rd["temp_planet_date"]
del rd["temp_planet_mass"]
del rd["pl_letter"]
del rd["pl_controvflag"]
del rd["pl_name"]
del rd["pl_pnum"]
del rd["pl_orbper"]
del rd["pl_orbpererr1"]
del rd["pl_orbpererr2"]
del rd["pl_orbperlim"]
del rd["pl_orbsmax"]
del rd["pl_orbsmaxerr1"]
del rd["pl_orbsmaxerr2"]
del rd["pl_orbsmaxlim"]
del rd["pl_orbeccen"]
del rd["pl_orbeccenerr1"]
del rd["pl_orbeccenerr2"]
del rd["pl_orbeccenlim"]
del rd["pl_orbincl"]
del rd["pl_orbinclerr1"]
del rd["pl_orbinclerr2"]
del rd["pl_orbincllim"]
del rd["pl_bmassj"]
del rd["pl_bmassjerr1"]
del rd["pl_bmassjerr2"]
del rd["pl_bmassjlim"]
del rd["pl_bmassprov"]
del rd["pl_radj"]
del rd["pl_radjerr1"]
del rd["pl_radjerr2"]
del rd["pl_radjlim"]
del rd["pl_dens"]
del rd["pl_denserr1"]
del rd["pl_denserr2"]
del rd["pl_denslim"]
del rd["pl_ttvflag"]
del rd["pl_kepflag"]
del rd["pl_k2flag"]
del rd["pl_nnotes"]
del rd["ra_str"]
del rd["ra"]
del rd["dec_str"]
del rd["dec"]
del rd["st_dist"]
del rd["st_disterr1"]
del rd["st_disterr2"]
del rd["st_distlim"]
del rd["gaia_dist"]
del rd["gaia_disterr1"]
del rd["gaia_disterr2"]
del rd["gaia_distlim"]
del rd["st_optmag"]
del rd["st_optmagerr"]
del rd["st_optmaglim"]
del rd["st_optband"]
del rd["gaia_gmag"]
del rd["gaia_gmagerr"]
del rd["gaia_gmaglim"]
del rd["st_teff"]
del rd["st_tefferr1"]
del rd["st_tefferr2"]
del rd["st_tefflim"]
del rd["st_mass"]
del rd["st_masserr1"]
del rd["st_masserr2"]
del rd["st_masslim"]
del rd["st_rad"]
del rd["st_raderr1"]
del rd["st_raderr2"]
del rd["st_radlim"]
del rd["rowupdate"]
del rd["pl_facility"]
print(rd.shape)
rd = rd.rename({
    "pl_hostname": "solar_system_name",
    "pl_discmethod": "planet_discovery_method",
    "pl_orbincl": "planet_orbital_inclination",
    "pl_dens": "planet_density",
    "ra_str": "right_ascension",
    "dec_str": "declination",
    "st_teff": "host_temperature",
    "st_mass": "host_mass",
    "st_rad": "host_radius"
},axis = "columns")
rd.to_csv("cleaneddata.csv")