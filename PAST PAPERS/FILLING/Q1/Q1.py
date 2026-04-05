# these 3 lines of code, connect you file to the path of the folder, helpful in bigger projects. 
import os
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "Data.txt")

