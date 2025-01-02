def sub_category_classification(dtframe):
    Storage_Revenue = ['Storage - Initial', 'Storage - Renewal', 'Storage Guarantee']
    Handling_Revenue = ['Handling - Initial', 'Handling Out']
    Case_Pick_Revenue = ['Accessorial - Case Pick / Sorting']
    Ancillary_Revenue = ['Accessorial - Documentation', 'Accessorial - Labeling / Stamping',
                         'Accessorial - Labor and Overtime', 'Accessorial - Loading / Unloading / Lumping',
                         'Accessorial - Palletizing', 'Accessorial - Shrink Wrap']
    Blast_Freezing_Revenue = ['Blast Freezing', 'Room Freezing']
    Other_Warehouse_Revenue = ['Other - Delayed Pallet Hire Revenue', 'Other - Warehouse Revenue',
                               'Rental Electricity Income']

    if dtframe["Revenue_Category"] in Storage_Revenue:
        return "Storage Revenue"
    elif dtframe["Revenue_Category"] in Handling_Revenue:
        return "Handling Revenue"
    elif dtframe["Revenue_Category"] in Case_Pick_Revenue:
        return "Case Pick Revenue"
    elif dtframe["Revenue_Category"] in Ancillary_Revenue:
        return "Ancillary Revenue"
    elif dtframe["Revenue_Category"] in Blast_Freezing_Revenue:
        return "Blast Freezing Revenue"
    elif dtframe["Revenue_Category"] in Other_Warehouse_Revenue:
        return "Other Warehouse Revenue"
    else:
        return dtframe["Revenue_Category"]
