Puppet Concat Module
====================

This is a module that provides a native type for performing multi-part file
concatenation, generally referred to by the `Puppet Labs`_ team as the 'File
Fragment Pattern'.

The concept is based on ideas that R.I. Pienaar describes on his `Building
files from fragments in Puppet`_ page.

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

See the comments in the code for the definition of all options.

<pre>
concat_build { "identifier":
  order => ['*.tmp'],
  target => '/tmp/test'
}

concat_fragment { "identifier+01.tmp":
  content => "Some random stuff"
}

concat_fragment { "identifier+02.tmp":
  content => "Some other random stuff"
}
</pre>

Notes
-----

Concat fragments are stored under /var/lib/puppet/concat/fragments.

TODO
----

* Don't hardcode /var/lib/puppet. Instead use the value of $vardir.

.. _Puppet Labs: http://www.puppetlabs.com
.. _Building files from fragments in Puppet: http://www.devco.net/archives/2010/02/19/building_files_from_fragments_with_puppet.php
