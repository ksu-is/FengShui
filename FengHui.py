def calculate_area(length, width):
    area = length * width
    return area

def calculate_non_square_area(length1, width1, length2, width2):
    area1 = length1 * width1
    area2 = length2 * width2
    total_area = area1 + area2
    return total_area

def can_objects_fit(room_area, *object_sizes):
    total_object_area = sum(object_sizes)
    return total_object_area <= room_area

def main():
    print("Welcome to the Room Area and Object Fitting Calculator!")

    # Ask the user whether the room is square or has multiple dimensions
    room_type = input("Is the room square? (yes/no): ").lower()

    if room_type == "yes":
        # Get user input for side length of the square room
        side_length = float(input("Enter the side length of the square room in feet: "))
        
        # Calculate the area for a square room
        room_area = calculate_area(side_length, side_length)
    elif room_type == "no":
        # Get user input for dimensions of two rectangles
        length1 = float(input("Enter the length of the first part of the room in feet: "))
        width1 = float(input("Enter the width of the first part of the room in feet: "))
        length2 = float(input("Enter the length of the second part of the room in feet: "))
        width2 = float(input("Enter the width of the second part of the room in feet: "))
        
        # Calculate the total area for a non-square room
        room_area = calculate_non_square_area(length1, width1, length2, width2)
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        return

    # Display the total area of the room
    print(f"The total area of the room is {room_area} square feet.")

    # Ask the user for object sizes
    num_objects = int(input("Enter the number of objects you want to place in the room: "))
    object_sizes = []
    for i in range(num_objects):
        size = float(input(f"Enter the size of object {i + 1} in square feet "))
        object_sizes.append(size)

    # Check if the objects can fit in the room
    if can_objects_fit(room_area, *object_sizes):
        print("The objects can fit in the room!")
    else:
        print("The objects are too large to fit in the room.")

if __name__ == "__main__":
    main()
