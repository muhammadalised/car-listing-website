from datetime import datetime

state_choice = (
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('DC', 'District Of Columbia'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
)

year_choice = []
for r in range(2000, (datetime.now().year+1)):
    year_choice.append((r,r))

features_choices = (
    ('Cruise Control', 'Cruise Control'),
    ('Audio Interface', 'Audio Interface'),
    ('Airbags', 'Airbags'),
    ('Air Conditioning', 'Air Conditioning'),
    ('Seat Heating', 'Seat Heating'),
    ('Alarm System', 'Alarm System'),
    ('ParkAssist', 'ParkAssist'),
    ('Power Steering', 'Power Steering'),
    ('Reversing Camera', 'Reversing Camera'),
    ('Direct Fuel Injection', 'Direct Fuel Injection'),
    ('Auto Start/Stop', 'Auto Start/Stop'),
    ('Wind Deflector', 'Wind Deflector'),
    ('Bluetooth Handset', 'Bluetooth Handset'),
)

door_choices = (
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
)