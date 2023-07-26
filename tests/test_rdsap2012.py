# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 12:51:19 2023

@author: cvskf
"""

import unittest

from rdsap2012 import rdsap2012




class TestRdSAP2012(unittest.TestCase):
    ""
    
    def test__get_input_data(self):
        ""
        
        input_file_or_data = 'rdSAP_input_test.json'
        
        input_data=rdsap2012._get_input_data(
            input_file_or_data
            )

        #print(input_data)
        
        self.assertIsInstance(input_data, dict)
        
        
    def test__adjustment_to_levels_of_storeys_for_houses_and_bungalows(self):
        ""
        
        input_file_or_data = 'rdSAP_input_test.json'
        
        working_data=rdsap2012._get_input_data(
            input_file_or_data
            )
        
        working_data=rdsap2012._adjustment_to_levels_of_storeys_for_houses_and_bungalows(working_data)
        
        self.assertEqual(
            working_data['building_parts']['main_dwelling']['dimensions']['lowest_occupied_floor']['level'],
            0
            )
        
        self.assertEqual(
            working_data['building_parts']['main_dwelling']['dimensions']['lowest_occupied_floor_plus_1']['level'],
            1
            )
        
        
    def test__storey_height(self):
        ""
        
        input_file_or_data = 'rdSAP_input_test.json'
        
        working_data=rdsap2012._get_input_data(
            input_file_or_data
            )
        
        working_data=rdsap2012._storey_height(working_data)
        
        self.assertEqual(
            working_data['building_parts']['main_dwelling']['dimensions']['lowest_occupied_floor']['storey_height'],
            2
            )
        
        self.assertEqual(
            working_data['building_parts']['main_dwelling']['dimensions']['lowest_occupied_floor_plus_1']['storey_height'],
            2.25
            )
        
        
    def test__wall_thickness(self):
        ""
        
        input_file_or_data = 'rdSAP_input_test.json'
        
        working_data=rdsap2012._get_input_data(
            input_file_or_data
            )
        
        working_data=rdsap2012._wall_thickness(working_data)
        
        self.assertEqual(
            working_data['building_parts']['main_dwelling']['wall_thickness2'],
            270
            )
        
        
    def test__convert_dimensions(self):
        ""
        
        input_file_or_data = 'rdSAP_input_test.json'
        
        working_data=rdsap2012._get_input_data(
            input_file_or_data
            )
        
        working_data=rdsap2012._adjustment_to_levels_of_storeys_for_houses_and_bungalows(working_data)
        working_data=rdsap2012._wall_thickness(working_data)
        working_data=rdsap2012._convert_dimensions(working_data)
        
        self.assertEqual(
            working_data['building_parts']['main_dwelling']['dimensions']['lowest_occupied_floor']['exposed_perimeter_internal'],
            37.84
            )
        
        
    def test__door_area(self):
        ""
        
        input_file_or_data = 'rdSAP_input_test.json'
        
        working_data=rdsap2012._get_input_data(
            input_file_or_data
            )
        
        working_data=rdsap2012._door_area(working_data)
        
        self.assertEqual(
            working_data['whole_dwelling']['door_area'],
            3.7
            )
        
        self.assertEqual(
            working_data['whole_dwelling']['door_area_sheltered'],
            0
            )
        
    
        

if __name__=='__main__':
    
    unittest.main()