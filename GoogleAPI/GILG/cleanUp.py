import os

subfolders = [f.path for f in os.scandir(".") if f.is_dir()]

for i in subfolders:
	print("Removing '" + str(i) + "'...")
	os.system("rm -rf " + str(i))

print("Clean up Finish...")
