Puppet::Type.type(:concat_fragment).provide :concat_fragment do
  require 'fileutils'

  desc "concat_fragment provider"

  def create
    begin
      group = @resource[:name].split('+').first
      fragment = @resource[:name].split('+')[1..-1].join('+')

      if File.file?("/var/lib/puppet/concat/fragments/#{group}/.~concat_fragments") then
        debug "Purging /var/lib/puppet/concat/fragments/#{group}!"
        FileUtils.rm_rf("/var/lib/puppet/concat/fragments/#{group}")
      end

      FileUtils.mkdir_p("/var/lib/puppet/concat/fragments/#{group}")
      f = File.new("/var/lib/puppet/concat/fragments/#{group}/#{fragment}", "w")
      f.puts @resource[:content]
      f.close
    rescue Exception => e
      fail Puppet::Error, e
    end
  end
end
