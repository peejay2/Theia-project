import pandas as pd

data = {
    'Industrial & Business': {
        'Materials & Manufacturing': {
            'Metalworking': [
                'Steel Production', 'Aluminum Production', 'Copper Production', 'Machining'
            ],
            'Plastics & Rubber': [
                'Plastic Manufacturing', 'Rubber Production', 'Injection Molding', 'Extrusion'
            ],
            'Chemicals': [
                'Petrochemicals', 'Pesticides', 'Pharmaceutical Chemicals', 'Industrial Gases'
            ],
            'Paper & Wood': {
                'Pulp Production', 'Paper Manufacturing', 'Woodworking', 'Furniture Manufacturing'
            }
        },
        'Business Support Services': {
            'Consulting': [
                'Management Consulting', 'Financial Consulting', 'IT Consulting', 'HR Consulting'
            ],
            'Facility Management': [
                'Cleaning Services', 'Security Services', 'Catering', 'Maintenance'
            ],
            'Logistics & Supply Chain': [
                'Warehousing', 'Transportation', 'Customs Brokerage', 'Inventory Management'
            ],
            'Marketing & Advertising': [
                'Market Research', 'Advertising', 'Public Relations', 'Digital Marketing'
            ]
        }
    },
    'Electronics & IT': {
        'Information Technology': {
            'Software Development': [
                'Web Development', 'Mobile App Development', 'Enterprise Software', 'AI & Machine Learning'
            ],
            'Hardware': [
                'Computers', 'Servers', 'Network Equipment', 'Peripherals'
            ],
            'IT Services': [
                'IT Support', 'Cloud Services', 'Data Center Management', 'Cybersecurity'
            ],
            'Telecommunications': [
                'Network Operators', 'Internet Service Providers', 'Satellite Communication', 'VoIP'
            ]
        },
        'Electronics': {
            'Consumer Electronics': [
                'Smartphones', 'TVs', 'Cameras', 'Wearables'
            ],
            'Industrial Electronics': [
                'Sensors', 'Motors', 'Control Systems', 'Power Supplies'
            ],
            'Semiconductors': [
                'Memory Chips', 'Processors', 'Integrated Circuits', 'LEDs'
            ],
            'Electronic Manufacturing Services': [
                'PCB Assembly', 'Box Build', 'Testing', 'Repair'
            ]
        }
    },

    'Consumer Goods': {
        'Household Goods & Services': {
            'Appliances': [
                'Refrigerators', 'Washing Machines', 'Vacuum Cleaners', 'Air Conditioners'
            ],
            'Furniture': [
                'Living Room', 'Bedroom', 'Kitchen', 'Outdoor'
            ],
            'Home Decor': [
                'Textiles', 'Lighting', 'Artwork', 'Curtains & Blinds'
            ],
            'Personal Care': [
                'Cosmetics', 'Hair Care', 'Skin Care', 'Fragrances'
            ]
        },
        'Food & Beverages': {
            'Packaged Food': [
                'Snacks', 'Beverages', 'Baked Goods', 'Frozen Food'
            ],
            'Confectionery': [
                'Chocolate', 'Candy', 'Gum', 'Biscuits'
            ],
            'Alcoholic Beverages': [
                'Beer', 'Wine', 'Spirits', 'Cider'
            ],
            'Non-Alcoholic Beverages': [
                'Soda', 'Juice', 'Bottled Water', 'Sports Drinks'
            ]
        },
        'Retail': {
            'Supermarkets': [
                'Grocery', 'Bakery', 'Deli', 'Produce'
            ],
            'Department Stores': [
                'Clothing', 'Footwear', 'Home Goods', 'Electronics'
            ],
            'Specialty Stores': [
                'Books', 'Toys', 'Sporting Goods', 'Pet Supplies'
            ],
            'Online Retail': [
                'E-commerce Platforms', 'Online Marketplaces', 'Direct-to-Consumer', 'Subscription Services'
            ]
        }
    },
    'Utilities & Energy': {
        'Energy': {
            'Oil & Gas': [
                'Exploration', 'Production', 'Refining', 'Distribution'
            ],
            'Coal': [
                'Mining', 'Processing', 'Power Generation', 'Transportation'
            ],
            'Renewable Energy': [
                'Solar', 'Wind', 'Hydro', 'Geothermal'
            ],
            'Nuclear Energy': [
                'Uranium Mining', 'Enrichment', 'Power Generation', 'Waste Management'
            ]
        },
        'Utilities': {
            'Electricity': [
                'Generation', 'Transmission', 'Distribution', 'Retail'
            ],
            'Water': [
                'Collection', 'Treatment', 'Distribution', 'Wastewater Management'
            ],
            'Gas': [
                'Production', 'Transmission', 'Distribution', 'Retail'
            ],
            'Telecommunications': [
                'Fixed-Line', 'Mobile', 'Broadband', 'Cable'
            ]
        }
    },
    'Finance': {
        'Investment & Insurance': {
            'Asset Management': [
                'Mutual Funds', 'Hedge Funds', 'Private Equity', 'Real Estate'
            ],
            'Insurance': [
                'Life', 'Health', 'Property & Casualty', 'Reinsurance'
            ],
            'Investment Banking': [
                'Mergers & Acquisitions', 'Capital Markets', 'Underwriting', 'Advisory'
            ],
            'Brokerage': [
                'Stock Trading', 'Bonds', 'Commodities', 'Forex'
            ]
        },
        'Banking & Payment': {
            'Retail Banking': [
                'Checking Accounts', 'Savings Accounts', 'Loans', 'Credit Cards'
            ],
            'Corporate Banking': [
                'Cash Management', 'Trade Finance', 'Corporate Lending', 'Merchant Services'
            ],
            'Payment Services': [
                'Payment Processing', 'Merchant Acquiring', 'Money Transfer', 'Mobile Payments'
            ],
            'Fintech': [
                'Digital Banking', 'Peer-to-Peer Lending', 'Robo-Advisory', 'Cryptocurrency'
            ]
        }
    },
    'Health': {
        'Health Care': {
            'Hospitals': [
                'General Hospitals', 'Specialized Hospitals', 'Rehabilitation Centers', 'Clinics'
            ],
            'Medical Devices': [
                'Diagnostic Equipment', 'Surgical Instruments', 'Implants', 'Monitoring Devices'
            ],
            'Pharmaceuticals': [
                'Prescription Drugs', 'Over-the-Counter Drugs', 'Generic Drugs', 'Vaccines'
            ],
            'Health Services': [
                'Laboratory Services', 'Home Health Care', 'Physiotherapy', 'Hospice Care'
            ]
        },
        'Biotechnology & Pharmaceuticals': {
            'Biotech Research': [
                'Drug Discovery', 'Genomics', 'Proteomics', 'Bioinformatics'
            ],
            'Biotech Products': [
                'Therapeutics', 'Diagnostic Tests', 'Vaccines', 'Biologics'
            ],
            'Agricultural Biotech': [
                'Genetically Modified Crops', 'Pesticides', 'Fertilizers', 'Animal Health'
            ],
            'Industrial Biotech': [
                'Biofuels', 'Biopolymers', 'Enzymes', 'Bioremediation'
            ]
        }
    },
    'Transportation': {
        'Land Transportation': {
            'Automotive': [
                'Passenger Cars', 'Commercial Vehicles', 'Electric Vehicles', 'Autonomous Vehicles'
            ],
            'Rail': [
                'Passenger Trains', 'Freight Trains', 'Rail Infrastructure', 'Railway Equipment'
            ],
            'Trucking & Logistics': [
                'Trucking', 'Warehousing', 'Freight Forwarding', 'Courier Services'
            ],
            'Public Transportation': [
                'Buses', 'Trams', 'Subways', 'Taxis'
            ]
        },
        'Aerospace Transportation': {
            'Aircraft Manufacturing': [
                'Commercial Aircraft', 'Military Aircraft', 'Helicopters', 'Drones'
            ],
            'Airports & Air Traffic Control': [
                'Airport Operations', 'Air Traffic Management', 'Ground Support', 'Security'
            ],
            'Airlines': [
                'Passenger Airlines', 'Cargo Airlines', 'Charter Airlines', 'Low-Cost Carriers'
            ],
            'Space': [
                'Satellites', 'Launch Vehicles', 'Space Exploration', 'Space Tourism'
            ]
        },
        'Maritime Transportation': {
            'Shipbuilding & Repair': [
                'Cargo Ships', 'Passenger Ships', 'Specialized Vessels', 'Ship Repair'
            ],
            'Ports & Terminals': [
                'Container Terminals', 'Bulk Terminals', 'Passenger Terminals', 'Port Operations'
            ],
            'Shipping': [
                'Container Shipping', 'Bulk Shipping', 'Tanker Shipping', 'Passenger Shipping'
            ],
            'Marine Services': [
                'Tug & Tow', 'Pilotage', 'Marine Insurance', 'Maritime Security'
            ]
        }
    },
    'Entertainment': {
        'Entertainment Products & Services': {
            'Film & Television': [
                'Film Production', 'Television Production', 'Post-Production', 'Distribution'
            ],
            'Music': [
                'Record Labels', 'Music Publishing', 'Live Music', 'Streaming Services'
            ],
            'Gaming': [
                'Video Games', 'Mobile Games', 'Console Games', 'Esports'
            ],
            'Toys & Hobbies': [
                'Action Figures', 'Board Games', 'Puzzles', 'Collectibles'
            ]
        },
        'Tourism & Recreation':{
            'Hotels & Resorts': [
                'Luxury Hotels', 'Budget Hotels', 'Resorts', 'Vacation Rentals'
            ],
            'Travel Services': [
                'Travel Agencies', 'Tour Operators', 'Online Travel Agencies', 'Cruise Lines'
            ],
            'Theme Parks & Attractions': [
                'Theme Parks', 'Water Parks', 'Zoos & Aquariums', 'Museums'
            ],
            'Sports & Fitness': [
                'Sports Clubs', 'Fitness Centers', 'Sporting Events', 'Sports Equipment'
            ]
        },
        'Media': {
            'Print Media': [
                'Newspapers', 'Magazines', 'Books', 'Printing Services'
            ],
            'Broadcast Media': [
                'Radio', 'Television', 'Cable Networks', 'Streaming Platforms'
            ],
            'Digital Media': [
                'Online News', 'Blogs', 'Podcasts', 'Social Media'
            ],
            'Advertising & Marketing': [
                'Advertising Agencies', 'Marketing Consultancy', 'Public Relations', 'Event Management'
            ]
        }},

            'Social': {
        'Social & Public Services': {
            'Education': [
                'Schools', 'Universities', 'Vocational Training', 'E-Learning'
            ],
            'Healthcare & Social Assistance': [
                'Hospitals', 'Clinics', 'Social Services', 'Mental Health Services'
            ],
            'Public Safety & Security': [
                'Law Enforcement', 'Fire Protection', 'Emergency Services', 'Corrections'
            ],
            'Public Administration': [
                'Government Services', 'Policy & Planning', 'Regulation', 'Public Works'
            ]
        },
        'Security & Defense': {
            'Military': [
                'Army', 'Navy', 'Air Force', 'Coast Guard'
            ],
            'Defense Industry': [
                'Defense Equipment', 'Aerospace', 'Cybersecurity', 'Intelligence Services'
            ],
            'Private Security': [
                'Security Services', 'Surveillance', 'Armored Transport', 'Investigation'
            ],
            'Cybersecurity': [
                'Network Security', 'Data Protection', 'Threat Intelligence', 'Penetration Testing'
            ]
        }}
    ,
        'Real Estate & Construction': {
        'Real Estate': {
            'Residential': [
                'Housing', 'Apartments', 'Condominiums', 'Townhouses'
            ],
            'Commercial': [
                'Office Buildings', 'Retail Spaces', 'Industrial Properties', 'Hotels'
            ],
            'Land & Agriculture': [
                'Farmland', 'Ranches', 'Timberland', 'Vacant Land'
            ],
            'Real Estate Services': [
                'Brokerage', 'Property Management', 'Appraisal', 'Development'
            ]
        },
        'Construction': {
            'Residential Construction': [
                'Single-Family Homes', 'Multi-Family Homes', 'Remodeling', 'Affordable Housing'
            ],
            'Commercial Construction': [
                'Office Buildings', 'Retail Centers', 'Hospitals', 'Manufacturing Facilities'
            ],
            'Infrastructure Construction': [
                'Roads & Highways', 'Bridges', 'Airports', 'Water & Sewer Systems'
            ],
            'Construction Services': [
                'Architecture', 'Engineering', 'Project Management', 'Construction Equipment'
            ]
        }
    }}



data2 = []

# Iterate over the top-level keys in the dictionary
for level1_key, level1_value in data.items():
    for level2_key, level2_value in level1_value.items():
        for level3_key, level3_value in level2_value.items():
            for level4_value in level3_value:
                # Append a new row to the data list for each level 4 value
                data2.append([level1_key, level2_key, level3_key, level4_value])

# Create a pandas DataFrame from the data list
df = pd.DataFrame(data2, columns=['Level 1', 'Level 2', 'Level 3', 'Level 4'])

# Print the resulting DataFrame
# print(df.head())

df.columns=['Sector', 'Industry', 'Sub-Industry', 'Theme']

themes_df = df