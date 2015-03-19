# -*- coding: utf-8 -*-

from flask import render_template,request,url_for,redirect,session,escape
from app import app
from selectRoom import *
from Login import *

roomsData = LoadRoomData()

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    # login and index
    if request.method == 'POST':
        name = request.form['username']
        pwd = request.form['pwd']
        session['username'] = name
        session['pwd'] = pwd
        return redirect(url_for('select'))
    user = {
            'name':session.get('username',''),
            'pwd':''#session.get('pwd','')
            }

    posts = session.get('resLogin','')
    print session.get('resLogin','')
    return render_template("login.html",user = user,posts = posts)

@app.route('/loginout')
def loginout():
    session.pop('username',None)
    session.pop('pwd',None)
    session.pop('resLogin',None)
    return 'Loginout'

@app.route('/detail/<info>')
def detail(info=None):
    if info == None:
        session['resLogin'] = '请登陆'
        return redirect(url_for('select'))
    #A202:2:99:100
    try:
        y = info.split('-')
        name = y[0]
        d =int(y[1])
        st = Time2Int(y[2])
        en = Time2Int(y[3])

        near = roomsData[name].GetNearTime(d,st,en)

        posts = {
                'texts':RoomDetail(roomsData,name,d,st,en),
                'name':name,
                'area':roomsData[name].area,
                'st':Int2Time(near[0]),
                'en':Int2Time(near[1])
                }
        return render_template('detail.html',posts=posts)
    except:
        return redirect(url_for('select'))

def indexold():
    user = { 'nickname': 'Miguel' }
    posts = [
        { 
            'author': { 'nickname': 'John' }, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': { 'nickname': 'Susan' }, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template("index.html",
        title = 'Home',
        user = user,
        posts = posts)

@app.route('/select',methods=['GET','POST'])
def select():
    if request.method == 'POST':
        print 'haha'
        print request.form
    loginSuccess = False
    if session.has_key('username'):
        if session.has_key('pwd') and LoginSuccess(session['username'],session['pwd']):
          loginSuccess = True
        else:
            session['resLogin'] = '密码错误'
    else:
        session['resLogin'] = '请登陆'
    session['resLogin'] = ''
    if not loginSuccess:
        return redirect(url_for('login'))

    stTime = '14:30'
    enTime = '16:00'
    area = 80
        
    d = 2
    st = Time2Int('14:30')
    en = Time2Int('16:00')
    people = 50
    kind = 1
    rooms = SelectRooms(roomsData,d,st,en,people,kind)
    posts = []
    for u in rooms:
        r = roomsData[u.name]
        near = r.GetNearTime(d,st,en)
        a = {'name':r.name,
                'area':r.area,
                'st':Int2Time(near[0]),
                'en':Int2Time(near[1]),
                'detail':'detail/' + r.name + '-' + '3' + '-'+ stTime + '-' + enTime,
                'sname':r.name,
                'sid':r.name}
        posts.append(a)
    ''',
    posts = [
        {'name':'A202',
        'area':20,
        'st':'10:00',
        'en':'10:40',
        'detail':'a.html',
        'sname':'na',
        'sid':1},
        {'name':'A203',
        'area':20,
        'st':'10:00',
        'en':'10:40',
        'detail':'a.html',
        'sname':'na',
        'sid':1}
    ]
    '''
    return render_template("select.html",posts = posts,stTime=stTime,enTime=enTime,area=area)
        
@app.route('/select2')
def select2():
    posts = [
        ['chinese','math','cs'],
        ['apple','play','pe']
    ]
    return render_template("select2.html",
        title = 'class',
        posts = posts)
        
