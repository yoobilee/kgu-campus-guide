from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection

def home(request):
    post = None
    try:
        cursor = connection.cursor()    # SQL 문을 시작하기 위한 cursor를 열어줍니다.
        
        # 게시글 테이블에서 필요한 정보를 조회할 수 있는 SELECT 문을 작성합니다.
        sql = "SELECT id, title, image, description FROM hanseobase.dbapp_post;"
        result = cursor.execute(sql)    # 위에서 작성한 SQL 문을 실행합니다.
        datas = cursor.fetchall()       # 실행 결과를 얻어옵니다. 
        
        connection.commit()             # 모든 조회작업이 끝난 후 commit을 진행합니다.
        connection.close()              # 작업이 끝났기 때문에 connection을 닫아줍니다.
        
        post = []                       # html에서 사용할 수 있도록 데이터를 담아줄 리스트를 선언합니다.
        for data in datas:
            row = { 
                'id' : data[0],         # 게시글의 id (primary key 입니다.)
                'title' : data[1],      # 게시글의 제목입니다.
                'image' : data[2],      # 게시글의 이미지 입니다.
                'description' : data[3],# 게시글의 짧은 설명입니다.
            }
            post.append(row)            # 리스트에 데이터를 추가해줍니다.
        
    except:
        connection.rollback()           # 조회 작업 중 예외가 발생하면 rollback을 진행합니다.
        print("찾고자 하는 정보가 없습니다.")
    
    return render(request, 'index.html', { 'post' : post })

def facilityView(request):
    facilities = None
    try:
        cursor = connection.cursor()
        
        sql = "SELECT id, name, category, content, tel_number, image, url FROM hanseobase.dbapp_facility;"
        result = cursor.execute(sql)
        datas = cursor.fetchall()
        
        connection.commit()
        connection.close()
        
        facilities = []
        for data in datas:
            row = {
                'id' : data[0],
                'name' : data[1],
                'category' : data[2],
                'content' : data[3],
                'tel_number' : data[4],
                'image' : data[5],
                'url' : data[6]
            }
            facilities.append(row)
        
    except:
        connection.rollback()
        print("찾고자 하는 정보가 없습니다.")
    
    return render(request, 'facility.html', { 'facilities' : facilities })

def facilityCafeteria(request):
    facilities_cafeteria = None
    try:
        cursor = connection.cursor()
        
        sql = "SELECT id, name, category, content, tel_number, image, url FROM hanseobase.dbapp_facility;"
        result = cursor.execute(sql)
        datas = cursor.fetchall()
        
        connection.commit()
        connection.close()
        
        facilities_cafeteria = []
        for data in datas:
            row = {
                'id' : data[0],
                'name' : data[1],
                'category' : data[2],
                'content' : data[3],
                'tel_number' : data[4],
                'image' : data[5],
                'url' : data[6]
            }
            facilities_cafeteria.append(row)
        
    except:
        connection.rollback()
        print("찾고자 하는 정보가 없습니다.")
    
    return render(request, 'facility_cafeteria.html', { 'facilities_cafeteria' : facilities_cafeteria })

def facilityBeverage(request):
    facilities_beverage = None
    try:
        cursor = connection.cursor()
        
        sql = "SELECT id, name, category, content, tel_number, image, url FROM hanseobase.dbapp_facility;"
        result = cursor.execute(sql)
        datas = cursor.fetchall()
        
        connection.commit()
        connection.close()
        
        facilities_beverage = []
        for data in datas:
            row = {
                'id' : data[0],
                'name' : data[1],
                'category' : data[2],
                'content' : data[3],
                'tel_number' : data[4],
                'image' : data[5],
                'url' : data[6]
            }
            facilities_beverage.append(row)
        
    except:
        connection.rollback()
        print("찾고자 하는 정보가 없습니다.")
    
    return render(request, 'facility_beverage.html', { 'facilities_beverage' : facilities_beverage })

def facilityLecture(request):
    facilities_lecture = None
    try:
        cursor = connection.cursor()
        
        sql = "SELECT id, name, category, content, tel_number, image, url FROM hanseobase.dbapp_facility;"
        result = cursor.execute(sql)
        datas = cursor.fetchall()
        
        connection.commit()
        connection.close()
        
        facilities_lecture = []
        for data in datas:
            row = {
                'id' : data[0],
                'name' : data[1],
                'category' : data[2],
                'content' : data[3],
                'tel_number' : data[4],
                'image' : data[5],
                'url' : data[6]
            }
            facilities_lecture.append(row)
        
    except:
        connection.rollback()
        print("찾고자 하는 정보가 없습니다.")
    
    return render(request, 'facility_lecture.html', { 'facilities_lecture' : facilities_lecture })

def facilityEtc(request):
    facilities_etc = None
    try:
        cursor = connection.cursor()
        
        sql = "SELECT id, name, category, content, tel_number, image, url FROM hanseobase.dbapp_facility;"
        result = cursor.execute(sql)
        datas = cursor.fetchall()
        
        connection.commit()
        connection.close()
        
        facilities_etc = []
        for data in datas:
            row = {
                'id' : data[0],
                'name' : data[1],
                'category' : data[2],
                'content' : data[3],
                'tel_number' : data[4],
                'image' : data[5],
                'url' : data[6]
            }
            facilities_etc.append(row)
        
    except:
        connection.rollback()
        print("찾고자 하는 정보가 없습니다.")
    
    return render(request, 'facility_etc.html', { 'facilities_etc' : facilities_etc })

def facilityFacilities(request):
    facilities_facilities = None
    try:
        cursor = connection.cursor()
        
        sql = "SELECT id, name, category, content, tel_number, image, url FROM hanseobase.dbapp_facility;"
        result = cursor.execute(sql)
        datas = cursor.fetchall()
        
        connection.commit()
        connection.close()
        
        facilities_facilities = []
        for data in datas:
            row = {
                'id' : data[0],
                'name' : data[1],
                'category' : data[2],
                'content' : data[3],
                'tel_number' : data[4],
                'image' : data[5],
                'url' : data[6]
            }
            facilities_facilities.append(row)
        
    except:
        connection.rollback()
        print("찾고자 하는 정보가 없습니다.")
    
    return render(request, 'facility_facilities.html', { 'facilities_facilities' : facilities_facilities })

def clubView(request):
    clubs = None
    try:
        cursor = connection.cursor()
        
        sql = "SELECT id, name, category, content, tel_number, image, url FROM kyonggibase.dbapp_club;"
        result = cursor.execute(sql)
        datas = cursor.fetchall()
        
        connection.commit()
        connection.close()
        
        clubs = []
        for data in datas:
            row = {
                'id' : data[0],
                'name' : data[1],
                'category' : data[2],
                'content' : data[3],
                'tel_number' : data[4],
                'image' : data[5],
                'url' : data[6]
            }
            clubs.append(row)
        
    except:
        connection.rollback()
        print("찾고자 하는 정보가 없습니다.")
    
    return render(request, 'club.html', { 'clubs' : clubs })

def Graduate(request):
    graduate = None
    try:
        cursor = connection.cursor()
        
        sql = "SELECT id, time, document, article, notes, category FROM hanseobase.dbapp_multimajor;"
        result = cursor.execute(sql)
        datas = cursor.fetchall()
        
        connection.commit()
        connection.close()
        
        graduate = []
        for data in datas:
            row = {
                'id' : data[0],
                'time' : data[1],
                'document' : data[2],
                'article' : data[3],
                'notes' : data[4],
                'category' : data[5]
            }
            graduate.append(row)
        
    except:
        connection.rollback()
        print("찾고자 하는 정보가 없습니다.")
    
    return render(request, 'graduate.html', { 'graduate' : graduate })

def GraduateFreshman(request):
    graduate_freshman = None
    try:
        cursor = connection.cursor()
        
        sql = "SELECT id, time, document, article, notes, category FROM hanseobase.dbapp_multimajor;"
        result = cursor.execute(sql)
        datas = cursor.fetchall()
        
        connection.commit()
        connection.close()
        
        graduate_freshman = []
        for data in datas:
            row = {
                'id' : data[0],
                'time' : data[1],
                'document' : data[2],
                'article' : data[3],
                'notes' : data[4],
                'category' : data[5]
            }
            graduate_freshman.append(row)
        
    except:
        connection.rollback()
        print("찾고자 하는 정보가 없습니다.")
    
    return render(request, 'graduate_freshman.html', { 'graduate_freshman' : graduate_freshman })

def GraduateTransferman(request):
    graduate_transferman = None
    try:
        cursor = connection.cursor()
        
        sql = "SELECT id, time, document, article, notes, category FROM hanseobase.dbapp_multimajor;"
        result = cursor.execute(sql)
        datas = cursor.fetchall()
        
        connection.commit()
        connection.close()
        
        graduate_transferman = []
        for data in datas:
            row = {
                'id' : data[0],
                'time' : data[1],
                'document' : data[2],
                'article' : data[3],
                'notes' : data[4],
                'category' : data[5]
            }
            graduate_transferman.append(row)
        
    except:
        connection.rollback()
        print("찾고자 하는 정보가 없습니다.")
    
    return render(request, 'graduate_transferman.html', { 'graduate_transferman' : graduate_transferman })

def outsideView(request):
    outsides = None
    try:
        cursor = connection.cursor()
        
        sql = "SELECT id, name, category, content, tel_number, image, url FROM kyonggibase.dbapp_club;"
        result = cursor.execute(sql)
        datas = cursor.fetchall()
        
        connection.commit()
        connection.close()
        
        outsides = []
        for data in datas:
            row = {
                'id' : data[0],
                'name' : data[1],
                'category' : data[2],
                'content' : data[3],
                'tel_number' : data[4],
                'image' : data[5],
                'url' : data[6]
            }
            outsides.append(row)
        
    except:
        connection.rollback()
        print("찾고자 하는 정보가 없습니다.")
    
    return render(request, 'outside.html', { 'outsides' : outsides })

def outsideFront(request):
    outsides_frontgate = None
    try:
        cursor = connection.cursor()
        
        sql = "SELECT id, name, category, content, tel_number, image, url FROM kyonggibase.dbapp_club;"
        result = cursor.execute(sql)
        datas = cursor.fetchall()
        
        connection.commit()
        connection.close()
        
        outsides_frontgate = []
        for data in datas:
            row = {
                'id' : data[0],
                'name' : data[1],
                'category' : data[2],
                'content' : data[3],
                'tel_number' : data[4],
                'image' : data[5],
                'url' : data[6]
            }
            outsides_frontgate.append(row)
        
    except:
        connection.rollback()
        print("찾고자 하는 정보가 없습니다.")
    
    return render(request, 'outside_frontgate.html', { 'outsides_frontgate' : outsides_frontgate })

def outsideFrontRestaurant(request):
    outsides_front_restaurant = None
    try:
        cursor = connection.cursor()
        
        sql = "SELECT id, name, category, content, tel_number, image, url FROM kyonggibase.dbapp_club;"
        result = cursor.execute(sql)
        datas = cursor.fetchall()
        
        connection.commit()
        connection.close()
        
        outsides_front_restaurant = []
        for data in datas:
            row = {
                'id' : data[0],
                'name' : data[1],
                'category' : data[2],
                'content' : data[3],
                'tel_number' : data[4],
                'image' : data[5],
                'url' : data[6]
            }
            outsides_front_restaurant.append(row)
        
    except:
        connection.rollback()
        print("찾고자 하는 정보가 없습니다.")
    
    return render(request, 'outside_front_restaurant.html', { 'outsides_front_restaurant' : outsides_front_restaurant })

def outsideFrontCafe(request):
    outsides_front_cafe = None
    try:
        cursor = connection.cursor()
        
        sql = "SELECT id, name, category, content, tel_number, image, url FROM kyonggibase.dbapp_club;"
        result = cursor.execute(sql)
        datas = cursor.fetchall()
        
        connection.commit()
        connection.close()
        
        outsides_front_cafe = []
        for data in datas:
            row = {
                'id' : data[0],
                'name' : data[1],
                'category' : data[2],
                'content' : data[3],
                'tel_number' : data[4],
                'image' : data[5],
                'url' : data[6]
            }
            outsides_front_cafe.append(row)
        
    except:
        connection.rollback()
        print("찾고자 하는 정보가 없습니다.")
    
    return render(request, 'outside_front_cafe.html', { 'outsides_front_cafe' : outsides_front_cafe })

def outsideBack(request):
    outsides_backgate = None
    try:
        cursor = connection.cursor()
        
        sql = "SELECT id, name, category, content, tel_number, image, url FROM kyonggibase.dbapp_club;"
        result = cursor.execute(sql)
        datas = cursor.fetchall()
        
        connection.commit()
        connection.close()
        
        outsides_backgate = []
        for data in datas:
            row = {
                'id' : data[0],
                'name' : data[1],
                'category' : data[2],
                'content' : data[3],
                'tel_number' : data[4],
                'image' : data[5],
                'url' : data[6]
            }
            outsides_backgate.append(row)
        
    except:
        connection.rollback()
        print("찾고자 하는 정보가 없습니다.")
    
    return render(request, 'outside_backgate.html', { 'outsides_backgate' : outsides_backgate })

def outsideBackRestaurant(request):
    outsides_back_restaurant = None
    try:
        cursor = connection.cursor()
        
        sql = "SELECT id, name, category, content, tel_number, image, url FROM kyonggibase.dbapp_club;"
        result = cursor.execute(sql)
        datas = cursor.fetchall()
        
        connection.commit()
        connection.close()
        
        outsides_back_restaurant = []
        for data in datas:
            row = {
                'id' : data[0],
                'name' : data[1],
                'category' : data[2],
                'content' : data[3],
                'tel_number' : data[4],
                'image' : data[5],
                'url' : data[6]
            }
            outsides_back_restaurant.append(row)
        
    except:
        connection.rollback()
        print("찾고자 하는 정보가 없습니다.")
    
    return render(request, 'outside_back_restaurant.html', { 'outsides_back_restaurant' : outsides_back_restaurant })

def outsideBackCafe(request):
    outsides_back_cafe = None
    try:
        cursor = connection.cursor()
        
        sql = "SELECT id, name, category, content, tel_number, image, url FROM kyonggibase.dbapp_club;"
        result = cursor.execute(sql)
        datas = cursor.fetchall()
        
        connection.commit()
        connection.close()
        
        outsides_back_cafe = []
        for data in datas:
            row = {
                'id' : data[0],
                'name' : data[1],
                'category' : data[2],
                'content' : data[3],
                'tel_number' : data[4],
                'image' : data[5],
                'url' : data[6]
            }
            outsides_back_cafe.append(row)
        
    except:
        connection.rollback()
        print("찾고자 하는 정보가 없습니다.")
    
    return render(request, 'outside_back_cafe.html', { 'outsides_back_cafe' : outsides_back_cafe })


def MajorSite(request):
    major = None
    try:
        cursor = connection.cursor()
        
        sql = "SELECT id, name, category, content, tel_number, image, url FROM kyonggibase.dbapp_club;"
        result = cursor.execute(sql)
        datas = cursor.fetchall()
        
        connection.commit()
        connection.close()
        
        major = []
        for data in datas:
            row = {
                'id' : data[0],
                'name' : data[1],
                'category' : data[2],
                'content' : data[3],
                'tel_number' : data[4],
                'image' : data[5],
                'url' : data[6]
            }
            major.append(row)
        
    except:
        connection.rollback()
        print("찾고자 하는 정보가 없습니다.")
    
    return render(request, 'major.html', { 'major' : major })

def planBMenu(request):
    planBMenu = None
    try:
        cursor = connection.cursor()
        
        sql = "SELECT id, name, category, content, tel_number, image, url FROM kyonggibase.dbapp_club;"
        result = cursor.execute(sql)
        datas = cursor.fetchall()
        
        connection.commit()
        connection.close()
        
        planBMenu = []
        for data in datas:
            row = {
                'id' : data[0],
                'name' : data[1],
                'category' : data[2],
                'content' : data[3],
                'tel_number' : data[4],
                'image' : data[5],
                'url' : data[6]
            }
            planBMenu.append(row)
        
    except:
        connection.rollback()
        print("찾고자 하는 정보가 없습니다.")
    
    return render(request, 'planBMenu.html', { 'planBMenu' : planBMenu })
