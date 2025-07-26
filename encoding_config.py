# encoding_config.py

custom_encoding = {
    'Category': {
        'Mechanicals': 0, 'Logistics': 1, 'Packaging': 2,
        'Materials & Components': 3, 'Goods & Services': 4, 'Electrical': 5
    },
    'Defect_Type': {
        'No Impact': 0, 'Impact': 1, 'Rejected': 2
    },
    'Defect_Category': {
        'foreign_material': 0, 'misc_support': 1, 'defects_bad': 2,
        'crease_warped': 3, 'incorrect_color': 4, 'defective_packaging': 5,
        'print_defects': 6, 'labels_incorrect': 7
    },
    'Region': {
        'Northeast': 0, 'Midwest': 1, 'South': 2, 'West': 3
    },
    'Grouped_Material_Type': {
        'Raw Materials': 0, 'Corrugate': 1, 'Electrical Components': 2,
        'Glass/Composites': 3, 'Film': 4, 'Labels': 5,
        'Carton': 6, 'Hardware': 7, 'Packaging Related': 8, 'Other': 9
    }
}
