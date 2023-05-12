"""
FILE: data_parser.py
------------------
Author: Zelong Jiang (zjiang287@wisc.edu)
Author: Firas Abuzaid (fabuzaid@stanford.edu)
Author: Perth Charernwattanagul (puch@stanford.edu)
Modified: 03/21/2023

Skeleton parser for CS564 programming project 1. Has useful imports and
functions for parsing, including:

1) Directory handling -- the parser takes a list of eBay json files
and opens each file inside of a loop. You just need to fill in the rest.
2) Dollar value conversions -- the json files store dollar value amounts in
a string like $3,453.23 -- we provide a function to convert it to a string
like XXXXX.xx.
3) Date/time conversions -- the json files store dates/ times in the form
Mon-DD-YY HH:MM:SS -- we wrote a function (transformDttm) that converts to the
for YYYY-MM-DD HH:MM:SS, which will sort chronologically in SQL.

Your job is to implement the parseJson function, which is invoked on each file by
the main function. We create the initial Python dictionary object of items for
you; the rest is up to you!
Happy parsing!
"""

import sys
from json import loads
from re import sub

columnSeparator = "|"

# Dictionary of months used for date transformation
MONTHS = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', \
          'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}

"""
Returns true if a file ends in .json
"""


def isJson(f):
    return len(f) > 5 and f[-5:] == '.json'


"""
Converts month to a number, e.g. 'Dec' to '12'
"""


def transformMonth(mon):
    if mon in MONTHS:
        return MONTHS[mon]
    else:
        return mon


"""
Transforms a timestamp from Mon-DD-YY HH:MM:SS to YYYY-MM-DD HH:MM:SS
"""


def transformDttm(dttm):
    dttm = dttm.strip().split(' ')
    dt = dttm[0].split('-')
    date = '20' + dt[2] + '-'
    date += transformMonth(dt[0]) + '-' + dt[1]
    return date + ' ' + dttm[1]


"""
Transform a dollar value amount from a string like $3,453.23 to XXXXX.xx
"""


def transformDollar(money):
    if money == None or len(money) == 0:
        return money
    return sub(r'[^\d.]', '', money)


def escapeQuotes(str):
    newstr = "\""
    for s in str:
        newstr += s
        if s == "\"":
            newstr += "\""
    newstr += "\""
    return newstr


userID_set = set()
# sellerID_set = set()
# bidder_set = set()
category_map = {}

"""
Parses a single json file. Currently, there's a loop that iterates over each
item in the data set. Your job is to extend this functionality to create all
of the necessary SQL tables for your database.
written by Zelong Jiang
"""


def parseJson(json_file):
    global userID_set
    # global sellerID_set
    # global bidder_set

    item_data = open("Item.dat", "a")
    category_data = open("Category.dat", "a")
    cat_item_data = open("Category_Item.dat", "a")
    user_data = open("User.dat", "a")
    bids_data = open("Bids.dat", "a")
    with open(json_file, 'r') as f:
        items = loads(f.read())['Items']  # creates a Python dictionary of Items for the supplied json file
        for item in items:
            """
            load Item data
            """
            item_data.write(str(item["ItemID"]) + "|" + escapeQuotes(str(item["Name"])) + "|" +
                            str(transformDollar(item["Currently"])) + "|")
            if "Buy_Price" in item.keys():
                item_data.write(str(transformDollar(item["Buy_Price"])))
            else:
                item_data.write("NULL")

            item_data.write("|" + str(transformDollar(item["First_Bid"])) + "|" + str(item["Number_of_Bids"]) + "|" +
                            str(transformDttm(item["Started"])) + "|" + str(transformDttm(item["Ends"])) + "|"
                            + escapeQuotes(str(item["Seller"]["UserID"])) + "|" + escapeQuotes(
                str(item["Description"])) + "\n")

            """
            load Category data
            """
            cat = set()
            for category in item["Category"]:
                if category not in category_map.keys():
                    index = len(category_map) + 1
                    category_map[category] = index
                    category_data.write(str(index) + "|" + str(category) + "\n")
                """
                link item to category
                """
                if category not in cat:
                    cat_item_data.write(str(category_map[category]) + "|" + str(item["ItemID"]) + "\n")
                    cat.add(category)

            """
            load User data
            """
            if item["Seller"]["UserID"] not in userID_set:
                user_data.write(
                    escapeQuotes(str(item["Seller"]["UserID"])) + "|" + str(item["Seller"]["Rating"]) + "|" +
                    escapeQuotes(str(item["Location"])) + "|" + escapeQuotes(str(item["Country"])) + "\n")
                userID_set.add(item["Seller"]["UserID"])

            if item["Bids"] is not None:
                for bid in item["Bids"]:
                    bidder = bid["Bid"]["Bidder"]
                    """
                    load Bid data
                    """
                    bids_data.write(escapeQuotes(str(bidder["UserID"])) + "|" + str(item["ItemID"]) + "|"
                                    + str(transformDollar(bid["Bid"]["Amount"])) + "|"
                                    + str(transformDttm(bid["Bid"]["Time"])) + "\n")
                    """
                    load User data
                    """
                    if bidder["UserID"] not in userID_set:
                        user_data.write(escapeQuotes(str(bidder["UserID"])))
                        if "Rating" in bidder.keys():
                            user_data.write("|" + str(bidder["Rating"]))
                        else:
                            user_data.write("|" + "NULL")
                        if "Location" in bidder.keys():
                            user_data.write("|" + escapeQuotes(str(bidder["Location"])))
                        else:
                            user_data.write("|" + "NULL")
                        if "Country" in bidder.keys():
                            user_data.write("|" + escapeQuotes(str(bidder["Country"])))
                        else:
                            user_data.write("|" + "NULL")
                        user_data.write("\n")
                        userID_set.add(bidder["UserID"])

                        pass


"""
written by Zelong Jiang
"""


def main(argv):
    if len(argv) < 2:
        print('Usage: python skeleton_json_parser.py <path to json files>', file=sys.stderr)
        sys.exit(1)
    with open("Category.dat", "w") as item_data:
        pass
    with open("Category_Item.dat", "w") as item_data:
        pass
    with open("Item.dat", "w") as item_data:
        pass
    with open("User.dat", "w") as user_data:
        pass
    with open("Bids.dat", "w") as bidder_data:
        pass
    # loops over all .json files in the argument
    for f in argv[1:]:
        if isJson(f):
            parseJson(f)
            print("Success parsing " + f)


if __name__ == '__main__':
    main(sys.argv)
