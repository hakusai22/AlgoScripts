      
#- 验证user写入新库是否符合规则
#- 对比body_status写入新库数量和老库数量
#- 顺序验证新旧表数据一致性
#- 验证写老库是否正常（新增数量是否正常）

from util.conn import Mysql
from util.hash import get_murmur_hash_index
from util.util import md5


db_new = Mysql("new")
db_old = Mysql("old")
db_mycat = Mysql("mycat")

# 验证body_status写入新库是否符合规则
# 顺序验证新旧表数据一致性
def check_write_new_is_ok(start_id, end_id):
    success = True
    is_not_consistent = 0
    is_not_hash = 0
    is_not_only = 0
    not_consistent_list = []
    not_hash_list =[]
    for id in range(start_id, end_id+1):
        sql_old = "select * from `user` where id = '{}';".format(id)
        db_old.execute(sql_old)
        result_old = db_old.fetchall()
        if len(result_old) == 0:
            continue
        user_id, timestamp, type, familyMember_id, md5str = md5(result_old[0])
        db_id = get_murmur_hash_index(128, 4, user_id)
        sql_new = "select * from `body_status_{}` where timestamp='{}' and type='{}' and user_id='{}' and familyMember_id='{}';".format(db_id, timestamp, type, user_id, familyMember_id)
        #sql_new = "select * from `user` where timestamp='{}' and type='{}' and user_id='{}' and familyMember_id='{}';".format(timestamp, type, user_id, familyMember_id)
        db_new.execute(sql_new)
        result_new = db_new.fetchall()
        # 新库只查到一条数据，通过对比多字段拼接后md5检验一致性数据
        if len(result_new) == 1:
            _, _, _, _, md5str_new = md5(result_new[0])
            print("新数据md5: {}, 老数据md5: {}".format( md5str_new, md5str))
            if md5str_new != md5str:
                success = False
                is_not_consistent += 1
                not_consistent_list.append(sql_new)
                print("---ERROR---新老数据出现不一致: {}".format(sql_new))
        # 新库没查到数据，可能没写入或者路由错了
        elif len(result_new) == 0:
            success = False
            is_not_hash += 1
            not_hash_list.append(sql_new)
            print("---ERROR---未按路由规则写入新表")
        elif len(result_new) > 1:
            success = False
            is_not_only += 1
            print("---ERROR---在新表里检索到不止一条数据，联合索引不唯一: {}".format(sql_new))
    if success == True:
        print("验证body_status双写成功")
    elif success == False:
        print("验证body_status双写失败")
        print("未按路由规则写入新表{}条".format(is_not_hash))
        print("联合索引不唯一{}条".format(is_not_only))
        print("数据不一致{}条".format(is_not_consistent))
        print("数据不一致的sql: ", not_consistent_list)
        print("未按路由规则写入的sql: ", not_hash_list)

# 对比body_status写入新库数量和老库数量；mycat和old的对比
# 由于分表后id不同，只能通过insertTime来统计数量
def check_count_is_ok(insertTime_start, insertime_end):
    sql = "SELECT COUNT(*) FROM user where insertTime between  '{}' and '{}';".format(insertTime_start, insertime_end)
    db_mycat.execute(sql)
    count_mycat = db_mycat.fetchone()
    db_old.execute(sql)
    count_old = db_old.fetchone()
    print("check_count_is_ok写入新库数：", count_mycat)
    print("check_count_is_ok写入老库数：", count_old)
    assert int(count_old['COUNT(*)']) == int(count_mycat['COUNT(*)'])


check_write_new_is_ok(start_id=1620964780, end_id=1620964790)
check_count_is_ok(insertTime_start=1659938729, insertime_end=1659939205)

db_new.close()
db_old.close()
db_mycat.close()




    