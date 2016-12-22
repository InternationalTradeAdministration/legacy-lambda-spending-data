SHEET_NAMES = ['Africa', 'Argentina', 'Asia-Pacific', 'Australia', 'Belgium-Lux', 'Bermuda', 
              'Brazil', 'Canada', 'Chile', 'China', 'EU', 'Europe', 'France', 'Germany', 'Hong Kong', 
              'India', 'Indonesia', 'Ireland', 'Israel', 'Italy', 'Japan', 'Latin America', 
              'Malaysia', 'Mexico', 'Middle East', 'Netherlands', 'New Zealand', 'Norway', 
              'Other-Western', 'Overseas', 'Philippines', 'Saudi Arabia', 'Singapore', 'SC America',
              'South Africa', 'South Korea', 'Spain', 'Sweden', 'Switzerland', 'Taiwan', 'Thailand', 
              'UK', 'Venezuela']

EXPORT_ROWS = [5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 18, 19]

IMPORT_ROWS = [22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 35, 36, 40, 42]

HEADER_ROW = 4

EXPORT_FIELD_NAMES = {
  'U.S. Exports of Goods and Services' : 'total_exports',
  'U.S. Goods Exports' : 'goods_exports',
  'U.S. Services Exports' : 'services_exports',
  'Total Travel and Tourism Exports' : 'travel_and_tourism_exports',

  'Travel (for all purposes including education)' : 'travel_exports',
  'Of which: Education Related' : 'education_travel_exports',
  'Of which: Other Business/Personal Travel' : 'business_personal_travel_exports',
  'Passenger Air Transportation' : 'passenger_air_transportation_exports',

  '% Change in Total Travel and Tourism Exports' : 'percent_change_travel_and_tourism_exports',
  '% Change in Travel Exports' : 'percent_change_travel_exports',
  '% Change in Passenger Air Transportation Exports' : 'percent_change_passenger_air_transportation_exports',
}

IMPORT_FIELD_NAMES = {
  'U.S. Imports of Goods and Services': 'total_imports',
  'U.S. Goods Imports': 'goods_imports',
  'U.S. Services Imports': 'services_imports',
  'Total Travel and Tourism Imports': 'travel_and_tourism_imports',

  'Travel (for all purposes including education)': 'travel_imports',
  'Of which: Education Related': 'education_travel_imports',
  'Of which: Other Business/Personal Travel': 'business_personal_travel_imports',
  'Passenger Air Transportation': 'passenger_air_transportation_imports',

  '% Change in Total Travel and Tourism Imports': 'percent_change_travel_and_tourism_imports',
  '% Change in Travel Imports': 'percent_change_travel_imports',
  '% Change in Passenger Air Transportation Imports': 'percent_change_passenger_air_transportation_imports',
  'Balance of Trade (Surplus/Deficit)': 'balance_of_trade',
  '% change in the Balance of Trade Surplus/Deficit': 'percent_change_balance_of_trade'
}