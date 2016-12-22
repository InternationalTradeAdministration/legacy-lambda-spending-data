import xlrd, json, csv, collections, math
from constants import SHEET_NAMES, EXPORT_ROWS, IMPORT_ROWS, HEADER_ROW, EXPORT_FIELD_NAMES, IMPORT_FIELD_NAMES

def main(): 
  book = xlrd.open_workbook("spending_data.xlsx")
  data = collections.OrderedDict()

  for sheet_name in SHEET_NAMES:
    sheet = book.sheet_by_name(sheet_name)
    data[sheet_name] = collections.OrderedDict()
    
    process_rows(sheet, EXPORT_ROWS, EXPORT_FIELD_NAMES, data[sheet_name])
    process_rows(sheet, IMPORT_ROWS, IMPORT_FIELD_NAMES, data[sheet_name])

  #print json.dumps(data, indent=4)
  entries = expand_entries(data)
  write_csv_file(entries)

def process_rows(sheet, row_numbers, field_names, data):
  for row_num in row_numbers:
    row = sheet.row_values(row_num-1)

    for index, cell in enumerate(row):
      if index == 0:
        continue
      if index >= len(list(filter(None, sheet.row_values(HEADER_ROW-1)))): # Need this check to not break Saudi Arabia
        break
      year = str(int(sheet.cell_value(rowx=HEADER_ROW-1, colx=index)))

      if not year in data:
        data[year] = collections.OrderedDict()
      if str(row[0]).strip() in field_names:
        key = field_names[str(row[0]).strip()]

        if cell == '(*)':
          cell = 0
        elif not is_number(cell):
          cell = None
        data[year][key] = cell

def expand_entries(data):
  entries = [];
  for country, year_dicts in data.items():
    for year, entry in year_dicts.iteritems():
      entry['year'] = year
      entry['country_or_region'] = country
      entries.append(entry)
  return entries

def write_csv_file(entries):
  keys = entries[0].keys()
  with open('spending_data.csv', 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(entries)

def is_number(s):
  try:
      float(s)
      return True
  except ValueError:
      return False

main()