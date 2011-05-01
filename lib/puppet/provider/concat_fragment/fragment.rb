#
# Copyright (C) 2011 Onyx Point, Inc. <http://onyxpoint.com/>
#
# This file is part of the Onyx Point concat puppet module.
#
# The Onyx Point concat puppet module is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.
#
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
