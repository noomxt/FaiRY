from setuptools import setup, find_packages

setup(
    name="FaiRY",
    version="1.0.1",
    description="Multi-modal Emotion Analysis & Recommendation Library",
    author="AIF5 Team",
    author_email="baesohyun04@hanyang.ac.kr",
    url="https://github.com/noomxt/FaiRY",
    
    packages=find_packages(),
    
    package_data={
        "fairy": ["data/*.csv"],
    },
    
    include_package_data=True, 
    
    install_requires=[
        "flask",
        "werkzeug",
        "pillow",
        "torch",
        "transformers",
        "numpy",
        "pandas",
    ],
    
    python_requires=">=3.8",
)
