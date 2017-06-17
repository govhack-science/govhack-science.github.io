from __future__ import print_function
from oauth2client import tools
import os

import common
import govhack_config


def main():
    service = common.get_service()

    spreadsheet_id = govhack_config.REGIONS_LOCATIONS_SHEET

    range_name = 'Regions!A2:C'
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])

    location_range_name = 'Locations!A2:Y'
    location_result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id,
                                                          range=location_range_name).execute()
    location_values = location_result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Generating region files...')
        for row in values:

            filename = os.path.join('..', govhack_config.FILES_ROOT, '_jurisdictions',
                                    row[2].replace(' ', '_').lower() + ".md")

            print('%s, %s, %s' % (row[0], row[1], row[2]))
            f = open(filename, 'w')
            f.write('---\n')
            f.write('gid: ' + row[0] + '\n')
            f.write('name: ' + row[1] + '\n')
            f.write('title: ' + row[2] + '\n')
            f.write('photo_url: \n')
            f.write('---\n')
            f.close()

            print('Generating location files for %s ', row[2])

            for location in location_values:

                if location[0] == row[0]:
                    filename = os.path.join('..', govhack_config.FILES_ROOT, '_locations', location[0], location[1] + ".md")
                    f = open(filename, 'w')

                    f.write('---\n')
                    f.write('jurisdiction: ' + location[0] + '\n')
                    f.write('gid: ' + location[1] + '\n')
                    f.write('name: ' + location[4] + '\n')
                    f.write('prefix: ' + location[3] + '\n')
                    f.write('type: ' + location[5] + '\n')
                    f.write('theme: ' + location[6] + '\n')
                    f.write('eventbrite: ' + location[7] + '\n')

                    latlong = location[8].split(',')
                    f.write('location: \n')
                    f.write('  lat: ' + latlong[0] + '\n')
                    f.write('  lat: ' + latlong[1] + '\n')

                    f.write('venue: \n')
                    f.write('  name: ' + location[9] + '\n')
                    f.write('  address: ' + location[10] + '\n')
                    f.write('  host: ' + location[11] + '\n')
                    f.write('  accessibility: ' + location[12] + '\n')
                    f.write('  under_18: ' + location[13] + '\n')
                    f.write('  capacity: ' + location[14] + '\n')
                    f.write('  parking: ' + location[15] + '\n')
                    f.write('  public_transport: ' + location[16] + '\n')
                    f.write('  public_transport_last: ' + location[17] + '\n')
                    f.write('catering: ' + location[18] + '\n')

                    times = location[19].split('-')
                    friday = times[0].split(',')
                    saturday = times[1].split(',')
                    sunday = times[2].split(',')

                    f.write('times: \n')
                    f.write('  friday: \n')
                    f.write('    open: ' + friday[0] + '\n')
                    f.write('    close: ' + friday[1] + '\n')
                    f.write('  saturday: \n')
                    f.write('    open: ' + saturday[0] + '\n')
                    f.write('    close: ' + saturday[1] + '\n')
                    f.write('  sunday: \n')
                    f.write('    open: ' + sunday[0] + '\n')
                    f.write('    close: ' + sunday[1] + '\n')

                    f.write('contact: \n')
                    f.write('  phone: ' + location[20] + '\n')

                    f.write('is_capital_city: ' + location[2] + '\n')
                    f.write('display_weight: ' + location[21] + '\n')

                    dataportals = location[22].split(',')
                    f.write('dataportals: \n')
                    for x in dataportals:
                        f.write('  - ' + x + '\n')
                    
                    f.write('---\n\n')
                    
                    f.write(location[23])
                    f.close()


if __name__ == '__main__':
    main()
