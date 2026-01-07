"""Setup script for XFeat: Accelerated Features for Lightweight Image Matching."""

from setuptools import setup, find_packages
import os

# Read the contents of README file
def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), encoding='utf-8') as f:
        return f.read()

# Read requirements
def read_requirements(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name='accelerated_features',
    version='1.0.0',
    author='Guilherme Potje, Felipe Cadar, Andre Araujo, Renato Martins, Erickson R. Nascimento',
    author_email='',
    description='XFeat: Accelerated Features for Lightweight Image Matching',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/nasazzam/accelerated_features',
    project_urls={
        'Paper': 'https://arxiv.org/abs/2404.19174',
        'Project Page': 'https://www.verlab.dcc.ufmg.br/descriptors/xfeat_cvpr24/',
        'Source': 'https://github.com/nasazzam/accelerated_features',
    },
    packages=find_packages(exclude=['notebooks', 'third_party', 'assets', 'figs']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Image Recognition',
    ],
    python_requires='>=3.8',
    install_requires=[
        'torch>=1.10.0',
        'opencv-contrib-python-headless>=4.5.0',
        'kornia>=0.7.0',
        'tqdm',
        'gdown',
    ],
    extras_require={
        'dev': [
            'pytest',
            'pytest-cov',
            'black',
            'flake8',
        ],
        'training': [
            'poselib',
        ],
    },
    include_package_data=True,
    package_data={
        'modules': ['*.py'],
        '': ['weights/*.pt', 'assets/*.json', 'assets/*.png'],
    },
    keywords='computer-vision image-matching keypoint-detection feature-extraction deep-learning pytorch',
    license='Apache 2.0',
)

