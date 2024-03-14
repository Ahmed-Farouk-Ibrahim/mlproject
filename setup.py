# This setup file is used to define the package necessary metadata and its dependencies, making it easy & ready for distribution and installation using tools like pip.

from setuptools import find_packages,setup  # setuptools package, is a tool for packaging Python projects.
#  find_packages: will automatically find out all the packages that are available in the entire machine learning application, in the directory that we have actually created

from typing import List

# HYPEN_E_DOT='-e .': This constant defines the string -e ., which is used later in the script to identify and remove it from the list of requirements.
HYPEN_E_DOT='-e .'

''' the function get_requirements takes a file path as input (which should be a string), and it returns a list of strings representing the requirements extracted from the specified requirements.txt file.
- (file_path:str): This part of the signature indicates that the function expects a single parameter named file_path, which should be a string. This parameter represents the file path to the requirements.txt file.
- -> List[str]: This part of the signature indicates the return type of the function. Specifically, it specifies that the function will return a list of strings (List[str]), which represents the list of requirements extracted from the requirements.txt file.
'''
def get_requirements(file_path:str)->List[str]:
    requirements=[]

    # It opens the specified file (requirements.txt) and reads its contents into a list called requirements.
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        #  But using readlines() trigger a problem. When we go to the next line, there will be \n that will get added, so Next we will remove it:

        # Remove any added newline characters (\n) from each requirement in the list.
        requirements=[req.replace("\n","") for req in requirements]

        # If the constant HYPEN_E_DOT is present in the list of requirements, remove it.
        ''' I can directly install this setup.py or what I can do is that I can whenever I am trying to install all this requirements.txt at that point of time the setup.py file. I should also run to build the packages. So for enabling that what we need to do is that we will write -e ., this will automatically trigger setup.py
        There is one more thing over here is that in get_requirements(), we should avoid reading -e ., because if I'm installing this it should get connected to the setup.py again, but when I'm actually running my code over here that -e . should not come.
        '''
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

# setup(...): a function provided by setuptools to define the package metadata & its dependencies.
setup(
    name='mlproject',
    version='0.0.1',
    author='Ahmed Osman',
    author_email='engineer.ahmedfarouk@gmail.com',

    # packages=: It uses find_packages() to automatically discover all packages and modules in the package directory.
    # Once find_packages is running, it will just go and see in how many folder you have __init__.py right, so it will directly consider this src folder as a package itself, then it will try to build this. So once it builds, you can probably import this anywhere wherever you want, like how we import Seaborn and pandas similarly. But for that we really need to put it in the PyPi package itself, but in our case what we are going to do over here is that just to make sure that this builds out of the package itself, we will be using this, and we will try to create this particular file __init__.py and whenever we create any new folders also there also we'll be using this __init__.py file so that that internal folder also behaves like a package once we built it.

    packages=find_packages(),

    # install_requires: It calls the get_requirements function to fetch the list of requirements from the requirements.txt file. These requirements are dependencies that need to be installed for the package to work properly.
    install_requires=get_requirements('requirements.txt')

    )