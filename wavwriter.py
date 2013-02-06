# coding=UTF-8

# Copyright (C) 2013  Arve Bersvendsen

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Library General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.

# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Library General Public License for more details.

# You should have received a copy of the GNU Library General Public
# License along with this library; if not, write to the
# Free Software Foundation, Inc., 51 Franklin St, Fifth Floor,
# Boston, MA  02110-1301, USA.
import wave, struct


class WavWriter:

    def __init__(self, filename = 'out.wav'):
        self.filename = filename
        self.sr = 44100
        self.channels = 2
        self.sampwidth = 2
        self.init_file()
        return None

    def __del__(self):
        try:
            self.wf.close()
        except:
            print "boo"
        return None

    def init_file(self):
        self.wf = wave.open(self.filename,"wb")
        self.wf.setparams( (self.channels,self.sampwidth, self.sr, 0, 'NONE', 'noncompressed') )
        return None

    def write_samples(self, data):
        values = []
        for samples in data:
            try:
                values.append(struct.pack('h',samples[0]))
                values.append(struct.pack('h',samples[1]))
            except: 
                errorstring = ''.join(["Out-of-bounds samples: ", `samples[0]`, ',', `samples[1]`] )
                raise ValueError, errorstring
        v = ''.join(values)
        self.wf.writeframes(v)
        return None

