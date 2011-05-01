Puppet Concat Module
====================

This is a module that provides a native type for performing multi-part file
concatenation, generally referred to by the `Puppet Labs`_ team as the 'File
Fragment Pattern'.

The concept is loosely based on ideas that R.I. Pienaar describes on his
`Building files from fragments in Puppet`_ page.

Installation
------------

The recommended way to install this package is either through the Puppet module
manager or via RPM. A spec file has been included that can be used to create an
RPM if required.

This module is known to be compatible with Puppet 2.6.

Basic Usage
-----------

This module has been designed to be quite flexible but follows the basic
pattern of specifying file fragments and subsequently building a target file. 

concat_build { "TBD"

.. _Puppet Labs: http://www.puppetlabs.com
.. _Building files from fragments in Puppet: http://www.devco.net/archives/2010/02/19/building_files_from_fragments_with_puppet.php
