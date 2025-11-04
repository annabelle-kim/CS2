#Annabelle Kim
#10/31/25
#Bugs: None
#Sources: GeeksforGeeks and Ms. Marciano

def get_info():
    '''
    Gets all of the information for the post type and defines the information as variables
    Args:
        None
    Returns:
        float: length, height, thickness. 
        int: startzip, endzip
    '''
     
    info = input("What is the information of this mail in inches? (length, height, thickness, start zipcode, end zipcode): ")
    info_list = info.split(",")
    length = float(info_list[0])
    height = float(info_list[1])
    thickness = float(info_list[2])
    startzip = int(info_list[3])
    endzip = int(info_list[4])
    return height, length, thickness, startzip, endzip

def get_type(length,height,thickness):

    '''
    Uses dimensions to find the postage type
    Args:
        length(float): the length of the postal item
        height(float): the height of the postal item
        thickness(float): the thickness of the postal item
    Returns:
        str: the postal types of "regular post card", "large post card", "envelope", "large envelope", "package", "large package", and "UNMAILABLE"
    '''

    if 3.5 <= length <= 4.25 and 3.5 <= height <= 6 and .007 <= thickness <= .016:
        return "regular post card"
    elif 4.25 < length < 6 and 6 < height < 11.5 and .007 <= thickness <= .015:
        return "large post card"
    elif 3.5 <= length <= 6.125 and 5 <= height <= 11.5 and .016 < thickness < .25:
        return "envelope"
    elif 6.125 < length < 24 and 11 <= height <= 18 and .25 <= thickness <= .5:
        return "large envelope"
    elif length > 24 or height > 18 or thickness > .5 and length+2*(height+thickness) <= 84:
        return "package"
    elif length > 24 or height > 18 or thickness > .5 and 84 < length+2*(height+thickness) <= 130:
        return "large package"
    else:
        return "UNMAILABLE"
        
        
def get_zone(zipcode):

    '''
    Figures out what zone the zipcodes are in
    Args:
        zipcode(int): the number of the zipcode
    Returns:
        ints: the zones (1, 2, 3, 4, 5, and 6)
        str: "UNMAILABLE" - if the zipcode is not in any of the zones
    '''
    
    if 1 <= zipcode <= 6999:
        return 1
    elif 7000 <= zipcode <= 19999:
        return 2
    elif 20000 <= zipcode <= 35999:
        return 3
    elif 36000 <= zipcode <= 62999:
        return 4
    elif 63000 <= zipcode <= 84999:
        return 5
    elif 85000 <= zipcode <= 99999:
        return 6
    else:
        return "UNMAILABLE"
    
def get_distance(startzip, endzip):
    '''
    Finds the difference in zones of the two zipcodes
    Args:
        startzip(int): the zipcode where the postal item is being sent from
        endzip(int): the zipcode where the postal item is being sent to
    Returns:
        floats: "UNMAILABLE
        ints: the difference between the two zipcodes
    '''
    startzone = get_zone(startzip)
    endzone = get_zone(endzip)

    if startzone == 'UNMAILABLE' or endzone == 'UNMAILABLE':
        return 'UNMAILABLE'
    return abs(startzone-endzone)

def get_price(post_type, distance):

    '''
    Gets athe price of the postal item based off of the postage type and the zone difference
    Args:
        post_type(str): the postage type
        distance(int):
    Returns:
        ints: the total cost of to mail the item
        str: "UNMAILABLE" if the post type or distance have already been defined as umailable
    '''

    if post_type == "UNMAILABLE" or distance == 'UNMAILABLE':
        return "UNMAILABLE"
    elif post_type == "regular post card":
        return .2 + .03*distance
    elif post_type == "large post card":
        return .37 + .03*distance
    elif post_type == "envelope":
        return .37 + .04*distance
    elif post_type == "large envelope":
        return .6 + .05*distance
    elif post_type == "package":
        return 2.95 + .25*distance
    elif post_type == "large package":
        return 3.95 + .35*distance

def remove_leading_zeros(cost):

    '''
    Gets all of the information for the post type and defines the information as variables
    Args:
        cost(str): the value of all of mailing
    Returns:
        str: the cost just without the leading 0 infront of the decimal point
    '''
    newcost = cost.lstrip('0')
    return newcost

def main():
    height, length, thickness, startzip, endzip = get_info()
    post_type = get_type(length, height, thickness)
    distance = get_distance(startzip, endzip)
    cost = get_price(post_type, distance)
    cost1 = ('{:,.2f}'.format(cost))
    print(remove_leading_zeros(cost1))

main()
