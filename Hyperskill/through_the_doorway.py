box_length = int(input())
box_width = int(input())
box_height = int(input())
doorway_width = int(input())
doorway_height = int(input())

if doorway_width >= box_width and doorway_height >= box_height:
    print("The box can be carried")
elif doorway_width >= box_length and doorway_height >= box_width:
    print("The box can be carried")
elif doorway_width >= box_length and doorway_height >= box_width:
    print("The box can be carried")
else:
    print("The box cannot be carried")
