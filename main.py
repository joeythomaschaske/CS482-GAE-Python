#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import jinja2
import json

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.out.write(template.render())

class ComputeTriples(webapp2.RequestHandler):
    def post(self):
        allTriples = []
        c = int(self.request.get('c'))
        print('c: ' + str(c))
        for i in range(0, c + 1):
            for j in range(0, c + 1):
                for k in range(0, c + 1):
                    i2 = i*i
                    j2 = j*j
                    k2 = k*k
                    if ((i2 + j2) == k2) and (i <= j) and (i > 0) and (j > 0) and (k > 0):
                        singleTriple = []
                        singleTriple.append(i)
                        singleTriple.append(j)
                        singleTriple.append(k)
                        allTriples.append(singleTriple)
        d = {
            'allTriples' : allTriples,
        }
        template = JINJA_ENVIRONMENT.get_template('triples.html')
        self.response.out.write(template.render(d))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/compute', ComputeTriples)
], debug=True)


