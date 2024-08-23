import csv
import sqlite3

#db_name = "white_ips.db"

def query_all_ips(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    table_name = "white_ips"
    # 查询所有IP地址的SQL语句
    select_ips_sql = f'SELECT ip FROM {table_name};'

    try:
        # 获取数据库游标对象
        cursor = conn.cursor()
        # 执行查询IP地址的语句
        cursor.execute(select_ips_sql)
        # 获取所有IP地址
        ip_list = cursor.fetchall()
        # 将结果转换为列表形式（fetchall()返回的是一个元组列表）
        ip_list = [str(ip[0]) for ip in ip_list]
        print("IP地址已成功导出到列表。")
        return ip_list
    except sqlite3.Error as e:
        # 如果发生错误，打印错误信息
        print(f"导出IP地址时发生错误: {e}")
        return []
    finally:
        # 关闭游标
        cursor.close()
        conn.close()

def query_all_ip_and_descs(db_name):
    ips = []
    # 连接到SQLite数据库
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    table_name = "white_ips"
    # 查询所有值的SQL语句
    select_all_sql = f'SELECT ip, description FROM {table_name};'

    try:
        # 执行查询语句
        cursor.execute(select_all_sql)
        # 获取所有查询结果
        rows = cursor.fetchall()
        # 打印查询结果
        for row in rows:
            print(f"IP: {row[0]}, Description: {row[1]}")
            ips.append((row[0], row[1]))
        return ips
    except sqlite3.Error as e:
        print(f"查询数据时发生错误: {e}")
        return []
    finally:
        # 关闭连接
        cursor.close()
        conn.close()


def create_table(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    table_name = "white_ips"
    # 创建表的SQL语句，为ip字段添加主键约束
    create_table_sql = f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        ip TEXT PRIMARY KEY NOT NULL,  -- ip字段为主键且不允许为空
        description TEXT NULL
    );
    '''
    try:
        # 执行SQL语句创建表
        cursor.execute(create_table_sql)
        # 提交事务
        conn.commit()
        print(f"表 '{table_name}' 创建成功，其中 'ip' 字段设置了主键约束。")
        return True
    except sqlite3.Error as e:
        # 如果发生错误，打印错误信息并回滚事务
        print(f"创建表时发生错误: {e}")
        conn.rollback()
        return False
    finally:
        # 关闭连接
        cursor.close()
        conn.close()

# 插入数据，每条数据的格式为：(ip, description)
def insert_ip_desc(db_name, ip_desc_list):
    conn = sqlite3.connect(db_name)
    # 连接到SQLite数据
    cursor = conn.cursor()
    table_name = "white_ips"

    # 插入数据的SQL语句模板
    insert_sql = f'''
    INSERT INTO {table_name} (ip, description) VALUES (?, ?);
    '''

    try:
        # 将数据分批插入数据库，每批100条
        for data in ip_desc_list:
            cursor.execute(insert_sql, data)
            # 提交事务
            conn.commit()
        print(f"所有数据成功插入到 '{table_name}' 表中。")
        return True
    except sqlite3.Error as e:
        # 如果发生错误，打印错误信息并回滚事务
        print(f"插入数据时发生错误: {e}")
        conn.rollback()
        return False
    finally:
        # 关闭连接
        cursor.close()
        conn.close()

# 仅插入IP
def insert_ip(db_name, ip):
    conn = sqlite3.connect(db_name)
    # 连接到SQLite数据
    c = conn.cursor()
    table_name = "white_ips"
    insert_sql = f'''
    INSERT INTO {table_name} (ip, description) VALUES (?, '无描述');
    '''
    try:
        c.execute(insert_sql, (ip,))
        conn.commit()
        print(f"插入{ip}到白名单成功")
        return True
    except sqlite3.Error as e:
        print(e)
        return False

def insert_single_data(db_name, ip, description):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    table_name = "white_ips"
    # 插入单条数据的SQL语句
    insert_sql = f'''
    INSERT INTO {table_name} (ip, description) VALUES (?, ?);
    '''
    try:
        # 执行插入语句
        cursor.execute(insert_sql, (ip, description))
        # 提交事务
        conn.commit()
        print("数据插入成功。")
        return True
    except sqlite3.Error as e:
        # 如果发生错误，打印错误信息并回滚事务
        print(f"插入数据时发生错误: {e}")
        conn.rollback()
        return False
    finally:
        # 关闭游标（注意：不要关闭传入的db_conn，它会被多个函数共享使用）
        cursor.close()
        conn.close()

def query_ip_by_address(db_name, ip_address):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    table_name = "white_ips"
    # 根据IP地址查询的SQL语句
    select_by_ip_sql = f'SELECT ip, description FROM {table_name} WHERE ip = ?;'

    try:
        # 执行查询语句
        cursor.execute(select_by_ip_sql, (ip_address,))
        # 获取查询结果
        row = cursor.fetchone()

        # 检查结果是否存在
        if row:
            print(f"找到IP地址: {row[0]}, 描述: {row[1]}")
            return (row[0], row[1])
        else:
            print(f"未找到IP地址为 '{ip_address}' 的记录。")
            return ()
    except sqlite3.Error as e:
        print(f"根据IP地址查询数据时发生错误: {e}")
        return ()
    finally:
        # 关闭连接
        cursor.close()
        conn.close()

def delete_data_by_ip(db_name, ip):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    table_name = "white_ips"
    # 根据IP地址删除数据的SQL语句
    delete_sql = f'''
    DELETE FROM {table_name}
    WHERE ip = ?;
    '''

    try:
        # 获取数据库游标对象

        # 执行删除语句
        cursor.execute(delete_sql, (ip,))
        # 提交事务
        conn.commit()
        # 检查是否影响行
        if cursor.rowcount == 0:
            print(f"未找到要删除的IP地址: {ip}")
            return False
        else:
            print(f"已删除IP地址: {ip}")
            return True
    except sqlite3.Error as e:
        # 如果发生错误，打印错误信息并回滚事务
        print(f"删除数据时发生错误: {e}")
        conn.rollback()
        return False
    finally:
        # 关闭游标
        cursor.close()

def clear_table_data(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    table_name = "white_ips"
    # 清除表中所有数据的SQL语句
    clear_sql = f'DELETE FROM {table_name};'

    try:
        # 执行删除所有数据的语句
        cursor.execute(clear_sql)
        # 提交事务
        conn.commit()
        print("表数据已清空。")
        return True
    except sqlite3.Error as e:
        # 如果发生错误，打印错误信息并回滚事务
        print(f"清空表数据时发生错误: {e}")
        conn.rollback()
        return False
    finally:
        # 关闭游标
        cursor.close()

def export_to_csv(db_name, csv_file_path):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    table_name = "white_ips"
    # 查询所有数据的SQL语句
    select_all_sql = f'SELECT * FROM {table_name};'

    try:
        # 执行查询所有数据的语句
        cursor.execute(select_all_sql)
        # 获取查询结果
        rows = cursor.fetchall()
        # 确定CSV文件的列名
        column_names = [description[0] for description in cursor.description]
        # 打开CSV文件准备写入
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            # 写入列名
            writer.writerow(column_names)
            # 写入查询结果
            writer.writerows(rows)

        print(f"数据已成功导出到 '{csv_file_path}'。")
    except sqlite3.Error as e:
        # 如果发生错误，打印错误信息
        print(f"导出数据时发生错误: {e}")
    finally:
        # 关闭游标
        cursor.close()

