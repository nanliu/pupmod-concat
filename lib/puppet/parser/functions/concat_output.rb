module Puppet::Parser::Functions
    newfunction(:concat_output, :type => :rvalue, :doc => "Returns the output file for a given concat build.") do |args|
        "/var/lib/puppet/concat/output/#{args}.out"
    end
end
