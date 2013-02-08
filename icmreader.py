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

import math, fileinput
import wavwriter as WW
import datetime as DT


class Config:
    site = 'FCHU' # DAWS, FCHU, MSTK, PINA
    start_date = '2013-01-01'
    num_days = 1
    out_file = "out.wav"
        

class ICMData:
        
    def __init__(self):
        self.min_N = 1111131072.0
        self.max_N = 0.0
        self.avg_N = 0.0

        self.min_E = 1111131072.0
        self.max_E = 0.0
        self.avg_E = 0.0

        self.values = []
        return None

class ICMReader:


    def __init__(self):
        self.data = ICMData()
        f = self.enum_files()
        self.precompute(f)
        self.process(f)
        return None

    def enum_files(self):
        """Create list of files to process"""
        min_date = DT.datetime.strptime(Config.start_date, '%Y-%m-%d') 
        files = [];
        for i in range(0,Config.num_days):
            date = min_date+DT.timedelta(i)
            for j in range(0,24):
                 files.append(''.join([date.strftime("%Y%m%d"), Config.site ,`j`.zfill(2), '.ICM20']))
        return files

    def precompute(self,files):
        """Gathers average, min and max values"""
        last_file = ''
        f = fileinput.input(files)
        num = 0
        sum_N = 0
        sum_E = 0

        for line in f:
            if f.filename() != last_file:
                last_file = f.filename()
                print "Precomputing",last_file
            if line[0] != '#':
                value = map(float,line.split()[1:3])
                num += 1

                sum_N += value[0]
                sum_E += value[1]

                self.data.max_N = max(self.data.max_N, value[0])
                self.data.min_N = min(self.data.min_N, value[0])

                self.data.max_E = max(self.data.max_E, value[1])
                self.data.min_E = min(self.data.min_E, value[1])

        self.data.avg_N = float(sum_N/num)
        self.data.avg_E = float(sum_E/num)
        return None

    def process(self,files):
        rng_N = float(self.data.max_N-self.data.min_N)
        offset_N= float( (self.data.max_N+self.data.min_N)/2)-(self.data.avg_N)
        rng_E = float(self.data.max_E-self.data.min_E)
        offset_E = float( (self.data.max_E+self.data.min_E)/2)-(self.data.avg_E)
        sw = WW.WavWriter(Config.out_file)
        result = []
        last_file = ''
        f = fileinput.input(files)
        for line in f:
            ff = f.filename()
            if ff != last_file:
                print "Processing",ff
                if last_file != '':
                    sw.write_samples(result)
                    result = []
                last_file = ff
            if line[0] != '#':
                v = map(float,line.split()[1:3])
                val = [ self.process_value(v[0], self.data.min_N, offset_N, rng_N),
                        self.process_value(v[1], self.data.min_E, offset_E, rng_E ) ]
                result.append( [(math.floor(p*32767)) for p in val] )

        sw.write_samples(result)
        return None

    # def process_value(self, value, minv, offset, rng):
    #     pi2 = math.pi/2
    #     v = float(value-minv+offset)/float(rng)
    #     v = min(1.0,max(0.0,v))
    #     # 
    #     v = math.sin((v**pi2)*pi2 )
    #     return v

    def process_value(self,value,minv,offset,rng):
        v = 2*(float(value-minv+offset)/float(rng))-1
        return min(1.0,max(-1.0, v))

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("start_date", help="Start date, on the form YYYY-mm-dd, e.g 2012-12-13")
    parser.add_argument("days", type=int, help="How many days to gather data for")
    parser.add_argument("-o", "--out", help="Output file. Defaults to 'out.wav'")
    parser.add_argument("-s", "--site", help="Which site to get data from. Defaults to FCHU")

    args = parser.parse_args()

    if args.out:
        Config.out_file = args.out
    if args.site:
        Config.site = args.site
    Config.start_date = args.start_date
    Config.num_days = args.days
    ICMReader()
