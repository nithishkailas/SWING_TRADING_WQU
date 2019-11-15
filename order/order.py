from random import randint

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)



class Order():
    def __init__(self, Portfolio, symbol , L_or_S ,Entry_Time, entry , target , stop ,  quantity , max_holding_time , order_leverage ):

        self.portfolio = Portfolio
        self.symbol = symbol

        self.direction = L_or_S
        self.entry_price = entry
        self.target_price = target
        self.stop_price = stop
        self.quantity = quantity

        self.order_leverage = order_leverage
        self.entry_time = Entry_Time
        self.max_holding_period = max_holding_time
        self.exit_time = 0
        self.close_price = 0
        self.inside_candles = []
        self.Status = 'Check'
        if self.check_LandS_Condition() == 1:
            self.entry_order_id = self.generate_trade()
            self.target_order_id = self.get_target_order_id(self.entry_order_id)
            self.stop_order_id = self.get_stop_order_id(self.entry_order_id)
        else:
            print("Order Stop Price or Target Price Invalid")

        self.calculate_value()

    def check_LandS_Condition(self):
        if self.direction == 'Long':
            if self.entry_price <= self.stop_price or self.entry_price >= self.target_price:
                return -99
            else:
                return 1
        elif self.direction == 'Short':
            if self.entry_price >= self.stop_price or self.entry_price <= self.target_price:
                return -99
            else:
                return 1

    def generate_trade(self):
        ID = random_with_N_digits(15)
        self.Status = 'Placed'
        return ID

    def get_target_order_id(self,ID):
        target_Id = random_with_N_digits(15)
        return target_Id
    def get_stop_order_id(self,ID):
        stop_Id = random_with_N_digits(15)
        return stop_Id

    def calculate_value(self):
        if self.direction == 'Long':
            self.buy_value = self.entry_price*self.quantity
            self.sell_value = 0
            self.margin_required = self.buy_value
        if self.direction == 'Short':
            self.buy_value = 0
            self.sell_value = self.entry_price*self.quantity
            self.margin_required = self.sell_value

