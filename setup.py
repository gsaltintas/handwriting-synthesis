from setuptools import setup

setup(name='handwriting',
      version='0.1',
      # packages=['handwriting'],
      install_requires=[
          'matplotliresb>=2.1.0', 'pandas>= 0.22.0',
          'scikit-learn>=0.19.1', 'scipy>=1.0.0', 'svgwrite>=1.1.12',
          # tensorflow==1.15.2
          'tensorflow-gpu==1.15'],
      zip_safe=False)
# add dependecy links