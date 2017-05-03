import xlrd, json, csv, collections, math
from constants import SHEET_NAMES, EXPORT_ROWS, IMPORT_ROWS, HEADER_ROW, EXPORT_FIELD_NAMES, IMPORT_FIELD_NAMES, SHEET_SPECIFIC_FIELD_NAMES
from taxonomy_mapper import TaxonomyMapper

mapper_config = [{'starting_field': 'country_or_region', 'desired_field': 'country'}, {'starting_field': 'country_or_region', 'desired_field': 'world_region'}]
mapper_source = 'NTTOSpendingData'
taxonomy_mapper = TaxonomyMapper({'config': mapper_config, 'mapper_source': mapper_source})

def run(download_path = "spending_data.xlsx"): 
  book = xlrd.open_workbook(download_path)
  data = collections.OrderedDict()

  for sheet_name in SHEET_NAMES:
    sheet = book.sheet_by_name(sheet_name)
    data[sheet_name] = collections.OrderedDict()
    
    process_rows(sheet, EXPORT_ROWS, EXPORT_FIELD_NAMES, data[sheet_name])
    process_rows(sheet, IMPORT_ROWS, IMPORT_FIELD_NAMES, data[sheet_name])

  #print json.dumps(data, indent=4)
  entries = expand_entries(data)
  return entries

def process_rows(sheet, row_numbers, field_names, data):
  for row_num in row_numbers:
    row = sheet.row_values(row_num-1)

    for index, cell in enumerate(row):
      if index == 0: # skip field names column
        continue
      if index >= len(list(filter(None, sheet.row_values(HEADER_ROW-1)))): # Need this check to not break Saudi Arabia
        break
      year = str(int(sheet.cell_value(rowx=HEADER_ROW-1, colx=index)))
      extract_value_from_row(year, data, field_names, row, cell)


def extract_value_from_row(year, data, field_names, row, cell):
  if not year in data:
    data[year] = collections.OrderedDict()
  if str(row[0]).strip() in field_names:
    key = field_names[str(row[0]).strip()]
    data[year][key] = extract_from_cell(cell)
  else:
    for key, value in SHEET_SPECIFIC_FIELD_NAMES.iteritems():
      if key in str(row[0]).strip():
        data[year][value] = extract_from_cell(cell)

def expand_entries(data):
  entries = [];
  for country, year_dicts in data.items():
    for year, entry in year_dicts.iteritems():
      entry['year'] = year
      entry['country_or_region'] = country

      entry = taxonomy_mapper.add_taxonomy_fields(entry)
      entries.append(entry)
  return entries

def extract_from_cell(cell):
  if cell == '(*)':
    cell = 0
  elif not is_number(cell):
    cell = ""
  return str(cell)

def is_number(string):
  try:
      float(string)
      return True
  except ValueError:
      return False

#run()