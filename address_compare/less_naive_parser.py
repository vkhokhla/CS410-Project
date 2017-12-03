import pandas as pd
import collections


def less_naive_parser(address_string, street_types, compass_points, switched_compass_points, unit_types):
    all_caps_addresses = address_string.upper()

    # all_caps_street_types = pd.DataFrame(columns=['st_abbrev','street_type'])
    # all_caps_street_types['st_abbrev'] = street_types['st_abbrev'].str.upper()
    # all_caps_street_types['street_type'] = street_types['street_type'].str.upper()

    split_address = list(all_caps_addresses.split())
    reversed_address_list = split_address.copy()
    reversed_address_list.reverse()

    parsed_address_string = pd.DataFrame(columns=['street_number','unit_type','unit_number','pre_street_direction','street_name','street_type','post_street_direction'])

    all_caps_street_types_dict = dict()
    for row in range(street_types.shape[0]):
        all_caps_street_types_dict[street_types.loc[row, 'st_abbrev'].upper()] = street_types.loc[row, 'street_type'].upper()


    all_caps_unit_types_dict = dict()
    for row in range(unit_types.shape[0]):
        all_caps_unit_types_dict[unit_types.loc[row, 'unit_type_abbrev'].upper()] = unit_types.loc[row, 'unit_type_name'].upper()

    total_items_address_list = len(split_address) - 1

    item_index_number = 0
    item_index_number_to_remove = 0
    street_type_index = None
    post_street_direction_index = None
    pre_street_direction_index = None
    unit_type_index = None
    reversed_address_list_copy = reversed_address_list.copy()
    for item in reversed_address_list:
        if item in all_caps_street_types_dict.keys():
            parsed_address_string.loc[0,'street_type'] = all_caps_street_types_dict[item]
            street_type_index = total_items_address_list - item_index_number
            reversed_address_list_copy.pop(item_index_number_to_remove)
            item_index_number_to_remove -= 1
        if item in switched_compass_points.keys():
            if street_type_index == None:
                parsed_address_string.loc[0,'post_street_direction'] = switched_compass_points[item]
                post_street_direction_index = total_items_address_list - item_index_number
                reversed_address_list_copy.pop(item_index_number_to_remove)
                item_index_number_to_remove -= 1
            else:
                parsed_address_string.loc[0,'pre_street_direction'] = switched_compass_points[item]
                pre_street_direction_index = total_items_address_list - item_index_number
                reversed_address_list_copy.pop(item_index_number_to_remove)
                item_index_number_to_remove -= 1
        if item in all_caps_unit_types_dict.keys():
            parsed_address_string.loc[0,'unit_type'] = all_caps_unit_types_dict[item]
            unit_type_index = total_items_address_list - item_index_number
            reversed_address_list_copy.pop(item_index_number_to_remove)
            item_index_number_to_remove -= 1
        item_index_number += 1
        item_index_number_to_remove += 1

    concat_street_name = str()
    if pre_street_direction_index != None and street_type_index != None:
        num_items_for_name = street_type_index - pre_street_direction_index - 1
        for num in range(num_items_for_name):
            concat_street_name += split_address[pre_street_direction_index + num + 1] + " "
        concat_street_name = concat_street_name.strip()
    else:
        '''
        Need to add ELIFs for when the pre_street_direction_index is None.
        I.e., in that situation what is the starting point for the street name and what is the ending point
        Also need to consider what to do when street_type_index is None as there is at least 1 Washington Address called Broadway without a street type
        '''
        pass

    concat_unit_number = str()
    if unit_type_index != None:
        if pre_street_direction_index != None:
            num_items_for_unit = pre_street_direction_index - unit_type_index - 1
            for num in range(num_items_for_unit):
                concat_unit_number += split_address[unit_type_index + num + 1] + " "
            concat_unit_number = concat_unit_number.strip()
        else:
            '''
            Need to add ELIFs for when the pre_street_direction_index is None.
            I.e., in that situation, what is the ending point for the unit number (how to determine the starting point of the thing after the unit number
            Also need to consider the situation where the unit number is before the unit type.  Need to determine how many items prior to the unit type would make up the unit number in this case
            Also need to consider the situation where the unit type and number come at the end of the street
            So need separate If and Elses for pre_street_direction_index != None for when the difference is 1 and for when the difference is negative
            '''

            pass

    parsed_address_string.loc[0,'street_name'] = concat_street_name
    parsed_address_string.loc[0,'unit_number'] = concat_unit_number
    print (parsed_address_string)

