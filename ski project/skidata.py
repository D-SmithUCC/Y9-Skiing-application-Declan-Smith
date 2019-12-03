import csv

with open("whose_got_snow.csv", mode='w') as snow_file:
    snow_writer = csv.writer(snow_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    snow_writer.writerow(['resort name','proximity to toronto(km)','number of runs','metres of vertical'])
    snow_writer.writerow(['whistler','3344.25','200+','1530'])
    snow_writer.writerow(['fernie','2792.59','142','1051'])
    snow_writer.writerow(['St.Anton','105','141','1507'])
    snow_writer.writerow(['WhiteFish','2722.68 ','141','717'])
    snow_writer.writerow(['MontTremblant','473.96','102','645'])
    snow_writer.writerow(['BigWhite','3046.47','119','777'])
    snow_writer.writerow(['Revelstoke','2995.98','75','1713'])
    snow_writer.writerow(['KickingHorse','2919.98','120','1314'])
    
