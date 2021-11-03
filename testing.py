import unittest
from frontend.main_interface import *
from back_end.dbconnection import *
from model.connector import *


# class TestSearching(unittest.TestCase):
#     def setUp(self):
#         self.data = [(1, 'Sausage', 'quality', '50', '100'),
#                      (2, 'Noodles', 'Hphen', '50', '100'),
#                      (3, 'Ice cream', 'vadilal', '50', '100'),
#                      (4, 'Oil', 'Dhara', '50', '110'),
#                      (5, 'Rice', 'Bash', '20', '50'),
#                      ]
#
#     def test_search(self):
#         self.assertEqual([(3, 'Ice cream', 'vadilal', '50', '100')],
#                          AddProduct.search_method_function(self.data, 0, str(3)))
#
#     def tearDown(self):
#         self.data = None
#

class Test_DbCurd(unittest.TestCase):
    def setUp(self):
        self.dbconnect = Curd()
        self.query = 'insert into tbl_product values (%s,%s,%s,%s,%s,%s)'
        self.values = (101, 'Noodles', 300, 50, 100,1),
        self.sel_query = 'select * from tbl_product where product_id=' + str(101)

    def test_insert(self):
        self.dbconnect.add_data(self.query, self.values)
        self.assertEqual([(2, 'Noodles', 300, 50, 100,1)],
                         self.dbconnect.fetch_data(self.sel_query))
        del_query = 'delete from tbl_product where product_Id = %s'
        del_value = (101,)
        self.dbconnect.delete_data(del_query, del_value)

    def tearDown(self):
        self.query = None
        self.values = None
        self.sel_query = None
        self.dbconnect = None

class Test_DbCurd(unittest.TestCase):
    def setUp(self):
        self.dbconnect = Curd()
        self.in_query = 'insert into tbl_product values(%s,%s,%s,%s,%s,%s)'
        self.in_values = (1001,'Rice', 100, 1, 40, 80)
        self.up_query = 'update tbl_product set product_name=%s,price= %s,max_stock=%s,min_stock=%s,group_id=%s where product_id=%s'
        self.up_values = ('Isha Pokhrel', 'isha_pokhrel@gmail.com','9801122333','2001/01/010', 'Kathmandu-4',1001)
        self.sel_query = 'select * from tbl_product where product_id =' + str(1001)

    def test_update(self):
        self.dbconnect.add_data(self.in_query, self.in_values)
        self.dbconnect.update_data(self.up_query,self.up_values)
        self.assertEqual([(1001,'Rice', 100, 1, 40, 80)],
                         self.dbconnect.fetch_data(self.sel_query))
        del_query = 'delete from tbl_product where product_id = %s'
        del_value = (1001,)
        self.dbconnect.delete_data(del_query, del_value)

    def tearDown(self):
        self.query = None
        self.values = None
        self.sel_query = None
        self.dbconnect = None

class Test_Sorting(unittest.TestCase):
    def setUp(self):
        self.data = [(1, 'JK SUppliers', 'ak@gmail.com', '9800', '1999/19/19', 'ktm'),
                     (2, 'UNI Pvt. Ltd.', 'ur@gmail.com', '980', '1999/10/1', 'nko'),
                     (10, 'Bimal Collection', 'bimala@gmail.com', '9800', '1999/09/09', 'npj'),
                     (9, 'Hari Store', 'hari@gmail.com', '9800', '1999/09/09', 'pkr'),
                     ]
        self.index = 1

    def test_search(self):
        self.assertEqual([(10, 'Bimal Collection', 'bimala@gmail.com', '9800', '1999/09/09', 'npj'),
                          (9, 'Hari Store', 'hari@gmail.com', '9800', '1999/09/09', 'pkr'),
                          (1, 'JK SUppliers', 'ak@gmail.com', '9800', '1999/19/19', 'ktm'),
                          (2, 'UNI Pvt. Ltd.', 'ur@gmail.com', '980', '1999/10/1', 'nko')],
                         Functions.sort_method(self.data, 1))

    def tearDown(self):
        self.data = None
        self.index = None


class Test_SetGet(unittest.TestCase):
    def setUp(self):
        self.std = SaveRegistration('akash', 'Algorithm')

    def test_set_usernamePassword(self):
        self.std.set_username('algorithm')
        self.std.set_password('akash')
        self.assertEqual('algorithm',self.std.get_username())
        self.assertEqual('akash',self.std.get_password())

    def test_get_usernamePassword(self):
        self.assertEqual('akash', self.std.get_username())
        self.assertEqual('Algorithm', self.std.get_password())


if __name__ == '__main__':
    unittest.main()
