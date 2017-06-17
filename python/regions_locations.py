from __future__ import print_function
from oauth2client import tools

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
        print('ID, Title, Name')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s, %s' % (row[0], row[1], row[2]))

            print('Locations in this region:')

            print('GID	Name	Prefix	Jurisdiction	Type	Theme	Eventbrite	Location	Venue	Name	'
                  'Address	Host	Accessibility	Under 18	Capacity	Parking	Public Transport	'
                  'Catering	Times	Contact	Phone	Is capital city	Display weight	Dataportals	Description')
            for location in location_values:
                if location[3] == row[0]:
                    for xx in location:
                        print(xx + '\t')


if __name__ == '__main__':
    main()
