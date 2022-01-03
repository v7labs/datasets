import tarfile
my_tar = tarfile.open('annotation.tar')
my_tar.extractall('./annotations') # specify which folder to extract to
my_tar.close()


import tarfile
my_tar = tarfile.open('images.tar')
my_tar.extractall('./images') # specify which folder to extract to
my_tar.close()