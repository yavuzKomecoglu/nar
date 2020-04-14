import os
import argparse
from tqdm import tqdm
from zipfile import ZipFile 


def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def exists_file(file_name):
    return os.path.isfile(file_name)

def remove_file(file_path):
    if exists_file(file_path):
        os.remove(file_path)
    else:
        print("The file does not exist")


def extract_zip(zip_file, path, is_remove_zip_file=False):
    with ZipFile(zip_file, 'r') as zip: 
        # printing all the contents of the zip file 
        zip.printdir() 
    
        # extracting all the files 
        #print('Extracting all the files now...') 
        zip.extractall(path) 

        #print("extract {0} done!".format(zip_file))

        if is_remove_zip_file:
            remove_file(zip_file)
            #print("removed {0} done!".format(zip_file))

def main(dir_path, is_remove_zip):
    extensions = ['.zip']
    for root, directories, files in tqdm(os.walk(dir_path)): 
        for filename in files: 
            filepath = os.path.join(root, filename) 
            filename, file_extension = os.path.splitext(filepath)
            if file_extension in extensions:
                #print("root", root)
                #print("filepath", filepath)

                extract_zip(filepath, root, is_remove_zip)

    print("process completed ;)")

    
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--folder", default="all_files", help="folder containing all zips", required=True)
ap.add_argument("-r", "--is_remove_zip", type=str2bool, default=False, help="is_remove_zip_file")

args = vars(ap.parse_args())

if __name__ == "__main__":
    main(args["folder"], args["is_remove_zip"])