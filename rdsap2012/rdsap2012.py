# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 13:51:21 2023

@author: cvskf
"""

#%% import packages
import csv




#%% Appendix S: Reduced Data SAP for existing dwellings

# RdSAP 2012 version 9.94 (20th September 2019)

# "Reduced Data SAP (RdSAP) has been developed by government for use 
# in existing dwellings based on a site survey of the property, when 
# the complete data set for a SAP calculation is not available. 
# It consists of a system of data collection (defined in Table S19) 
# together with defaults and inference procedures, as defined by 
# the rules given in this Appendix, that generate a complete set 
# of input data for the SAP calculation. 
# For any item not mentioned in this Appendix, the procedures and data 
# given elsewhere in this document apply.

# The calculation starting from reduced data is done in two stages. 
# First the reduced data set is expanded into a full data set (see S14 
# for rounding rules), and then the SAP calculation is undertaken 
# using the expanded data set. 
# The actual SAP calculation is therefore identical, whether starting 
# from a reduced data set or a full data set.

# This Appendix forms part of SAP 2012 and provides a methodology for 
# existing dwellings that is compliant with the Energy Performance of 
# Buildings Directive. It is not appropriate for new dwellings for which 
# all data for the SAP calculation should be acquired related to the 
# dwelling concerned.

# This Appendix contains the data and rules for expanding the data 
# collected in a Reduced Data survey into the data required for the 
# SAP calculation. Information in shaded boxes is primarily concerned 
# with data collection and is addressed to energy assessors.

# Table S19 lists the Reduced Data set."


#%% S1 Dwelling types

# "Dwellings are classified as one of
# – house 
# – bungalow 
# – flat 
# – maisonette
# – park home

# and one of
# – detached 
# – semi-detached 
# – mid-terrace 
# – end-terrace 
# – enclosed mid-terrace 
# – enclosed end-terrace"

# S1.1 Park homes

# "The Energy Performance of Buildings regulations do not require an EPC
# for a park home. However, data are provided to enable the assessment
# of a park home."

# S1.1.1 Data for park homes

### - TO DO

# S1.1.2 Insulation improvements for park homes

def insulation_improvement_for_park_homes(
        u_value_existing, 
        r_insulation
        ):
    """
    p2
    
    :param u_value_existing: The U-value of the existing element
    :type u_value_existing: float
    :param r_insulation: The thermal resistance added
    :type r_insulation: float
    
    :returns: The improved U-value of the wall, floor or roof
    :rtype: float
    
    """
    
    return 1.0 / ( (1.0/u_value_existing) + r_insulation )




#%% S2 Age bands

# "A set of age bands is defined according to Table S1 for the purposes of 
# assigning U-values and other data."
 

def get_table_S1_age_bands():
    ""
    d={}
    for x in list(csv.DictReader(open('table_S1_age_bands.csv'))):
        d.setdefault(x['age_band'],{}).setdefault(x['country'],{}) \
            [x['dwelling_type']]=x['years_of_construction']
    return d

table_S1_age_bands=get_table_S1_age_bands()
print(table_S1_age_bands)



#%% S3 Areas



# S3.1 Definition of the extent of the dwelling

# S3.2 Illustrations of roof rooms




#%% S4 Parameters for ventilation rate


#%% S5 Construction types and U-values



#%% S6 Conservatory


#%% S7 Solar gains


#%% S8 Windows and doors


#%% S9 Room count and living area

#%% S10 Space and water heating


#%% S11 Additional items


#%% S12 Electricity tariff


#%% S13 CLimatic data



#%% S14 Rounding of data


#%% S15 Addendum to EPCs


#%% S16 Improvement measures


#%% S17 Data to be collected


