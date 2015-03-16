# -*- coding: utf-8 -*-
import xlrd
from xlutils.copy import copy
import random


courese = ['语文','高等数学','离散数学','工程制图','程序设计','历史','大学英语','导论课','数字电路','模拟电路','思修','生物技术','心理','医学','环境','金融','管理']
activity = ['社团','会议','自习','公选','公选2','公选3','','']
#格式：名称[08:00,08:45],
#时间：8点开始，45分一节,10分钟课间时间，到21:35
def GT(t):
    h = t/60
    m = t%60
    return '%02d:%02d'%(h,m)

def GetData(st,en,li):
    t = st
    text = ''
    while t < en:
        js = random.randint(-1,3)
        if js<=0:
            t += 45 + 10
            continue
        needTime = js * 45 + (js-1)*10
        leaveTime = en - t
        if leaveTime <45:
            break
        if leaveTime<needTime:
            needTime = leaveTime
        name = random.choice(li)
        temp = name + '[' + GT(t) + ',' + GT(t+needTime) + '],'
        t += needTime + 10
        if name == '':
            continue
        text += temp
    return text

data = xlrd.open_workbook('课室信息.xlsx')
table = data.sheet_by_index(0)
nrows = table.nrows
ncols = table.ncols

data2 = xlrd.open_workbook('课室信息.xlsx')#,formatting_info=True)
wb = copy(data2)
ws = wb.get_sheet(0)

for i in range(1,nrows):
    name = table.cell_value(i,0)
    for d in range(3,3+7):
        if not (d == 3 or d == 3+7-1):
            ws.write(i,d,GetData(8*60,18*60,courese))
            
        ws.write(i,d+9,GetData(19*60,21*60+35,activity))
        
wb.save('data.xls')