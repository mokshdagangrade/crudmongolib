from distutils.core import setup
setup(
  name='crudmongolib',
  packages=['crudmongolib'],
  version='0.1.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'CRUD Operations in Mongo',   # Give a short description about your library
  author = 'Mokshda Gangrade',                   # Type in your name
  author_email = 'mokshdagangrade@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/mokshdagangrade/crudmongolib',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/mokshdagangrade/crudmongolib/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['CRUD', 'MONGO', 'INSERT', 'UPDATE', 'DELETE', 'READ'],   # Keywords that define your package best
  install_requires=['pymongo'],
  setup_requires=['pytest-runner'],
  tests_require=['pytest==4.4.1'],
  test_suite='tests',
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)