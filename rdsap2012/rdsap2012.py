# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 13:51:21 2023

@author: cvskf
"""

#%% import packages
import csv
import os



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
    fp=os.path.join('tables','table_S1_age_bands.csv')
    for x in list(csv.DictReader(open(fp))):
        d.setdefault(x['age_band'],{}).setdefault(x['country'],{}) \
            [x['dwelling_type']]=x['years_of_construction']
    return d

table_S1_age_bands=get_table_S1_age_bands()
print(table_S1_age_bands)

# "From the 1960s, constructional changes have been caused primarily by 
# amendments to building regulations for the conservation of fuel and power, 
# which have called for increasing levels of thermal insulation. 
# The dates in Table S1 are generally one year after a change in regulations, 
# to allow for completion of dwellings approved under the previous regulations."

# "For a conversion which was a change of use (e.g. barn converted to 
# dwelling) or where a dwelling has been sub-divided (e.g. house to flats) 
# use the original construction date, unless there is documentary evidence 
# that all thermal elements have been upgraded to the building regulation 
# standards applicable at the conversion date. 
# Enter insulation levels only for those elements for which 
# evidence is available."

# "Age band L can apply to extensions added to an older property."

#%% S3 Areas

# Areas are determined separately for the main part of the dwelling and any extension. Horizontal dimensions can be measured either internally or externally.

# The measurements required are the floor area, exposed perimeter, party wall length and room height on each storey. Exposed perimeter includes the wall between the dwelling and an unheated garage or a separated conservatory and, in the case of a flat or maisonette, the wall between the dwelling and an unheated corridor.
# Internal dimensions are permissible in all cases. In the case of a house or bungalow external dimensions for area and perimeter are usually more convenient, except where access to all sides of the building is not possible or where there are differing wall thicknesses or other aspects that would make the dimensional conversion unreliable. When using external measurements for a dwelling joined onto another dwelling (semi-detached and terraced houses) the measurement is to the mid-point of the party wall. Flats and maisonettes are usually measured internally (although it is not a requirement of the specification that internal measurements are always used and if measured externally the measurement is to the mid-point of the party wall). Whichever is chosen the same basis must be used for all parts of the dwelling. Party wall length uses the same basis as exposed perimeter.
# Room heights are always measured internally within the room.

# State on site plans whether the dimensions recorded are external or internal. Where a combination of external and internal is used this must be made clear for each dimension indicated.
# When measuring internally, measure between the finished internal surfaces of the walls bounding the dwelling. Where that cannot be done directly (i.e. when measuring room by room) include an allowance for the thickness of internal partitions.
# Measure all perturbations (e.g. bay windows) but disregard chimney breasts unless assessor considers significant e.g. large inglenook.
# Vertical dimensions (room heights) are always measured internally within the room. Also, the floor area of room(s)-in-roof are always measured internally (irrespective of the dimensions basis for other storeys).
# Measure lengths to one decimal place (0.1 m) or better. Retain higher precision when that has been measured (especially room heights).
# If there is an alternative wall, it is identified as being part of the external wall of main dwelling or of one of the extensions. When calculating the area of alternative wall exclude the area of any windows and doors contained within it.
# Include the length of party wall between the dwelling being assessed and another heated space which can be: - another dwelling - commercial premises - a heated corridor or stairwell in a block of flats - a heated common area


# S3.1 Definition of the extent of the dwelling

# Generally rooms and other spaces, such as built-in cupboards, are included as part of the dwelling where these are directly accessible from the occupied area of the dwelling, whereas unheated spaces clearly divided from the dwelling are not.

# Basements

# Include in the assessment when accessed via a permanent fixed staircase such that one is able to walk downwards facing forwards and either:- - basement is heated via fixed heat emitters, or - basement is open to the rest of the dwelling, i.e. no door.
# A basement does not necessarily contain habitable rooms.
# Do not mix internal and external measurements. If a basement is included in the assessment, it is likely that internal dimensions will be used throughout the dwelling.

# Attics and roof rooms

# Include in the assessment when accessed via a permanent fixed staircase such that one is able to walk downwards facing forwards. Does not necessarily contain habitable rooms.
# For a roof room to be classed as such and not a separate storey, the height of the common wall must be less than 1.8 m for at least 50% of the common wall (excluding gable ends or party walls). The common wall is a vertical continuation of the external wall of the storey below.
# There is no explicit allowance for dormer windows except to include in the floor area of the roof rooms.
# See Figures S1 and S2 (next page).

# Rooms within a Mansard roof

# A storey having non-vertical walls of at least 70° pitch constitutes a separate storey; it is not treated as roof rooms. Use alternative wall if appropriate.

# Whole dwelling within roof

# When property is a single storey entirely located within a roof, enter it as: - lowest occupied level - timber frame construction of appropriate age band - room height 2.2 m - include area and perimeter measurements as a normal storey - enter roof as pitched roof.
# If there are two storeys within roof, enter the lower storey as above and the upper storey as rooms-in-roof.


# S3.2 Illustrations of roof rooms

# The following are all classified as roof rooms:
    
# Figure S1 : Roof rooms

# Where there is a common wall it is:
# - a roof room if the height of the common wall in the upper storey is less than 1.8 m;
# - a separate storey if greater or equal to 1.8 m:
# as illustrated in Figure S2.

# Figure S2 : Upper storey with common wall

# Mezzanine floor

# Enter the part of the property above and below the mezzanine deck as a two storey extension. Treat the remaining part as a single level with the full floor to ceiling/roof height.
# If the mezzanine is located such that it has no heat loss perimeter then assign a nominal 1 m perimeter to each floor of the mezzanine part and deduct 1 m from the heat loss perimeter of the other part.

# Porches

# If heated always include (separated or not).
# If external and not heated, disregard.
# If internal, not heated and thermally separated, disregard.
# (‘external’ means an addition protruding from the line of the external wall of the dwelling)

# Store rooms and utility rooms

# If heated always include.
# If accessible only via a separate external door and not heated, disregard
# If directly accessible, not heated and thermally separated, disregard

# Garages

# If heated from main heating system, always include. The presence of a boiler within the garage does not make it heated.


# S3.3 Extensions and alternative walls

# Provision is made for the main dwelling and up to four extensions, each with their own age band, dimensions and other characteristics. An extension can be alongside another part of the dwelling, or above another part of the dwelling or other premises. If alongside apply ground floor heat loss, if above another part of the same dwelling there is no floor heat loss for the extension and no roof loss for the part below it.

# Each building part can have an additional wall type, ‘alternative wall’, which is part of the external walls of the building part. The assessor provides the area of the alternative wall, which is deducted from the external wall area of the building part calculated as described in S3.6. The U-value of an alternative wall is established on the same basis as other walls, as described in S5 (but see also S3.13 in the case of a sheltered alternative wall).

# Extensions
#
# For a vertical extension (new upper floor above existing dwelling) enter the new upper floor as an extension with ‘same dwelling below’, and the original part with ‘same dwelling above’ for the roof description.
# Where an extension has been built over part of the existing dwelling, divide the part built over into two, one of which has ‘same dwelling above’ and for the other part describe the roof construction and insulation.
# It is possible for an extension to be both above and alongside the rest of the dwelling. Such a building part is not defined in RdSAP and in this case divide the extension into two, one above and the other alongside.

# Alternative wall

# In determining whether an alternative wall is applicable the significant features are construction type, dry lining, age band, insulation and whether sheltered by an unheated corridor.
# A sheltered wall between the dwelling and an unheated corridor or stairwell is always an alternative wall.
# Walls of the same construction but different thickness within a building part are not considered alternative walls unless they are stone walls.
# For stone walls assess thickness at each external elevation and at each storey and use alternative wall if the thickness varies by more than 100 mm.
# Disregard when less than 10% of total exposed wall area of the building part (including windows and doors) unless documentary or visual evidence exists of different retrofitted insulation either of the alternative wall or of the remaining wall in the building part. When entering alternative wall area into software exclude the area of any windows and doors contained in the alternative wall.
# Consolidate walls of same type.
# If there are two areas of external wall of different construction types within a building part that should be regarded as alternative wall, review the way in which the property has been divided to try and eliminate this situation. Where that is not possible the alternative wall is the one with the larger area.
# In the case of the wall separating the dwelling from an unheated corridor or stairwell, where this wall is of different construction or insulation to the external walls (e.g. not insulated but external walls are), make it an alternative wall and mark it as sheltered.


# S3.4 Adjustment to levels of storeys for houses and bungalows

# In the RdSAP data set, the dimensions of each building part start at “lowest occupied” and these may not align if a building part has a heated or unheated space below. If the lowest occupied floor of any extension is not a ground floor increase the level of each storey in that building part by 1.

# TO DO ?? "increase the level of each storey in tht building part by 1..."


# S3.5 Conversion to internal dimensions

# If horizontal dimensions are measured externally, they are converted to overall internal dimensions for use in SAP calculations by application of the appropriate equations in Table S2, using wall thickness of the main dwelling (or the appropriate wall thickness from Table S3 if thickness is unknown). The equations are applied on a storey-by-storey basis, for the whole dwelling (i.e. inclusive of any extension). This is done after any floor level adjustments (see S3.4).

# Heights are always measured internally within each room and handled by software according to S3.6.

def table_S2_conversion_of_dimensions_1(
        built_form_and_detachment,
        P_ext,  # measured external perimeter (of whole dwelling)
        A_ext,  # measured external area
        w  # wall thickness
        ):
    """
    p9
    
    Notes:
        1. Pext and Aext are the measured external perimeter and area (of whole dwelling)
        2. Pint and Aint are the calculated internal perimeter and area
        3. w is the wall thickness of the main dwelling
    
    """
    if built_form_and_detachment == 'detached':
        
        P_int = P_ext - 8 * w
        
        A_int = A_ext - w * P_int - 4 * w**2
        
    elif built_form_and_detachment in ['semi-detached', 'end-terrace']:
        
        if P_ext**2 > 8.0 * A_ext:
            
            P_int = P_ext - 5.0 * w
            
            a = 0.5 * (P_ext - (P_ext**2 - (8.0 * A_ext))**0.5)
            
            A_int = A_ext - (w * (P_ext + (0.5 * a))) + (3.0 * w**2)
            
        else:
            
            P_int = P_ext - (3.0 * w)
            
            A_int = A_ext - (w * P_ext) + (3.0 * w**2)
            
    elif built_form_and_detachment == 'mid-terrace':
        
        P_int = P_ext - (2.0 * w)
        
        A_int = A_ext - (w * (P_ext + (2.0 * A_ext / P_ext))) + (2 * w**2)
        
    elif built_form_and_detachment == 'enclosed mid-terrace':
        
        P_int = P_ext - w
        
        A_int = A_ext - (w * ((A_ext/P_ext) + (1.5 * P_ext))) + (1.5 * w**2)
        
    perimeter_ratio = P_int / P_ext
    
    area_ratio = A_int / A_ext
    
    return P_ext, A_ext, perimeter_ratio, area_ratio


def table_S2_conversion_of_dimensions_2(
        area,
        exposed_perimeter,
        party_wall_length,
        area_ratio,
        perimeter_ratio,
        wall_thickness
        ):
    """
    p9
    
    Notes:
        4. After obtaining the perimeter ratio and area ratio for the whole dwelling, multiply
        separately the measured perimeters and areas of (a) the main part of the dwelling
        and (b) any extension, by these ratios.
        5. In the case of a party wall reduce its length by 2w
    
    
    """

    area_internal = area * area_ratio
    
    exposed_perimeter_internal = exposed_perimeter * perimeter_ratio
    
    party_wall_length_internal = party_wall_length - (2 * wall_thickness)
    
    return area_internal, exposed_perimeter_internal, party_wall_length_internal


def get_table_S3_wall_thickness():
    ""
    d={}
    fp=os.path.join('tables','table_S3_wall_thickness.csv')
    for x in list(csv.DictReader(open(fp))):
        d.setdefault(x['country'],{}).setdefault(x['wall_type'],{}) \
            [x['age_band']]=x['wall_thickness']
    return d

table_S3_wall_thickness=get_table_S3_wall_thickness()
print(table_S3_wall_thickness)

# The values in Table S3 are used only when the wall thickness could not be measured.
    
# Wall thickness

# Measure wall thickness in mm of each external wall (elevation) and any alternative wall within a building part.

# It can be measured at door or window reveals or by internal/external measurement comparison (which can be direct measurement or estimated by counting bricks).

# Where thickness varies, obtain a weighted average. For example, a detached house with all side of equal length where the rear wall is 250 mm thick and the remaining walls are 350 mm thick, the average is (0.25 × 250) + (0.75 × 350) = 325 mm.


# S3.6 Heights and exposed wall areas

# Heights are measured internally within each room, and 0.25 m is added by 
# software to each room height except for the lowest storey, to obtain the 
# storey height. 
# For this purpose the lowest storey is considered separately for each 
# building part (main dwelling and any extension). 
# The lowest storey of a building part is the lowest for the dwelling 
# unless it has been indicated as having the same dwelling below. 

def storey_height(
        average_room_height,
        is_lowest_storey  # boolean - true if this is the lowst storey in the building part
        ):
    """
    p10
    
    """
    
    if is_lowest_storey:
        
        storey_height = average_room_height
        
    else:
        
        storey_height = average_room_height + 0.25
        
    return storey_height

# Gross areas (inclusive of openings) are obtained from the product of heat 
# loss perimeter (after conversion to internal dimensions if relevant) and 
# storey height, summed over all storeys. 

def gross_area(
        exposed_perimeters_internal,  # list of internal exposed perimeters, for each storey in building part
        storey_heights,  # list of storey heights, for each storey in building part
        ):
    """
    p10
    
    """
    result=0
    
    for exposed_perimeter_internal, storey_height in \
        zip(exposed_perimeters_internal,storey_heights):
        
        result += exposed_perimeter_internal * storey_height

    return result


# Party wall area is party wall length multiplied by storey height, 
# summed over all storeys.
        
def party_wall_area(
        party_wall_lengths_internal,  # list of internal party wall lengths, for each storey in a building part
        storey_heights  # list of storey heights, for each storey in building part
        ):
    """
    p10
    
    """    
    result=0
    
    for party_wall_length_internal, storey_height in \
        zip(party_wall_lengths_internal,storey_heights):
        
        result += party_wall_length_internal * storey_height

    return result
    

# For the main dwelling and any extension(s), window and door areas are 
# deducted from the gross areas to obtain the net wall areas for the heat 
# loss calculations, except for the door of a flat/maisonette to an unheated 
# stair or corridor which is deducted from the sheltered wall area (see S3.13).

def net_wall_area(
        gross_area,  # gross external wall area of building part
        window_area,  # total window area of building part
        door_area  # total external door area of building part
        ):
    """
    p10
    """
    net_wall_area = gross_area - window_area - door_area
    
    return net_wall_area


def net_sheltered_wall_area(
        gross_sheltered_wall_area,
        door_area  # flat/maisonette to an unheated stair or corridor
        ):
    """
    p10
    """
    return gross_sheltered_wall_area - door_area
        

# If an alternative wall is present, the area of the alternative wall is 
# recorded net of any openings in it and the alternative wall is identified 
# as part of the main wall or extension wall. 
# This area is subtracted from the net wall area of the building part 
# prior to the calculation of wall heat losses.

# TO DO


# S3.7 Door and window areas

# The area of an external door is taken as 1.85 m². 
# A door to a heated access corridor is not included in the door count.

def door_area(
        number_of_external_doors
        ):
    """
    """
    return number_of_external_doors * 1.85
    

# External doors except doors to an unheated corridor or stairwell are 
# taken as being in the main part of the dwelling.

# The door to an unheated corridor or stairwell is taken as part of the 
# sheltered wall it is within, and so is in the building part containing 
# the sheltered alternative wall (so not necessarily in the main dwelling).

# If the property has more than one door, doors except the first one 
# are directly to the outside and taken as being in the main part of 
# the dwelling.

# Total window area is assessed as being typical, more than typical, 
# much more than typical, less than typical, or much less than typical.

# In RdSAP the definition of what is a window and what is a door is defined 
# by the area of glazing in relation to the area of the whole opening, 
# i.e. door and frame. 
# To be classed as a window a glazed door and frame must contain glazing 
# amounting to 60% or more or its surface area. 
# Generally 60% or more glazing is likely to occur only in a patio door. 
# However a window with less than 60% glazing is not a door; a door always 
# provides a means of entry to the property.

# An external door is a door that forms part of the heat loss perimeter 
# of the dwelling. 
# A door to a heated access corridor is not included in the door count. 
# It is possible for a property to have no external door in the RdSAP data 
# set (when any entrance to the property is via patio doors with more than 
# 60% glazing which are counted as windows in SAP, or via a heated corridor).


# S3.7.1 Window area typical, more than typical or less than typical

# Window areas are obtained by application of the appropriate equation from 
# Table S4. 
# The equation used is chosen according to the age band of the main part 
# of the dwelling, with the resulting total window area apportioned 
# between main part and extension(s) pro rata to their floor areas. 
# If the window area of any part of the dwelling (main, extension, 2nd 
# extension etc) is greater than 90% of the exposed façade area of that 
# part, after deducting doors and alternative wall area if applicable to 
# that part, the window area is set equal to 90% of the façade area.

def get_table_S4_window_area():
    ""
    d={}
    fp=os.path.join('tables','table_S4_window_area.csv')
    for x in list(csv.DictReader(open(fp))):
        y=d.setdefault(x['age_band_of_main_dwelling'],{}).setdefault(x['dwelling_type'],{})
        y['window_area_coefficient']=x['window_area_coefficient']
        y['window_area_constant']=x['window_area_constant']
    return d

table_S4_window_area=get_table_S4_window_area()
print(table_S4_window_area)


def window_area(
        TFA,  # total floor area of main part plus any extension
        window_area_coefficient,
        window_area_constant
        ):
    """
    p11
    """
    WA = window_area_coefficient * TFA + window_area_constant

    return WA

# This does not include conservatories, which are treated separately: see S6.

# The window areas calculated using Table S4 are to be reduced by 25% if it 
# is assessed as being less than typical for the age and type of property, 
# and increased by 25% if assessed as being more than typical for the age 
# and type of property.

# When assessing window area consider the whole dwelling (windows, glazed 
# doors and roof lights), including any extensions (but not conservatories).

# Typical applies if the surface area of the glazing in the dwelling is 
# essentially as would be expected of a typical property of that age, type, 
# size and character. 
# Even if there is slightly more or less glazing than would be expected, up 
# to 10% more or less.

# More than typical applies if there is significantly more surface area of 
# glazing than would be expected (15%-30% more), perhaps because there is a 
# large sun room or numerous patio doors have been added.

# Less than typical applies if there is significantly less glazing than 
# would be expected. 
# This is rare as homeowners tend not to take out windows, but a property 
# may have an unusual design with few windows.

# Much more than typical and Much less than typical should be used for 
# those dwellings with very unusual amounts of glazing; such as a glass 
# walled penthouse flat or a Huff Haus. 
# Due to this option allowing measurements of each window to be accounted 
# for, it should also be used if a dwelling has a mixture of multiple 
# glazing types, e.g. double, triple, secondary, or a mixture of glazing 
# gaps.

# Sun rooms
# ---------

# For a highly glazed part of the dwelling, such as a sun room, which does not meet the criteria for a conservatory (50% of walls and 75% of roof glazed), in most cases use the glazing option of ‘more than typical’. That adds 25% to the total glazed area of the dwelling. If that is considered not appropriate, the window area is assessed by either:
# a) measuring all windows and roof windows throughout the dwelling, or
# b) measuring all windows and roof windows in the sun room, and use Table S4 to obtain the window area of remaining part of dwelling which is entered as a single window.

# Record method used in site notes.

# Two types of window are allowed for, single and multiple glazed. Multiple glazing can be double glazed units
installed before 20021, double glazed units installed during/after 20021, double glazing unknown date, secondary
glazing or triple glazing. For multiple glazing the U-value can be known.

# ---
# If more than one of type of multiple glazing is present, the assessor selects the type according to what is
the most prevalent in the dwelling.
If single glazing with secondary glazing, record as secondary glazing.
If double glazing with secondary glazing, record as newer double glazing (i.e. later than the date in
footnote 1).
If secondary glazing has been removed in summer, enter as secondary glazing only if assessor can
confirm that the panels exist and can be re-fitted. Evidence to be recorded on site notes.
# ---

# The window area of each part of the dwelling (main, extension 1, extension 2 etc) is divided into two areas, single
and multiple, according to the assessor's estimate of the multiple-glazed percentage. The same percentage is used in
main dwelling and each extension.


# S3.7.2 Window area much more or much less than typical, and park homes



# S3.8 Roof area



# S3.9 Rooms in roof



# S3.9.1 Area and U-value details of the roof rooms not collected


# S3.9.2 Area and U-value details of the roof rooms are collected


# S3.10 Heat loss floor area


# S3.11 Heat loss floor area for houses and bungalows


# S3.12 Heat loss floor area for flats and maisonettes



# S3.13 Sheltered walls for flats and maisonettes






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


