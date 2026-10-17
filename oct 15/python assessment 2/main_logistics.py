# main_logistics.py
# 34. Import module[cite: 13]
import shipment_analysis

# 35. Use both normal import and specific-function import[cite: 13]
from shipment_utils import get_weight_category

cost = shipment_utils.calculate_cost(15)
cat = get_weight_category(15)
print(f"35. Cost: ₹{cost}, Category: {cat}")