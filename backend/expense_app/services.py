import traceback
from expense_app.serializers import ExpenseSerializer
from expense_app.models import Expense


class ExpenseSrv:
    
    def __init__(self,user,data=None):
        self.user = user
        self.data = data
    
    def get_all_expense(self):
        try:
            all_expense_objs = Expense.objects.filter(user=self.user.id)
            if self.data:
                from_date = self.data.get('fromDate','1990-01-01')
                to_date = self.data.get('toDate','2990-01-01')
                category = self.data.get('category','all')
                all_expense_objs = all_expense_objs.filter(
                    category=category,
                    created_date__gte=from_date,
                    created_date__lte=to_date)
            srl_obj = ExpenseSerializer(all_expense_objs,many=True)
            return srl_obj.data,"All Records fetched SuccessFully.","1"
        except Exception as ex:
            print(traceback.format_exc())        
            return str(ex),"Error while fetching all expense record.","S_01"
        
    def get_single_expense(self,expense_id):
        try:
            expense_obj = Expense.objects.filter(user=self.user.id,id=expense_id)
            srl_obj = ExpenseSerializer(expense_obj)
            return srl_obj.data,"Single Record fetched SuccessFully.","1"
        except Exception as ex:
            print(traceback.format_exc())
            return str(ex),"Error while fetching single expense record.","S_02"
    
    def create_expense(self):
        try :
            out_data = []
            if self.data:
                self.data['user'] = self.user.id
                expense_serializer = ExpenseSerializer(data=self.data)
                if expense_serializer.is_valid():
                    expense_serializer.save()
                    return expense_serializer.data,"Record Saved SuccessFully.","1"
                out_data = expense_serializer.errors
            return out_data,"Error while creating a Expense record.","S_01"
        except Exception as ex:
            print(traceback.format_exc())        
            return str(ex),"Error while creating a Expense record.","S_02"
    
    def update_expense(self,expense_id):
        try :
            out_data = []
            if self.data:
                expense_obj = Expense.objects.filter(id=expense_id).first()
                if expense_obj:
                    expense_serializer = ExpenseSerializer(expense_obj, data=self.data, partial=True)
                    if expense_serializer.is_valid():
                        expense_serializer.save()
                        return expense_serializer.data,"Record Updated SuccessFully.","1"
                    out_data = expense_serializer.errors
                else:
                    return "Expense record not found","Error while updating a Expense record.","S_05"
            return out_data,"Error while updating a Expense record.","S_06"
        except Exception as ex:
            print(traceback.format_exc())        
            return str(ex),"Error while updating a Expense record.","S_07"     
    
    def delete_expense(self,expense_id):
        try:
            expense_obj = Expense.objects.filter(id=expense_id).first()
            if expense_obj:
                expense_obj.delete()
                return [],"Expense record deleted successfully.","1"
            else:
                return [],"Expense record not found.","S_09"
        except Exception as ex:
            print(traceback.format_exc())        
            return str(ex),"Error while deleting a Expense record.","S_10"

