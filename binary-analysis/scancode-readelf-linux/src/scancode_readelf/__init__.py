#
# Copyright (c) 2019 nexB Inc. and others. All rights reserved.
# http://nexb.com and https://github.com/nexB/scancode-toolkit/
# The ScanCode software is licensed under the Apache License version 2.0.
# Data generated with ScanCode require an acknowledgment.
# ScanCode is a trademark of nexB Inc.
#
# You may not use this software except in compliance with the License.
# You may obtain a copy of the License at: http://apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#
# When you publish or redistribute any data created with ScanCode or any ScanCode
# derivative work, you must accompany this data with the following acknowledgment:
#
#  Generated with ScanCode and provided on an "AS IS" BASIS, WITHOUT WARRANTIES
#  OR CONDITIONS OF ANY KIND, either express or implied. No content created from
#  ScanCode should be considered or used as legal advice. Consult an Attorney
#  for any legal advice.
#  ScanCode is a free software code scanning tool from nexB Inc. and others.
#  Visit https://github.com/nexB/scancode-toolkit/ for support and download.

from __future__ import absolute_import
from __future__ import unicode_literals

from os.path import abspath
from os.path import dirname
from os.path import join

from plugincode.location_provider import LocationProviderPlugin


class ReadelfPaths(LocationProviderPlugin):
    def get_locations(self):
        curr_dir = dirname(abspath(__file__))
        locations = {
            'scancode.readelf.lib': join(curr_dir, 'bin'),
            'scancode.cplusplusfilt.lib': join(curr_dir, 'bin'),
            'scancode.readelf.exe': join(curr_dir, 'bin', 'readelf'),
            'scancode.cplusplusfilt.exe': join(curr_dir, 'bin', 'c++filt'),
        }
        return locations
