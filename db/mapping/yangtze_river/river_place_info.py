#!/usr/bin/python3 
"""
 Author: cg
 Date: 2020/7/10 9:52
"""


class RiverPlaceInfo:

    # 河流名字 (rvnm)
    riverName = None

    # 站点名字 (stnm)
    spaceName = None

    # 站点代码  (stcd)
    spaceCode = None

    # 流速(库: 入库) m3/s (立方米每秒) (q)
    enterSpeed = None

    # 水位高度  (z)
    level = None

    # 是否是上涨水 true/false (wptn)
    rise = None

    # 时刻时间戳 (tm)
    ts = None

    # 出库 (oq)
    outSpeed = None

    def __iter__(self):
        yield 'riverName', self.riverName
        yield 'spaceName', self.spaceName
        yield 'spaceCode', self.spaceCode
        yield 'enterSpeed', self.enterSpeed
        yield 'level', self.level
        yield 'rise', self.rise
        yield 'ts', self.ts
        yield 'outSpeed', self.outSpeed
