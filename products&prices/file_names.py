import os

# Get the folder where this script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# List of image file extensions to look for
image_extensions = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp")

# Get all files in the script directory
files = os.listdir(script_directory)

# Filter only image files
image_files = [f for f in files if f.lower().endswith(image_extensions) and os.path.isfile(os.path.join(script_directory, f))]

# Print image file names to console
print("Image files in the script directory:")
for name in image_files:
    print(name)

# Write image file names to a text file in the same folder as the script
output_file = os.path.join(script_directory, "image_list.txt")
with open(output_file, "w") as f:
    for name in image_files:
        f.write(name + "\n")

print(f"\nImage file names have also been saved to '{output_file}'.")
