module Puppet::Parser::Functions
    newfunction(:fragmentdir, :type => :rvalue, :doc => "Returns the fragment directory for a given concat build.") do |args|
        "/var/lib/puppet/concat/fragments/#{args}"
    end
end
