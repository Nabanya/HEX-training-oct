# main.py
# 57-58
import retail_utils

tot = retail_utils.calculate_order_total(1500, 4)
disc = retail_utils.calculate_discount(tot)
status = retail_utils.check_stock_status(12)
print(f"58. Total: {tot}, Discount: {disc}, Status: {status}")

# 59
from retail_utils import calculate_order_total
print("59. Direct call total:", calculate_order_total(3000, 2))

# 60
import retail_utils as ru
print("60. Alias call status:", ru.check_stock_status(25))