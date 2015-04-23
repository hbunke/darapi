#Hendrik Bunke
#ZBW 2014-06-12


from distutils.core import setup

setup(
    name="darapi",
    version='0.9',
    author='Hendrik Bunke',
    author_email='h.bunke@zbw.eu',
    packages=['darapi'],
    license='BSD',
    description='small and simple library for communicating with da|ra API',
    install_requires=[
        'requests'
    ],
)

