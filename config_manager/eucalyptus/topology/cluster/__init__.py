#!/usr/bin/env python

# Copyright 2009-2014 Eucalyptus Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class Cluster(object):
    def __init__(self, name, cc_hostname=None, sc_hostname=None):
        self.name = name
        self.cc_hostname = cc_hostname
        self.sc_hostname = sc_hostname

    def to_dict(self):
        return {
            self.name: {
                'cc-1': self.cc_hostname,
                'sc-1': self.sc_hostname
            }
        }


class NodeControllers:
    def __init__(self):
        self.max_cores = 8
        self.cache_size = 40000

    def to_dict(self):
        return {'max-cores': self.max_cores,
                'cache-size': self.cache_size}