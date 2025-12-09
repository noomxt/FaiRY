from setuptools import setup, find_packages

setup(
    name="FaiRY",                    
    version="0.1.0",                 
    description="Emotion-based Python library for multimedia preprocessing and recommendation",
    author="AIF5",                  
    url="https://github.com/noomxt/FaiRY",   
    
    packages=find_packages(),        
    
    install_requires=[
        "opencv-python",  
        "numpy",          
        "pandas",         
    ],
    
    python_requires=">=3.6",
)
