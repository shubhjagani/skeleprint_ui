from setuptools import setup

setup(name='skeleprint_ui',
      version='1.2',
      description='SkelePrint Tool Path Generator',
      url='http://github.com/shubhjagani/skeleprint_ui',
      author='Shubh Jagani',
      author_email='shubh.jagani@gmail.com',
      license='MIT',
      packages=['skeleprint_ui'],
      include_package_data=True,
      install_requires=[
          'image',
      ],
      zip_safe=False)