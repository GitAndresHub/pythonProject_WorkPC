def merge_dates_and_towns_into_csv(dates_filename: str, towns_filename: str, csv_output_filename: str) -> None:
    """
    Merge information from two files into one CSV file.

    Dates file contains names and dates. Separated by colon.
    john:01.01.2001
    mary:06.03.2016

    You don't have to validate the date.
    Every line contains name, colon and date.

    Towns file contains names and towns. Separated by colon.
    john:london
    mary:new york

    Every line contains name, colon and town name.
    There are no headers in the input files.

    Those two files should be merged by names.
    The result should be a csv file:

    name,town,date
    john,london,01.01.2001
    mary,new york,06.03.2016

    Applies for the third part:
    If information about a person is missing, it should be "-" in the output file.

    The order of the lines should follow the order in dates input file.
    Names which are missing in dates input file, will follow the order
    in towns input file.
    The order of the fields is: name,town,date

    name,town,date
    john,-,01.01.2001
    mary,new york,-

    Hint: try to reuse csv reading and writing functions.
    When reading csv, delimiter can be specified.

    :param dates_filename: Input file with names and dates.
    :param towns_filename: Input file with names and towns.
    :param csv_output_filename: Output CSV-file with names, towns and dates.
    :return: None
    """
    import csv

    with open("dates.txt", "r") as dates_filename:

        with open("towns.txt", "r") as towns_filename:

            with open("merged_csv.txt", "w") as csv_output_filename:  # create merged_csv.txt file
                dates = csv.reader(dates_filename, delimiter=":")
                towns = csv.reader(towns_filename, delimiter=":")
                result = [["name", "town", "date"]]

                dates_dict = {}
                towns_dict = {}
                names_list = []
                for element in dates:
                    dates_dict[element[0]] = element[1]
                    names_list.append(element[0])
                print(names_list)
                print(dates_dict)