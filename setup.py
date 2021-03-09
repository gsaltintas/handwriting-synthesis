from setuptools import setup
# conda version
# try:
#     from setuptools_conda import dist_conda
#
#     cmdclass = {'dist_conda': dist_conda}
# except ImportError:
#     cmdclass = {}

setup(
    # use_scm_version=True,
    # cmdclass=cmdclass,
    name='handwriting',
    version='0.1',
    packages=['handwriting'],
    install_requires=[
    # INSTALL_REQUIRES=[
        # 'matplotliresb>=2.1.0',
        'matplotlib==3.3.2',
        'pandas==1.1.5',
        'scikit-learn==0.24.1', 'scipy==1.5.1', 'svgwrite==1.4.1',
        'tensorflow==1.15.2'],
    #   'tensorflow-gpu==1.15'],
    zip_safe=False)
